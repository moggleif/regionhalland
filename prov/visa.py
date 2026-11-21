"""Prov: skriver urvalets sidor som små JPEG i base64 i loggen, en rad per
sida, så att de kan ses utan att binärer checkas in."""

import base64
import io
import json
import sys
import time
import urllib.request

import pypdfium2 as pdfium

UA = "kommunhandlingar (+https://github.com/moggleif/kommunhandlingar)"

senast = {}
for r in json.load(open(sys.argv[1])):
    if r["url"].startswith("["):
        continue
    vard = r["url"].split("/")[2]
    time.sleep(max(0, 5 - (time.time() - senast.get(vard, 0))))
    senast[vard] = time.time()
    req = urllib.request.Request(r["url"], headers={"User-Agent": UA})
    data = urllib.request.urlopen(req, timeout=120).read()
    bild = pdfium.PdfDocument(data)[r["sida"] - 1].render(scale=60 / 72).to_pil().convert("RGB")
    bild.thumbnail((520, 740))
    ut = io.BytesIO()
    bild.save(ut, "JPEG", quality=55)
    print("BILD", r["id"], base64.b64encode(ut.getvalue()).decode(), flush=True)
