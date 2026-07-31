# Validation Checklist

Use this checklist against a design brief, prototype, PRD, or implemented autonomous AI feature.

## User Job and Autonomy

- The design names the primary user, job, success outcome, and workflow boundary.
- The AI role is classified as advise, draft, plan, act with approval, or act with monitoring.
- The selected autonomy level matches the task stakes, reversibility, cost, and user expertise.
- High-impact, privacy-sensitive, external, or irreversible actions require human review.

## Capability and Orchestration

- The design maps each AI capability to a concrete user need.
- Users can discover what the system can do through relevant examples, controls, templates, or mode labels.
- The interface shows active models, tools, data sources, memory, or permissions when they affect behavior.
- Capability changes are visible when models, tools, data, modes, or permissions change.
- Unsupported capabilities have a fallback, refusal, or escalation path.

## Input and Context

- Users can provide intent through text, context, and direct manipulation.
- The interface shows what context the AI will use.
- Users can adjust, remove, narrow, replace, or freeze context.
- Clarifying questions appear when ambiguity creates meaningful cost or risk.
- Editable assumptions appear when the system proceeds without clarification.

## Planning and Execution

- Multistep, long-running, high-stakes, or expensive work reveals a plan before meaningful action.
- The plan shows sequence, dependencies, branch points, delegated tools or agents, and expected outputs at the right level of detail.
- Users can approve, edit, reorder, skip, or cancel planned work where it affects outcome.
- Tool use and delegated agent work are visible enough to evaluate risk.

## Progress, Permissions, and Recovery

- Latency feedback matches task duration and stakes.
- Progress is visible at notification, overview, detail, and record levels when needed.
- Checkpoints exist before assumptions, permissions, external actions, irreversible changes, and major artifact transitions.
- Permission prompts explain access, purpose, duration, revocation, next action, and denial outcome.
- The user can pause, edit direction, resume, retry, skip, cancel, branch, or roll back.
- Errors explain what happened, what was preserved, and what the user can do next.

## Outputs and Onward Action

- Outputs are clear, verifiable, grounded, actionable, and adjustable.
- Claims have sources, provenance, comparisons, review paths, or stated uncertainty where appropriate.
- Draft, preview, send, publish, commit, delete, and external-share actions are visually and behaviorally distinct.
- Users can revise selected parts, regenerate variants, compare versions, or accept partial outputs.
- The design supports at least four walkthroughs: happy path, ambiguous input, tool or permission failure, and high-risk or irreversible action.
