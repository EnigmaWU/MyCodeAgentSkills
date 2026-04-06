# Skill Template

Use this file to choose the right `SKILL.md` shape for the skill you are creating.

## 5W1H Guide

| Item | What to capture |
| --- | --- |
| Who | Who should use this skill, or who the work is for |
| What | What problem the skill solves and what output it should produce |
| When | When the skill should be invoked, including trigger phrases and boundaries |
| Where | Which files, folders, systems, or contexts it applies to |
| Why | Why this skill exists, including value, constraints, and risks |
| How | The workflow, tools, decision points, and validation steps |

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

## How
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

## Output
- <Expected deliverable>
- <Validation evidence or artifacts>

## Constraints
- <Safety, scope, tool, or style rules>
- <Things this skill must not do>

## One More Thing
If anything is unclear, missing, or conflicting, stop and ask the user before proceeding.

## How
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

## Output
- <Expected deliverable>
- <Validation evidence or artifacts>

## Constraints
- <Safety, scope, tool, or style rules>
- <Things this skill must not do>

## One More Thing
If anything is unclear, missing, or conflicting, stop and ask the user before proceeding.

## How

### Phase 1: <discovery or decision>
<What to do and why it matters.>

### Phase 2: <execution>
<What to do and why it matters.>

### Phase 3: <validation or iteration>
<What to do and why it matters.>

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
