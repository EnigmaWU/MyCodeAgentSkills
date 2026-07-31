---
name: task-commit-trigger
description: >
  WHEN/WHERE/WHO: [Scheduling: Developers or agents who have just finished a task and want a structured commit message.]
  HOW: [Structural: Use this SKILL to auto-trigger a commit prompt and generate a structured WHAT/HOW/WHY git commit.]
  WHY: [Scheduling: Capturing the rationale immediately after task completion ensures accurate context and saves time.]
---

# Task Commit Trigger

## Who
Developers or agents who have just finished a task and want a structured, high-quality git commit message.

## What
Auto triggers or notices developer when a task is just completed by asking: "Shall we commit just completed work?". If the user agrees, it generates a structured git commit message explaining the rationale (WHAT, HOW, WHY) and performs the commit.

## When
- A user request or task discussed in the conversation context is fulfilled/completed.
- The user says something like "we're done with this task", "looks good", "save the progress", or explicitly asks to commit.
- The agent finishes a logical unit of work during the interaction.

## Where
Applies to the local git repository in the workspace.

## Why
- Good commit messages are essential for project maintainability.
- Capturing the WHAT, HOW, and WHY immediately after task completion ensures accurate context.
- It saves developers time and cognitive effort.

## Inputs
- **Changes made**: The diff or description of the files modified during the task.
- **Task context**: The goal of the task that was just completed.

## Output (Logical Evidence)
- A structured commit message containing:
  - **WHAT**: A short summary of what was solved or added.
  - **HOW**: A brief explanation of the technical changes made.
  - **WHY**: The rationale behind the chosen approach or design decisions.
- Execution of the git commit (if approved).

## Optimization Readiness
- **Failure Signals**: Commit prompts trigger too early, unrelated files are mixed in, commit messages lose the WHAT/HOW/WHY structure, or the rationale becomes a restatement of the diff.
- **Evidence To Collect**: Diff summaries, drafted commit messages, approval responses, and examples where the commit prompt aligned with a completed logical unit of work.
- **Safe Mutation Boundaries**: Refine trigger wording, diff-review guidance, message formatting, and approval steps without changing the core post-completion commit flow.
- **Acceptance Criteria**: Accept revisions only if the skill still asks at the right time, keeps changes scoped, and produces a concise WHAT/HOW/WHY commit rationale.
- **Rejected Revision Handling**: Record premature prompts, unrelated diff bundles, and vague commit rationales so they are not repeated.
- **Transfer Check**: Verify the workflow still works for small tasks and larger multi-file completions.
- **Stop Rule**: If the completed task or changed-files scope is unclear, stop and ask before drafting a commit.

## Constraints (Logical Boundaries)
- Do not commit changes unrelated to the completed task.
- Keep the commit message concise but informative.
- Ensure the WHY section focuses on design decisions, not just repeating the HOW.

## One More Thing
If anything is unclear, missing, or conflicting, stop and ask the user before proceeding.

## How (Structural Workflow)
1. **Proactive Notification**: Immediately upon completing a task in the conversation, auto trigger or notice developer: "Shall we commit just completed work?".
2. **Analyze the changes**: If the user agrees, review the git diff and the completed task context.
3. **Draft the message**: Structure the commit message with clear headers or bullet points for WHAT, HOW, and WHY.
4. **Present to user**: Show the drafted commit message to the user for final review.
5. **Commit**: Upon approval, execute the git commit command.
