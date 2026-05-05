---
name: comment-alive-test-driven-development
description: 'Use when: writing new tests from scratch, designing verification for a new feature or module, applying CaTDD, starting a new test file with comment-alive design. Helps with: creating structured test files using CaTDD (Comment-alive Test-Driven Development) methodology with US/AC/TC design, priority-based test categories, and LLM-friendly verification comments. Applies to: new test files for UnitTesting, SysTesting, and UserTesting in any language.'
---

# Comment-alive Test-Driven Development (CaTDD)

## Who
Developers and agents who want to write new tests from scratch using CaTDD (Comment-alive Test-Driven Development), where structured comments define verification design before code is written. Applies to any testing level: unit tests, system tests, or user acceptance tests.

## What
Apply the CaTDD methodology to create a new test file that serves as a living design document. The main deliverables are:
- An **OVERVIEW** section describing what, where, and why the file tests.
- **User Stories (US)** expressing value from the user perspective.
- **Acceptance Criteria (AC)** in GIVEN/WHEN/THEN format making stories testable.
- **Test Case (TC) specifications** with structured metadata (`@[Name]`, `@[Purpose]`, `@[Brief]`, `@[Expect]`).
- **Test implementations** following the four-phase pattern (SETUP → BEHAVIOR → VERIFY → CLEANUP).
- A **TODO/implementation tracking section** with status markers (⚪ TODO → 🔴 RED → 🟢 GREEN).
- **Priority classification** (P1 Functional → P2 Design → P3 Quality → P4 Addons).

The result is a self-contained design document that is readable by humans, parseable by LLMs, and verified by tests.

## When
- The user says "use CaTDD", "write tests with CaTDD", "create a new test file with comment-alive design", "apply comment-alive TDD", or "start TDD with CaTDD".
- A new feature, module, or component needs tests written from scratch.
- The user wants structured US/AC/TC verification design embedded in a new test file.
- The user wants LLM-friendly test design for unit tests, system tests, or user acceptance tests.
- Do **not** use this skill to convert or refactor *existing* test files (use the `UnitTesting-convert2CaTDD` skill for that).
- Do **not** apply this skill to production source files, configuration files, or build scripts.

## Where
- New test files of any language (C/C++, Python, Go, Java, TypeScript, etc.).
- The test file may target any level: unit tests (`UT_*.cxx`), system tests (`ST_*.py`), or user tests (`UAT_*.ts`).
- The output is placed in the project's test directory following the project's naming conventions.
- Reference materials are bundled in `references/` alongside this skill.

## Why
- CaTDD ensures verification is designed before code is written, producing higher-quality tests.
- Structured US/AC/TC comments give LLMs the context needed to generate correct test and production code.
- The priority framework (P1–P4) guides what to test first based on business value and risk.
- Comments live in the test file and evolve with the code, so design intent never goes stale.
- The result is a single source of truth that bridges human intent and machine-executable tests.

## Inputs
- **Feature or module description** (required): what functionality the new tests should verify.
- **API headers, interface definitions, or specifications** (recommended): enables accurate TC design.
- **Target language and test framework** (optional): defaults to the project's existing choices.
- **Testing level** (optional): UnitTesting, SysTesting, or UserTesting — affects OVERVIEW framing.
- **Priority focus** (optional): e.g., "reliability-critical" promotes Fault; "high-concurrency" promotes Concurrency.

## Output
- A new test file in CaTDD format with all required sections (OVERVIEW, DESIGN, IMPLEMENTATION, TODO).
- A summary of User Stories, Acceptance Criteria, and Test Cases designed.
- A TODO tracking section showing the planned implementation order (⚪ TODO for all new TCs).
- Guidance on which TCs to implement first based on the priority framework.

## Constraints
- Write TC specifications (the design) before writing test code (the implementation).
- Follow the US → AC → TC traceability chain; every TC must trace to an AC and US.
- Follow the test naming convention: `verifyBehavior_byCondition_expectResult`.
- Keep ≤3 key assertions per test. If more are needed, split into separate tests.
- Use the four-phase test pattern: SETUP → BEHAVIOR → VERIFY → CLEANUP.
- Do not invent User Stories or Acceptance Criteria that are not grounded in the actual feature specification.
- Do not add production code until a failing test exists for it (RED before GREEN).
- Adapt the template to the project's existing test framework; do not assume frameworks that are not in the project.

## One More Thing
If the feature description, target language, or testing level is unclear or missing, stop and ask the user before writing any design or code.

## How

### Phase 1: Define Scope and Coverage Strategy

1. Read the feature description, API headers, or specification provided.
2. Identify the testing level: UnitTesting (single module/function), SysTesting (component interactions), or UserTesting (end-to-end user flows).
3. Write the **OVERVIEW** section:
   - `[WHAT]`: What functionality this file verifies.
   - `[WHERE]`: Which module, service, or system layer.
   - `[WHY]`: Key quality attributes to ensure (correctness, reliability, performance, etc.).
   - `SCOPE`: What is in scope vs. out of scope.
   - `KEY CONCEPTS`: Core concepts the tests rely on.
