---
name: facilitate-example-mapping
description: >
  WHEN/WHERE/WHO: [Scheduling: Business analysts, Product Owners, or agents leading a Backlog Refinement or "Three Amigos" session.]
  HOW: [Structural: Use this SKILL to decompose a User Story into Business Rules (Blue), Concrete Examples (Green), and Open Questions (Pink).]
  WHY: [Scheduling: Example Mapping provides a visual breadth-first constraint to flush out unknowns before coding starts.]
---

# Facilitate Example Mapping

## Who
Business Analysts, Product Owners, Scrum Masters, and AI Agents. The agent uses this skill to facilitate structured requirements discovery.

## What
This skill implements the Example Mapping technique created by Matt Wynne. It is a timeboxed (usually 25-30 minute) workshop where the team breaks a User Story (Yellow card) down into:
- **Business Rules (Blue):** Known constraints or acceptance criteria.
- **Examples (Green):** Concrete scenarios that illustrate the rule.
- **Questions (Pink):** Ambiguities or unknowns that prevent development.

## When
Invoke this skill during Backlog Refinement, Sprint Planning, or whenever a new User Story is introduced to the development team. Trigger phrases include: "let's map this story," "do an example mapping," "what are the edge cases," or "break down this user story."

## Where
Applies to JIRA User Stories, planning meetings, and PRD reviews.

## Why
Traditional requirements sessions often dive too deep into a single edge case, ignoring the rest of the story. Example Mapping forces a breadth-first approach. If you have too many Pink (Question) cards, the story isn't ready. If you have too many Blue (Rule) cards, the story is too big and should be sliced.

## Inputs
- A User Story or a high-level feature request.

## Output (Logical Evidence)
- A visual or structured text map of the Rules, Examples, and Questions.
- A decision on whether the story is "Ready" for development.

## Optimization Readiness
- **Failure Signals**: The map drifts into technical tasks, examples are abstract, unresolved questions are ignored, or the readiness decision is made before the rule/example balance is understood.
- **Evidence To Collect**: Rule/example/question cards, readiness decisions, ambiguity notes, and examples showing how counter-examples exposed hidden rules.
- **Safe Mutation Boundaries**: Refine facilitation prompts, card-color guidance, readiness criteria, and question-handling rules without changing the core breadth-first discovery workflow.
- **Acceptance Criteria**: Accept revisions only if every rule has concrete examples, uncertainty is surfaced as questions instead of debate, and the final readiness decision follows from the mapped cards.
- **Rejected Revision Handling**: Record abstract examples, technical-task inputs, and ignored pink-card questions so they are not repeated.
- **Transfer Check**: Verify the workflow still works for both simple stories and larger stories with multiple hidden rules.
- **Stop Rule**: If the input is a technical chore rather than business behavior, stop and redirect before building the map.

## Constraints (Logical Boundaries)
- Keep it fast. Do not spend time debating the precise Given/When/Then Gherkin syntax during Example Mapping. Use "Friends episode" titles (e.g., "The one where the credit card is expired").
- If there are unresolved Pink cards, the story cannot be moved to development.

## One More Thing
If the input text is a technical task (e.g., "Upgrade database to Postgres 13"), stop and inform the user that Example Mapping is for exploring *business behavior*, not technical chores.

## How (Structural Workflow)
### Phase 1: The Story
1. Place the User Story (Yellow) at the top of the map.

### Phase 2: Rules and Examples
2. Identify the first Business Rule (Blue) and place it under the story.
3. For that rule, ask the team for a concrete Example (Green). Then ask for a counter-example (e.g., a failure case).
4. Repeat this process to discover more rules. Often, an attempt to find an example will uncover a hidden rule.

### Phase 3: Surfacing Uncertainty
5. Whenever the team disagrees, or an assumption cannot be immediately verified, write it down as a Question (Pink) card. Do not debate it.

### Phase 4: Review and Slice
6. Review the map. If there are too many Rules, propose slicing the story into smaller stories. If there are critical Questions, assign someone to answer them before the next session.

## Resources
- [Example Mapping Rules](./details/example-mapping-rules.md)

## Review In Mind (ReviewInMindGenie)

Before delivering, activate the ReviewInMindGenie: stop authoring, switch to a skeptical reviewer, and critique the artifact as if someone else had produced it.

1. **Review Against Own Rules**: Re-read the output against this skill's `What`, `Constraints (Logical Boundaries)`, and `Validation` criteria. Check each rule explicitly; do not assume it passed because it was easy to write.
2. **Classify Findings**: Label each defect as BLOCKER (output unusable), MAJOR (violates a core rule), or MINOR (polish/consistency).
3. **Fix or Escalate**: Fix BLOCKER and MAJOR findings immediately when the fix is unambiguous. After each fix, re-check the affected criteria. If a finding cannot be fixed without new input (missing evidence, conflicting requirements, or a user decision), do not guess — report it as an open question or known gap.
4. **Deliver with a Review Note**: Present the output with a short note: what was checked, what was fixed, and what remains as a known gap. Never present an unreviewed artifact as final.

Review lens for this skill:
- Does the output separate rules, examples, and questions into the correct card types?
- Is every rule supported by at least one concrete example, with open questions explicit?
- Could the team start development without hidden ambiguity?

## Validation
1. Verify that every Rule has at least one Example.
2. Verify that the Examples are concrete (using real data/personas) rather than abstract.
