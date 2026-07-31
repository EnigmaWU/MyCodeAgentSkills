# Agentic Workflow Patterns

## Autonomy Levels

- **Advise**: The AI explains, recommends, or critiques. The user acts.
- **Draft**: The AI creates a candidate artifact. The user edits or accepts.
- **Plan**: The AI decomposes and sequences work. The user approves or revises the plan.
- **Act With Approval**: The AI performs steps but pauses before sensitive or external action.
- **Act With Monitoring**: The AI runs routine, reversible work with visible progress and interruption controls.

Do not choose a higher autonomy level than the risk profile can justify.

## Planning Rules

- Show a plan before multistep, high-stakes, expensive, or hard-to-reverse work.
- Keep plans short for quick tasks.
- Use phases, dependencies, branch points, and expandable substeps for longer workflows.
- Let users approve, edit, reorder, remove, add, or skip steps where the plan affects outcome.
- Give users a "just do it" path only for low-risk work with strong recovery.

## Branching and Delegation

Expose conditional logic in human terms:

- "If the data quality check passes, create the report. If it fails, ask for missing fields."
- "If permission is denied, pause the task and offer a manual upload path."
- "If the draft conflicts with policy, produce a safe alternative and explain what changed."

If multiple tools or agents participate, show enough responsibility boundaries for the user to understand who or what is acting.

## Intervention Points

Add intervention points at:

- plan approval
- ambiguous assumptions
- permission requests
- external actions
- irreversible changes
- low-confidence branches
- major artifact transitions
- error recovery

At each point, offer explicit options: approve, edit, continue, skip, retry, cancel, branch, or roll back.
