#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

if ! command -v docker >/dev/null 2>&1; then
  echo "[analyze-in-docker] Error: docker is required." >&2
  exit 1
fi

exec docker compose run --rm dev bash -lc '
  set -euo pipefail
  echo "[devtools] Toolchain summary"
  clang --version | head -n 1
  make --version | head -n 1
  python3 --version
  echo "[devtools] Generating tags/cscope"
  make tags cscope
'
