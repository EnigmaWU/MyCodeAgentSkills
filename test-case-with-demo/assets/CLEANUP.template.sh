#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DEMO_ROOT="$SCRIPT_DIR"
WORK_DIR="${DEMO_WORK_DIR:-$DEMO_ROOT/.demo-work}"
OUTPUT_DIR="$DEMO_ROOT/outputs"

printf 'Removing demo work directory: %s\n' "$WORK_DIR"
rm -rf "$WORK_DIR"

if [[ "${KEEP_DEMO_OUTPUTS:-0}" != "1" ]]; then
  printf 'Removing demo outputs: %s\n' "$OUTPUT_DIR"
  rm -rf "$OUTPUT_DIR"
else
  printf 'Keeping demo outputs because KEEP_DEMO_OUTPUTS=1\n'
fi

printf 'Cleanup complete.\n'
