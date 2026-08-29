---
name: UnitTesting-convert2CaTDD
description: >
  WHEN/WHERE/WHO: [Scheduling: Developers or agents refactoring tests to CaTDD. Applies to existing test files lacking US/AC/TC structure.]
  HOW: [Structural: Use this SKILL to extract User Stories, Acceptance Criteria, and Test Cases from legacy code into the Comment-alive format.]
  WHY: [Scheduling: Legacy tests lack design rationale. CaTDD makes tests living, structured design documents parseable by AI.]
---

# Convert to CaTDD

## Who
Developers or agents who want to convert existing or legacy test files into CaTDD (Comment-alive Test-Driven Development) format so that tests become living design documents with structured verification design.

## What
Analyze existing test files and restructure them into CaTDD format. The main deliverables are:
- An OVERVIEW section describing what, where, and why.
- User Stories (US) expressing value from the user perspective.
- Acceptance Criteria (AC) in GIVEN/WHEN/THEN format making stories testable.
- Test Cases (TC) specifications with structured metadata (`@[Name]`, `@[Purpose]`, `@[Brief]`, `@[Expect]`).
- Test implementations following the four-phase pattern (SETUP → BEHAVIOR → VERIFY → CLEANUP).
- A TODO/implementation tracking section with status markers (⚪ TODO → 🔴 RED → 🟢 GREEN).
- Priority classification (P1 Functional → P2 Design → P3 Quality → P4 Addons).

The converted file is a self-contained design document that is readable by humans, parseable by LLMs, and verified by tests.

## When
- The user says "convert to CaTDD", "refactor tests to CaTDD", "apply CaTDD", or "make tests comment-alive".
- The user asks to add US/AC/TC structure to existing tests.
- The user asks to restructure tests for better LLM collaboration.
- The user wants to add verification design comments to a test file.
- Do **not** use this skill to write brand-new tests from scratch (use the CaTDD methodology directly with the template for that).
- Do **not** use this skill for non-test files such as production code, build scripts, or documentation.

## Where
- Source material comes from existing test files in the user's project.
- The output replaces or augments the original test file with CaTDD structure.
- Reference materials are bundled in `references/` alongside this skill.

## Why
- Legacy tests often lack design rationale, making them hard to maintain and extend.
- Without structured comments, LLMs cannot effectively generate or modify tests.
- CaTDD's US/AC/TC format bridges human intent and machine-executable tests.
- Converting tests to CaTDD makes the test file a living design document that never goes stale.
- Structured verification design (what to verify) separated from implementation (how to verify) enables better human-AI collaboration.

## Inputs
- **Existing test file(s)** (required): the test code to convert.
- **Production code or interface headers** (recommended): helps identify what the tests are verifying.
- **Target language** (optional): defaults to the language of the existing tests.
- **Priority focus** (optional): which test priority categories matter most (e.g., "reliability-critical" promotes Fault and Robust).

## Output (Logical Evidence)
- A converted test file in CaTDD format containing all required sections.
- A summary of User Stories, Acceptance Criteria, and Test Cases extracted.
- A TODO tracking section showing the status of each test case.
- Recommendations for additional tests to fill coverage gaps.

## Optimization Readiness
- **Failure Signals**: Existing test behavior changes during conversion, extracted stories or criteria are unsupported by the source tests, CaTDD structure is added mechanically without clarifying intent, or multi-assert legacy risks remain invisible.
- **Evidence To Collect**: Original and converted test files, extracted US/AC/TC summaries, preserved test-group mappings, and notes about coverage gaps or oversized assertions.
- **Safe Mutation Boundaries**: Refine extraction prompts, grouping heuristics, overview structure, and TODO guidance without changing the core requirement to preserve existing logic while surfacing design intent.
- **Acceptance Criteria**: Accept revisions only if the converted file preserves all original test behavior, adds clear CaTDD structure, and grounds every extracted story or criterion in real test or interface evidence.
- **Rejected Revision Handling**: Record unsupported inferred stories, destructive restructures, and fake coverage improvements so they are not repeated.
- **Transfer Check**: Verify the workflow still works across different test frameworks and for both well-commented and comment-poor legacy test suites.
- **Stop Rule**: If the source tests or production interfaces are too unclear to infer design intent responsibly, stop and ask before converting the file.

## Constraints (Logical Boundaries)
- Preserve all existing test logic. Do not remove or break any passing test.
- Do not invent User Stories or Acceptance Criteria that are not supported by the existing tests or production code.
- Follow the test naming convention: `verifyBehavior_byCondition_expectResult`.
- Keep ≤3 key assertions per test. If an existing test has more, note it but do not split unless the user approves.
- Use the four-phase test pattern: SETUP → BEHAVIOR → VERIFY → CLEANUP.
- Keep the converted file self-contained. Move long reference material into comments or separate files only if the file exceeds ~500 lines.
- Do not assume frameworks, utilities, or macros that do not exist in the target project. Adapt CaTDD patterns to the project's existing test framework.

## One More Thing
If anything is unclear, missing, or conflicting, stop and ask the user before proceeding.

## How (Structural Workflow)
### Phase 1: Analyze the Existing Tests

1. Read the target test file(s) completely.
2. Identify the test framework being used (GTest, pytest, Jest, JUnit, etc.).
3. List every test case and what it appears to verify.
4. Identify the production code or interfaces under test.
5. Group tests by apparent purpose: happy path, edge case, error handling, state, concurrency, performance, etc.
6. Note any existing comments, docstrings, or documentation that express design intent.
7. Present a summary to the user:

   > "I found [N] tests in [file]. They appear to verify [component/feature].
   > Test groups: [list groups with counts].
   > Existing design comments: [present/absent].
   > Ready to convert?"

