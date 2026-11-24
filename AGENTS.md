# AGENTS.md – regionhalland

Region Hallands politiska handlingar som Markdown och CSV. Repot har ingen
egen kod: det kör koden i
[moggleif/kungsbackakommun](https://github.com/moggleif/kungsbackakommun)
på den commit som står i `kodversion.txt`. Vad repot innehåller och hur det
körs står i [README.md](README.md).

Det här är den stående vägledningen för den som arbetar här, människa som
AI-agent. Den säger bara det som är eget för repot.

## Kungsbackakommuns vägledning gäller

Läs [kungsbackakommuns AGENTS.md](https://github.com/moggleif/kungsbackakommun/blob/main/AGENTS.md).
Huvudregeln, reglerna som inte förhandlas och arbetsflödet i faser gäller
här också, med fasernas filer där. Det som skiljer:

- **Ingen kod här.** Saknas något görs koden i kungsbackakommun mer
  generell, och en ny version tas in här.
- **Krav och beslut** får nummer i kungsbackakommuns serie (K och ADR) och
  skrivs i PR-texten här, eftersom repot inte har egna dokument. Kontrollera
  att numret är ledigt där, också i öppna PR:er.

## Vem skriver vad

- **`data/` och `versioner/`** skrivs av koden, i första hand nattkörningen.
  Ett dokument rättas för hand bara som en granskning enligt
  [K34](https://github.com/moggleif/kungsbackakommun/blob/main/docs/02-KRAV.md#k34--dokument-granskas-för-hand-och-granskningen-står-kvar).
- **Spårfilerna** (`mal/`, `uppfoljningar/` och de andra i
  [Sidorna över tid](README.md#sidorna-över-tid)) skrivs för hand ur
  handlingarna. Varje text ska stå på källans sida.
- **`kodversion.txt`** byts i en egen PR, med jämförelsen i
  [README](README.md#jämförelse-med-nuvarande-läge).
- **Inställningarna** (`kommuner/regionhalland.toml`, `hamtning.toml`) och
  arbetsflödena i `.github/workflows/` ändras för hand.

## Grönt före merge

- Kontrollen **Datakontrollerna** på PR:en.
- Ändras en spårfil eller `kodversion.txt`: webbplatsen byggd lokalt enligt
  [jämförelsen](README.md#jämförelse-med-nuvarande-läge), eftersom bygget
  annars prövar spårfilerna först efter merge.

## Agentfiler

`CLAUDE.md` importerar den här filen. Ändra bara här.
