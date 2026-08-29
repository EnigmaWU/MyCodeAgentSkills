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
| Optimization Readiness | **Logical** | Failure signals, revision evidence, safe mutation boundaries, acceptance criteria, rejection handling, and stop rules. |
| Constraints | **Logical** | Invariants, required tools, and Anti-Pattern Mapping (what NOT to do). |

## Choose a Version

| Version | Use when | Default shape |
| --- | --- | --- |
| SIMPLE | One straight-line workflow, light context, one main output | 5W1H, a short How, and Validation |
| COMPLICATED | Multi-step workflow, multiple tools, explicit inputs and outputs | 5W1H plus Inputs, Output, and Constraints |
| COMPLEX | Branching workflow, review loops, bundled resources, or multiple save targets | 5W1H plus Inputs, Output, Constraints, Resources, and Validation |

## Depth Rules

Choose the tier by workflow depth and control structure, not by document length.

- **SIMPLE = one path**: Use when the skill is mostly a straight-line execution with 1 to 2 main steps, little or no branching, and direct local validation.
- **COMPLICATED = one path plus decisions**: Use when the skill has multiple steps, at least one meaningful decision point, explicit constraints, or non-trivial input/output handling.
- **COMPLEX = multiple paths plus iteration**: Use when the skill has phased execution, branching paths, retries, review loops, escalation rules, multiple artifacts, or resource handoffs.

Practical test:

1. If the skill can be executed as one linear checklist, choose `SIMPLE`.
2. If the skill still has one main flow but needs explicit branching or stronger state checks, choose `COMPLICATED`.
3. If the skill requires iteration, alternative paths, or a multi-phase control loop, choose `COMPLEX`.

Do not upgrade the tier only because the topic is important or the explanation is long. Upgrade the tier when the execution logic becomes deeper.

## Activation Checklist

Before finalizing any skill, check the discovery surface explicitly.

1. Put the strongest exact trigger phrases in the frontmatter `description`, not only in `## When`.
2. Put the strongest near-miss boundaries in the frontmatter `description`, not only in `## When`.
3. Make the frontmatter specific enough that a model can choose the skill without reading the full body first.
4. Keep `## When` and the frontmatter aligned; they should reinforce each other instead of describing different trigger logic.
5. If the skill is auto-invocable, prefer concrete user-language examples such as `save as skill`, `improve this skill`, or `create a skill from [book]` over abstract summaries like `preserve reusable knowledge`.
6. If activation is weak in practice, fix the frontmatter first before widening the body content.

## Review In Mind (ReviewInMindGenie)

Every skill, regardless of tier, MUST include a `## Review In Mind (ReviewInMindGenie)` section. It is the skill's built-in review gene: after producing the artifact, the agent stops authoring, switches to a skeptical reviewer, and critiques the output as if someone else had produced it. The section MUST contain the four-step loop below plus a skill-specific "Review lens" derived from that skill's `What`, `Constraints (Logical Boundaries)`, and `Validation` criteria. Place it immediately before `## Validation` (or at the end of the file if the skill has no Validation section).

```md
## Review In Mind (ReviewInMindGenie)

Before delivering, activate the ReviewInMindGenie: stop authoring, switch to a skeptical reviewer, and critique the artifact as if someone else had produced it.

1. **Review Against Own Rules**: Re-read the output against this skill's `What`, `Constraints (Logical Boundaries)`, and `Validation` criteria. Check each rule explicitly; do not assume it passed because it was easy to write.
2. **Classify Findings**: Label each defect as BLOCKER (output unusable), MAJOR (violates a core rule), or MINOR (polish/consistency).
3. **Fix or Escalate**: Fix BLOCKER and MAJOR findings immediately when the fix is unambiguous. After each fix, re-check the affected criteria. If a finding cannot be fixed without new input (missing evidence, conflicting requirements, or a user decision), do not guess — report it as an open question or known gap.
4. **Deliver with a Review Note**: Present the output with a short note: what was checked, what was fixed, and what remains as a known gap. Never present an unreviewed artifact as final.

Review lens for this skill:
- <Question 1 derived from this skill's What/Constraints/Validation>
- <Question 2 derived from this skill's What/Constraints/Validation>
```

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

## Optimization Readiness
- **Failure Signals**: <What repeated signs show this skill is not working well enough.>
- **Evidence To Collect**: <What examples, traces, or outputs should be gathered before revising it.>
- **Safe Mutations**: <What parts may be revised without changing the skill's core scope.>
- **Acceptance Criteria**: <What independent check proves the revision is better.>
- **Rejected Revision Rule**: <How to record a failed rewrite or anti-pattern.>
- **Stop Rule**: <When to stop iterating and ask for more evidence or user input.>

