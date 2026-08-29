---
name: improve-user-story
description: >
  WHEN/WHERE/WHO: [Scheduling: Developers, product owners, QA engineers, or agents keeping BDD-style user stories up to date.]
  HOW: [Structural: Use this SKILL to proactively detect when a conversation introduces a new edge case or change, and update the Story.]
  WHY: [Scheduling: Requirements evolve during discussion, and keeping BDD acceptance criteria aligned prevents testing gaps.]
---

# Improve User Story

## Common Contract (Load First)

When this skill is activated, first load [skill-common](../skill-common/SKILL.md) and apply the shared conventions it defines: canonical section order, frontmatter rules, anti-pattern guidance, and the Review In Mind loop in [review-in-mind](../skill-common/details/review-in-mind.md). This skill adds only domain-specific rules below.

## Who
Developers, Product Owners, QA Engineers, and AI Agents. The agent uses this skill to proactively maintain living documentation as requirements evolve.

## What
Detects when a conversation introduces a new improvement, edge case, or feature change, and updates the relevant existing User Story to reflect it. It carefully adds, removes, or updates the BDD `Given / When / Then` scenarios without destroying the intent of the unaffected scenarios.

## When
Invoke this skill when a conversation introduces a new edge case, bug fix, or feature enhancement. Trigger phrases include: "let's also add...", "what if...?", "we should also handle...", or "update the story".

## Where
Modifies existing markdown files containing User Stories, ticket bodies, or outputs the updated story to the chat.

## Why
Keeping the BDD acceptance criteria perfectly aligned with the latest conversation prevents testing gaps. Proactive updates save time and reduce cognitive load for developers trying to track changes.

## Inputs
- **Existing User Story** (required): The current version of the user story (from a file or chat context).
- **New Improvement/Feature** (required): The new requirement, edge case, or workflow change.

## Output (Logical Evidence)
- An updated User Story that strictly follows the `write-user-story` formatting rules.

## Optimization Readiness
- **Failure Signals**: Unaffected scenarios are rewritten unnecessarily, new edge cases are dropped, the story loses its original intent, or the update introduces implementation coupling.
- **Evidence To Collect**: Original and updated stories, added or removed scenarios, and examples where the modification addressed the new improvement without damaging unaffected behavior.
- **Safe Mutation Boundaries**: Refine scenario-editing guidance, edge-case prompting, and format-preservation rules without changing the core requirement to keep the existing story alive.
- **Acceptance Criteria**: Accept revisions only if the updated story preserves unaffected scenarios, adds the new behavior precisely, and keeps BDD acceptance criteria executable.
- **Rejected Revision Handling**: Record accidental deletions, over-broad rewrites, and implementation-coupled scenario drafts so they are not repeated.
- **Transfer Check**: Verify the workflow still works for both minor edge-case additions and meaningful feature shifts.
- **Stop Rule**: If it is unclear which story to update or the new improvement conflicts with a core requirement, stop and ask before editing.

## Constraints (Logical Boundaries)
- **RULE 1: BDD Executable Specifications First.** Acceptance Criteria MUST be written as strict BDD `Given/When/Then` scenarios.
- **Primary Story Format:** Use the traditional `As a <role>, I want <capability>, So that <value>` format by default.
- **Advisory Story Format:** You may optionally suggest the `In order to <value>, As a <role>, I want <capability>` format.
- **Preserve Existing Scenarios:** Do not rewrite scenarios that are unaffected by the new improvement. Only modify what needs to change.

## One More Thing
If it's unclear *which* User Story to update, or if the new improvement conflicts with a core requirement, stop and ask the user for clarification.

## How (Structural Workflow)
### Phase 1: Detect Change & Identify Target
1. Notice when a new feature, improvement, or edge case is agreed upon in the conversation.
2. Locate the existing user story that covers this domain.

### Phase 2: Analyze Impact
3. Determine if the new feature changes the core objective (the "I want" / "So that").
4. Identify whether existing scenarios need modification (e.g., a "happy path" now has a new condition) or if entirely new scenarios must be created.

### Phase 3: Apply Formatting Guidelines
5. Keep the standard Story structure.
6. Draft new `Given / When / Then` scenarios that cover the new feature.
7. Use Data Tables (Scenario Outlines) if the new improvement introduces multiple data variations to an existing scenario.

### Phase 4: Deliver the Update
8. Output the complete, updated user story.
9. Provide a brief summary of what specific scenarios were altered or added.

## Resources
- [Story Refactoring Guide](./details/story-refactoring-guide.md)

## Review In Mind (ReviewInMindGenie)

Execute the common review loop in [review-in-mind](../skill-common/details/review-in-mind.md) before delivering.

Review lens for this skill:
- Do updated scenarios preserve unaffected behavior and the story's original intent?
- Are new edge cases reflected in Given/When/Then without implementation coupling?
- Is the diff minimal and traceable to the new information?

## Validation
1. Verify that unaffected scenarios were not accidentally deleted.
2. Verify that the new scenarios map directly to the improvement discussed.
