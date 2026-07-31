# Principles

## Control Loop

Design autonomous AI interfaces as one loop rather than separate screens:

1. **Configuration**: Accounts, tools, memory, defaults, and permissions decide what the system can do.
2. **Input**: Human intent enters through prompts, context, direct manipulation, files, selections, or inferred state.
3. **Computation**: The system interprets, retrieves, plans, routes, generates, checks, and may call tools.
4. **Output**: The interface presents a result as a designed artifact, not merely an answer.
5. **Action**: The user verifies, edits, approves, rejects, publishes, sends, commits, or feeds the result back into the loop.

## Core Principles

1. Start with the user job, not model novelty.
2. Make capability discoverable through task-specific examples and controls.
3. Split intent capture across implicit context, explicit prompting, and direct manipulation.
4. Show hidden context and make it correctable.
5. Make orchestration intentional, transparent, and recognizable.
6. Reveal plans before high-stakes, expensive, or long-running autonomous work.
7. Design progress as layered communication, from glanceable status to full records.
8. Treat latency as part of the experience, not merely a performance defect.
9. Present output as an artifact users inspect, edit, verify, and act on.
10. Support verification before action, especially for objective claims or real-world effects.
11. Preserve shared control: pause, redirect, approve, deny, resume, branch, and roll back.
12. Make recovery normal by preserving prompts, assumptions, partial outputs, checkpoints, and user edits.

## Autonomy Test

Before adding autonomy, answer these questions:

- What is the user delegating?
- What remains under explicit human control?
- What can the AI do without asking?
- What always requires approval?
- What is reversible?
- What evidence lets the user trust, reject, or revise the result?
