---
name: validate-requirements-criteria
description: >
  WHEN/WHERE/WHO: [Scheduling: QA engineers, agents, or business analysts reviewing drafted requirements before development.]
  HOW: [Structural: Use this SKILL to hunt for ambiguous words, identify edge cases, and translate the text into strict BDD Acceptance Criteria.]
  WHY: [Scheduling: Ambiguous requirements lead to bugs. Fixing requirements defects is cheapest during the analysis phase.]
---

# Validate Requirements Criteria

## Who
Quality Assurance (QA) engineers, developers, and AI agents. The agent uses this skill to ensure requirements are ready for implementation.

## What
This skill "tests" requirements text. It scans for ambiguity, missing exception paths, and untestable claims. It then formalizes the validated requirement into strict Behavior-Driven Development (BDD) Acceptance Criteria (`Given / When / Then`).

## When
Invoke this skill just before a sprint begins, during story refinement, or when reviewing a PRD draft. Trigger phrases include: "review this requirement," "find ambiguity," "write acceptance criteria," or "test this user story."

## Where
Applies to User Stories, PRDs, acceptance criteria fields in JIRA, and BDD feature files.

## Why
Words like "fast," "seamless," and "robust" mean different things to different people. If a developer builds a system to be "fast" (500ms) but the stakeholder meant "real-time" (10ms), the product fails. This skill removes that ambiguity.

## Inputs
- Drafted requirements, user stories, or PRD text.

## Output (Logical Evidence)
- A list of Ambiguity Warnings and clarifying questions.
- Formalized Acceptance Criteria in BDD format.

## Optimization Readiness
- **Failure Signals**: Ambiguous words remain unchallenged, exception paths are omitted, scenarios contain multiple behaviors, or the criteria drift into implementation details.
- **Evidence To Collect**: Ambiguity warnings, clarifying questions, drafted BDD scenarios, and examples where a vague claim was converted into a testable expectation.
- **Safe Mutation Boundaries**: Refine ambiguity-check prompts, exception-path analysis, and BDD wording guidance without changing the core requirements-validation workflow.
- **Acceptance Criteria**: Accept revisions only if every scenario has one behavior, at least one exception path is included when relevant, and untestable words are removed from the final `Then` clauses.
- **Rejected Revision Handling**: Record guessed thresholds, multi-behavior scenarios, and implementation-style phrasing so they are not repeated.
- **Transfer Check**: Verify the workflow still works for PRDs, backlog items, and story refinements with missing clarity.
- **Stop Rule**: If the input is a technical implementation detail rather than a user requirement, stop and redirect before drafting acceptance criteria.

## Constraints (Logical Boundaries)
- Do not make up thresholds for ambiguous words; flag them so the stakeholder can decide. (e.g., If the text says "timeout quickly," ask "Is 'quickly' 5 seconds or 30 seconds?")
- Ensure every `Given / When / Then` scenario tests exactly one behavior.

## One More Thing
If the input text is a technical implementation detail rather than a user requirement (e.g., "Use a Redis cache"), inform the user that this is an architecture decision, not a business requirement.

## How (Structural Workflow)
### Phase 1: Ambiguity Hunt
1. Scan the text against the Ambiguity Checklist. Look for adjectives, adverbs, and unbounded absolutes (e.g., "always," "never").
2. Highlight the dangerous words and generate specific clarifying questions.

### Phase 2: Exception Path Analysis
3. Ask "What if..." for the inputs and environment:
   - What if the user is logged out?
   - What if the network fails?
   - What if the input is negative or empty?

### Phase 3: Acceptance Criteria Drafting
4. Translate the happy path and the discovered exception paths into BDD syntax:
   - **Scenario:** [Name of behavior]
   - **Given** [Initial context]
   - **When** [Action occurs]
   - **Then** [Observable outcome]

## Resources
- [Ambiguity Checklist](./details/ambiguity-checklist.md)

## Validation
1. Verify that the generated BDD scenarios cover at least one error/exception path.
2. Ensure that no ambiguous words from the input survived into the final `Then` clauses.
