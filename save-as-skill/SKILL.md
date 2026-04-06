---
name: save-as-skill
description: 'Use when: a long conversation solved a hard problem, a debugging session produced a reusable workflow, a multi-step implementation finally converged, or the user says "save as skill", "capture this as a skill", or "turn this into a skill". Helps with: extracting a reusable SKILL.md, preserving the reasoning and artifacts from the conversation, and drafting optional review prompts. Applies to: the current conversation, generated skill packages, and skill handoff for Copilot, Continue, Cline, and Claude Code.'
---

# Save As Skill

## Who
Agents or maintainers who want to preserve a solved conversation as a reusable skill that can be invoked again later.

## What
Turn the current conversation into a self-contained skill package. The main deliverable is a reusable `SKILL.md`. When the conversation produced reusable artifacts, also recommend `scripts/`, `references/`, and `assets/` alongside the skill file.

## When
- The user says "save as skill", "capture this as a skill", or "turn this into a skill".
- A long or non-obvious conversation ended with a working solution.
- The conversation uncovered a reusable debugging path, migration, checklist, or helper script.
- The solution required pivots, failed attempts, or reasoning that would be expensive to rediscover.
- Do not use this for one-liners, trivial lookups, or permanent team conventions that belong in instructions or project docs.

## Where
- Source material comes from the current conversation and any files, commands, logs, or scripts produced during it.
- Generated content belongs in a skill directory that contains `SKILL.md` and any bundled resources.
- Common save targets include `.github/skills/<name>/SKILL.md`, `.continue/prompts/<name>.prompt`, `.cline/skills/<name>/SKILL.md`, and `.claude/skills/<name>/SKILL.md`.

## Why
- Good conversations are expensive. Without a skill, the reasoning disappears when the chat ends.
- The value is not only the final answer. The useful part is often the trigger conditions, the pivots, the failed attempts, and the artifacts that made the solution work.
- A self-contained skill makes future agent behavior faster, more consistent, and easier to review.
- Anchoring the skill to what really happened avoids over-generalized advice that sounds good but does not hold up in practice.

## Inputs
- The full current conversation.
- Commands, code snippets, configs, logs, or scripts produced during the conversation.
- Optional target platform, save location, or preferred template tier.

## Output
- A reusable `SKILL.md` written in the SIMPLE, COMPLICATED, or COMPLEX template tier that best fits the conversation.
- A suggested skill directory structure when bundled resources are needed.
- Two or three realistic evaluation prompts when review is desired.
- A recommendation to use instructions or project docs instead when the conversation is not skill-worthy.

## Constraints
- Preserve the original intent of the conversation. Do not invent steps that did not happen.
- Use real artifacts from the conversation whenever possible.
- Explain why steps matter instead of turning the skill into a rigid checklist.
- Keep the skill self-contained and concise. Move overflow into `references/` when needed.
- Do not claim files, tooling, or setup exist unless you verified them in the target environment.
- If the conversation is too simple, say so and stop instead of forcing a skill.

## One More Thing
If anything is unclear, missing, or conflicting, stop and ask the user before proceeding.

## How

### Phase 1: Assess Skill-Worthiness
1. Review the whole conversation for complexity, reusability, and completeness.
2. Check whether the solution required multiple steps, non-obvious reasoning, or domain knowledge.
3. Check whether the problem was actually solved.
4. If the conversation is too simple, respond with:

   > This conversation is too simple to be a skill. Consider saving it as:
   > - A rule (`.github/copilot-instructions.md` or `.instructions.md`) if it is a coding preference or convention
   > - A workflow note in project docs if it is a one-off procedure

5. Stop after that response.

### Phase 2: Capture the Source Material
1. Mine the conversation for tools and commands used.
2. Capture the order of steps, including corrections, pivots, and failed attempts that taught something useful.
3. Capture input/output formats, key prompts, and helper scripts or templates that future users would need.
4. Summarize what you extracted and ask the user to confirm gaps before generating the skill.

### Phase 3: Choose the Template Tier
- Choose SIMPLE for a short, straight-line workflow with one main output and no bundled resources.
- Choose COMPLICATED for a multi-step workflow with clear inputs, outputs, and constraints.
- Choose COMPLEX for branching workflows, review loops, bundled scripts, or multi-platform save guidance.
- Use the lightest tier that still captures the real workflow clearly.