## How (Structural Workflow)
<Use strict, deterministic instructions. No ambiguous prose (e.g., 'try to').>
1. **Input State**: <Gather the explicit context needed.>
2. **Execution**: <Perform the deterministic task.>

Example shape:

1. **Input State**: Read the user request and confirm the target artifact name.
2. **Execution**: Generate the artifact in one pass using the required format.
3. **Validation**: Check that the artifact exists and matches the requested shape.

## Review In Mind (ReviewInMindGenie)

Before delivering, activate the ReviewInMindGenie: stop authoring, switch to a skeptical reviewer, and critique the artifact as if someone else had produced it.

1. **Review Against Own Rules**: Re-read the output against this skill's `What`, `Constraints (Logical Boundaries)`, and `Validation` criteria. Check each rule explicitly; do not assume it passed because it was easy to write.
2. **Classify Findings**: Label each defect as BLOCKER (output unusable), MAJOR (violates a core rule), or MINOR (polish/consistency).
3. **Fix or Escalate**: Fix BLOCKER and MAJOR findings immediately when the fix is unambiguous. After each fix, re-check the affected criteria. If a finding cannot be fixed without new input (missing evidence, conflicting requirements, or a user decision), do not guess — report it as an open question or known gap.
4. **Deliver with a Review Note**: Present the output with a short note: what was checked, what was fixed, and what remains as a known gap. Never present an unreviewed artifact as final.

Review lens for this skill:
- <Question 1 derived from this skill's What/Constraints/Validation>
- <Question 2 derived from this skill's What/Constraints/Validation>

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

## Optimization Readiness
- **Failure Signals**: <What recurring failure patterns, ambiguities, or low-quality outcomes indicate the skill needs revision.>
- **Evidence To Collect**: <What traces, examples, review comments, or outputs should be compared before revising the skill.>
- **Safe Mutation Boundaries**: <Which sections may be tightened or restructured, and which invariants must remain stable.>
- **Acceptance Criteria**: <What independent comparison, checklist, or harness proves the new version improved.>
- **Rejected Revision Handling**: <How to record failed candidate edits so they are not repeated blindly.>
- **Transfer Check**: <How to confirm the change still works on at least one nearby use case.>
- **Stop Rule**: <When to stop iterating and escalate for missing context or conflicting evidence.>

## Constraints (Logical Boundaries)
- <Safety, scope, or style rules>
- <Required CLI tools or APIs>
- **Anti-Pattern Mapping**: <Explicitly state what this skill MUST NOT do to prevent loops/reasoning drift>

## How (Structural Workflow)
<Use imperative state-machine logic. Every step must have a clear input/output state.>
1. **Input Phase**: <Gather and validate the required context.>
2. **Execution Phase**: <Perform the main task using explicit conditional branching.>

Example shape:

1. **Input Phase**: Gather the request, required files, and success criteria. If a required input is missing, stop and ask for it; otherwise continue.
2. **Decision Phase**: Choose the correct output path based on the input type. If the request is a new artifact, use the creation path; if it is an existing artifact, use the revision path.
3. **Execution Phase**: Produce or revise the artifact using the selected path.
4. **Validation Phase**: Run the relevant checks and report whether the output satisfied the criteria.

## Review In Mind (ReviewInMindGenie)

Before delivering, activate the ReviewInMindGenie: stop authoring, switch to a skeptical reviewer, and critique the artifact as if someone else had produced it.

1. **Review Against Own Rules**: Re-read the output against this skill's `What`, `Constraints (Logical Boundaries)`, and `Validation` criteria. Check each rule explicitly; do not assume it passed because it was easy to write.
2. **Classify Findings**: Label each defect as BLOCKER (output unusable), MAJOR (violates a core rule), or MINOR (polish/consistency).
3. **Fix or Escalate**: Fix BLOCKER and MAJOR findings immediately when the fix is unambiguous. After each fix, re-check the affected criteria. If a finding cannot be fixed without new input (missing evidence, conflicting requirements, or a user decision), do not guess — report it as an open question or known gap.
4. **Deliver with a Review Note**: Present the output with a short note: what was checked, what was fixed, and what remains as a known gap. Never present an unreviewed artifact as final.

Review lens for this skill:
- <Question 1 derived from this skill's What/Constraints/Validation>
- <Question 2 derived from this skill's What/Constraints/Validation>