### Phase 2: Extract Verification Design

1. **Write the OVERVIEW section**:
   - `[WHAT]`: What functionality the file verifies.
   - `[WHERE]`: Which module or subsystem.
   - `[WHY]`: Key quality attributes (correctness, reliability, performance, etc.).
   - `SCOPE`: What is in scope vs out of scope.
   - `KEY CONCEPTS`: Core concepts the tests rely on.

2. **Define the Coverage Strategy**:
   - Identify 2-3 key dimensions for systematic coverage.
   - Build a coverage matrix mapping dimensions to scenarios.

3. **Write User Stories (US)**:
   - Extract 2-5 User Stories from the grouped tests.
   - Format: `US-n: As a [role], I want [capability], So that [value].`
   - Each US should map to one or more test groups.

4. **Write Acceptance Criteria (AC)**:
   - For each US, define 1-4 ACs.
   - Format: `AC-n: GIVEN [context], WHEN [action], THEN [outcome].`
   - Each AC must be independently verifiable.

5. **Write Test Case Specifications (TC)**:
   - For each existing test, create a TC spec.
   - Format:
     ```
     [@AC-n,US-n]
      TC-n:
        @[Name]: verifyBehavior_byCondition_expectResult
        @[Purpose]: Why this test matters
        @[Brief]: What the test does
        @[Expect]: How to verify success
     ```
   - Rename tests to follow `verifyBehavior_byCondition_expectResult` convention if they do not already.

### Phase 3: Restructure the Test File

1. **Add the OVERVIEW section** at the top of the file as a block comment.

2. **Add the UNIT TESTING DESIGN section** containing:
   - Test Case Design Aspects/Categories (priority framework).
   - User Story Design (US definitions with coverage matrix).
   - Acceptance Criteria Design (AC definitions).
   - Test Cases Design (TC specifications with status markers).

3. **Restructure the IMPLEMENTATION section**:
   - Add four-phase comments (SETUP/BEHAVIOR/VERIFY/CLEANUP) to each test.
   - Add `@[Name]` and `@[Steps]` comments above each test implementation.
   - Group tests by category (Typical, Edge, Misuse, Fault, State, etc.).

4. **Add the TODO/IMPLEMENTATION TRACKING section** at the bottom:
   - List all test cases organized by priority (P1 → P2 → P3 → P4).
   - Mark status: ⚪ TODO for tests that need improvement, 🟢 GREEN for tests that are fully converted and passing.
   - Add gate checkpoints between priority levels.

5. **Classify each test** into the priority framework:
   - P1 Functional: Typical → Boundary → Misuse → Fault.
   - P2 Design: State → Capability → Concurrency.
   - P3 Quality: Performance → Robust → Compatibility → Configuration.
   - P4 Addons: Demo/Example.

### Phase 4: Validate and Report

1. Verify every original test is accounted for in the converted file.
2. Verify the US → AC → TC traceability chain is complete.
3. Verify tests still compile and pass (do not break existing tests).
4. Identify coverage gaps: scenarios that should be tested but are not.
5. Present a conversion report:

   > "Conversion complete for [file]:
   > - User Stories: [count]
   > - Acceptance Criteria: [count]
   > - Test Cases converted: [count]
   > - Priority distribution: P1=[count], P2=[count], P3=[count], P4=[count]
   > - Coverage gaps found: [list or none]
   > - All original tests preserved: [Yes/No]"

## Resources
- `references/CaTDD_UserGuide.md` — Full CaTDD user guide with examples and workflow.
- `references/CaTDD_DesignPrompt.md` — CaTDD methodology specification with priority framework and quality gates.
- `references/CaTDD_ImplTemplate.cxx` — C++ implementation template showing the complete CaTDD file structure.

## Review In Mind (ReviewInMindGenie)

Before delivering, activate the ReviewInMindGenie: stop authoring, switch to a skeptical reviewer, and critique the artifact as if someone else had produced it.

1. **Review Against Own Rules**: Re-read the output against this skill's `What`, `Constraints (Logical Boundaries)`, and `Validation` criteria. Check each rule explicitly; do not assume it passed because it was easy to write.
2. **Classify Findings**: Label each defect as BLOCKER (output unusable), MAJOR (violates a core rule), or MINOR (polish/consistency).
3. **Fix or Escalate**: Fix BLOCKER and MAJOR findings immediately when the fix is unambiguous. After each fix, re-check the affected criteria. If a finding cannot be fixed without new input (missing evidence, conflicting requirements, or a user decision), do not guess — report it as an open question or known gap.
4. **Deliver with a Review Note**: Present the output with a short note: what was checked, what was fixed, and what remains as a known gap. Never present an unreviewed artifact as final.

Review lens for this skill:
- Does every US/AC/TC carry structured metadata and an executable GIVEN/WHEN/THEN format?
- Do test implementations follow SETUP → BEHAVIOR → VERIFY → CLEANUP with priority classification?
- Could a fresh reader or LLM regenerate the tests from the design document alone?

## Validation
1. Verify the converted file contains all required CaTDD sections (OVERVIEW, US, AC, TC, IMPLEMENTATION, TODO).
2. Verify every original test case has a corresponding TC specification.
3. Verify the US → AC → TC traceability links are present and correct.
4. Verify all tests still compile and pass after conversion.
5. Report any coverage gaps or missing traceability links.
