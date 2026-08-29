---
name: write-user-story
description: >
  WHEN/WHERE/WHO: [Scheduling: Developers, product owners, or agents formalizing requirements into backlog items.]
  HOW: [Structural: Use this SKILL to write User Stories backed strictly by BDD "Given/When/Then" executable specifications.]
  WHY: [Scheduling: Vague stories lead to misunderstandings. BDD-style criteria make expected behavior explicit and testable.]
---

# Write User Story in BDD Style

## Who
Developers, product owners, business analysts, or AI Agents. The agent uses this skill to produce well-structured user stories with BDD-style acceptance criteria.

## What
Generate a user story that focuses on business value and testability. The output is a self-contained story package: story statement, executable BDD criteria, concrete business examples, and ambiguity/risk notes ready for backlog refinement.

## When
Invoke this skill when asked to write, create, or draft a user story, or when asked for BDD-style acceptance criteria based on a feature description.

## Where
Applies to product requirements, feature descriptions, and backlog items (e.g., JIRA, markdown files).

## Why
BDD-style acceptance criteria make expected behavior explicit, testable, and unambiguous. Consistent story format reduces back-and-forth between product and engineering, and Given/When/Then maps directly to automated acceptance tests.

## Inputs
- **Feature description** (required): What the user wants to build.
- **Business goal / expected outcome** (required): Why this feature should exist and what measurable behavior change is expected.
- **Role/persona** (optional): Who the end-user is.
- **Business value** (optional): Why this feature matters.
- **Edge cases** (optional): Known constraints or error paths.

## Output (Logical Evidence)
- A User Story formatted using the standard templates.
- Executable BDD criteria with at least one happy path and one error/edge path.
- A compact example set with realistic domain data.
- A short ambiguity/risk list for unresolved decisions.

## Optimization Readiness
- **Failure Signals**: The story collapses into a technical task, scenarios focus on UI clicks instead of business behavior, acceptance criteria are not executable, or realistic examples are replaced with vague placeholders.
- **Evidence To Collect**: Story drafts, BDD scenarios, example sets, ambiguity lists, and reviewer feedback on whether the story drives implementation and testing cleanly.
- **Safe Mutation Boundaries**: Refine story phrasing, scenario-shaping prompts, example guidance, and ambiguity-reporting rules without changing the core business-goal-first and BDD-first structure.
- **Acceptance Criteria**: Accept revisions only if the story ties capability to business value, includes executable Given/When/Then criteria, covers both success and edge behavior, and avoids implementation-coupled `Then` clauses.
- **Rejected Revision Handling**: Record technical-chore stories, UI-script scenarios, and placeholder-heavy example patterns so they are not reused blindly.
- **Transfer Check**: Verify the workflow still works for greenfield feature stories and refinements of partially defined backlog items.
- **Stop Rule**: If the request has no observable business behavior, stop and tell the user it is not a valid user-story candidate.

## Constraints (Logical Boundaries)
- **RULE 1: BDD Executable Specifications First.** The absolute most important part of the story is the Acceptance Criteria. They MUST be written as strict BDD `Given/When/Then` scenarios that can be directly translated into automated tests (e.g., Cucumber).
- **RULE 2: Goal Before Detail.** Derive scenario scope from business outcome first. Do not start from UI click paths.
- **Primary Story Format:** Use the traditional `As a <role>, I want <capability>, So that <value>` format by default.
- **Advisory Story Format:** You may optionally suggest the `In order to <value>, As a <role>, I want <capability>` format if the business goal seems to be getting lost in the technical details.
- Keep scenarios atomic: one behavior per scenario. Do not write "end-to-end test scripts" disguised as scenarios.
- Keep examples concrete, realistic, and domain-readable; avoid placeholders that hide rules.
- Do not couple `Then` clauses to implementation details, APIs, or database internals.

## One More Thing
If the input is purely a technical chore (e.g., "Update dependency X to version Y") with no observable business behavior, stop and inform the user that BDD User Stories are for functional requirements, not technical debt.

## How (Structural Workflow)
### Phase 1: Gather Context
1. Identify the **role** (who), the **capability** (what), and the **business value** (why).
2. If any of these are missing or vague, ask the user before continuing.
3. Confirm the expected business outcome and scope boundary before drafting scenarios.

### Phase 2: Write the Story Statement
3. Compose the Primary Story statement (`As a... I want... So that...`).

### Phase 3: Identify Scenarios
4. Extract the **happy path** first — the main success flow.
5. Identify **alternate paths** — valid variations of the input or context.
6. Identify **error or edge-case paths** — invalid input, missing data, permission failures, timeouts, etc.

### Phase 4: Write BDD Acceptance Criteria
7. For each scenario, write the executable specifications using `Given / When / Then`.
8. Ensure scenarios are declarative (focusing on business intent) rather than imperative (focusing on UI clicks and keystrokes).
9. Use realistic example values and explicit expected outcomes in `Then`.

### Phase 5: Refine for Specification Quality
10. Remove ambiguous words from `Then` clauses (for example: fast, robust, seamless) unless quantified.
11. Verify each scenario tests one behavior and has clear pass/fail observables.
12. Add a brief ambiguity/risk note for unresolved business decisions.

## Resources
- [BDD Story Format](./details/bdd-story-format.md)
- [Specification by Example Enhancements](./details/specification-by-example-enhancements.md)

## Review In Mind (ReviewInMindGenie)

Before delivering, activate the ReviewInMindGenie: stop authoring, switch to a skeptical reviewer, and critique the artifact as if someone else had produced it.

1. **Review Against Own Rules**: Re-read the output against this skill's `What`, `Constraints (Logical Boundaries)`, and `Validation` criteria. Check each rule explicitly; do not assume it passed because it was easy to write.
2. **Classify Findings**: Label each defect as BLOCKER (output unusable), MAJOR (violates a core rule), or MINOR (polish/consistency).
3. **Fix or Escalate**: Fix BLOCKER and MAJOR findings immediately when the fix is unambiguous. After each fix, re-check the affected criteria. If a finding cannot be fixed without new input (missing evidence, conflicting requirements, or a user decision), do not guess — report it as an open question or known gap.
4. **Deliver with a Review Note**: Present the output with a short note: what was checked, what was fixed, and what remains as a known gap. Never present an unreviewed artifact as final.

Review lens for this skill:
- Does the story state role, capability, and business value with executable Given/When/Then scenarios?
- Is there at least one error/edge path with concrete examples and no implementation-coupled `Then` clauses?
- Would a skeptical PO/QA accept it as testable without further clarification?

## Validation
1. Verify that every scenario has at least one Given, one When, and one Then.
2. Verify that the story includes a clear business value statement.
3. Verify at least one error/edge path exists and is behavior-focused.
4. Verify all `Then` clauses are concrete and testable without implementation coupling.
