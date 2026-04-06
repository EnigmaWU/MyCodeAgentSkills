# Skill Template

Use this as the starting point for a new `SKILL.md` file.

## 5W1H Guide

| Item | What to capture |
| --- | --- |
| Who | Who should use this skill, or who the work is for |
| What | What problem the skill solves and what output it should produce |
| When | When the skill should be invoked, including trigger phrases |
| Where | Which files, folders, systems, or contexts it applies to |
| Why | Why this skill exists, including constraints, risks, or value |
| How | The concrete workflow, tools, and validation steps |

## Template

```md
---
name: <skill-name>
description: 'Use when: <when this skill should be invoked>. Helps with: <what it does>. Applies to: <where it applies>.'
---

# <Skill Title>

## Who
<Who should use this skill or who the task is for.>

## What
<What this skill does and what outcome it should produce.>

## When
<When the agent should invoke this skill. Include trigger phrases and clear boundaries.>

## Where
<Which files, folders, systems, or contexts this skill applies to.>

## Why
<Why this skill exists. Call out value, risks, or constraints that matter.>

## How
1. <Gather the required context.>
2. <Perform the main task.>
3. <Validate the result.>
4. <Report the outcome clearly.>

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
```

## Notes

- Keep the `description` specific because it is the discovery surface for the agent.
- Keep `name` aligned with the skill folder name.
- Quote the `description` when it contains colons.
