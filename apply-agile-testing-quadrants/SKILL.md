---
name: apply-agile-testing-quadrants
description: >
  WHEN/WHERE/WHO: [Scheduling: Use when: defining a test strategy or planning tests for a feature. Applies to: test planning, feature review, acceptance criteria]
  HOW: [Structural: Helps with: balancing test coverage across business/technology and support/critique dimensions]
  WHY: [Scheduling: Provides structured workflow execution to prevent errors and ensure standards.]
---

# Apply Agile Testing Quadrants

## Who
The primary users are developers, testers, and product owners working collaboratively to define a testing strategy. The agent uses this skill to facilitate test planning.

## What
This skill applies the Agile Testing Quadrants framework to categorize and plan tests. It produces a balanced testing strategy that incorporates unit, functional, exploratory, and non-functional tests, ensuring no critical aspect of system quality is ignored.

## When
Invoke this skill during feature design, sprint planning, or when writing acceptance criteria for user stories. Trigger phrases include: "plan tests for this feature," "apply testing quadrants," "define test strategy," or "ensure balanced test coverage."

## Where
Applies to feature requirement documents, sprint planning notes, test strategy wikis, and acceptance criteria fields within project management tools (e.g., JIRA, Trello).

## Why
Focusing solely on one type of testing (e.g., automated unit tests) leaves blind spots. The Agile Testing Quadrants framework ensures a holistic approach, communicating the intent of different tests to the whole team and highlighting areas where specialized skills (like security testing or UX evaluation) might be needed.

## Inputs
- Feature description, user story, or acceptance criteria.
- System context or architecture documents.

## Output (Logical Evidence)
- A categorized list of proposed tests mapped to the four Agile Testing Quadrants.
- Identified testing gaps and recommendations.

## Optimization Readiness
- **Failure Signals**: The plan collapses into only one or two quadrants, exploratory or non-functional testing is omitted, or the quadrants are misused as a delivery timeline instead of a coverage taxonomy.
- **Evidence To Collect**: Proposed quadrant mappings, identified gaps, automation versus manual choices, and review feedback about missing coverage or quadrant confusion.
- **Safe Mutation Boundaries**: Refine quadrant prompts, coverage-review structure, and capability-mapping guidance without changing the core four-quadrant planning model.
- **Acceptance Criteria**: Accept revisions only if the strategy distinguishes Q1/Q2 from Q3/Q4 clearly, covers the relevant quadrants for the feature, and surfaces both exploratory and technical-quality risks.
- **Rejected Revision Handling**: Record automation-only plans, timeline-style quadrant misuse, and recurring blind spots so they are not reintroduced.
- **Transfer Check**: Verify the workflow still works for small feature stories and larger cross-cutting test strategy exercises.
- **Stop Rule**: If the feature or system context is too thin to reason about testing intent across quadrants, stop and ask before proposing the strategy.

## Constraints (Logical Boundaries)
- Do not assume all tests must be automated (Quadrant 3 is typically manual/exploratory).
- Do not treat the quadrants as sequential phases; they are a taxonomy, not a timeline.

## One More Thing
If anything is unclear, missing, or conflicting, stop and ask the user before proceeding.

## How (Structural Workflow)
### Phase 1: Quadrant 1 and 2 Analysis (Supporting the Team)
Analyze the feature to define tests that guide development.
- **Q1 (Technology-facing):** Define unit and component tests that verify the internal quality of the code.
- **Q2 (Business-facing):** Define functional tests, story tests, and UI prototypes that verify the business logic and user flows.

### Phase 2: Quadrant 3 and 4 Analysis (Critiquing the Product)
Analyze the feature to define tests that evaluate the finished (or near-finished) product.
- **Q3 (Business-facing):** Plan exploratory testing, usability testing, and UAT. Focus on user experience and edge cases.
- **Q4 (Technology-facing):** Identify necessary performance, load, security, and "ility" tests (scalability, maintainability).

### Phase 3: Strategy Consolidation and Review
Combine the identified tests into a holistic strategy.
- Map the proposed tests against the team's capabilities.
- Identify which tests should be automated vs. manual.
- Flag any quadrants that have insufficient coverage.

## Resources
- [Quadrant Examples](./details/quadrant-examples.md)
- [Test Planning Checklist](./details/test-planning-checklist.md)

## Validation
1. Verify that the resulting test strategy covers at least some aspect of all four quadrants (if applicable to the feature).
2. Ensure that the distinction between "supporting the team" (Q1/Q2) and "critiquing the product" (Q3/Q4) is maintained.
3. Confirm that exploratory and non-functional testing needs have not been omitted.
