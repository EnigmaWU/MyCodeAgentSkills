# Input Patterns

## Three Intent Channels

1. **Implicit context**: Current document, selected text, open workspace, user role, history, location, source data, or prior state.
2. **Explicit prompt**: The user's typed or spoken request.
3. **Direct manipulation**: Selecting, dragging, highlighting, attaching, toggling, choosing from menus, or editing structured fields.

Use all three when possible. Do not force users to describe in prose what the interface already knows or can let them select.

## CARE Prompt Support

When explicit prompting is needed, help the user supply:

- **Context**: Situation, role, audience, constraints, and why the request matters.
- **Action**: The exact analysis, transformation, generation, comparison, or decision support needed.
- **Results**: Desired format, length, tone, structure, and level of detail.
- **Examples**: Reference inputs, style samples, expected output shapes, or counterexamples.

Use forms, chips, inline suggestions, examples, and clarifying questions to gather CARE elements without making the interface feel like a questionnaire.

## Context Visibility

Show what the AI will use before costly or risky work:

- selected text or objects
- attached files and data sources
- active project, workspace, or account
- memories or prior conversation used
- tool mode or model mode
- assumptions inferred by the system

Users must be able to remove, replace, narrow, expand, or freeze context.

## Clarification Rules

- Ask a clarifying question when ambiguity creates meaningful cost, risk, or rework.
- Proceed with editable assumptions when the task is low-risk and easy to revise.
- Prefer one focused clarification over a long setup interview.
- Make the assumption visible if the system proceeds without asking.
