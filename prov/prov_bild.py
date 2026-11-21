"""Prov: kan en oläst eller OCR-läst sida kännas igen som bild, eller som
text med en bildyta? Hämtar urvalets PDF:er, renderar sidorna och mäter.
Bara ett prov: skriver till prov-ut/, ändrar inget i poolen."""

import csv
import io
import json
import subprocess
import sys
import tempfile
import time
import urllib.request
from collections import deque
from pathlib import Path

import numpy as np
import pypdfium2 as pdfium
from PIL import Image

UA = "kommunhandlingar (+https://github.com/moggleif/kommunhandlingar)"
UT = Path("prov-ut")
RUTOR = 48  # rutnätet som bildytor söks i


def hamta(url, senast):
    vard = url.split("/")[2]
    vanta = 5 - (time.time() - senast.get(vard, 0))
    if vanta > 0:
        time.sleep(vanta)
    senast[vard] = time.time()
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=120) as svar:
        return svar.read()


def ocr(bild):
    with tempfile.TemporaryDirectory() as k:
        fil = Path(k) / "s.png"
        bild.save(fil)
        r = subprocess.run(
            ["tesseract", fil, "-", "-l", "swe", "--dpi", "300", "tsv"],
            capture_output=True, text=True, timeout=300,
        )
    rader = list(csv.DictReader(io.StringIO(r.stdout), delimiter="\t", quoting=csv.QUOTE_NONE))
    return [x for x in rader if x.get("text", "").strip() and x["conf"] != "-1"]


def medel(ord_):
    return round(sum(float(o["conf"]) for o in ord_) / len(ord_), 1) if ord_ else None


def ordmask(ord_, form, skala):
    m = np.zeros(form, bool)
    for o in ord_:
        if float(o["conf"]) < 50 or len(o["text"].strip()) < 2:
            continue
        x, y, b, h = (int(int(o[k]) * skala) for k in ("left", "top", "width", "height"))
        m[max(0, y - 3): y + h + 3, max(0, x - 3): x + b + 3] = True
    return m


def bildyta(farg, ordm):
    """Största sammanhängande yta av rutor med mycket bläck eller färg och
    utan säkra ord, som andel av sidan, och dess ruta i pixlar."""
    a = np.asarray(farg.convert("RGB")).astype(int)
    gra = a.mean(axis=2)
    satt = a.max(axis=2) - a.min(axis=2)
    black = gra < 200
    fargad = (satt > 40) & (gra < 245)
    h, b = gra.shape
    rh, rb = h // RUTOR, b // RUTOR
    rut = np.zeros((RUTOR, RUTOR), bool)
    for i in range(RUTOR):
        for j in range(RUTOR):
            s = np.s_[i * rh:(i + 1) * rh, j * rb:(j + 1) * rb]
            if ordm[s].mean() > 0.3:
                continue
            rut[i, j] = black[s].mean() > 0.25 or fargad[s].mean() > 0.3
    basta, ruta = 0, None
    sett = np.zeros_like(rut)
    for i in range(RUTOR):
        for j in range(RUTOR):
            if not rut[i, j] or sett[i, j]:
                continue
            ko, celler = deque([(i, j)]), []
            sett[i, j] = True
            while ko:
                y, x = ko.popleft()
                celler.append((y, x))
                for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < RUTOR and 0 <= nx < RUTOR and rut[ny, nx] and not sett[ny, nx]:
                        sett[ny, nx] = True
                        ko.append((ny, nx))
            ys, xs = zip(*celler)
            yta = (max(ys) - min(ys) + 1) * (max(xs) - min(xs) + 1)
            if yta > basta:
                basta = yta
                ruta = (min(xs) * rb, min(ys) * rh, (max(xs) + 1) * rb, (max(ys) + 1) * rh)
    return round(basta / RUTOR**2, 3), ruta, round(float(black.mean()), 3), round(float(fargad.mean()), 3)


def mat(sida):
    farg = sida.render(scale=100 / 72).to_pil()
    gra = sida.render(scale=300 / 72, grayscale=True).to_pil()
    ord1 = ocr(gra)
    skala = 100 / 300
    ordm = ordmask(ord1, (farg.height, farg.width), skala)
    andel, ruta, blackandel, fargandel = bildyta(farg, ordm)
    ut = dict(ord=len(ord1), sakerhet=medel(ord1), ord_saker=sum(float(o["conf"]) >= 70 for o in ord1),
              ordyta=round(float(ordm.mean()), 3), bildyta=andel, black=blackandel, farg=fargandel)
    if ruta and andel >= 0.04:
        maskad = gra.copy()
        x0, y0, x1, y1 = (int(v / skala) for v in ruta)
        maskad.paste(255, (x0, y0, x1, y1))
        ord2 = ocr(maskad)
        ut.update(ord_maskad=len(ord2), sakerhet_maskad=medel(ord2))
    return farg, ut, ruta


def main():
    urval = json.loads(Path(sys.argv[1]).read_text())
    (UT / "sidor").mkdir(parents=True, exist_ok=True)
    senast, resultat, cache = {}, [], {}
    for r in urval:
        try:
            data = cache.get(r["url"]) or hamta(r["url"], senast)
            cache = {r["url"]: data}
            pdf = pdfium.PdfDocument(data)
            sida = pdf[r["sida"] - 1]
            farg, matt, ruta = mat(sida)
            liten = farg.copy()
            liten.thumbnail((700, 1000))
            liten.save(UT / "sidor" / f"{r['id']}.png")
            r.update(matt, ruta=ruta, tecken=len(sida.get_textpage().get_text_range()))
        except Exception as fel:  # ett prov: felet skrivs ut och nästa sida prövas
            r["fel"] = repr(fel)[:200]
        print(json.dumps(r, ensure_ascii=False), flush=True)
        resultat.append(r)
    (UT / "resultat.json").write_text(json.dumps(resultat, ensure_ascii=False, indent=1))


main()
