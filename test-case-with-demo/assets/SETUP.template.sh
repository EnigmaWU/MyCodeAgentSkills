#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DEMO_ROOT="$SCRIPT_DIR"
WORK_DIR="${DEMO_WORK_DIR:-$DEMO_ROOT/.demo-work}"
FIXTURE_DIR="$DEMO_ROOT/fixtures"
OUTPUT_DIR="$DEMO_ROOT/outputs"

printf 'Preparing demo work directory: %s\n' "$WORK_DIR"
rm -rf "$WORK_DIR"
mkdir -p "$WORK_DIR" "$OUTPUT_DIR"

if [[ -d "$FIXTURE_DIR" ]]; then
  mkdir -p "$WORK_DIR/fixtures"
  cp -R "$FIXTURE_DIR"/. "$WORK_DIR/fixtures/"
fi

# TODO: Create any local repositories, sample protocol files, config files,
# or generated inputs required by the UserGuide workflow.

printf 'Setup complete. Outputs will be written under: %s\n' "$OUTPUT_DIR"
