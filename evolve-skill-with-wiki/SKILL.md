---
name: evolve-skill-with-wiki
description: >
  WHEN/WHERE/WHO: [Scheduling: Agents or maintainers who need to evolve an agent skill across many execution runs — user says "evolve this skill", "set up skill evolution", "apply WikiSkill", "improve this skill from past runs", or wants a skill that compounds lessons over time. Do not use for a single-conversation fix (use improve-existing-skill) or for brand-new skills (use save-as-skill).]
  HOW: [Structural: Use this COMPLEX SKILL to run the WikiSkill loop — three-layer workspace (raw/wiki/skills), an Inference Agent doing rollouts without wiki access, a Wiki Maintainer consolidating patterns, a Skill Proposer reading the wiki to propose one atomic patch per iteration, and validation gating that rolls back skills but never the wiki.]
  WHY: [Scheduling: One-shot skill patches waste most of the learning signal — the WikiSkill paper (arXiv:2608.27454) shows persistent, compounding wiki knowledge adds ~15 points over iteration-local methods and prevents re-proposing rejected ideas.]
---

# Evolve Skill with Wiki

## Common Contract (Load First)

When this skill is activated, first load [skill-common](../skill-common/SKILL.md) and apply the shared conventions it defines: canonical section order, frontmatter rules, anti-pattern guidance, and the Review In Mind loop in [review-in-mind](../skill-common/details/review-in-mind.md). This skill adds only domain-specific rules below.

## Who
Agents or maintainers who run an agent on a task repeatedly and want the procedural skill (the `SKILL.md` the agent follows) to get better across those runs instead of staying static.

## What
Run an evolutionary loop that co-evolves one or more skills with a persistent knowledge wiki. Each iteration: roll out the agent on training tasks using the current skills, consolidate sampled traces into the wiki, propose one atomic skill update informed by the wiki, and accept or reject the update by measuring validation performance. The wiki is never rolled back, so later iterations build on accumulated knowledge, rejected proposals are not repeated, and recurring failure patterns get progressively documented.

## When
- User says: "evolve this skill", "set up skill evolution", "apply WikiSkill", "make this skill learn from past runs", "improve this skill using execution history", or "run skill evolution".
- The agent has (or can cheaply produce) a batch of execution traces on similar tasks, plus a way to score outcomes (correct/incorrect, pass/fail, or a rubric score).
- The user wants a skill that compounds knowledge over multiple rollout iterations rather than a one-off patch.
- **Near-miss boundaries**: single-conversation fixes belong to `improve-existing-skill`; extracting a brand-new skill from one conversation belongs to `save-as-skill`; user-facing agent memory (not skill-evolution knowledge) belongs to `build-agent-memory-systems`; skill *execution state* for long-horizon runs belongs to the SKILL.state line of work, not this skill.

## Where
- A workspace directory such as `evolution-runs/<task-domain>/` with three layers: `raw/` (immutable traces), `wiki/` (compounding knowledge), and `skills/` (active skills).
- The wiki layer uses files: `wiki/patterns/<pattern-name>.md`, `wiki/patterns/index.md`, `wiki/logs.md`, and `wiki/skill-impact.md`.
- Each evolved skill directory holds `SKILL.md` (procedural content) and `PURPOSE.md` (which wiki patterns motivated the skill or its latest edit).

## Why
Single-shot improvement passes discard most of the learning signal. The WikiSkill paper (arXiv:2608.27454) shows that giving the skill proposer access to a persistent, compounding wiki improves average benchmark performance by ~15 points over proposers that only see current traces, and that without a persistent history agents re-propose interventions that already failed. Skills also keep improving late into an evolution run (39–58% of accepted updates happen after the first two iterations), so the value is in the loop, not the first patch.

## Inputs
- **Task set with scores** (required): training tasks to roll out on, validation tasks used for gating, and (optionally) held-out test tasks for final reporting. Each task needs a scoring function.
- **Agent harness** (required): the agent (with its tools) that executes tasks and can be run with or without an injected skill set.
- **Initial skills** (optional): an empty set is fine; the loop discovers skills from scratch.
- **Iteration budget** (recommended): e.g., 5–8 iterations, or early-stop at validation score 1.0.

