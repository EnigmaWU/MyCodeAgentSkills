# Skill Template

Use this file to choose the right `SKILL.md` shape for the skill you are creating.

## Hybrid 5W1H + SSL Guide

This template merges the human-readable 5W1H structure with the machine-readable Scheduling-Structural-Logical (SSL) representation (arXiv:2604.24026) for optimal agent execution.

| Section | SSL Layer | What to capture |
| --- | --- | --- |
| Frontmatter | **Scheduling** | Explicit trigger phrases, boundaries, and context lock. |
| Who | **Scheduling** | Who should use this skill, or who the work is for. |
| What | **Logical** | What the skill does and explicit concrete side effects. |
| When | **Scheduling** | Exact trigger conditions and explicit near-miss definitions. |
| Where | **Scheduling** | Explicit path boundaries or system contexts required. |
| Why | **Scheduling** | Why this skill exists, including value, constraints, and risks. |
| How | **Structural** | The execution state-machine, explicit phases, and branching logic. |
| Constraints | **Logical** | Invariants, required tools, and Anti-Pattern Mapping (what NOT to do). |

## Choose a Version

| Version | Use when | Default shape |
| --- | --- | --- |
| SIMPLE | One straight-line workflow, light context, one main output | 5W1H, a short How, and Validation |
| COMPLICATED | Multi-step workflow, multiple tools, explicit inputs and outputs | 5W1H plus Inputs, Output, and Constraints |
| COMPLEX | Branching workflow, review loops, bundled resources, or multiple save targets | 5W1H plus Inputs, Output, Constraints, Resources, and Validation |

## SIMPLE

Use this when the skill is short, direct, and does not need bundled files.

```md
---
name: <skill-name>
description: 'Use when: <trigger phrases>. Helps with: <task>. Applies to: <scope>.'
OR
description: 
  WHEN/WHERE/WHO: is doing WHAT will activate this SKILL, 
  HOW to use this SKILL to make a BETTER RESULT, 
  and some WHY it matters.
---

# <Skill Title>

## Who
<Who should use this skill or who the task is for.>

## What
<What this skill does and what outcome it should produce.>

## When
<When the agent should invoke this skill. Include trigger phrases and boundaries.>

## Where
<Which files, folders, systems, or contexts this skill applies to.>

## Why
<Why this skill exists and why this workflow is worth reusing.>

## How (Structural Workflow)
<Use strict, deterministic instructions. No ambiguous prose (e.g., 'try to').>
1. **Input State**: <Gather the explicit context needed.>
2. **Execution**: <Perform the deterministic task.>

## Validation (Verifiable Rewards)
1. <Execute a strict checklist, schema validation, or harness command to prove success.>

## One More Thing
If anything is unclear, missing, or conflicting, stop and ask the user before proceeding.
```

## COMPLICATED

Use this when the skill has multiple steps, non-trivial inputs, or clear operating constraints.

```md
---
name: <skill-name>
description: 'Use when: <trigger phrases>. Helps with: <task>. Applies to: <scope>.'
---

# <Skill Title>

## Who
<Who should use this skill or who the task is for.>

## What
<What this skill does and what outcome it should produce.>

## When
<When the agent should invoke this skill. Include trigger phrases and boundaries.>

## Where
<Which files, folders, systems, or contexts this skill applies to.>

## Why
<Why this skill exists and what tradeoffs or risks matter.>

## Inputs
- <Required input or context>
- <Optional input or assumption>

## Output (Logical Evidence)
- <Expected deliverable>
- <Explicitly declared state changes or side effects>

## Constraints (Logical Boundaries)
- <Safety, scope, or style rules>
- <Required CLI tools or APIs>
- **Anti-Pattern Mapping**: <Explicitly state what this skill MUST NOT do to prevent loops/reasoning drift>

## One More Thing
If anything is unclear, missing, or conflicting, stop and ask the user before proceeding.

## How (Structural Workflow)
<Use imperative state-machine logic. Every step must have a clear input/output state.>
1. **Input Phase**: <Gather and validate the required context.>
2. **Execution Phase**: <Perform the main task using explicit conditional branching.>

## Validation (Verifiable Rewards)
1. <Execute a strict checklist, script, or command to prove success before concluding.>
2. <Report the outcome and side-effects clearly.>
```

## COMPLEX

Use this when the skill needs phases, review loops, bundled scripts or assets, or multiple destination platforms.

```md
---
name: <skill-name>
description: 'Use when: <trigger phrases>. Helps with: <task>. Applies to: <scope>.'
---

# <Skill Title>

## Who
<Who should use this skill or who the task is for.>

## What
<What this skill does and what outcome it should produce.>

## When
<When the agent should invoke this skill. Include trigger phrases, boundaries, and near-miss cases.>

## Where
<Which files, folders, systems, or contexts this skill applies to.>

## Why
<Why this skill exists, including value, risks, and why the workflow is worth preserving.>

## Inputs
- <Required input or context>
- <Optional input or assumption>

## Output (Logical Evidence)
- <Expected deliverable>
- <Explicitly declared state changes or side effects>

## Constraints (Logical Boundaries)
- <Safety, scope, or style rules>
- <Required CLI tools or APIs>
- **Anti-Pattern Mapping**: <Explicitly state what this skill MUST NOT do to prevent loops/reasoning drift>

## One More Thing
If anything is unclear, missing, or conflicting, stop and ask the user before proceeding.

## How (Structural Workflow)
<Use imperative state-machine logic. Every phase must explicitly define branching (If/Then/Else).>

### Phase 1: <discovery or decision>
<Explicit input state expectation and execution steps.>

### Phase 2: <execution>
<Explicit execution steps and expected output state.>

### Phase 3: <iteration>
<Explicit review loops (with hard retry limits) between phases.>

## Resources
- <scripts/>
- <references/>
- <assets/>

## Validation (Verifiable Rewards)
1. <Execute a strict test harness, script, or checklist to mathematically prove success.>
2. <Report gaps, risks, or follow-up work only after verification passes.>
```

## Notes

- Start with the simplest version that can describe the workflow accurately.
- Keep the `description` specific because it is the discovery surface for the agent.
- Keep `name` aligned with the skill folder name.
- Quote the `description` when it contains colons.
- Keep the `One More Thing` section in every version.
- Prefer real examples and real artifacts over abstract placeholders.
