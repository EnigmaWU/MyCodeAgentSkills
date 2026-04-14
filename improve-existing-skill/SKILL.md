---
name: improve-existing-skill
description: 'Use when: an existing skill was applied but did not fully solve the problem, the user iterated further in conversation to reach a working solution, and the user says "improve this skill", "update the skill", "the skill needs fixing", or "make this skill better". Helps with: updating an existing SKILL.md with lessons learned from a conversation that went beyond what the original skill covered. Applies to: existing skill packages in .github/skills/, .cline/skills/, .continue/prompts/, or .claude/skills/.'
---

# Improve Existing Skill

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
- The user's description of what was insufficient or wrong (recommended).
- Any new artifacts, commands, configs, or scripts produced during the conversation (optional).

## Output
- A revised `SKILL.md` that incorporates the improvements while preserving the original skill's identity.
- A diff summary showing what changed and why.
- Updated bundled resources (`scripts/`, `references/`, `assets/`) when the conversation produced new artifacts.
- A recommendation to leave the skill unchanged when the conversation did not actually improve it.

## Constraints
- Preserve the original skill's `name`, overall purpose, and template tier unless the user explicitly asks to change them.
- Do not remove steps, constraints, or artifacts from the original skill unless they are proven wrong by the conversation.
- Add new material only where the conversation provides evidence. Do not invent improvements that did not happen.
- Keep the updated skill self-contained. If overflow grows too large, move it into `references/`.
- Maintain template compliance. The updated skill must still pass validation against its template tier (SIMPLE, COMPLICATED, or COMPLEX).
- If the conversation did not actually improve the skill, say so and stop instead of forcing a change.

## One More Thing
If anything is unclear, missing, or conflicting, stop and ask the user before proceeding.

## How

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

### Phase 4: Apply the Improvements
1. Edit the `SKILL.md` in place, preserving its existing structure as much as possible.
2. For each gap identified in Phase 2:
   - Add missing steps to the `How` section in the correct position.
   - Update `Inputs`, `Output`, or `Constraints` when new requirements emerged.
   - Update `When` if new trigger phrases or boundaries were discovered.
   - Add new artifacts to `scripts/`, `references/`, or `assets/` when the conversation produced them.
3. Use real commands, code, and file paths from the conversation instead of abstract placeholders.
4. Explain why each addition matters so the skill teaches reasoning, not just procedure.

### Phase 5: Validate the Updated Skill
1. Verify the updated skill still matches its template tier. Use the section-order rules:
   - SIMPLE: `Who`, `What`, `When`, `Where`, `Why`, `How`, `One More Thing`.
   - COMPLICATED: `Who`, `What`, `When`, `Where`, `Why`, `Inputs`, `Output`, `Constraints`, `One More Thing`, `How`.
   - COMPLEX: `Who`, `What`, `When`, `Where`, `Why`, `Inputs`, `Output`, `Constraints`, `One More Thing`, `How`, `Resources`, `Validation`.
2. If `scripts/validate_skill.py` is available, run:

   ```bash
   python <skill-root>/scripts/validate_skill.py <updated-skill-path> --tier <tier>
   ```

3. Fix any validation failures before returning the result.

### Phase 6: Present the Diff and Save
1. Show a concise diff summary to the user, listing what was added, changed, or removed and why.
2. Ask the user to confirm the update.
3. Save the updated `SKILL.md` and any new bundled resources to the original skill location.
4. If the skill is deployed to multiple platforms (Copilot, Cline, Continue, Claude Code), remind the user to sync copies.

## Resources
- `save-as-skill/SKILL.md` — the companion skill for creating new skills from scratch.
- `save-as-skill/scripts/validate_skill.py` — validator for checking `SKILL.md` files against template tiers.
- `SKILL-TEMPLATE.md` — the master template reference for SIMPLE, COMPLICATED, and COMPLEX tiers.

## Validation
1. Verify the updated `SKILL.md` has valid frontmatter with `name` and `description`.
2. Verify the section layout matches the skill's template tier.
3. Verify every change traces back to something that actually happened in the conversation.
4. Verify the skill still contains the stop-and-ask rule in `One More Thing`.
5. Run `scripts/validate_skill.py` when available and fix any reported issues.