## Output (Logical Evidence)
- An evolved skill set under `skills/`, each skill containing `SKILL.md` and `PURPOSE.md`.
- A persistent `wiki/` with pattern pages, an index, an evolution log, and a skill-impact tracker recording every proposal's diff, validation score, and accept/reject outcome.
- A validation record: baseline score, per-iteration validation scores, acceptance decisions, and final test performance when a test split exists.
- Declared state changes: skills are the only reversible layer; wiki content and raw traces are retained.

## Optimization Readiness
- **Failure Signals**: repeated validation failures on the same error class, the proposer re-proposing a rejected idea, skills that keep growing without validation gains, or rollouts that get worse when the wiki is exposed to the executing agent.
- **Evidence To Collect**: raw traces per iteration, wiki pattern pages and edit history, skill-impact entries (proposal diff + validation score + outcome), and the evolution log.
- **Safe Mutation Boundaries**: you may refine prompt instructions for the Maintainer and Proposer, sampling budgets, gating thresholds, and wiki file conventions. Invariants that must stay fixed: skills roll back on degradation while the wiki never resets; the inference agent must not read the wiki during rollouts; each proposal is one atomic skill change.
- **Acceptance Criteria**: accept a revision of this skill only if a validation score improves over the previous best while the wiki audit trail stays complete (every proposal recorded with diff, score, and outcome).
- **Rejected Revision Handling**: record every rejected proposal in `wiki/skill-impact.md` and the relevant failure pattern in `wiki/patterns/` so later iterations avoid it.
- **Transfer Check**: confirm the loop works for at least two different task domains (e.g., one reasoning domain and one tool-use domain) without changing the architecture.
- **Stop Rule**: stop when the validation score reaches 1.0, the iteration budget is exhausted, or two consecutive iterations produce no accepted proposal. Then deliver the best skill set and the full wiki rather than continuing unbounded evolution.

