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
| `.github/workflows/nattkorning.yml` | Nattkörningen, och versionen av kommunhandlingar den kör.   |
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
`nattkorning.yml`, och kör samma upptäckt och steg 2 som för kommunerna, med
samma tidsbudget. Den checkar in på en egen gren och öppnar en PR, som mergas
när kontrollen gått igenom. Det nyaste mötet hämtas först över alla organ.

En ny version av kommunhandlingar tas in genom att byta commit i
`nattkorning.yml` i en PR.

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
2018–2026, ur verksamhetsplanerna (2020 ur årsredovisningen, eftersom
planen inte finns i poolen; 2024 bara nämndens egna utvecklingsområden ur
beslutsförslaget; 2026 ur planen nämnden fick i oktober 2025). Utfallet står
för 2020–2022 och 2025. Årsredovisningarna 2023 och 2024 har tabeller som
inte går att läsa mål för mål, och 2018–2019 följs bara upp med indikatorer.
Motionerna har fullmäktiges beslut där beslutet finns bland nämndens
handlingar; resten kommer när regionfullmäktige är hämtat.
Lokalbehov, detaljplaner och projekt används inte: de följer en kommuns
lokalplan och planmonopol.
