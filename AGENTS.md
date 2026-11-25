# AGENTS.md – regionhalland

Region Hallands politiska handlingar som Markdown och CSV. Vad repot
innehåller, var koden finns och hur det körs står i [README.md](README.md).

Det här är den stående vägledningen för den som arbetar här, människa som
AI-agent. Den säger bara det som är eget för repot.

## Kungsbackakommuns vägledning gäller

Läs [kungsbackakommuns AGENTS.md](https://github.com/moggleif/kungsbackakommun/blob/main/AGENTS.md).
Huvudregeln, reglerna som inte förhandlas och arbetsflödet i faser gäller
här också, med fasernas filer i
[`.claude/`](https://github.com/moggleif/kungsbackakommun/tree/main/.claude)
där. Repot har inga egna tester; att en ändring inte ändrar något visas med
[jämförelsen](README.md#jämförelse-med-nuvarande-läge).

## Vem skriver vad

- **`data/` och `versioner/`** skrivs av koden, i första hand nattkörningen.
  Ett dokument rättas för hand bara som en granskning enligt
  [K34](https://github.com/moggleif/kungsbackakommun/blob/main/docs/02-KRAV.md#k34--dokument-granskas-för-hand-och-granskningen-står-kvar).
- **Spårfilerna** skrivs för hand, som [Sidorna över tid](README.md#sidorna-över-tid)
  beskriver.
- **`kodversion.txt`** byts som [Körningen](README.md#körningen) beskriver.
- **Inställningarna** (`kommuner/regionhalland.toml`, `hamtning.toml`) och
  arbetsflödena och mallarna i `.github/` ändras för hand.

## Grönt före merge

- Kontrollen **Datakontrollerna** på PR:en. Den bygger också webbplatsen
  och prövar då spårfilerna, utom på nattkörningens PR.

## Agentfiler

`CLAUDE.md` importerar den här filen. Ändra bara här.
