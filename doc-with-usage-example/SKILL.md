---
name: doc-with-usage-example
description: 'Use when: the user asks to create or update documentation. Helps with: producing docs that always include 5W1H context and a copy-exec Usage Example. Applies to: markdown documents, READMEs, guides, and runbooks.'
---

# Document with Usage Example

## Who
Developers, maintainers, and agents who create or revise technical documentation.

## What
Produce documentation that is immediately actionable by always including a **Usage Example** section users can copy and execute, while organizing core context with the 5W1H structure.

## When
- The user asks to create, draft, or update documentation.
- The document explains how to use a command, script, API, or workflow.
- The user needs higher confidence through runnable examples.

## Where
- Markdown docs such as `README.md`, `docs/*.md`, and operational guides.
- Chat responses when no target file path is provided.

## Why
- 5W1H keeps documentation complete and understandable.
- A copy-exec **Usage Example** reduces ambiguity and speeds adoption.
- Concrete examples increase confidence more than abstract instructions.

## Inputs
- Target document path or output destination.
- Topic/workflow that the document must explain.
- Required commands, parameters, and expected results.

## Output
A document section set that includes:
- 5W1H coverage: **Who, What, When, Where, Why, How**.
- A dedicated `## Usage Example` section with copy-exec snippets.

## Constraints
- Always include a section titled exactly `## Usage Example`.
- Ensure examples are executable as written (no placeholder-only commands unless explicitly labeled).
- Keep examples aligned with the documented environment and paths.
- If details are missing or conflicting, do not guess.

## One More Thing
If anything is unclear, missing, or conflicting, stop and ask the developer before proceeding.

## How
1. Gather the minimum context: audience, goal, environment, and expected outcome.
2. Draft the document using 5W1H headings (Who/What/When/Where/Why/How).
3. Add `## Usage Example` with at least one copy-exec command block and brief expected result.
4. Validate consistency between narrative steps and the example commands.
5. Deliver to the requested file or return in chat.
