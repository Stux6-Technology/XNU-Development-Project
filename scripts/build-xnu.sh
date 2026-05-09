#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

SDKROOT="${SDKROOT:-/}"
ARCH_CONFIGS="${ARCH_CONFIGS:-X86_64}"
KERNEL_CONFIGS="${KERNEL_CONFIGS:-DEVELOPMENT}"
MAKEJOBS="${MAKEJOBS:-}"

if [[ "$(uname -s)" != "Darwin" ]]; then
  echo "[build-xnu] Error: Full XNU kernel build must run on macOS (Darwin host)." >&2
  exit 1
fi

if ! command -v xcodebuild >/dev/null 2>&1; then
  echo "[build-xnu] Error: xcodebuild not found. Install Xcode Command Line Tools first." >&2
  exit 1
fi

cd "$ROOT_DIR"

cmd=(make "SDKROOT=${SDKROOT}" "ARCH_CONFIGS=${ARCH_CONFIGS}" "KERNEL_CONFIGS=${KERNEL_CONFIGS}")
if [[ -n "$MAKEJOBS" ]]; then
  cmd+=("MAKEJOBS=${MAKEJOBS}")
fi

printf '[build-xnu] Running: %q ' "${cmd[@]}"
printf '\n'
"${cmd[@]}"
