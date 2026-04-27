# Demo Test Case: {{DEMO_NAME}}

## Purpose
Describe the user workflow this demo proves, which user story it satisfies, and why it matters.

## Status
Draft | Ready | Passing | Manual-only | Blocked

## UserGuide and UserStories Coverage
| Source | Section, story, or AC | Demo evidence |
| --- | --- | --- |
| {{USER_GUIDE_FILE}} | {{SECTION_OR_HEADING}} | {{HOW_THE_DEMO_SHOWS_USAGE}} |
| {{USER_STORIES_FILE}} | {{US_ID}} / {{AC_ID}} | {{HOW_THE_DEMO_SATISFIES_THE_STORY}} |

## Demo Flow
1. `SETUP.sh` prepares local fixtures and work directories.
2. `RUN.sh` executes the user-facing workflow exactly as documented.
3. The demo test or manual check compares actual outputs with `expected/`, the UserGuide contract, and the linked UserStories/AC expected outcomes.
4. `CLEANUP.sh` removes generated work when the evidence is no longer needed.

## Files
| Path | Purpose |
| --- | --- |
| `ManualInstruction.md` | Human-readable runbook for setup, execution, verification, and cleanup. |
| `SETUP.sh` | Creates demo work directories and fixture state. |
| `RUN.sh` | Runs the documented command or workflow. |
| `CLEANUP.sh` | Removes generated demo work. |
| `demo_manifest.json` | Machine-readable traceability and artifact manifest. |
| `fixtures/` | Checked-in input data for the demo. |
| `expected/` | Checked-in expected outputs or comparison data. |
| `outputs/` | Generated outputs from local demo runs. |

## Automated Check
```bash
./SETUP.sh
./RUN.sh
{{TEST_COMMAND}}
```

## Manual Run
See `ManualInstruction.md`.

## Notes
- Keep this demo focused on one visible UserGuide workflow and its matching UserStories/AC.
- Add separate demo packages for materially different workflows.
