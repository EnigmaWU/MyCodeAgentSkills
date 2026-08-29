---
name: doc-with-usage-example
description: >
  WHEN/WHERE/WHO: [Scheduling: Use when: the user asks to create or update documentation. Applies to: markdown documents, READMEs, guides, and runbooks]
  HOW: [Structural: Helps with: producing docs that always include 5W1H context and a copy-exec Usage Example]
  WHY: [Scheduling: Provides structured workflow execution to prevent errors and ensure standards.]
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

## Output (Logical Evidence)
A document section set that includes:
- 5W1H coverage: **Who, What, When, Where, Why, How**.
- A dedicated `## Usage Example` section with copy-exec snippets.

## Optimization Readiness
- **Failure Signals**: The document lacks a usage example, examples are not executable, 5W1H coverage is incomplete, or the example drifts away from the documented environment.
- **Evidence To Collect**: Draft docs, usage snippets, consistency checks, and examples showing how the copy-exec section improved comprehension or execution readiness.
- **Safe Mutation Boundaries**: Refine 5W1H prompts, usage-example structure, and validation guidance without changing the core requirement to include an executable example.
- **Acceptance Criteria**: Accept revisions only if the final document includes a clear Usage Example, keeps the narrative aligned with the example commands, and remains executable as written.
- **Rejected Revision Handling**: Record non-executable examples, placeholder-only commands, and missing-5W1H drafts so they are not repeated.
- **Transfer Check**: Verify the workflow still works for READMEs, runbooks, and operational guides.
- **Stop Rule**: If the environment, expected result, or command details are unclear, stop and ask before drafting the document.

## Constraints (Logical Boundaries)
- Always include a section titled exactly `## Usage Example`.
- Ensure examples are executable as written (no placeholder-only commands unless explicitly labeled).
- Keep examples aligned with the documented environment and paths.
- If details are missing or conflicting, do not guess.

## One More Thing
If anything is unclear, missing, or conflicting, stop and ask the developer before proceeding.

## How (Structural Workflow)
1. Gather the minimum context: audience, goal, environment, and expected outcome.
2. Draft the document using 5W1H headings (Who/What/When/Where/Why/How).
3. Add `## Usage Example` with at least one copy-exec command block and brief expected result.
4. Validate consistency between narrative steps and the example commands.
5. Deliver to the requested file or return in chat.

## Review In Mind (ReviewInMindGenie)

Before delivering, activate the ReviewInMindGenie: stop authoring, switch to a skeptical reviewer, and critique the artifact as if someone else had produced it.

1. **Review Against Own Rules**: Re-read the output against this skill's `What`, `Constraints (Logical Boundaries)`, and `Validation` criteria. Check each rule explicitly; do not assume it passed because it was easy to write.
2. **Classify Findings**: Label each defect as BLOCKER (output unusable), MAJOR (violates a core rule), or MINOR (polish/consistency).
3. **Fix or Escalate**: Fix BLOCKER and MAJOR findings immediately when the fix is unambiguous. After each fix, re-check the affected criteria. If a finding cannot be fixed without new input (missing evidence, conflicting requirements, or a user decision), do not guess — report it as an open question or known gap.
4. **Deliver with a Review Note**: Present the output with a short note: what was checked, what was fixed, and what remains as a known gap. Never present an unreviewed artifact as final.

Review lens for this skill:
- Does the doc include a copy-executable Usage Example with expected results?
- Do the 5W1H sections and the example agree on paths, commands, and behavior?
- Would a new developer succeed by following only the doc?
