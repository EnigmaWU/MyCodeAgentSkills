---
name: update-spec-context
description: >
  WHEN/WHERE/WHO: [Scheduling: Use when: a vibe-coding or AI-assisted coding conversation changes requirements, design decisions, plans, task status, or implementation context. Applies to: GitHub Spec Kit-style specs, plans, tasks, constitutions, and repository planning docs]
  HOW: [Structural: Helps with: updating spec-driven-development context files before the details are lost]
  WHY: [Scheduling: Provides structured workflow execution to prevent errors and ensure standards.]
---

# Update Spec Context

## Common Contract (Load First)

When this skill is activated, first load [skill-common](../skill-common/SKILL.md) and apply the shared conventions it defines: canonical section order, frontmatter rules, anti-pattern guidance, and the Review In Mind loop in [review-in-mind](../skill-common/details/review-in-mind.md). This skill adds only domain-specific rules below.

## Who
Developers, maintainers, product owners, and coding agents who use AI-assisted coding but want the project context to stay explicit, reviewable, and reusable.

## What
Update the repository's spec context after a conversation produces new requirements, decisions, implementation progress, risks, or lessons learned. The deliverable is a focused update to existing spec-driven-development artifacts such as specs, plans, task lists, decision notes, or status documents.

## When
- A conversation resolves an ambiguity, bug, edge case, or design choice that future work should remember.
- The user says "update the spec", "update context", "write this down", "sync the plan", "record this decision", or "keep Spec Kit context current".
- A completed coding step changes task status, implementation plan, acceptance criteria, constraints, or known risks.
- Use `save-as-skill` instead when the reusable output is a new workflow or slash-command-like skill.
- Do not use this skill for trivial comments, transient brainstorming, or facts that should remain only in chat.

## Where
- Spec Kit-style feature folders such as `specs/<feature>/spec.md`, `plan.md`, `tasks.md`, `research.md`, `data-model.md`, or `contracts/`.
- CaTDD SpecFlow-style artifacts such as `projectContext.md`, `pendingNews/`, `todoUS/`, `doingUS/`, `abortUS/`, `doneUS/`, module design docs, or `WorkingProcessLog.md`.
- Repository planning or product docs such as `docs/`, `README.md`, issue bodies, ADRs, backlog files, or user-story markdown.
- The current conversation, recent diffs, test output, and validation logs that explain what changed and why.

## Why
- Vibe coding can solve real problems while leaving the durable project context stale.
- Spec-driven development treats specs, plans, and tasks as the source of truth for humans and agents, not as after-the-fact documentation.
- Updating context immediately preserves decisions, prevents repeated clarification, and gives the next agent better grounding.
- GitHub Spec Kit popularized an explicit loop of specify, plan, tasks, and implement; this skill keeps those artifacts aligned as implementation evolves.

## Inputs
- The relevant conversation segment, including the solved problem, final decision, and any discarded alternatives.
- Existing spec-context artifacts or the location where the user expects context to live.
- Current implementation state, changed files, test results, or task progress when available.
- Optional reference model such as GitHub Spec Kit's specify/plan/tasks/implement workflow or CaTDD `Px SpecFlow`.

## Output (Logical Evidence)
- A short plan shown to the user before editing, listing the artifacts to update and the reason each update is needed.
- Minimal edits to the selected spec-context files.
- A concise summary of what changed, what remains open, and which files were updated.
- Validation evidence such as a diff review, checklist update, or relevant test/docs command when available.

## Optimization Readiness
- **Failure Signals**: Spec artifacts drift from implementation, open questions are written as facts, the skill updates too many files for a small change, or decisions and task status become mixed together.
- **Evidence To Collect**: Update plans, edited artifact diffs, validation output, and examples of context that was accepted, deferred, or left open.
- **Safe Mutation Boundaries**: Refine planning prompts, artifact-selection rules, section wording, and validation checks without changing the core requirement to keep durable spec context aligned with evidence.
- **Acceptance Criteria**: Accept revisions only if the skill updates the smallest correct artifact set, preserves the repository's existing context structure, and distinguishes facts, decisions, tasks, and open questions clearly.
- **Rejected Revision Handling**: Record over-broad edit patterns, unsupported context additions, and structure drift so they are not repeated in later revisions.
- **Transfer Check**: Confirm the workflow still works for requirement changes, decision updates, and task-progress updates rather than only one artifact type.
- **Stop Rule**: If the durable value or factual basis of a proposed context update is unclear, stop and ask before editing project files.

## Constraints (Logical Boundaries)
- Plan first. Do not edit spec-context files until the user has seen the proposed update plan, unless the user explicitly asked for direct editing.
- Preserve the existing artifact structure and terminology. Do not introduce a Spec Kit layout into a repository that uses a different convention unless the user asks.
- Update only context that is supported by the conversation, repository state, or validation output. Mark uncertain items as open questions instead of inventing details.
- Keep edits surgical: update the smallest set of files needed to keep specs, plans, and tasks accurate.
- Separate facts, decisions, tasks, and open questions so future agents can consume the context quickly.
- Do not store secrets, credentials, private personal data, or temporary chat-only details in durable project files.

