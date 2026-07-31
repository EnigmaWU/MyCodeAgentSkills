# Output, Validation, and Recovery

## Output Principles

AI outputs should be:

- **Clear**: Instantly understandable and structured for scanning.
- **Verifiable**: Connected to sources, data, evidence, or review methods when claims matter.
- **Grounded**: Shaped by the user's context and constraints.
- **Actionable**: Oriented toward the user's next step.
- **Adjustable**: Easy to edit, regenerate, compare, fork, or partially accept.

## Presentation Choices

Choose the output format by the next action:

- summary for orientation
- table for comparison
- canvas or document for drafting
- diff for changes
- preview for external actions
- checklist for review
- citation-backed answer for claims
- recommendation plus rationale for decisions
- generated artifact plus editing controls for creative work

## Verification Rules

- Provide citations, source snippets, provenance, comparisons, data lineage, or human review when objective claims matter.
- Disclose AI-generated or synthetic content when users could mistake it for human-authored or authoritative material.
- Do not decorate output with unsupported confidence percentages.
- Separate uncertainty, assumptions, and missing information from the main result.
- For high-risk domains, make review-before-act the default.

## Onward Action Rules

- Visually distinguish draft, preview, send, publish, commit, delete, and external-share actions.
- Make destructive or external actions require explicit confirmation.
- Let users accept partial output, revise selected sections, regenerate variants, compare versions, and continue from an edited result.
- Preserve the relationship between final output and the input, context, plan, sources, and checkpoints that produced it.

## Recovery Rules

Errors should say:

- what happened
- what work was preserved
- whether the task is paused, failed, or partially complete
- what options the user has now
- whether the system can retry safely

Recovery options should include edit input, retry, retry from checkpoint, skip, replace data, grant permission, continue manually, cancel, branch, or roll back.
