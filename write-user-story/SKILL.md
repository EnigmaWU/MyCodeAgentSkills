---
name: write-user-story
description: >
  WHEN/WHERE/WHO: Developers, product owners, or agents formalizing requirements into backlog items.
  HOW: Use this SKILL to write User Stories in the standard "As a... I want..." format, backed strictly by BDD "Given/When/Then" executable specifications.
  WHY: Vague stories lead to misunderstandings and bugs. BDD-style acceptance criteria make expected behavior explicit, testable, and unambiguous.
---

# Write User Story in BDD Style

## Who
Developers, product owners, business analysts, or AI Agents. The agent uses this skill to produce well-structured user stories with BDD-style acceptance criteria.

## What
Generate a user story that focuses on business value and testability. The output is a single, self-contained user story ready for a backlog or specification document.

## When
Invoke this skill when asked to write, create, or draft a user story, or when asked for BDD-style acceptance criteria based on a feature description.

## Where
Applies to product requirements, feature descriptions, and backlog items (e.g., JIRA, markdown files).

## Why
BDD-style acceptance criteria make expected behavior explicit, testable, and unambiguous. Consistent story format reduces back-and-forth between product and engineering, and Given/When/Then maps directly to automated acceptance tests.

## Inputs
- **Feature description** (required): What the user wants to build.
- **Role/persona** (optional): Who the end-user is.
- **Business value** (optional): Why this feature matters.
- **Edge cases** (optional): Known constraints or error paths.

## Output
- A User Story formatted using the standard templates.

## Constraints
- **RULE 1: BDD Executable Specifications First.** The absolute most important part of the story is the Acceptance Criteria. They MUST be written as strict BDD `Given/When/Then` scenarios that can be directly translated into automated tests (e.g., Cucumber).
- **Primary Story Format:** Use the traditional `As a <role>, I want <capability>, So that <value>` format by default.
- **Advisory Story Format:** You may optionally suggest the `In order to <value>, As a <role>, I want <capability>` format if the business goal seems to be getting lost in the technical details.
- Keep scenarios atomic: one behavior per scenario. Do not write "end-to-end test scripts" disguised as scenarios.

## One More Thing
If the input is purely a technical chore (e.g., "Update dependency X to version Y") with no observable business behavior, stop and inform the user that BDD User Stories are for functional requirements, not technical debt.

## How

### Phase 1: Gather Context
1. Identify the **role** (who), the **capability** (what), and the **business value** (why).
2. If any of these are missing or vague, ask the user before continuing.

### Phase 2: Write the Story Statement
3. Compose the Primary Story statement (`As a... I want... So that...`).

### Phase 3: Identify Scenarios
4. Extract the **happy path** first — the main success flow.
5. Identify **alternate paths** — valid variations of the input or context.
6. Identify **error or edge-case paths** — invalid input, missing data, permission failures, timeouts, etc.

### Phase 4: Write BDD Acceptance Criteria
7. For each scenario, write the executable specifications using `Given / When / Then`.
8. Ensure scenarios are declarative (focusing on business intent) rather than imperative (focusing on UI clicks and keystrokes).

## Resources
- [BDD Story Format](./details/bdd-story-format.md)

## Validation
1. Verify that every scenario has at least one Given, one When, and one Then.
2. Verify that the story includes a clear business value statement.
