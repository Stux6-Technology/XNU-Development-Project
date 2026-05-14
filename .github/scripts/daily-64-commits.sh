#!/usr/bin/env bash
set -euo pipefail

COUNT="${COUNT:-64}"
TARGET_FILE=".github/commit-bot/daily-activity.log"

mkdir -p "$(dirname "$TARGET_FILE")"

touch "$TARGET_FILE"

for i in $(seq 1 "$COUNT"); do
  ts="$(date -u +"%Y-%m-%dT%H:%M:%SZ")"
  echo "$ts | automated activity commit #$i" >> "$TARGET_FILE"

  git add "$TARGET_FILE"
  git commit -m "chore(activity): daily commit $i/$COUNT" >/dev/null

done
