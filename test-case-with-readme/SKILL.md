---
name: test-case-with-readme
description: 'Use when: the user creates a new test case, plans to write a test, or asks to generate a readme for an existing test. Helps with: planning and documenting test files with structured purpose, status, coverage, and manual steps. Applies to: any test creation workflow or existing test files like .py, .cxx, etc.'
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

## Output
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

## Constraints
- Do not modify the original test code file.
- Ensure the generated file uses the exact base name of the test file, appending `_readme.md` to it (e.g. `test_login.cxx` -> `test_login_readme.md`).
- Analyze the test code to infer the content of the sections. If some details are not inferable, use placeholders or prompt explicitly.

## One More Thing
If anything is unclear, missing, or conflicting, stop and ask the user before proceeding.

## How
1. **Identify the File & Intent**: Determine the target test file name and whether the test is already written, or if it is being planned/newly created.
2. **Determine the Output File Name**: Strip the file extension and append `_readme.md` (e.g. `test_user_story.py` becomes `test_user_story_readme.md`).
3. **Analyze or Plan the Test Context**: 
   - If the test code does not exist yet (planning phase), infer or ask the user what the test's "Purpose" and "Covered" areas should be.
   - If the test exists, review the provided test code to extract this information.
4. **Generate the Markdown**: Draft the content following the exact Output format. If the test is unwritten, mark "Status" as "Draft" or "Planned".
5. **Write the File**: Save the generated documentation to the target `.md` file beside the test case.
