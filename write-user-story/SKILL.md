---
name: write-user-story
description: 'Use when: the user says "write user story", "create user story", "BDD story", "write a feature", or asks for acceptance criteria in Given/When/Then format. Helps with: writing user stories in BDD style with structured acceptance criteria. Applies to: product requirements, feature descriptions, and backlog items.'
---

# Write User Story in BDD Style

## Who
Developers, product owners, or agents who need to produce well-structured user stories with BDD-style acceptance criteria.

## What
Generate a user story that follows the standard **As a / I want / So that** format, with acceptance criteria written as BDD **Given / When / Then** scenarios. The output is a single, self-contained user story ready for a backlog or specification document.

## When
- The user asks to write, create, or draft a user story.
- The user asks for BDD-style acceptance criteria.
- The user describes a feature or requirement and wants it formalized.
- The user says "write user story", "BDD story", "Given/When/Then", or "acceptance criteria".
- Do **not** use this skill for bug reports, technical tasks, or epics that need decomposition first.

## Where
- Output goes wherever the user specifies: a markdown file, a ticket body, the chat, or a backlog tool.
- If no target is specified, output directly in the conversation.

## Why
- BDD-style acceptance criteria make expected behavior explicit, testable, and unambiguous.
- Consistent story format reduces back-and-forth between product and engineering.
- Given/When/Then maps directly to automated acceptance tests.

## Inputs
- **Feature or requirement description** (required): what the user wants to build or change.
- **Role / persona** (optional): who the end user is. Defaults to "user" if not provided.
- **Business value or goal** (optional): why this feature matters.
- **Edge cases or constraints** (optional): any known boundary conditions, error paths, or non-functional requirements.

## Output
A user story in the following structure:

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

#### Scenario 2: <scenario title>
- **Given** <precondition>
- **When** <action>
- **Then** <expected outcome>

### Notes
- <Any assumptions, open questions, or out-of-scope items>
```

## Constraints
- Each scenario must have at least one **Given**, one **When**, and one **Then** step.
- Use **And** to chain additional steps within a Given/When/Then block when needed.
- Keep scenarios atomic: one behavior per scenario.
- Do not invent requirements the user did not mention. If something is ambiguous, list it in **Notes** as an open question.
- Write in plain language that both technical and non-technical readers can understand.
- Aim for 3–7 scenarios per story. If more are needed, suggest splitting the story.

## One More Thing
If anything is unclear, missing, or conflicting, stop and ask the user before proceeding.

## How

### Step 1: Gather Context
1. Read the user's feature description carefully.
2. Identify the **role** (who), the **capability** (what), and the **business value** (why).
3. If any of these are missing or vague, ask the user before continuing.

### Step 2: Write the Story Statement
1. Compose the **As a / I want / So that** statement.
2. Keep it concise — one sentence per clause.

### Step 3: Identify Scenarios
1. Extract the **happy path** first — the main success flow.
2. Identify **alternate paths** — valid variations of the input or context.
3. Identify **error or edge-case paths** — invalid input, missing data, permission failures, timeouts, etc.
4. If the user provided explicit edge cases, include them. Do not fabricate scenarios beyond what the description supports.

### Step 4: Write Given/When/Then for Each Scenario
1. **Given** sets up the precondition or system state.
2. **When** describes the user action or system event.
3. **Then** states the observable outcome or system response.
4. Use **And** for additional steps within a block:
   ```
   - **Given** the user is logged in
   - **And** the user has admin privileges
   - **When** the user deletes a record
   - **Then** the record is removed
   - **And** an audit log entry is created
   ```

### Step 5: Add Notes
1. List any assumptions made during writing.
2. Flag open questions or ambiguities for the user to resolve.
3. Note anything explicitly out of scope.

### Step 6: Deliver
1. Output the complete user story in the format shown in **Output**.
2. If the user specified a file path, write it there. Otherwise, output in the conversation.
