# regionhalland

Region Hallands politiska handlingar – kallelser, protokoll och bilagor från
regionfullmäktige, regionstyrelsen, driftnämnderna och övriga organ –
konverterade till Markdown och CSV, med källa och kvalitet i varje dokument.

Koden finns i [moggleif/kungsbackakommun](https://github.com/moggleif/kungsbackakommun).
Det här repot har bara regionens inställningar, datat och arbetsflödet som kör
koden. Format, regler och beslut står där:

- [Arkitekturen](https://github.com/moggleif/kungsbackakommun/blob/main/docs/03-ARKITEKTUR.md),
  med kommunfilen, adaptern för Meetings Plus och front matter.
- [Kraven](https://github.com/moggleif/kungsbackakommun/blob/main/docs/02-KRAV.md),
  för Meetings Plus K57.
- [ADR-0080](https://github.com/moggleif/kungsbackakommun/blob/main/docs/decisions/0080-meetings-plus-las-motessidorna-nyast-forst.md),
  hur plattformen läses.

## Innehåll

| Fil eller katalog                   | Vad                                                         |
| ----------------------------------- | ----------------------------------------------------------- |
| `kommuner/regionhalland.toml`       | Organen, deras sidor och samlingsmötena.                    |
| `hamtning.toml`                     | User-Agent och intervall mellan anropen.                    |
| `data/regionhalland/`               | Dokumenten, ett per fil i källan, skrivna av nattkörningen. |
| `versioner/regionhalland.csv`       | Varje ny version av ett dokument, skriven av nattkörningen. |
| `mal/`, `uppfoljningar/` och spåren | Sidorna över tid, skrivna för hand ur handlingarna (nedan). |
| `kodversion.txt`                    | Versionen av kommunhandlingar som alla körningar använder.  |
| `.github/workflows/nattkorning.yml` | Nattkörningen.                                              |
| `.github/workflows/kontroll.yml`    | Datakontrollerna på varje PR.                               |
| `.github/workflows/webbplats.yml`   | Webbplatsen, byggd och publicerad efter varje merge.        |

Saknas något i inställningsfilen görs koden i kommunhandlingar mer generell;
här skrivs ingen egen kod.

## Källan

Regionen publicerar på Formpipe Meetings Plus, <https://politik.regionhalland.se/>.
Uppmätt 2026-11-15:

- **17 publika organ.** Organets sida listar alla dess möten, 2013–2027,
  också kommande. Regionstyrelsens utskott har ingen egen sida.
- **Mötets sida** har kallelsen, protokollet och bilagorna under varje
  ärendepunkt, en PDF per bilaga. Zip-paketen läses inte.
- **Samlingsmöten.** Före 2018 ligger regionfullmäktiges och
  regionstyrelsens protokoll samlade i ett möte per år, daterat 1 januari,
  med sammanträdets datum i filnamnet. De står i inställningsfilen.
  Där står också tre andra möten daterade 1 januari, vars filer inte har
  något datum i filnamnet och därför inte hämtas: plattformens manual
  (Kultur och skola 2020), ett tomt möte (Regionservice 2024) och fem
  revisionsrapporter (2022).
- **`robots.txt`** stänger bara `/admin`.
- **Omfånget.** Den första upptäckten gav 20 632 filer: 804 protokoll,
  742 kallelser och 19 086 bilagor, 2013–2026. Med två sekunder mellan
  anropen och konverteringen tar det flera nätter innan poolen är ikapp.

## Körningen

Nattkörningen installerar kommunhandlingar på den commit som står i
`kodversion.txt`, och kör samma upptäckt och steg 2 som för kommunerna, med
samma tidsbudget. Steg 2 går i delar om 15 minuter, och efter varje del
kontrolleras det klara och pushas på körningens egen gren, så att ett fel
kostar högst en del. Grenen får en PR, som mergas när kontrollen gått
igenom, också när körningen fallit efter en sparad del. Det nyaste mötet
hämtas först över alla organ.

En ny version av kommunhandlingar tas in genom att byta commit i
`kodversion.txt` i en PR. Versionen står inte i workflow-filen, eftersom
GitHub vägrar en pågående körning att pusha sin gren när workflow-filen på
main har ändrats under tiden, och körningens arbete då går förlorat.

## Webbplatsen

Webbplatsen har samma sidor som Kungsbackas och byggs av samma version av
kommunhandlingar som nattkörningen, efter varje merge till main. Den
publiceras på <https://moggleif.github.io/regionhalland/>. Menyn delar in
organen i grupperna i inställningsfilen. Kallelser och protokoll visar
texten på sin sida; bilagornas sidor visar härkomsten och länkar till
Markdown-filen här, så att webbplatsen ryms under GitHub Pages gräns på 1 GB.

## Sidorna över tid

Varje driftnämnd kan få samma sidor över tid som Kungsbackas nämnder, och
tre till som regionen behöver. Filerna skrivs för hand ur handlingarna, och
bygget prövar att varje text står på källans sida. Formatet står i
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

Först ute är Driftnämnden Närsjukvård, 2017–2026. Målen står för
2018–2026, ur verksamhetsplanerna (2020 och 2024 ur årsredovisningen,
eftersom planen inte finns i poolen, och för 2024 också nämndens egna
utvecklingsområden ur beslutsförslaget; 2026 ur planen nämnden fick i
oktober 2025). Utfallet står för 2020–2025; 2018–2019 följs bara upp med
indikatorer.
Motionerna har fullmäktiges beslut där beslutet finns bland nämndens
handlingar; resten kommer när regionfullmäktige är hämtat.
Gemensam nämnd för hemsjukvård och hjälpmedel har sidorna för 2017–2026:
överenskommelserna med kommunerna
(hemsjukvården, samverkansavtalet, trygg och effektiv utskrivning och
betalningsmodellen), redovisningarna (hjälpmedelsuppdraget och
indikatorrapporterna), initiativärendena och granskningarna. Nämnden fick
egna mål först i verksamhetsplanen för 2025; årsredovisningen följer inte
upp dem mål för mål, så de står utan utfall. Stegen tar med beslut i andra
organ när de gäller nämndens överenskommelser.
Driftnämnden Psykiatri har sidorna för 2019–2026. Målen står för
2021–2026: utfallet ur årsredovisningarna 2021–2025, målen ur
verksamhetsplanerna 2022–2026 (planen för 2021 finns inte i poolen) och
prognosen för 2026 ur uppföljningsrapport 2. Årsredovisningarna för 2019 och
2020 följer inte upp målen ett och ett, så de åren står utan mål.
Handlingsplanerna har den regionala handlingsplanen för suicidprevention,
åtgärderna för ekonomi i balans, digitaliseringsplanen och
kompetensförsörjningsplanen. Motionerna har fullmäktiges beslut, och
granskningarna revisorernas bedömning där den står i rapporten.
Regionstyrelsens och fullmäktiges beslut står med när de gäller nämndens
lokaler, planer, remisser och motioner.
Driftnämnden Ambulans, diagnostik och hälsa har sidorna för 2019–2026.
Målen står för 2020–2026: nämndens utvecklingsområden ur
verksamhetsplanerna 2020–2026, utfallet ur årsredovisningarna 2022–2025 och
prognosen för 2026 ur uppföljningsrapport 2. Årsredovisningarna för 2019–2021
finns inte i poolen, så 2020 och 2021 står utan utfall. Handlingsplanerna
har åtgärdsplanerna för ekonomi i balans och kompetensförsörjningsplanen,
initiativärendena tre initiativ från 2022 och motionerna med fullmäktiges
beslut, och investeringarna nämndens och regionstyrelsens beslut om
röntgen, laboratorier och lokaler. Mötena 2020-03-31 och 2025-04-02 har
inget protokoll i poolen, och protokollet från 2024-09-04 ligger som
bilaga. Hjälpmedelsuppdraget som nämnden utför står hos Gemensam nämnd för
hemsjukvård och hjälpmedel och skrivs inte av här.

Driftnämnden Hallands sjukhus har sidorna för 2019–2026. Målen står för
2020–2026 ur verksamhetsplanerna, med utfallet för 2024 ur årsredovisningen
och prognosen för 2025 ur uppföljningsrapport 2, som ligger som bilagor.
Övriga år står utan utfall, eftersom uppföljningarna inte finns i poolen.
Lokaler och investeringar har utrustning, lokaler och sjukhusstrukturen i
Halland med regionstyrelsens och fullmäktiges beslut. Initiativärendena har
nämndens initiativ och motionerna med fullmäktiges beslut, granskningarna
revisorernas grundläggande granskning av nämnden med nämndens svar.
Mötena 2021-09-01 och 2023-09-06 har inget protokoll i poolen, och
fullmäktiges beslut om sjukhusstrukturen 2023-12-06 saknas eftersom
protokollet inte finns där.

Driftnämnden Regionservice har sidorna för 2019–2026. Målen står för
2020–2026 ur verksamhetsplanerna, med utfallet för 2024 ur årsredovisningen
och prognosen för 2026 ur uppföljningsrapport 2. Övriga år följer upp målen
med symboler som inte går att läsa ur poolen och står utan utfall. Lokaler
och investeringar har kök, kontorslokaler, beredskapslager och centrallagret
i Halmstad, överenskommelserna serviceöverenskommelserna,
livsmedelsprinciperna och café- och butiksverksamheten. Redovisningarna har
bland annat den framtida kost- och måltidsförsörjningen, initiativärendena
motionerna med fullmäktiges beslut och granskningarna revisorernas
grundläggande granskning och de fördjupade granskningarna med nämndens svar.
Lokaler som nämnden tar fram åt sjukhusen och ambulansen står hos de
nämnderna.

Driftnämnden Kollektivtrafik har sidorna för 2023–2026; nämnden tog över
verksamheten från Hallandstrafiken AB 2023. Målen står för 2023 och 2025–2026
ur verksamhetsplanerna, med utfallet för 2025 ur årsredovisningen. Planen för
2024 finns inte i poolen, så 2024 står med prognosen ur uppföljningsrapport 2,
och 2023 följs bara upp med indikatorer. Handlingsplanerna har
kollektivtrafikplanerna år för år och det regionala
trafikförsörjningsprogrammet 2026–2030 fram till fullmäktiges beslut,
överenskommelserna trafikavtalen för Öresundstågen, Västtågen och Pågatågen,
Krösatågen, principerna för kommunala tillköp av biljetter och upphandlingen
av busstrafiken i Kungsbacka. Lokaler och investeringar har bussdepån i
Halmstad och nästa generation Öresundståg. Remisser och yttranden har
regionens yttranden över kommunernas detaljplaner, som är avstämda med
Hallandstrafiken, och svaret till Kungsbacka kommun om busstrafiken.
Initiativärendena har motionerna med fullmäktiges beslut. Protokollet från
2023-09-28 ligger som bilaga, och 2026-09-30 och 2026-11-19 har inget
protokoll i poolen än.

Driftnämnden Kultur och skola har målen för 2019–2026: utfallet ur
årsredovisningarna 2019–2025, målen ur verksamhetsplanerna 2020–2026 och
prognosen för 2026 ur uppföljningsrapport 2. För 2019 står målen bara som
årsredovisningen följer upp dem, utan bedömning. Mål som bytt ordalydelse
mellan plan och årsredovisning, eller mellan åren, står ihop i ett spår.
Uppföljningarna har nämndens beslut om årsredovisningar och
uppföljningsrapporter och dragningarna inför verksamhetsplanen. Mötena
2019-10-02, 2020-12-14, 2023-02-15, 2023-10-12, 2025-09-18 och 2026-10-23
har protokollet som bilaga, och 2021-03-18 och 2024-12-31 har inget
protokoll i poolen.

Kultur och skolas övriga sidor går över 2019–2026. Initiativärendena har
motionerna med fullmäktiges beslut och ett initiativärende om
musikutbildningar. Handlingsplanerna har kulturplanerna, kulturstrategierna
och biblioteksplanerna med fullmäktiges beslut, och kriterierna för
kulturstödet. Överenskommelserna har kultursamverkansmodellen med
statsbidragen år för år och överenskommelserna om regional
kulturverksamhet. Lokaler och investeringar har folkhögskolornas,
naturbruksgymnasiets och Teater Hallands lokaler, remisserna nämndens
yttranden till staten och kommunerna och redovisningarna nämndens uppdrag
till förvaltningen och de återkommande verksamhetsberättelserna.
Granskningarna har revisorernas grundläggande granskning och de fördjupade
granskningarna med nämndens svar.

Patientnämnden Halland har sidorna för 2019–2026. Målen står för 2020 och
2023–2026 ur verksamhetsplanerna; planerna för 2019, 2021 och 2022 finns inte
i poolen. Utfallet står för 2025 ur årsrapporten, och för 2023 står målen som
årsrapporten följer upp dem, utan bedömning. Redovisningarna har nämndens
analyser av klagomålen, till exempel den årliga analysen tillsammans med
Inspektionen för vård och omsorg, med driftnämndernas, regionstyrelsens och
fullmäktiges mottagande, kvartalsrapporterna och redogörelserna till
inspektionen. Initiativärendena har ett initiativ om nämndens organisation
och motionen om att redovisa nämndens ärenden för fullmäktige,
granskningarna den grundläggande granskningen och granskningen av
följsamheten till lagen om stöd vid klagomål med nämndens svar, och
överenskommelserna reglementet och samverkansavtalet med kommunerna.
Handlingsplanerna har informationshanterings- och kommunikationsplanen.
Enskilda patientärenden står inte med. Mötena 2020-04-15, 2020-12-02,
2021-12-09 och 2026-09-18 har inget protokoll i poolen, utom 2021-12-09 och
2026-09-18 där protokollet ligger som bilaga.

Lokalbehov, detaljplaner och projekt används inte: de följer en kommuns
lokalplan och planmonopol.
