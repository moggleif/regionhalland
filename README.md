# regionhalland

Region Hallands politiska handlingar – kallelser, protokoll och bilagor från
regionfullmäktige, regionstyrelsen, driftnämnderna och övriga organ –
konverterade till Markdown och CSV, med källa och kvalitet i varje dokument.

Koden finns i [moggleif/kungsbackakommun](https://github.com/moggleif/kungsbackakommun),
med kommunfilen, adaptern för Meetings Plus och front matter i
[arkitekturen](https://github.com/moggleif/kungsbackakommun/blob/main/docs/03-ARKITEKTUR.md),
Meetings Plus i [K57](https://github.com/moggleif/kungsbackakommun/blob/main/docs/02-KRAV.md#k57--handlingarna-på-formpipe-meetings-plus)
och hur plattformen läses i
[ADR-0080](https://github.com/moggleif/kungsbackakommun/blob/main/docs/decisions/0080-meetings-plus-las-motessidorna-nyast-forst.md).
Det här repot har bara regionens inställningar, datat och arbetsflödet som
kör koden. Saknas något i inställningsfilen görs koden där mer generell;
här skrivs ingen egen kod.

## Innehåll

| Fil eller katalog                   | Vad                                                         |
| ----------------------------------- | ----------------------------------------------------------- |
| `kommuner/regionhalland.toml`       | Organen, deras sidor och samlingsmötena.                    |
| `hamtning.toml`                     | User-Agent och intervall mellan anropen.                    |
| `data/regionhalland/`               | Dokumenten, ett per fil i källan, skrivna av nattkörningen. |
| `versioner/regionhalland.csv`       | Varje ny version av ett dokument, skriven av nattkörningen. |
| `mal/`, `uppfoljningar/` och spåren | Sidorna över tid, skrivna för hand ur handlingarna (nedan). |
| `TACKNING.md`                       | Vilka år och källor sidorna över tid har, nämnd för nämnd.  |
| `kodversion.txt`                    | Versionen av kommunhandlingar som alla körningar använder.  |
| `.github/workflows/nattkorning.yml` | Nattkörningen, varje natt 01:41 UTC och vid manuell start.  |
| `.github/nattkorning/`              | Nattkörningens delar och incheckning, som skript.           |
| `.github/workflows/kontroll.yml`    | Datakontrollerna på varje PR och på main, och på PR:en, utom nattkörningens, ett bygge av webbplatsen utan publicering. |
| `.github/workflows/webbplats.yml`   | Webbplatsen, byggd och publicerad efter varje merge, när en issue ändras och vid manuell start. |
| `.github/actions/installera/`       | Python och kodversionen, installerade för de tre flödena.   |
| `.github/actions/levande/`          | Nattkörningens upptäckt och steg 2 för varje kommunfil.     |
| `.github/ISSUE_TEMPLATE/`           | Mallen för avvikelser i källan, med etiketten `avvikelse`.  |
| `.github/pull_request_template.md`  | Mallen för en PR: vad som ändras och hur det kontrollerats. |
| `AGENTS.md` och `CLAUDE.md`         | Vägledningen för den som arbetar i repot.                   |

## Källan

Regionen publicerar på Formpipe Meetings Plus, <https://politik.regionhalland.se/>.
Uppmätt 2026-11-15:

- **17 publika organ.** Organets sida listar alla dess möten, 2013–2027,
  också kommande. Regionstyrelsens utskott har ingen egen sida.
- **Mötets sida** har kallelsen, protokollet och bilagorna under varje
  ärendepunkt, en PDF per bilaga. Zip-paketen läses inte.
- **Samlingsmöten.** Några möten rymmer flera sammanträdens filer, och
  datumet läses då ur filnamnet. De står i inställningsfilen, med skälet
  för varje möte som inte ger någon kandidat.
- **`robots.txt`** stänger bara `/admin`.
- **Omfånget.** Den första upptäckten gav 20 632 filer: 804 protokoll,
  742 kallelser och 19 086 bilagor, 2013–2026. Med två sekunder mellan
  anropen och konverteringen var poolen ikapp först den 24 november 2026.

## Körningen

Nattkörningen installerar kommunhandlingar på den commit som står i
`kodversion.txt` och kör samma upptäckt och steg 2 som för kommunerna, med
samma tidsbudget. Stoppas upptäckten av källan, till exempel när en sida
inte går att hämta, hoppas steg 2 över med en rad i sammanfattningen, jobbet
fälls inte och nästa körning försöker igen; varje annat fel fäller jobbet.
Det står i `.github/actions/levande`, med samma kod som kungsbackakommuns.
Steg 2 går i delar om 15 minuter, och efter varje del kontrolleras det klara
och pushas på körningens egen gren, så att ett fel kostar högst en del.
Varje del blir en commit med datum och klockslag. Grenen får en PR, som
mergas när kontrollen gått igenom, också när körningen fallit efter en
sparad del. Går det inte att fråga GitHub om grenen finns fälls jobbet, så
att sparat data inte tyst blir utan PR. Det nyaste mötet hämtas först över
alla organ.

Skripten i `.github/nattkorning/` har samma kod som kungsbackakommuns utom
pushen: där pushar ett eget jobb utan att läsa det hämtade, här pushar
nattkörningen själv. PR-jobbet och steget Sammanfattning är kopior av
kungsbackakommuns, och kommentaren vid dem säger var originalet står och,
för PR-jobbet, varför det skiljer sig.

En ny version av kommunhandlingar tas in genom att byta commit i
`kodversion.txt` i en PR. Versionen står inte i workflow-filen, eftersom
GitHub vägrar en pågående körning att pusha sin gren när workflow-filen på
main har ändrats under tiden, och körningens arbete då går förlorat.

### Jämförelse med nuvarande läge

Repot har inga egna tester. Att en ändring inte ändrar något visas så här:

- **Kodversionen:** webbplatsen byggs lokalt på samma commit av datat, före
  och efter bytet i `kodversion.txt`, och de tre talen nedan ska vara samma.
- **Arbetsflödena:** kontrollens bygge på PR:en publiceras inte. Den
  publicerade webbplatsens artefakt `github-pages` ger samma tal med samma
  kommandon i den uppackade `artifact.tar`.
- **Nattkörningen** omfattas inte. Den prövas med en manuell körning som
  inte ska skriva om befintliga filer under `data/`.

Kommandona körs från repots rot, i Linux. Avvikelsefilen lämnas tom, så att
öppna issues inte spelar in.

```sh
rm -rf /tmp/jamfor /tmp/_site
python3.12 -m venv /tmp/jamfor
/tmp/jamfor/bin/pip install "$(cat kodversion.txt)"
/tmp/jamfor/bin/pip freeze
: > /tmp/avvikelser.jsonl
/tmp/jamfor/bin/python -m kommunhandlingar.webbplats /tmp/_site \
  https://github.com/moggleif/regionhalland /tmp/avvikelser.jsonl
( cd /tmp/_site
  find . -type f | wc -l
  find . -type f | LC_ALL=C sort | sha256sum
  find . -type f -print0 | LC_ALL=C sort -z \
    | xargs -0 sed 's/Sidan byggdes [0-9-]* [0-9:]* UTC//' | sha256sum )
```

Talen är antalet filer, en kontrollsumma över filnamnen och en över
innehållet utan byggtiden i sidfoten. Innehållet beror också på dagen,
till exempel när ett protokoll räknas som saknat, så båda byggena görs
samma dag (UTC). Beroendena i `pip freeze` ska vara desamma båda gångerna,
utom kommunhandlingar. [#59](https://github.com/moggleif/regionhalland/issues/59)
visar att metoden ger samma tal som CI och mellan byggen.

## Webbplatsen

Webbplatsen har samma sidor som Kungsbackas och publiceras på
<https://moggleif.github.io/regionhalland/>. Menyn delar in organen i
grupperna i inställningsfilen. Kallelser och protokoll visar texten på sin
sida; bilagornas sidor visar härkomsten och länkar till Markdown-filen här,
så att webbplatsen ryms under GitHub Pages gräns på 1 GB.

## Sidorna över tid

Varje driftnämnd kan få samma sidor över tid som Kungsbackas nämnder, och
tre till som regionen behöver. Filerna skrivs för hand ur handlingarna, och
bygget prövar att varje text står på källans sida. Vilka år och källor
varje nämnd har står i [TACKNING.md](TACKNING.md). Formatet står i
[arkitekturen](https://github.com/moggleif/kungsbackakommun/blob/main/docs/03-ARKITEKTUR.md)
och de nya slagen i
[ADR-0085](https://github.com/moggleif/kungsbackakommun/blob/main/docs/decisions/0085-lokaler-remisser-och-overenskommelser-som-spar.md).

| Fil                                    | Sidan                                            |
| -------------------------------------- | ------------------------------------------------ |
| `mal/regionhalland.csv`                | Mål och direktiv: nämndens mål och utfallet.     |
| `uppfoljningar/regionhalland.csv`      | Uppföljningarna av målen i protokollen.          |
| `investeringar/regionhalland.csv`      | Lokaler och investeringar.                       |
| `initiativ/regionhalland.csv`          | Initiativärenden, och motioner som nämnden yttrat sig över. |
| `handlingsplaner/regionhalland.csv`    | Handlingsplaner.                                 |
| `redovisningar/regionhalland.csv`      | Redovisningar av uppdrag och återkommande rapporter. |
| `granskningar/regionhalland.csv`       | Revisionens granskningar och nämndens svar.      |
| `remisser/regionhalland.csv`           | Remisser och yttranden.                          |
| `overenskommelser/regionhalland.csv`   | Överenskommelser och vårdval.                    |

Lokalbehov, detaljplaner och projekt används inte: de följer en kommuns
lokalplan och planmonopol.
