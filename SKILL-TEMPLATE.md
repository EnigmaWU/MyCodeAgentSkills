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
| How | **Structural** | The execution structure, explicit phases, and review loops. |
| Constraints | **Logical** | Invariants, safety boundaries, and explicitly required tools. |

## Choose a Version

| Version | Use when | Default shape |
| --- | --- | --- |
| SIMPLE | One straight-line workflow, light context, one main output | 5W1H plus a short How |
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
1. <Gather the minimum context.>
2. <Do the task.>
3. <Validate the result.>

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
- <Things this skill must not do>

## One More Thing
If anything is unclear, missing, or conflicting, stop and ask the user before proceeding.

## How (Structural Workflow)
1. <Gather the required context.>
2. <Perform the main task.>
3. <Validate the result.>
4. <Report the outcome clearly.>
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
- <Things this skill must not do>

## One More Thing
If anything is unclear, missing, or conflicting, stop and ask the user before proceeding.

## How (Structural Workflow)

### Phase 1: <discovery or decision>
<What to do and why it matters.>

### Phase 2: <execution>
<What to do and why it matters.>

### Phase 3: <validation or iteration>
<Explicit review loops or validation gates between phases.>

## Resources
- <scripts/>
- <references/>
- <assets/>

## Validation
1. <Check the frontmatter and section names.>
2. <Run the validation or review flow.>
3. <Report gaps, risks, or follow-up work.>
```

## Notes

- Start with the simplest version that can describe the workflow accurately.
- Keep the `description` specific because it is the discovery surface for the agent.
- Keep `name` aligned with the skill folder name.
- Quote the `description` when it contains colons.
- Keep the `One More Thing` section in every version.
- Prefer real examples and real artifacts over abstract placeholders.
