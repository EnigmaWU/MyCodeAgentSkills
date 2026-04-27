---
name: test-case-with-demo
description: 'Use when: the user asks to create a demo test case, example test, UserGuide demo, UserStories demo, manual demo, setup-backed test case, or explicitly invokes test-case-with-demo. Helps with: building an end-to-end demonstration test package that shows how to use a feature according to the UserGuide and how it satisfies UserStories/acceptance criteria, including setup scripts, manual instructions, fixtures, expected outputs, and traceability. Applies to: documentation-oriented P4 demo/example tests for CLIs, APIs, tools, workflows, repository user guides, and user story specifications.'
---

# Test Case with Demo

## Who
Developers, QA engineers, documentation maintainers, or agents who need a demo-style test case that teaches a real user workflow while still being verifiable.

## What
Create a self-contained demo test package for one UserGuide workflow and its matching UserStories/acceptance criteria. The package demonstrates how a user sets up inputs, runs the feature, observes expected outputs, and cleans up afterward. It should include setup and run scripts, `ManualInstruction.md`, traceability back to the UserGuide, UserStories, and acceptance criteria, fixture data, expected artifacts, and at least one runnable check when the project has a test framework.

Demo tests are P4 Addons: they are for documentation, onboarding, and workflow verification. They complement but do not replace focused P1/P2/P3 automated tests that prove individual acceptance criteria.

## When
- The user asks for a "demo test case", "example test", "manual demo", "UserGuide demo", "test-case-with-demo", or "setup script plus ManualInstruction".
- A feature already has a UserGuide or README workflow and needs a runnable example showing how to use it.
- A CLI, API, or workflow is hard to understand from unit tests alone and needs an end-to-end demonstration.
- A fork or sample implementation needs a lightweight proof that it satisfies a visible UserGuide path and the related UserStories/AC scenarios.
- Do not use this skill for a narrow unit test without a user-facing workflow. Use `test-case-with-readme` or regular TDD instead.

## Where
- Start from the project's user-facing docs, especially `README_UserGuide.md`, `README_UserStories.md`, API docs, CLI docs, or equivalent files. Treat UserGuide and UserStories as paired sources when both exist.
- Place the generated demo package in the repository's existing demo/test/example location. If no convention exists, use `tests/demo/<demo-name>/`.
- Use bundled templates from this skill's `assets/` directory as starting points, then adapt them to the target project and language.

## Why
- A demo test makes the UserGuide executable enough that future maintainers can verify it still works.
- Setup scripts remove hidden prerequisites and make the workflow repeatable.
- Manual instructions help humans reproduce the same behavior when automation fails or when the demo is part of onboarding.
- Traceability prevents examples from drifting away from UserGuide behavior, user stories, and acceptance criteria.

## Inputs
- Required: the UserGuide or workflow documentation to demonstrate.
- Required when available: matching UserStories and acceptance criteria for the workflow.
- Required: the feature, command, API, or workflow name.
- Recommended: related user stories or acceptance criteria.
- Recommended: existing test framework, fixture conventions, and project setup commands.
- Optional: target demo name, preferred output folder, platform constraints, and whether the demo should be fully automated or manual-first.

## Output
- A demo package, normally shaped like:

  ```text
  tests/demo/<demo-name>/
    README.md
    ManualInstruction.md
    SETUP.sh
    RUN.sh
    CLEANUP.sh
    demo_manifest.json
    fixtures/
    expected/
    outputs/        # generated, ignored or cleaned when appropriate
    test_<demo_name>.<ext>
  ```

- A traceability section linking the demo to UserGuide sections, User Story IDs, and AC IDs when available.
- Idempotent setup/run/cleanup scripts that work from a clean checkout.
- Manual instructions with prerequisites, setup, run, expected result, troubleshooting, cleanup, and evidence to capture.
- Validation evidence showing which scripts or tests were run.

## Constraints
- Do not invent CLI flags, files, outputs, or product behavior. Read the UserGuide, UserStories, and existing implementation before writing the demo.
- Do not treat a UserGuide-only usage example as sufficient when UserStories/AC exist. The demo must show both how to use the workflow and which user-facing requirement it satisfies.
- Keep the demo small and deterministic. Prefer local fixture repositories, sample JSON, temporary directories, and generated outputs over network dependencies.
- Scripts must be idempotent, fail fast, and avoid destructive actions outside the demo directory or explicitly configured temp directory.
- `ManualInstruction.md` must be understandable without reading the agent conversation.
- Keep generated outputs out of source control unless they are intentionally checked-in expected fixtures.
- If the feature is not implemented yet, create a planned demo package and mark the executable test as RED or blocked instead of pretending it passes.

