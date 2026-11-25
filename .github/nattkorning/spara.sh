#!/usr/bin/env bash
# Checkar in det klara: datakontrollerna, bara textfiler under data/ och
# versioner/, och en commit som pushas på körningens gren (K11, ADR-0088).
# Varje fel stoppar körningen; det som redan pushats står kvar på grenen.
# Samma kod som kungsbackakommuns .github/nattkorning/spara.sh (K102,
# ADR-0125), utom pushen. Där har jobbet bara läsrätt och PR-jobbet
# pushar (K95, ADR-0118); här pushar jobbet självt, och bara när något
# nytt checkats in.
# Användning: spara.sh <commit-meddelande>
# Kräver GREN i miljön.
set -euo pipefail
python -m kommunhandlingar.datakontroll data
git add -A
if git -c core.quotePath=false diff --cached --no-renames --name-only | grep -Ev '^(data|versioner)/'; then exit 1; fi
if git diff --cached --numstat | grep '^-'; then exit 1; fi
git diff --cached --quiet && exit 0
git -c user.name="github-actions[bot]" \
  -c user.email="41898282+github-actions[bot]@users.noreply.github.com" \
  commit -q -m "$1"
git push -q origin "HEAD:refs/heads/$GREN"