## Validation (Verifiable Rewards)
1. <Execute a strict checklist, script, or command to prove success before concluding.>
2. <Report the outcome and side-effects clearly.>

## One More Thing
If anything is unclear, missing, or conflicting, stop and ask the user before proceeding.
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

## Optimization Readiness
- **Failure Signals**: <What repeated defects, routing misses, or unstable outputs trigger a revision cycle.>
- **Evidence To Collect**: <What multi-run traces, benchmark cases, reviews, or transcripts must be gathered.>
- **Safe Mutation Boundaries**: <Which instructions, checklists, examples, or resource links may be changed, and what must remain fixed.>
- **Acceptance Criteria**: <What independent validation gate must pass before accepting a rewrite.>
- **Rejected Revision Handling**: <Where rejected edits, anti-patterns, or failed hypotheses are captured.>
- **Transfer Check**: <How to verify the rewrite generalizes across nearby tasks, users, or environments.>
- **Stop Rule**: <What hard limit or evidence threshold ends the current optimization cycle.>

## Constraints (Logical Boundaries)
- <Safety, scope, or style rules>
- <Required CLI tools or APIs>
- **Anti-Pattern Mapping**: <Explicitly state what this skill MUST NOT do to prevent loops/reasoning drift>

## How (Structural Workflow)
<Use imperative state-machine logic. Every phase must explicitly define branching (If/Then/Else).>

### Phase 1: <discovery or decision>
<Explicit input state expectation and execution steps.>

Example:
If the task goal, evidence, or destination is unclear, stop and resolve the ambiguity. Otherwise classify the request into the correct execution path and record the planned validation gate.

### Phase 2: <execution>
<Explicit execution steps and expected output state.>

Example:
Execute the chosen path and produce the first candidate output. If execution fails because a dependency or constraint blocks progress, switch to the recovery path; otherwise continue to validation.

### Phase 3: <iteration>
<Explicit review loops (with hard retry limits) between phases.>

Example:
Validate the candidate output against the acceptance criteria. If validation passes, finalize the result. If validation fails and the retry budget remains, revise only the allowed sections and rerun validation. If the retry budget is exhausted, stop and escalate with the failed evidence.

## Review In Mind (ReviewInMindGenie)

Before delivering, activate the ReviewInMindGenie: stop authoring, switch to a skeptical reviewer, and critique the artifact as if someone else had produced it.

1. **Review Against Own Rules**: Re-read the output against this skill's `What`, `Constraints (Logical Boundaries)`, and `Validation` criteria. Check each rule explicitly; do not assume it passed because it was easy to write.
2. **Classify Findings**: Label each defect as BLOCKER (output unusable), MAJOR (violates a core rule), or MINOR (polish/consistency).
3. **Fix or Escalate**: Fix BLOCKER and MAJOR findings immediately when the fix is unambiguous. After each fix, re-check the affected criteria. If a finding cannot be fixed without new input (missing evidence, conflicting requirements, or a user decision), do not guess — report it as an open question or known gap.
4. **Deliver with a Review Note**: Present the output with a short note: what was checked, what was fixed, and what remains as a known gap. Never present an unreviewed artifact as final.

Review lens for this skill:
- <Question 1 derived from this skill's What/Constraints/Validation>
- <Question 2 derived from this skill's What/Constraints/Validation>

## Resources
- <scripts/>
- <references/>
- <assets/>

## Validation (Verifiable Rewards)
1. <Execute a strict test harness, script, or checklist to mathematically prove success.>
2. <Report gaps, risks, or follow-up work only after verification passes.>

## One More Thing
If anything is unclear, missing, or conflicting, stop and ask the user before proceeding.
```

## Notes

- Start with the simplest version that can describe the workflow accurately.
- Keep the `description` specific because it is the discovery surface for the agent.
- Keep `name` aligned with the skill folder name.
- Quote the `description` when it contains colons.
- Keep the `One More Thing` section in every version.
- Keep the `## Review In Mind (ReviewInMindGenie)` section in every version, placed before `## Validation` (or at the end if no Validation section exists).
- Prefer real examples and real artifacts over abstract placeholders.
- Keep operational instructions in natural language so the workflow is executable from text alone.
- Treat diagrams, figures, and visual assets as optional references, not required execution steps.
- Keep the optimization-ready section lightweight by default; use stronger multi-run evidence only when the skill is high-value or repeatedly unstable.
- These optimization-ready conventions are inspired by controllable skill-evolution patterns from SkillOpt and SkillOpt-Lite, adapted here as plain-language authoring guidance rather than research-protocol boilerplate.