## One More Thing
If anything is unclear, missing, or conflicting, stop and ask the user before proceeding.

## How (Structural Workflow)
### Phase 1: Decide Whether This Belongs in Spec Context
1. Review the conversation and identify durable information:
   - **Requirement**: new behavior, acceptance criteria, constraints, or non-goals.
   - **Decision**: chosen approach, rationale, and rejected alternatives.
   - **Plan**: implementation steps, dependencies, risks, or sequencing.
   - **Task status**: completed, blocked, deferred, or newly discovered work.
   - **Evidence**: tests, logs, demos, or validation results that support the update.
2. If the information is a reusable workflow, consider `save-as-skill` instead.
3. If it is a one-off fact with no future value, do not write it into durable context.

### Phase 2: Locate the Right Artifact
1. Search for existing spec-context files before creating new ones.
2. Map the update to the artifact that owns it:
   - `spec.md` or user-story docs for user-visible requirements and acceptance criteria.
   - `plan.md` for architecture, approach, dependencies, sequencing, and risks.
   - `tasks.md` for actionable work items and status changes.
   - `research.md`, ADRs, or decision logs for tradeoffs and rationale.
   - `projectContext.md` for stable project facts, constraints, conventions, and confirmed decisions.
   - `pendingNews/`, `todoUS/`, `doingUS/`, `abortUS/`, and `doneUS/` for CaTDD SpecFlow work-item lifecycle status.
   - `WorkingProcessLog.md` for optional traces of command transitions, review decisions, and unresolved questions.
   - `README.md` or docs only when they are the repository's actual source of project context.
3. If no suitable file exists, propose the smallest new artifact and explain why it is needed.

### Phase 3: Show the Update Plan First
Before editing, present a concrete plan:

```markdown
Plan:
1. Update `<file>` to record `<requirement/decision/status>` because `<why it matters>`.
2. Update `<file>` to mark `<task>` as `<status>` with evidence `<test/log/diff>`.
3. Leave `<topic>` as an open question because `<missing information>`.
```

Ask for confirmation when the target files, scope, or facts are ambiguous.

### Phase 4: Apply Minimal Context Edits
1. Edit only the selected artifacts from the plan.
2. Preserve headings, numbering, checkboxes, and local vocabulary.
3. Write updates in a form future agents can act on:
   - Requirements should be testable.
   - Decisions should include rationale.
   - Tasks should have clear completion criteria.
   - Open questions should name the missing decision owner or missing evidence when known.
4. When changing task status, include the evidence that justifies the status.
5. Avoid broad rewrites unless the current artifact is too stale to update safely; if broad rewrite is needed, ask first.

### Phase 5: Validate the Context
1. Review the diff and check that every edit traces back to the conversation or repository state.
2. Confirm that specs, plans, and tasks do not contradict each other.
3. Run existing docs, lint, build, or test commands only when the edited artifacts require it or when the update references validation evidence.
4. If validation exposes uncertainty, update the artifact with an open question rather than hiding the gap.

### Phase 6: Report the Result
1. Summarize updated files and the exact kind of context added.
2. List remaining open questions, blocked tasks, or follow-up validation.
3. If no file was changed, explain why the conversation did not contain durable spec context.

## Resources
- GitHub Spec Kit: https://github.com/github/spec-kit
- GitHub Blog, "Spec-driven development with AI: Get started with a new open source toolkit": https://github.blog/ai-and-ml/generative-ai/spec-driven-development-with-ai-get-started-with-a-new-open-source-toolkit/
- Microsoft Developer Blog, "Diving Into Spec-Driven Development With GitHub Spec Kit": https://developer.microsoft.com/blog/spec-driven-development-spec-kit
- EnigmaWU MyCaTDD `Px SpecFlow`: https://github.com/EnigmaWU/MyCaTDD/blob/main/slashCommands/flows/Px-SpecFlow.md
- `save-as-skill/SKILL.md` for turning a solved workflow into a reusable skill instead of a project-context update.
- `improve-existing-skill/SKILL.md` for folding lessons back into an existing skill.

## Review In Mind (ReviewInMindGenie)

Execute the common review loop in [review-in-mind](../skill-common/details/review-in-mind.md) before delivering.

Review lens for this skill:
- Is the update focused on new requirements, decisions, progress, risks, or lessons, without rewriting unrelated history?
- Does it keep existing spec artifacts consistent (no contradictory status)?
- Is every change traceable to a conversation event?

## Validation
1. Verify the frontmatter `name` matches the folder name.
2. Verify the section layout matches the COMPLEX template.
3. Verify the skill includes the plan-first rule and the stop-and-ask rule.
4. Verify references are informational and the workflow remains self-contained without opening them.
5. Run:

   ```bash
   python save-as-skill/scripts/validate_skill.py update-spec-context/SKILL.md --tier complex
   ```