## One More Thing
If anything is unclear, missing, or conflicting, stop and ask the user before proceeding.

## How

### Phase 1: Read the User Workflow
1. Read the relevant UserGuide, README, and UserStories completely enough to understand the intended workflow and requirement intent.
2. Extract the exact user-visible command, API call, input files, output files, and success criteria from the UserGuide.
3. Extract the matching AS A / I WANT / SO THAT story and GIVEN / WHEN / THEN acceptance criteria from the UserStories.
4. Identify the smallest demo scenario that proves both the workflow and the matching story/AC. Prefer a happy-path demo first, then add edge demos only if the UserGuide or UserStories require them.
5. Record traceability: UserGuide section names, user story IDs, AC IDs, and any protocol or contract files involved.

### Phase 2: Design the Demo Package
1. Choose a clear demo name such as `aggregate-core-metrics-demo` or `cli-basic-usage-demo`.
2. Follow the project's existing test or example layout. If none exists, create `tests/demo/<demo-name>/`.
3. Copy or adapt these bundled templates:
   - `assets/README.template.md` to `README.md`.
   - `assets/ManualInstruction.template.md` to `ManualInstruction.md`.
   - `assets/SETUP.template.sh` to `SETUP.sh`.
   - `assets/RUN.template.sh` to `RUN.sh`.
   - `assets/CLEANUP.template.sh` to `CLEANUP.sh`.
   - `assets/demo_manifest.template.json` to `demo_manifest.json`.
   - `assets/test_case.template.md` as the design source for the automated demo test.
4. Create `fixtures/` for demo inputs and `expected/` for expected outputs or comparison data.

### Phase 3: Build Repeatable Scripts
1. Make `SETUP.sh` create or copy everything needed for the demo into a local work directory.
2. Make `RUN.sh` execute the user-facing workflow exactly as the UserGuide describes it.
3. Make `CLEANUP.sh` remove temporary work without deleting checked-in fixtures or expected results.
4. Use `set -euo pipefail`, derive paths from the script location, and print concise status messages.
5. Avoid hard-coded absolute paths. If a tool path is needed, accept it through an environment variable and document it in `ManualInstruction.md`.

### Phase 4: Write the Demo Test
1. Use the repository's existing test framework and language when available.
2. Structure the test around SETUP -> BEHAVIOR -> VERIFY -> CLEANUP.
3. Verify user-visible outputs, not private implementation details.
4. Keep the demo broad but shallow. It should prove the workflow from a user's perspective, not exhaust every branch.
5. If automation is not practical, write the test spec and manual verification path clearly, and mark the status as manual-only.

### Phase 5: Validate and Report
1. Run `SETUP.sh`, `RUN.sh`, and the demo test when possible.
2. Run this skill's validator when a generated demo directory exists:

   ```bash
    python3 .github/skills/test-case-with-demo/scripts/check_demo_case.py tests/demo/<demo-name>
   ```

3. Compare actual outputs with `expected/`, the UserGuide's output contract, and the linked UserStories/AC expected outcomes.
4. Update the demo status in `README.md`, `ManualInstruction.md`, and `demo_manifest.json`.
5. Report what was created, which UserGuide path and UserStories/AC it demonstrates, and which commands/tests were run.

## Resources
- `assets/README.template.md` - demo package README template.
- `assets/ManualInstruction.template.md` - manual runbook template.
- `assets/SETUP.template.sh` - setup script template.
- `assets/RUN.template.sh` - run script template.
- `assets/CLEANUP.template.sh` - cleanup script template.
- `assets/demo_manifest.template.json` - traceability manifest template.
- `assets/test_case.template.md` - demo test design template.
- `scripts/check_demo_case.py` - lightweight validator for generated demo packages.

## Validation
1. Verify the skill frontmatter has `name: test-case-with-demo` and a quoted `description`.
2. Verify the generated demo contains `README.md`, `ManualInstruction.md`, `SETUP.sh`, `RUN.sh`, `CLEANUP.sh`, and `demo_manifest.json`.
3. Verify `ManualInstruction.md` contains Purpose, Prerequisites, Setup, Run, Expected Result, Troubleshooting, Cleanup, and Evidence sections.
4. Verify the demo maps to real UserGuide sections, User Story IDs, and AC IDs when available.
5. Run the generated scripts and automated test when possible. If not possible, record exactly what blocked execution.
