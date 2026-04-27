# ManualInstruction: {{DEMO_NAME}}

## Purpose
Explain what the demo shows from a user's point of view and which UserStories/AC it satisfies.

## Prerequisites
- Repository is checked out locally.
- Required tool or command is available: `{{COMMAND_UNDER_TEST}}`.
- Required runtime is installed: `{{RUNTIME_OR_PACKAGE_MANAGER}}`.
- Run commands from this demo directory unless a step says otherwise.

## Setup
```bash
./SETUP.sh
```

Expected setup result:
- Demo work directory exists.
- Fixtures are copied or generated.
- Required input files are present.

## Run
```bash
./RUN.sh
```

Expected run result:
- Command exits with status `0`.
- UserGuide output artifact is created at `{{EXPECTED_OUTPUT_PATH}}`.
- Logs are written to `outputs/` or stderr as documented.

## Expected Result
Describe the observable success criteria. Include exact filenames, important JSON fields, metric values, stdout/stderr behavior, linked UserStories/AC outcomes, or screenshots only when those are part of the UserGuide/UserStories contract.

## Troubleshooting
| Symptom | Likely cause | Fix |
| --- | --- | --- |
| Command not found | Tool is not built or not on `PATH` | Build the project or set `COMMAND_UNDER_TEST`. |
| Missing fixture | `SETUP.sh` was not run | Run `./SETUP.sh` again. |
| Output differs | Implementation or UserGuide drift | Compare `outputs/` with `expected/` and update only after confirming the contract changed. |

## Cleanup
```bash
./CLEANUP.sh
```

Cleanup should remove generated work directories and outputs while preserving checked-in fixtures and expected files.

## Evidence
Capture these items when reporting or reviewing the demo:
- Commands executed.
- Exit codes.
- Output artifact paths.
- Important output snippets or diff summary.
- Linked User Story ID and AC ID.
- Any skipped or blocked validation step.
