#!/usr/bin/env bash
# Steg 2 för en kommunfil i delar om 15 minuter. Efter varje del checkas
# det klara in, så att ett fel kostar högst en del (K11, ADR-0088).
# Steg 2 avslutar med kod 4 (MER_I_NASTA_DEL i hamta.py) när delen tog
# slut och kandidater väntar inom budgeten; varje annan kod än 0 och 4
# stoppar körningen.
# Samma kod som kungsbackakommuns .github/nattkorning/hamta_i_delar.sh;
# håll dem lika (K102, ADR-0125, numren i kungsbackakommuns serie).
# Användning: hamta_i_delar.sh <kommunfil> [flaggor till steg 2]
# Kräver START, DEL, GREN och RUNNER_TEMP i miljön.
set -euo pipefail
kommunfil="$1"
shift
while :; do
  kod=0
  python -m kommunhandlingar.hamta "$kommunfil" "$RUNNER_TEMP/arbete" \
    --start "$START" --del 15 "$@" | tee -a "$RUNNER_TEMP/sammanfattning.txt" || kod=$?
  [ "$kod" -eq 0 ] || [ "$kod" -eq 4 ] || exit "$kod"
  "$(dirname "$0")/spara.sh" "Nattkörning $(date -u +%F), $DEL, $(date -u +%H:%M)"
  [ "$kod" -eq 4 ] || exit 0
done