### Phase 4: Build the Skill Descriptor
Create the following fields from the conversation:

- `name`: a lowercase, hyphenated identifier derived from the core action.
- `description`: what it does, when to use it, and where it applies. Include trigger phrases so the skill does not undertrigger.
- `who`: who the skill is for.
- `what`: the task the skill accomplishes.
- `when`: obvious triggers and near-miss scenarios.
- `where`: files, systems, or contexts it applies to.
- `why`: why this workflow is valuable.
- `how`: ordered steps or phases with reasoning.
- `inputs`, `output`, and `constraints`: only include what the conversation actually supports.

### Phase 5: Generate the Skill Package
1. Write `SKILL.md` using the chosen template tier.
2. Keep the sections explicit so the next agent can scan the skill quickly.
3. Use imperative instructions, but explain why each step matters.
4. Add real commands, code, configs, or file patterns from the conversation instead of abstract placeholders whenever possible.
5. If the conversation produced reusable helpers, recommend a structure like:

   ```text
   <skill-name>/
     SKILL.md
     scripts/
     references/
     assets/
   ```

6. Keep `SKILL.md` under about 500 lines. Move long reference material into `references/` and point to it from the skill.

### Phase 5A: Check Template Compliance
Before returning the generated skill, compare it against the chosen template tier.

- Frontmatter: `name` is present, `description` is present, and the description is quoted when it contains colons.
- SIMPLE requires these level-2 sections in order: `Who`, `What`, `When`, `Where`, `Why`, `How`, `One More Thing`.
- COMPLICATED requires these level-2 sections in order: `Who`, `What`, `When`, `Where`, `Why`, `Inputs`, `Output`, `Constraints`, `One More Thing`, `How`.
- COMPLEX requires these level-2 sections in order: `Who`, `What`, `When`, `Where`, `Why`, `Inputs`, `Output`, `Constraints`, `One More Thing`, `How`, `Resources`, `Validation`.
- `One More Thing` must explicitly tell the next agent to stop and ask when something is unclear, missing, or conflicting.
- If `scripts/validate_skill.py` exists in the current package, run:

   ```bash
   python <skill-root>/scripts/validate_skill.py <generated-skill-path> --tier <simple|complicated|complex>
   ```

- Fix validation failures before returning the generated skill.

### Phase 6: Test the Skill
1. Draft 2 or 3 realistic prompts that should trigger the new skill.
2. If the user wants a review loop, save them in `<skill-name>-workspace/evals.json`.
3. For each test prompt, create a directory that contains `eval_metadata.json` and an `outputs/` folder with the generated result.
4. If the bundled review tool exists in the current skill package, launch it with:

   ```bash
   python <skill-root>/scripts/generate_review.py <skill-name>-workspace/ --skill-name "my-skill"
   ```

5. For environments without a browser, write a static review file with:

   ```bash
   python <skill-root>/scripts/generate_review.py <skill-name>-workspace/ --skill-name "my-skill" --static /tmp/review.html
   ```

6. If static mode downloads feedback locally instead of writing it back to the workspace, copy that file into `<skill-name>-workspace/feedback.json` before the next iteration.

### Phase 7: Iterate and Save
1. Read `feedback.json` after review when it exists. Empty feedback usually means the output was acceptable.
2. Improve the skill only where the review exposed real gaps.
3. Save the finished skill to the user's target platform.
4. Tell the user where the file belongs and what, if anything, still needs manual follow-up.

## Resources
- `scripts/generate_review.py` to review generated outputs.
- `scripts/validate_skill.py` to check generated skills against the SIMPLE, COMPLICATED, or COMPLEX template tiers.
- `references/` for long docs, checklists, or background material.
- `assets/` for templates, configs, or boilerplate files.

## Validation
1. Verify the frontmatter is valid and `name` matches the skill folder.
2. Run the manual template checklist, and run `scripts/validate_skill.py` when it is available.
3. Verify the section layout matches the chosen template tier.
4. Verify the examples, commands, and file paths come from the conversation or the current workspace.
5. Verify the skill includes the stop-and-ask rule before returning it to the user.