## Constraints (Logical Boundaries)
- **RULE 1: Skills roll back, wiki persists.** If a candidate skill set does not beat the best validation score, revert `skills/` to the last accepted state; never delete or revert `wiki/` or `raw/`.
- **RULE 2: No wiki during rollouts.** The inference agent executes tasks with skills injected only. Wiki access during rollouts measurably degrades the final skill quality (the paper's ablation: 63.7 → 60.9 average), because the agent solves tasks from the wiki instead of exercising the skills.
- **RULE 3: One atomic proposal per iteration.** Each iteration creates one new skill or applies one incremental, patch-based edit to one skill. No mega-updates spanning several skills.
- **RULE 4: Strict acceptance gate.** Accept only when the validation score strictly improves over the best-so-far baseline. Do not accept "neutral" proposals (the paper notes this is a deliberate limitation; changing it requires user approval).
- **Context budgets**: keep each wiki pattern page and skill edit concise; sample at most ~8 traces per iteration (about 5 failing + 3 passing) and cap each trace excerpt (~15k chars) to avoid context exhaustion.
- **Anti-Pattern Mapping**: MUST NOT expose the wiki to the inference agent; MUST NOT reset the wiki on rejection; MUST NOT accept a proposal without a validation rollout; MUST NOT let the proposer rewrite multiple skills in one iteration; MUST NOT prune the wiki automatically without a user decision (the paper flags pruning as open work).

## One More Thing
This section is a pre-flight checkpoint placed **before** `## How` on purpose: it is the last place an agent can stop and ask before taking any real action. If the task set, scoring function, validation split, or iteration budget is missing or unclear, stop and ask the user before running the evolution loop; do not start Phase 0 with unresolved assumptions.

## How (Structural Workflow)

### Phase 0: Set Up the Workspace and Baseline
1. Create the three-layer workspace:
   ```text
   evolution-runs/<task-domain>/
     raw/                          # immutable execution traces, one file per task per iteration
     wiki/
       patterns/                   # one .md per failure mode or successful strategy
       patterns/index.md           # catalog of all patterns
       logs.md                     # chronological evolution history
       skill-impact.md             # proposal diff + validation score + accept/reject, per iteration
     skills/                       # active skill set (may start empty)
   ```
2. Initialize `wiki/patterns/index.md`, `wiki/logs.md`, and `wiki/skill-impact.md` with empty headers.
3. Roll out the agent with the empty skill set on the validation split to establish the baseline score `R_best`. If the baseline is already 1.0, stop — no skill evolution is needed.
4. Record the baseline in `wiki/logs.md`.

### Phase 1: Inference Agent — Rollouts
1. For each training task, run the agent with the full content of the current active skills injected into its system prompt. Do NOT give it wiki access.
2. Save each complete trajectory (reasoning, tool calls, tool outputs, final answer, and score) as an immutable file under `raw/iter-<k>/`.
3. If a task fails to run because of harness or environment issues, record the failure and continue; do not silently drop the task.

### Phase 2: Wiki Maintainer — Pattern Consolidation
1. Sample up to ~8 traces: aim for about 5 failing traces (for root-cause analysis) and up to 3 passing traces (to capture successful strategies and guard against regressions). Cap each excerpt to roughly 15,000 characters.
2. For each failing trace, identify the root cause and write or update a pattern page under `wiki/patterns/`:
   - Document the failure mode, evidence (iteration + trace ids), and actionable workaround.
   - If the pattern already exists, append fresh evidence or refine the workaround; do not delete prior evidence.
3. For passing traces, extract the successful strategy and note it in the relevant pattern page or a strategy page.
4. Update `wiki/patterns/index.md` to reflect created/edited pages.
5. Append a summary of this iteration's findings to `wiki/logs.md` (patterns created, patterns updated, errors that recurred).

### Phase 3: Skill Proposer — One Atomic Proposal
1. Give the proposer the wiki index, `wiki/skill-impact.md`, and a concise summary of training outcomes (task id, pass/fail, prediction, ground truth).
2. Let the proposer read specific pattern pages and raw traces on demand (ReAct style) before writing the proposal.
3. Require exactly one atomic proposal: create one new skill (with `SKILL.md` and a `PURPOSE.md` citing the motivating patterns) or apply one patch-based edit to one existing skill.
4. If the skill-impact log shows the same idea was already rejected, the proposer must propose something different or skip the iteration.

### Phase 4: Gating and Rollback
1. Apply the proposal to produce candidate skill set `S'`.
2. Roll out the candidate on the validation split and compute its score.
3. If the score strictly exceeds `R_best`: accept the candidate as the active skill set and update `R_best`. If it reaches 1.0, stop after recording.
4. Otherwise: revert `skills/` to the last accepted set. Do not touch `wiki/` or `raw/`.
5. Programmatically append an entry to `wiki/skill-impact.md` with: iteration, proposal description, target skill, unified diff, validation score, and `Accepted`/`Rejected`.
6. If the iteration budget remains and at least one proposal was accepted recently, continue to the next iteration; otherwise deliver.

### Phase 5: Report and Finalize
1. Present the final skill set, the per-iteration acceptance history, and (when a test split exists) the final test score.
2. Point out which wiki patterns drove the accepted skills, citing `PURPOSE.md` and `wiki/logs.md`.
3. If the evolution produced no accepted skill, report that outcome and keep the wiki as the artifact.

## Resources
- [wikiskill-paper-digest](references/wikiskill-paper-digest.md) — condensed method details from the source paper (arXiv:2608.27454), including its key numbers and ablations.
- [improve-existing-skill](../improve-existing-skill/SKILL.md) — single-iteration fallback; use it when only one evidence cycle is available.
- [save-as-skill](../save-as-skill/SKILL.md) and [validate_skill.py](../save-as-skill/scripts/validate_skill.py) — validation for any `SKILL.md` the loop produces or edits.

## Review In Mind (ReviewInMindGenie)

Execute the common review loop in [review-in-mind](../skill-common/details/review-in-mind.md) before delivering.

Review lens for this skill:
- Is the workspace split into immutable `raw/`, persistent `wiki/`, and reversible `skills/`, with skills never rolling the wiki back?
- Does the loop keep the inference agent wiki-free, propose exactly one atomic change per iteration, and gate acceptance on a strict validation improvement?
- Is every proposal recorded in `skill-impact.md` with its diff, score, and outcome so rejected ideas are not re-proposed?

## Validation (Verifiable Rewards)
1. Verify the workspace contains the three layers and that no accepted proposal was ever rolled back by deleting wiki content.
2. Verify `wiki/skill-impact.md` has one entry per iteration, each with a diff, validation score, and accept/reject outcome.
3. Verify each evolved skill directory contains `SKILL.md` and `PURPOSE.md` linking to at least one wiki pattern.
4. Verify each accepted skill passes [validate_skill.py](../save-as-skill/scripts/validate_skill.py) against its tier.
5. Report baseline, per-iteration validation scores, final skill set, and any remaining gaps (e.g., no test split, neutral proposals excluded).
