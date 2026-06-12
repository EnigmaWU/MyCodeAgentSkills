---
name: facilitate-example-mapping
description: >
  WHEN/WHERE/WHO: Business analysts, Product Owners, or agents leading a Backlog Refinement or "Three Amigos" session.
  HOW: Use this SKILL to decompose a User Story into Business Rules (Blue), Concrete Examples (Green), and Open Questions (Pink).
  WHY: Unstructured conversations ramble and miss edge cases. Example Mapping provides a visual breadth-first constraint to flush out unknowns before coding starts.
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

## Validation
1. Verify that every Rule has at least one Example.
2. Verify that the Examples are concrete (using real data/personas) rather than abstract.
