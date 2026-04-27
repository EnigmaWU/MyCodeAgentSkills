#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DEMO_ROOT="$SCRIPT_DIR"
WORK_DIR="${DEMO_WORK_DIR:-$DEMO_ROOT/.demo-work}"
OUTPUT_DIR="$DEMO_ROOT/outputs"
COMMAND_UNDER_TEST="${COMMAND_UNDER_TEST:-{{COMMAND_UNDER_TEST}}}"

if [[ ! -d "$WORK_DIR" ]]; then
  printf 'Missing work directory: %s\nRun ./SETUP.sh first.\n' "$WORK_DIR" >&2
  exit 2
fi

mkdir -p "$OUTPUT_DIR"

printf 'Running demo command: %s\n' "$COMMAND_UNDER_TEST"

# TODO: Replace the placeholder command below with the exact UserGuide workflow.
# Example shape for a CLI:
# "$COMMAND_UNDER_TEST" \
#   --repoUrl "$WORK_DIR/repo" \
#   --repoBranch main \
#   --startTime 2026-01-01T00:00:00Z \
#   --endTime 2026-04-01T00:00:00Z \
#   --genCodeDescDir "$WORK_DIR/genCodeDesc" \
#   --outputDir "$OUTPUT_DIR" \
#   > "$OUTPUT_DIR/stdout.txt" \
#   2> "$OUTPUT_DIR/stderr.log"

printf 'TODO: implement RUN.sh for this demo.\n' >&2
exit 3
