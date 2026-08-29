---
name: design-agentic-screenplay-model
description: >
  WHEN/WHERE/WHO: [Scheduling: Use when an AI Agent or Architect is designing the core reasoning and execution loop for a multi-agent or autonomous system.]
  HOW: [Structural: Use this SKILL to define the system strictly in terms of Actors (Agents), Abilities (Tools), Tasks (Prompts/Chains), and Interactions (Tool Executions).]
  WHY: [Scheduling: Monolithic prompts and unstructured tool usage lead to reasoning drift. The Screenplay pattern forces deterministic, composable agent behavior.]
---

# Design Agentic Screenplay Model

## Common Contract (Load First)

When this skill is activated, first load [skill-common](../skill-common/SKILL.md) and apply the shared conventions it defines: canonical section order, frontmatter rules, anti-pattern guidance, and the Review In Mind loop in [review-in-mind](../skill-common/details/review-in-mind.md). This skill adds only domain-specific rules below.

## Who
AI Agents, Orchestrators, and System Architects designing autonomous AI systems.

## What
Translates the classic test-automation Screenplay Pattern into a deterministic Agentic Architecture. It teaches agents how to define themselves as `Actors`, bind their tools as `Abilities`, structure their reasoning loops as `Tasks`, and execute commands as `Interactions`.

## When
Invoke this skill when scaffolding a new agentic workflow, refactoring a complex monolithic prompt into manageable steps, or designing multi-agent communication protocols.
*Near-miss*: Do not use this if you are just writing a simple UI test script. For traditional software testing, use `apply-screenplay-pattern` instead.

## Where
Applies to the architecture design and core loop implementation of agentic codebases (e.g., LangGraph, AutoGen, or custom agent loops).

## Why
In classic SE, Screenplay was used to separate "what" from "how" in UI tests. In Agentic SE, the LLM *is* the Actor. If we do not explicitly separate its Abilities (tools) from its Tasks (goals), the agent's context window becomes bloated and it suffers from reasoning drift. Screenplay forces agents into a strict, composable state machine.

## Inputs
- **Business Goal**: The high-level objective the agent swarm must achieve.
- **Available Tools**: The APIs, CLIs, or access points available to the system.

## Output (Logical Evidence)
- A defined set of `Actors` (Agents with specific personas).
- A mapped set of `Abilities` (Tools granted to each Actor).
- A hierarchical breakdown of `Tasks` (Multi-step reasoning prompts) and `Interactions` (Atomic tool executions).

## Optimization Readiness
- **Failure Signals**: Actors blur together, tasks invoke tools directly, abilities are over-shared, or the model collapses back into one monolithic prompt instead of a cast-task-interaction structure.
- **Evidence To Collect**: Actor-to-ability maps, task hierarchies, interaction breakdowns, and examples of delegation failures or successful actor isolation.
- **Safe Mutation Boundaries**: Refine persona naming, task decomposition guidance, interaction examples, and delegation rules without changing the core Actor, Ability, Task, and Interaction model.
- **Acceptance Criteria**: Accept revisions only if the design preserves actor isolation, routes technical execution through interactions, and keeps tasks focused on business intent rather than raw tool calls.
- **Rejected Revision Handling**: Record monolithic-prompt rewrites, direct-task-to-tool shortcuts, and weak actor definitions so they are not reintroduced.
- **Transfer Check**: Verify the workflow still works for single-agent screenplay designs and multi-actor collaborations with delegated abilities.
- **Stop Rule**: If the available abilities or actor responsibilities are undefined, stop and ask before drafting the screenplay topology.

## Constraints (Logical Boundaries)
- **Actor Isolation**: Actors MUST NOT share abilities unless explicitly granted. An agent without the `QueryDatabase` ability cannot perform a database interaction.
- **Anti-Pattern Mapping**: 
  1. DO NOT write monolithic prompts that instruct an agent to "think, plan, and execute" in one go. You must break it down into `Tasks`.
  2. DO NOT allow `Tasks` to directly invoke external systems. `Tasks` must delegate to `Interactions` (the actual tool call).
  3. DO NOT use generic actor names (e.g., "The Agent"). Give them personas (e.g., "The Code Reviewer").

## One More Thing
If the required tools (Abilities) are not well-defined, stop and ask the user to clarify the technical interfaces before designing the Screenplay model.

## How (The 4-Phase Refinement Protocol)

### Phase 1: Actor and Ability Discovery
**Input State**: A raw business goal and a list of available tools.
1. Identify the **Actors** required to achieve the goal. Give each a clear persona.
2. Map the available tools to **Abilities**. Assign abilities only to the actors that need them.
3. *Branch*: If an actor lacks the ability to complete its core function, pause and request new tools.
**Output State**: A defined Cast of Actors and their Abilities.

### Phase 2: Task Hierarchies (The "What")
**Input State**: A defined Cast of Actors.
1. For each Actor, define the high-level **Tasks** they must perform.
2. A Task represents a reasoning step or a sequence of actions (e.g., `ReviewPullRequest`).
3. Ensure Tasks are declarative and focus on the business intent, not the technical implementation.
**Output State**: A mapped hierarchy of Tasks for each Actor.

### Phase 3: Interactions and Questions (The "How")
**Input State**: A mapped hierarchy of Tasks.
1. Break down each Task into **Interactions** (atomic tool executions, e.g., `CallGitHubAPI`) and **Questions** (state queries, e.g., `CheckBuildStatus`).
2. *Branch*: If a Task requires an Interaction the actor does not have the Ability for, refactor the Task to delegate to another Actor.
**Output State**: A complete, executable Screenplay state machine.

### Phase 4: Slicing the Agentic Loop
**Input State**: A complete Screenplay state machine.
1. Identify the "Functional Walking Skeleton"—the minimum set of Tasks and Interactions required for the agents to achieve a basic successful outcome.
2. Discard or defer edge-case tasks (e.g., advanced error recovery) until the walking skeleton is proven.
**Output State**: A streamlined agentic workflow ready for implementation.

## Review In Mind (ReviewInMindGenie)

Execute the common review loop in [review-in-mind](../skill-common/details/review-in-mind.md) before delivering.

Review lens for this skill:
- Are Actor/Ability/Task/Interaction roles clearly separated and bound to tools?
- Do the reasoning loops and exit conditions match the agent's actual capabilities?
- Could a new agent configuration execute the model deterministically?

## Validation (Verifiable Rewards)
1. Verify that every Interaction maps to exactly one Ability.
2. Verify that no Task directly executes a system command without delegating to an Interaction.
3. If verification passes, output the Agentic Screenplay Model in Markdown or Mermaid diagram format.
