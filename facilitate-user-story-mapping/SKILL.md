---
name: facilitate-user-story-mapping
description: >
  WHEN/WHERE/WHO: [Scheduling: Use when a user or Product Owner wants to break down an epic, feature, or new product idea into a structured User Story Map.]
  HOW: [Structural: Use this SKILL to explicitly execute the state-machine phases of Context Gathering, Backbone Creation, Task Fleshing, and Slice Definition.]
  WHY: [Scheduling: Prevents building the wrong thing by forcing shared understanding, explicit narrative flow, and early identification of functional walking skeletons.]
---

# Facilitate User Story Mapping

## Who
AI Agents acting as Agile Facilitators, Product Owners, or Business Analysts helping a team break down complex product requirements.

## What
Guides the user through Jeff Patton's User Story Mapping process to generate a deterministic, 2D matrix (Story Map) consisting of a horizontal backbone (Activities) and vertical building blocks (Tasks).

## When
Invoke this skill when the user says "let's break down this epic", "help me map out this feature", or explicitly asks to "create a story map".
*Near-miss*: Do not use this if the user just wants to write a single Jira ticket or acceptance criteria (use a story-writing skill instead).

## Where
Applies to the discovery phase of a product or feature. Outputs are typically saved as Markdown tables, JSON structures, or directly pushed to a backlog tool.

## Why
Incremental delivery often fails because it delivers "parts of a car" rather than a "skateboard, then bicycle". Story mapping ensures iterative delivery by focusing on end-to-end narrative flow and slicing by outcome, guaranteeing that every release is a functional walking skeleton.

## Inputs
- **Product/Feature Idea**: A high-level description of what needs to be built.
- **Target User**: Who this feature is primarily for.

## Output (Logical Evidence)
- A structured User Story Map (Markdown or JSON).
- Explicit identification of the "Functional Walking Skeleton" slice.

## Constraints (Logical Boundaries)
- **Formatting**: Tasks MUST be written as short, active verb phrases (e.g., "Check email", "Reset password").
- **Goal-Levels**: Differentiate strictly between "Activities" (high-level goals) and "Tasks" (sea-level actions).
- **Anti-Pattern Mapping**: 
  1. DO NOT write detailed acceptance criteria until the entire backbone and primary tasks are mapped.
  2. DO NOT allow "slicing" by architectural component (e.g., "Database layer"). Slices MUST be end-to-end user outcomes.
  3. DO NOT use passive voice or ambiguous terms (e.g., "System processes data"). 

## One More Thing
If anything is unclear, missing, or conflicting, stop and ask the user before proceeding.

## How (Structural Workflow)
<Use imperative state-machine logic. Every phase must explicitly define branching (If/Then/Else).>

### Phase 1: Opportunity Framing
**Input State**: User provides a raw idea.
1. Ask the user to explicitly define the Target User and the Business Outcome.
2. *Branch*: If the user cannot define the outcome, pause and refuse to map until the "Why" is established.
**Output State**: A confirmed target user and outcome.

### Phase 2: Building the Backbone (Activities)
**Input State**: Confirmed outcome.
1. Prompt the user to list the high-level steps the user takes from start to finish (the narrative flow).
2. Synthesize these into 4-8 high-level "Activities" (e.g., "Manage Account", "Find Product").
3. *Branch*: If an activity is too granular (a sea-level task), push it down to Phase 3.
**Output State**: A confirmed horizontal array of Activities.

### Phase 3: Fleshing out Tasks
**Input State**: A confirmed backbone.
1. For each Activity, iterate horizontally. Ask the user: "What specific tasks does the user do to accomplish [Activity]?"
2. Write these as vertical columns of short verb phrases under each Activity.
3. Play "What-About" to extract exceptions and variations (e.g., "What if the password fails?"). Place these deeper down the vertical column.
**Output State**: A 2D grid of Activities and Tasks.

### Phase 4: Slicing the Walking Skeleton
**Input State**: A fully fleshed 2D grid.
1. Draw a horizontal line across the top tasks.
2. Ask the user: "What is the absolute minimum set of tasks needed to reach the end of the narrative flow, even if it lacks error handling?"
3. Move those critical tasks above the line to form Slice 1: The Functional Walking Skeleton.
**Output State**: A sliced Story Map ready for execution.

## Validation (Verifiable Rewards)
1. Verify that the output map contains a continuous narrative flow from left to right.
2. Verify that Slice 1 contains at least one task for every critical Activity (proving end-to-end viability).
3. If verification passes, output the final Story Map in Markdown format.
