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
