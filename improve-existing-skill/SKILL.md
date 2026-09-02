---
name: improve-existing-skill
description: >
   WHEN/WHERE/WHO: [Scheduling: Use when an existing skill was applied, did not fully solve the problem, and the user says "improve this skill", "update the skill", "the skill needs fixing", "make this skill better", or "this skill didn't work". Do not use for brand-new skills or formatting-only edits.]
   HOW: [Structural: Use this COMPLEX SKILL to identify evidence-backed gaps, classify the update scope, preserve the original skill's identity, apply improvements, record rejected revisions, migrate legacy formats to the Hybrid 5W1H + SSL standard, and validate the final skill through an independent acceptance gate.]
   WHY: [Scheduling: Skills degrade over time. Folding proven fixes back into the original skill keeps it accurate, reusable, and easier for the agent to trigger reliably in future conversations.]
---

# Improve Existing Skill

## Common Contract (Load First)

When this skill is activated, first load [skill-common](../skill-common/SKILL.md) and apply the shared conventions it defines: canonical section order, frontmatter rules, anti-pattern guidance, and the Review In Mind loop in [review-in-mind](../skill-common/details/review-in-mind.md). This skill adds only domain-specific rules below.

## Who
Agents or maintainers who applied an existing skill, found it insufficient, iterated in conversation to reach the actual goal, and now want to fold those improvements back into the original skill.

## What
Update an existing `SKILL.md` so it reflects what actually worked. The deliverable is a revised `SKILL.md` that incorporates the missing steps, corrected reasoning, new constraints, or additional artifacts discovered during the conversation. The original skill's identity and purpose are preserved; only the gaps are filled.

## When
- The user says "improve this skill", "update the skill", "the skill needs fixing", "make this skill better", or "this skill didn't work".
- A conversation applied an existing skill but required extra steps, corrections, or workarounds to reach a working solution.
- The user explicitly points out that a skill is outdated, incomplete, or wrong.
- The conversation produced new artifacts, constraints, or edge cases that the original skill did not cover.
- Do **not** use this skill when the conversation solved a brand-new problem with no prior skill. Use `save-as-skill` instead.
- Do **not** use this skill for cosmetic or formatting-only edits. Edit the file directly instead.
- Do **not** use this skill when the goal is multi-iteration evolution across many rollout runs (or a persistent knowledge wiki is required). Use `evolve-skill-with-wiki` instead; this skill is the single-iteration fallback of that workflow.

## Where
- The source skill lives in a skill directory such as `.github/skills/<name>/SKILL.md`, `.cline/skills/<name>/SKILL.md`, `.continue/prompts/<name>.prompt`, or `.claude/skills/<name>/SKILL.md`.
- The improvement material comes from the current conversation.
- The updated skill is written back to the same location as the original.

## Why
- Skills degrade over time. Tools change, environments shift, and edge cases appear that the original conversation never encountered.
- Iterating in conversation and then discarding the improvements wastes effort. Folding fixes back into the skill keeps it accurate.
- An improved skill makes future invocations faster and more reliable because the agent does not have to rediscover the same workarounds.
- Preserving the original skill's identity avoids duplicating skills that solve the same problem.

## Inputs
- The existing `SKILL.md` that was applied (required).
- The current conversation containing the iteration that went beyond the original skill (required).
- Any new artifacts, commands, configs, or scripts produced during the conversation (optional).

## Output (Logical Evidence)
- A revised `SKILL.md` that incorporates the improvements while preserving the original skill's identity, migrated to the Hybrid 5W1H + SSL format if it wasn't already.
- Explicitly declared state changes (diff summary).
- Updated bundled resources (`scripts/`, `references/`, `assets/`).
- A short validation record listing the confirmed gaps, the chosen update scope, and any rejected edits that should not be repeated blindly.

## Optimization Readiness
- **Failure Signals**: The original skill was triggered but required undocumented extra steps, used wrong assumptions, missed important boundaries, or failed to produce a working result without conversational rescue.
- **Evidence To Collect**: The original skill text, concrete steps from the current conversation, commands or files that actually worked, user corrections, and failed attempts that exposed weak instructions.
- **Safe Mutation Boundaries**: Revise frontmatter triggers, workflow steps, constraints, validation, and supporting resources while preserving the skill's original purpose and name.
- **Acceptance Criteria**: Accept the updated skill only if every meaningful change traces back to conversation evidence, the tier still matches the workflow depth, the routing language is clearer, and the validation steps are more actionable than before.
- **Rejected Revision Handling**: Record discarded trigger phrases, structural rewrites, or speculative improvements that were considered but not supported by evidence.
- **Transfer Check**: Confirm that the updated skill would also help on at least one nearby recurrence of the same problem class, not only the exact conversation instance.
- **Stop Rule**: If the conversation did not actually improve the original skill, or two revision attempts fail the same acceptance check, stop and report that no justified update is available.

## Constraints (Logical Boundaries)
- **RULE 1: Template Migration.** If the existing skill is not using the Hybrid 5W1H + SSL format (e.g., missing multi-line YAML, missing `(Structural Workflow)` headers), you MUST migrate it to the new standard during the update.
- **RULE 2: Token Efficiency.** Ensure the updated `SKILL.md` remains under 500 lines. Push verbose checklists or examples into a `details/` directory.
- Preserve the original skill's `name` and overall purpose.
- Do not remove steps, constraints, or artifacts from the original skill unless they are proven wrong by the conversation.
- Maintain template compliance against the target tier (SIMPLE, COMPLICATED, or COMPLEX).
- Add new material only where the conversation provides evidence. Do not invent improvements that did not happen.
- Keep the updated skill self-contained. If overflow grows too large, move it into `references/`.
- Maintain template compliance. The updated skill must still pass validation against its template tier (SIMPLE, COMPLICATED, or COMPLEX).
- If the conversation did not actually improve the skill, say so and stop instead of forcing a change.
- Make the routing language explicit enough that the frontmatter alone can signal when this skill should activate.

## One More Thing
If anything is unclear, missing, or conflicting, stop and ask the user before proceeding.

## How (Structural Workflow)

### Phase 1: Identify the Original Skill
1. Determine which skill was applied in the conversation. Look for explicit references, slash commands, or file paths.
2. Read the original `SKILL.md` completely. Note its template tier, sections, and any bundled resources.
3. If the skill cannot be found or the user is unsure which skill was applied, ask the user to confirm before continuing.

### Phase 2: Capture the Gap
1. Compare what the original skill prescribed with what actually happened in the conversation.
2. Identify the deltas:
   - **Missing steps**: actions the user or agent had to take that the skill did not mention.
   - **Wrong assumptions**: constraints, tool versions, or environment details that turned out to be incorrect.
   - **New artifacts**: scripts, configs, commands, or patterns that emerged during iteration.
   - **Edge cases**: failure modes or boundary conditions the original skill did not anticipate.
   - **Outdated references**: links, tool names, or API surfaces that have changed.
3. Summarize the gaps and present them to the user for confirmation:

   > "I found these gaps between the original skill and what this conversation needed:
   > 1. [gap description]
   > 2. [gap description]
   > ...
   > Shall I fold these into the skill?"

### Phase 3: Classify the Change
1. Decide the scope of the update:
   - **Patch**: fix a wrong detail, add a missing constraint, or correct a command. The structure stays the same.
   - **Extend**: add new steps, phases, inputs, or outputs. The structure grows but the purpose stays the same.
   - **Restructure**: the template tier needs to change (e.g., SIMPLE → COMPLICATED) because the workflow is now more complex.
2. If the change is a **Restructure**, confirm with the user before proceeding because it changes the skill's shape significantly.
3. Record any rejected scope options so future edits do not reopen unsupported rewrites.

### Phase 4: Template Migration (SSL Upgrade)
1. Check if the original skill uses the modern **Hybrid 5W1H + SSL** format. 
2. If it does NOT, rewrite the frontmatter to the multi-line `description: >` format (`WHEN/WHERE/WHO:`, `HOW:`, `WHY:`).
3. Add the explicit layer mappings to the headers (e.g., `## How (Structural Workflow)`, `## Constraints (Logical Boundaries)`).
4. Extract any overly long code blocks or checklists (>500 lines) into a `details/` directory.

### Phase 5: Apply the Improvements
1. Edit the `SKILL.md` in place, preserving its existing structure as much as possible.
2. For each gap identified in Phase 2:
   - Add missing steps to the `How` section in the correct position.
   - Update `Inputs`, `Output`, or `Constraints` when new requirements emerged.
   - Update `When` if new trigger phrases or near-miss boundaries were discovered.
   - Add new artifacts to `scripts/`, `references/`, or `assets/` when the conversation produced them.
3. Use real commands, code, and file paths from the conversation instead of abstract placeholders.
4. If the skill is missing `## Optimization Readiness`, add it and fill it with evidence-backed failure signals, acceptance criteria, and stop rules derived from the conversation.

### Phase 6: Validate the Updated Skill
1. Verify the updated skill still matches its template tier. Use the section-order rules:
   - SIMPLE: `Who`, `What`, `When`, `Where`, `Why`, `How`, `One More Thing`.
   - COMPLICATED: `Who`, `What`, `When`, `Where`, `Why`, `Inputs`, `Output`, `Constraints`, `One More Thing`, `How`.
   - COMPLEX: `Who`, `What`, `When`, `Where`, `Why`, `Inputs`, `Output`, `Optimization Readiness`, `Constraints`, `One More Thing`, `How`, `Resources`, `Validation`.
2. If `scripts/validate_skill.py` is available, run:

   ```bash
   python <skill-root>/scripts/validate_skill.py <updated-skill-path> --tier <tier>
   ```

3. Verify that the updated frontmatter description now carries the strongest trigger phrases and near-miss boundaries, rather than hiding them only in `## When`.
4. Fix any validation failures before returning the result.

### Phase 7: Present the Diff and Save
1. Show a concise diff summary to the user, listing what was added, changed, or removed and why.
2. Ask the user to confirm the update.
3. Save the updated `SKILL.md` and any new bundled resources to the original skill location.
4. If the skill is deployed to multiple platforms (Copilot, Cline, Continue, Claude Code), remind the user to sync copies.

## Resources
- `evolve-skill-with-wiki/SKILL.md` — the companion meta-skill for multi-iteration, wiki-backed skill evolution across many rollouts. Use this skill when you need more than one evidence cycle.
- `save-as-skill/SKILL.md` — the companion skill for creating new skills from scratch.
- `save-as-skill/scripts/validate_skill.py` — validator for checking `SKILL.md` files against template tiers.
- `../CREATING-SKILL-TEMPLATE/details/SKILL-TEMPLATE.md` — the master template reference for SIMPLE, COMPLICATED, and COMPLEX tiers.

## Review In Mind (ReviewInMindGenie)

Execute the common review loop in [review-in-mind](../skill-common/details/review-in-mind.md) before delivering.

Review lens for this skill:
- Are changes limited to gaps discovered in real use, preserving the original skill's identity and purpose?
- Does the revision update the Optimization Readiness evidence and validation gates?
- Would the improved skill pass its own Validation and Review In Mind sections?

## Validation
1. Verify the updated `SKILL.md` has valid frontmatter with `name` and `description`.
2. Verify the section layout matches the skill's template tier.
3. Verify every change traces back to something that actually happened in the conversation.
4. Verify the skill still contains the stop-and-ask rule in `One More Thing`.
5. Verify that the strongest trigger phrases and near-miss boundaries are present in the frontmatter description, not only in `## When`.
6. Run `scripts/validate_skill.py` when available and fix any reported issues.
