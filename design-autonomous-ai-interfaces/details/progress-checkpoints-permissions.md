# Progress, Checkpoints, and Permissions

## Latency Guidance

- **Under 0.1 seconds**: Surface the result immediately.
- **Around 1 second**: Minimal status is acceptable if the user remains in flow.
- **Around 10 seconds or more**: Provide visible progress, step state, or an expectation of what is happening.
- **Long-running autonomous work**: Let users step away and return to a stable record of progress, decisions, and outputs.

The purpose is not distraction. The purpose is to show why the wait exists and whether progress is being made.

## Progress Layers

Design progress at four levels:

1. **Notification**: A small signal that work started, paused, completed, or needs attention.
2. **Overview**: Current phase, estimated effort, and next expected event.
3. **Detail**: Step-by-step plan, tool calls, intermediate outputs, and blockers.
4. **Record**: Durable history of prompts, assumptions, permissions, artifacts, checkpoints, and actions.

## Checkpoints

A checkpoint pauses work or records a stable state so the user can inspect, approve, edit, or recover.

Create checkpoints before:

- executing a plan
- using new data or permissions
- sending, publishing, buying, deleting, committing, or changing external state
- locking in assumptions
- moving from analysis to generated artifact
- taking a low-confidence branch

Each checkpoint must show what happened, what happens next, and what choices are available.

## Rollback and Branching

- Preserve stable states for evolving artifacts.
- Restoring a checkpoint should create a new branch or snapshot rather than deleting current work.
- Show differences between versions when the artifact is text, code, configuration, design, or data.
- Treat user edits as new input for later steps, not as disposable changes.

## Permission Prompts

Every permission prompt must answer:

- What will be accessed?
- Why is it needed now?
- What will the AI do after access is granted?
- How long does access last?
- How can the user revoke it?
- What happens if the user denies it?

Use consistent placement, language, and visual treatment so consent is recognizable.
