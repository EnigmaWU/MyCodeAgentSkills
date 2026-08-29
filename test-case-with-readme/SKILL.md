---
name: test-case-with-readme
description: >
  WHEN/WHERE/WHO: [Scheduling: Use when: the user creates a new test case, plans to write a test, or asks to generate a readme for an existing test. Applies to: any test creation workflow or existing test files like ]
  HOW: [Structural: Helps with: planning and documenting test files with structured purpose, status, coverage, and manual steps]
  WHY: [Scheduling: Provides structured workflow execution to prevent errors and ensure standards.]
---

# Test Case with Readme

## Who
Developers, QA engineers, or agents who need to document individual test cases with a consistent structure.

## What
Generates a companion markdown readme file for a given test case file. For a test file named `test_something.ext` (e.g., `test_user_story.py`), it creates a corresponding `test_something_readme.md` (e.g., `test_user_story_readme.md`). The readme includes specific structured sections: Purpose, Status, Covered, and Manual. This skill can be used to defensively document existing tests, or proactively as a planning tool to design a test before its code is written.

## When
- A new test case file is created by the user or an agent.
- The user is planning or about to write a new test case, triggering a "readme first" planning approach.
- The user asks to "create a readme for a test case".
- The user provides an existing test file and asks for its documentation.
- The user explicitly invokes the `test-case-with-readme` skill.

## Where
- The generated readme file should be placed in the same directory as the target test file, unless the user specifies otherwise.

## Why
- Promotes test-planning and Test-Driven Development (TDD) by formalizing the test's intent and scope before implementation.
- Keeps test documentation consistent across different languages and frameworks.
- Helps track the status, scope, and coverage of individual tests.
- Provides a clear place for manual execution steps or environmental setup requirements if needed.

## Inputs
- **Test case file** (required): The path or content of the test file (e.g., `test_user_story.py`).
- **Additional context** (optional): Any specific details about the purpose, status, coverage, or manual steps the user wants to include.

## Output (Logical Evidence)
A markdown file named `<test_filename_without_extension>_readme.md` (e.g., `test_user_story_readme.md`) with the following structure:

```markdown
# Test Case: <Test Name>

## Purpose
<Describe what this test case is verifying and the business logic or edge case it targets.>

## Status
<Current status of the test: e.g., Draft, Implemented, Passing, Failing, Flaky>

## Covered
<List of requirements, user stories, functions, or specific code paths explicitly covered by this test.>

## Manual
<Steps required to run or reproduce this test manually, including any necessary manual setup or teardown.>
```

## Example

### Target Test File
`test_payment_gateway.py` (Not yet written, planning phase)

### Output (`test_payment_gateway_readme.md`)
```markdown
# Test Case: test_payment_gateway

## Purpose
This test verifies the payment gateway's integration with the Stripe API, focusing on successful charges and graceful handling of declined cards.

## Status
Planned / Draft

## Covered
- Successful charge flow via `StripeClient.charge()`.
- Error handling for `card_declined` API exceptions.
- User story: "Checkout with Credit Card".

## Manual
1. Ensure the `STRIPE_TEST_KEY` environment variable is exported.
2. Provide a mock credit card number.
3. Run with `pytest test_payment_gateway.py -v`.
```

## Optimization Readiness
- **Failure Signals**: The companion file is misnamed, the readme invents purpose or coverage not supported by the test, lifecycle status is inaccurate, or manual steps become generic filler rather than useful guidance.
- **Evidence To Collect**: Source test files, generated readmes, inferred-purpose notes, and examples where coverage or manual details were accurate versus guessed.
- **Safe Mutation Boundaries**: Refine filename derivation, section prompts, inference guidance, and placeholder policy without changing the core one-readme-per-test documentation workflow.
- **Acceptance Criteria**: Accept revisions only if the generated file name is exact, the content reflects the real or planned test intent faithfully, and any inferred details remain clearly grounded in available context.
- **Rejected Revision Handling**: Record bad filename patterns, invented-purpose drafts, and low-value manual-step templates so they are not reused.
- **Transfer Check**: Verify the workflow still works for both planned tests and already-implemented tests across multiple languages.
- **Stop Rule**: If the available test context is too thin to describe purpose or coverage responsibly, stop and ask instead of fabricating details.

## Constraints (Logical Boundaries)
- Do not modify the original test code file.
- Ensure the generated file uses the exact base name of the test file, appending `_readme.md` to it (e.g. `test_login.cxx` -> `test_login_readme.md`).
- Analyze the test code to infer the content of the sections. If some details are not inferable, use placeholders or prompt explicitly.

## One More Thing
If anything is unclear, missing, or conflicting, stop and ask the user before proceeding.

## How (Structural Workflow)
1. **Identify the File & Intent**: Determine the target test file name and whether the test is already written, or if it is being planned/newly created.
2. **Determine the Output File Name**: Strip the file extension and append `_readme.md` (e.g. `test_user_story.py` becomes `test_user_story_readme.md`).
3. **Analyze or Plan the Test Context**: 
   - If the test code does not exist yet (planning phase), infer or ask the user what the test's "Purpose" and "Covered" areas should be.
   - If the test exists, review the provided test code to extract this information.
4. **Generate the Markdown**: Draft the content following the exact Output format. If the test is unwritten, mark "Status" as "Draft" or "Planned".
5. **Write the File**: Save the generated documentation to the target `.md` file beside the test case.

## Review In Mind (ReviewInMindGenie)

Before delivering, activate the ReviewInMindGenie: stop authoring, switch to a skeptical reviewer, and critique the artifact as if someone else had produced it.

1. **Review Against Own Rules**: Re-read the output against this skill's `What`, `Constraints (Logical Boundaries)`, and `Validation` criteria. Check each rule explicitly; do not assume it passed because it was easy to write.
2. **Classify Findings**: Label each defect as BLOCKER (output unusable), MAJOR (violates a core rule), or MINOR (polish/consistency).
3. **Fix or Escalate**: Fix BLOCKER and MAJOR findings immediately when the fix is unambiguous. After each fix, re-check the affected criteria. If a finding cannot be fixed without new input (missing evidence, conflicting requirements, or a user decision), do not guess — report it as an open question or known gap.
4. **Deliver with a Review Note**: Present the output with a short note: what was checked, what was fixed, and what remains as a known gap. Never present an unreviewed artifact as final.

Review lens for this skill:
- Does the readme contain Purpose, Status, Covered, and Manual that match the test code?
- Is the Status accurate (Draft/Planned vs. actual)?
- Would the readme help a reader understand what the test verifies and how to run it manually?
