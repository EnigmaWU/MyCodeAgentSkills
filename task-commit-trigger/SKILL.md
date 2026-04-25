---
name: task-commit-trigger
description: 'Use when: a task is just completed. Helps with: auto triggering or noticing developer "shall we commit just completed work?", and generating a structured WHAT/HOW/WHY commit message. Applies to: git repositories and conversation context.'
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

## Output
- A structured commit message containing:
  - **WHAT**: A short summary of what was solved or added.
  - **HOW**: A brief explanation of the technical changes made.
  - **WHY**: The rationale behind the chosen approach or design decisions.
- Execution of the git commit (if approved).

## Constraints
- Do not commit changes unrelated to the completed task.
- Keep the commit message concise but informative.
- Ensure the WHY section focuses on design decisions, not just repeating the HOW.

## One More Thing
If anything is unclear, missing, or conflicting, stop and ask the user before proceeding.

## How
1. **Proactive Notification**: Immediately upon completing a task in the conversation, auto trigger or notice developer: "Shall we commit just completed work?".
2. **Analyze the changes**: If the user agrees, review the git diff and the completed task context.
3. **Draft the message**: Structure the commit message with clear headers or bullet points for WHAT, HOW, and WHY.
4. **Present to user**: Show the drafted commit message to the user for final review.
5. **Commit**: Upon approval, execute the git commit command.
