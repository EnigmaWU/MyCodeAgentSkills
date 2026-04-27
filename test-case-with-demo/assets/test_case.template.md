# Demo Test Design: {{DEMO_NAME}}

## Traceability
- UserStories file: {{USER_STORIES_FILE}}
- User story: {{US_ID_OR_NAME}}
- Acceptance criteria: {{AC_ID_OR_NAME}}
- UserGuide file: {{USER_GUIDE_FILE}}
- UserGuide section: {{USER_GUIDE_SECTION}}

## Test Case
[@{{AC_ID}},{{US_ID}}]
TC-Demo-1:
  @[Name]: verifyUserGuideWorkflow_byRunningDemoScripts_expectDocumentedOutputs
  @[Purpose]: Demonstrate the documented workflow and prove the linked UserStories/AC outcome.
  @[Brief]: Run setup, execute the user-facing command, then compare observable outputs with the UserGuide contract and UserStories/AC expected result.
  @[Expect]: Command succeeds, required artifacts exist, important output values match `expected/`, and the linked AC is satisfied.

## Implementation Pattern
Use the repository's existing test framework when available.

```text
SETUP
- Run or inline the behavior of SETUP.sh.
- Prepare fixture paths and output directories.

BEHAVIOR
- Run the documented command or API workflow.

VERIFY
- Check exit code.
- Check expected files exist.
- Check key output fields or values.
- Check logs follow the UserGuide contract when relevant.
- Check the linked UserStories/AC expected outcome is satisfied.

CLEANUP
- Run CLEANUP.sh or remove temporary test directories.
```

## Manual Fallback
If the workflow cannot be automated in this repository yet, keep this test design and mark the demo status as `Manual-only` or `Blocked` in `README.md` and `demo_manifest.json`.