4. Identify 2–3 key dimensions for systematic coverage (e.g., Role × Mode × State).
5. Build a coverage matrix mapping dimension combinations to scenarios.
6. Present the OVERVIEW and coverage strategy to the user for confirmation before proceeding.

### Phase 2: Structured Verification Design (CaTDD Comments)

1. **Write User Stories (US)**:
   - Extract 2–5 User Stories from the coverage matrix.
   - Format: `US-n: As a [role], I want [capability], So that [value].`
   - Each US should represent a distinct user value or quality attribute.

2. **Write Acceptance Criteria (AC)**:
   - For each US, define 1–4 ACs using GIVEN/WHEN/THEN format.
   - Format: `AC-n: GIVEN [context], WHEN [action], THEN [outcome].`
   - Each AC must be independently verifiable.

3. **Write Test Case Specifications (TC)**:
   - For each AC, write 1 or more TC specs (add more for boundary and error cases).
   - Format:
     ```
     [@AC-n,US-n]
      TC-n:
        @[Name]: verifyBehavior_byCondition_expectResult
        @[Purpose]: Why this test matters
        @[Brief]: What the test does in one sentence
        @[Expect]: How to verify success (observable outcome)
     ```
   - Classify each TC using the priority framework:
     - **P1 Functional**: Typical → Boundary → Misuse → Fault
     - **P2 Design**: State → Capability → Concurrency
     - **P3 Quality**: Performance → Robust → Compatibility → Configuration
     - **P4 Addons**: Demo/Example
   - Mark all new TCs as ⚪ TODO.

4. Use risk scoring to adjust priority order when needed:
   - `Risk Score = Impact × Likelihood × Uncertainty` (each 1–3, max 27).
   - Score ≥ 18: Move that category immediately after Boundary in P1.

### Phase 3: Implementation — Red→Green Cycle

For each TC in priority order (P1 first):

1. **Write the test implementation** (SETUP → BEHAVIOR → VERIFY → CLEANUP).
   - Add `@[Name]` and `@[Steps]` comments above the test function.
   - Reference the TC spec in the implementation section.
2. **Run the test — confirm RED** (failing because feature is missing, not due to errors).
   - Update TC status: ⚪ TODO → 🔴 RED.
   - If it passes immediately, the test does not prove anything; fix the test.
3. **Write minimal production code** to make the test pass.
4. **Run the test — confirm GREEN**.
   - Update TC status: 🔴 RED → 🟢 GREEN.
   - Run the full test file to confirm no regressions.
5. **Refactor** the test and production code while keeping all tests green.
6. Advance to the next TC. Stop at each priority gate before moving to the next priority level.

**Priority Gate Checklist** (before advancing from P1 to P2):
- ✅ All Typical and Boundary tests GREEN.
- ✅ All Misuse and Fault tests GREEN or documented with a known issue.
- ✅ No critical correctness bugs.

### Phase 4: Validate and Report

1. Verify the file contains all required CaTDD sections: OVERVIEW, DESIGN (US/AC/TC), IMPLEMENTATION, TODO/TRACKING.
2. Verify the US → AC → TC traceability chain is complete and consistent.
3. Verify all implemented tests pass and no regressions exist.
4. Identify coverage gaps: scenarios that should be tested but are not yet specified.
5. Present a design report:

   > "CaTDD design complete for [file]:
   > - Testing level: [Unit / System / User]
   > - User Stories: [count]
   > - Acceptance Criteria: [count]
   > - Test Cases designed: [count] (P1=[count], P2=[count], P3=[count], P4=[count])
   > - Tests implemented and GREEN: [count]
   > - Coverage gaps: [list or none]"

## Resources
- `references/CaTDD_UserGuide.md` — Full CaTDD user guide with examples, quick-start guide, and workflow.
- `references/CaTDD_DesignPrompt.md` — Complete methodology specification with priority framework, category definitions, quality gates, and context-specific priority adjustments.
- `references/CaTDD_ImplTemplate.cxx` — C++ implementation template showing the complete CaTDD file structure (copy and adapt for any language).
- `references/CaTDD-UserGuide-PPT.md` — Presentation-style overview of CaTDD covering all concepts with slides, diagrams, and examples.

## Validation
1. Verify the new test file contains all required sections: OVERVIEW, UNIT TESTING DESIGN, UNIT TESTING IMPLEMENTATION, TODO/TRACKING.
2. Verify every TC has a traceability link to an AC and US.
3. Verify TC names follow the `verifyBehavior_byCondition_expectResult` convention.
4. Verify each test implementation uses the four-phase pattern (SETUP → BEHAVIOR → VERIFY → CLEANUP).
5. Verify all implemented tests compile and pass before reporting complete.
6. Report any coverage gaps or missing traceability links.
