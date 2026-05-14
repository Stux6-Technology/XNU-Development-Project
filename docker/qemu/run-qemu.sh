#!/usr/bin/env bash
set -euo pipefail

ISO_PATH="${ISO_PATH:-/vm/iso/kernel.iso}"
RAM_MB="${RAM_MB:-4096}"
CPUS="${CPUS:-4}"

if [[ ! -f "$ISO_PATH" ]]; then
  echo "[qemu] ISO not found: $ISO_PATH" >&2
  echo "[qemu] Put your ISO under ./docker/iso and set ISO_PATH if needed." >&2
  exit 1
fi

exec qemu-system-x86_64 \
  -m "$RAM_MB" \
  -smp "$CPUS" \
  -cdrom "$ISO_PATH" \
  -boot d \
  -nographic \
  -serial mon:stdio
