---
name: improve-user-story
description: 'Use when: the user discusses new features, improvements, edge cases, or changes to an existing workflow in the conversation. Helps with: proactively extracting those changes and updating an existing user story to keep it accurate. Applies to: existing product requirements, backlog items, or BDD specification files.'
---

# Improve User Story

## Who
Developers, product owners, QA engineers, or agents needing to keep existing BDD-style user stories up to date as new ideas or changes are discussed.

## What
Proactively detects when a conversation introduces a new improvement, edge case, or feature change, and updates the relevant existing user story to reflect it. It modifies the **As a / I want / So that** statement if necessary, and carefully adds, removes, or updates the BDD **Given / When / Then** scenarios, adhering strictly to the `write-user-story` formatting standards.

## When
- A conversation introduces a new edge case, bug fix, or feature enhancement.
- The user says "let's also add...", "what if...?", or "we should also handle...".
- The user explicitly asks to "improve the user story" or "update the story".
- The agent recognizes that a newly discussed requirement renders an existing user story incomplete or outdated.

## Where
- Modifies existing markdown files containing user stories (e.g., `README_UserStories.md`), ticket bodies, or outputs the updated story to the chat.

## Why
- Requirements evolve during discussion, and documentation often goes stale.
- Keeping the BDD acceptance criteria perfectly aligned with the latest conversation prevents testing gaps.
- Proactive updates save time and reduce cognitive load for developers trying to track changes.

## Inputs
- **Existing User Story** (required): The current version of the user story (from a file or chat context).
- **New Improvement/Feature** (required): The new requirement, edge case, or workflow change introduced in the conversation.

## Output
An updated user story that strictly follows the `write-user-story` format:

```markdown
## User Story: <concise title>

**As a** <role>,
**I want** <capability>,
**So that** <business value>.

### Acceptance Criteria

#### Scenario 1: <scenario title>
- **Given** <precondition>
- **When** <action>
- **Then** <expected outcome>

### Notes
- <Any assumptions, open questions, or out-of-scope items, including notes about the recent improvement>
```

## Constraints
- **Preserve Existing Scenarios**: Do not rewrite scenarios that are unaffected by the new improvement. Only modify what needs to change.
- **Strict BDD Format**: Every scenario must have at least one **Given**, one **When**, and one **Then** step. Use **And** to chain steps.
- **No Hallucination**: Only add scenarios supported by the recent conversation. If the improvement is vague, ask clarifying questions before updating.
- **Traceability**: Clearly indicate what was added or improved (e.g., in the Notes section or by highlighting the new scenario).

## One More Thing
If it's unclear *which* user story to update, or if the new improvement conflicts with a core requirement, stop and ask the user for clarification.

## How

### Step 1: Detect Change & Identify Target
1. Notice when a new feature, improvement, or edge case is agreed upon in the conversation.
2. Locate the existing user story that covers this domain (e.g., checking `README_UserStories.md` or recent chat context).

### Step 2: Analyze Impact
1. Determine if the new feature changes the core objective (the "I want" / "So that").
2. Identify whether existing scenarios need modification (e.g., a "happy path" now has a new condition) or if entirely new scenarios must be created.

### Step 3: Apply `write-user-story` Guidelines
1. Keep the standard **As a / I want / So that** structure.
2. Draft new **Given / When / Then** scenarios that cover the new feature.
3. Keep scenarios atomic: one behavior per scenario.

### Step 4: Deliver the Update
1. Output the complete, updated user story.
2. Provide a brief summary of what specific scenarios were altered or added to accommodate the conversational improvement.
3. Save it to the target file if working within a repository.
