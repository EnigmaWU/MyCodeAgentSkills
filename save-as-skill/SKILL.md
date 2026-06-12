---
name: save-as-skill
description: >
  WHEN/WHERE/WHO: [Scheduling: Agents or users wanting to preserve a completed, complex conversation or debugging session into a reusable skill.]
  HOW: [Structural: Use this SKILL to extract the workflow, format it into the Hybrid 5W1H + SSL structure, and evaluate it via Ctx2Skill Self-Play.]
  WHY: [Scheduling: Good conversations are expensive. Saving them explicitly to the machine-readable SSL standard ensures future agents can perfectly index and reuse the reasoning without degradation.]
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

## Output (Logical Evidence)
- A reusable `SKILL.md` written in the Hybrid 5W1H + SSL framework (SIMPLE, COMPLICATED, or COMPLEX tier).
- A suggested skill directory structure when bundled resources are needed.
- Explicitly declared state changes or side effects (if any).
- A Ctx2Skill self-play evaluation report: scored probe tasks, failure diagnosis, and version history.
- A recommendation to use instructions or project docs instead when the conversation is not skill-worthy.

## Constraints (Logical Boundaries)
- **RULE 1: Token Efficiency.** Ensure the generated `SKILL.md` remains under 500 lines. Move verbose reference material into `details/` or `references/`.
- Preserve the original intent of the conversation. Do not invent steps that did not happen.
- Use real artifacts from the conversation whenever possible.
- Explain why steps matter instead of turning the skill into a rigid checklist.
- Keep the skill self-contained and concise. Move overflow into `references/` when needed.
- Do not claim files, tooling, or setup exist unless you verified them in the target environment.
- If the conversation is too simple, say so and stop instead of forcing a skill.

## One More Thing
If anything is unclear, missing, or conflicting, stop and ask the user before proceeding.

## How (Structural Workflow)

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
4. Classify why each non-obvious step was needed using these failure-pattern categories (from Ctx2Skill):
   - **Content gap** — required information existed but wasn't surfaced at first.
   - **Format/structure error** — the response had the wrong shape or organization.
   - **Constraint violation** — a limit, count, or exact requirement was missed.
   - **Reasoning error** — incorrect logic or calculation required a correction.
   - **Task misunderstanding** — the initial interpretation of the request was wrong.
   - **System prompt non-compliance** — a behavioral rule (persona, tone, forbidden content) was ignored.
5. Summarize what you extracted and ask the user to confirm gaps before generating the skill.

### Phase 3: Choose the Template Tier
- Choose SIMPLE for a short, straight-line workflow with one main output and no bundled resources.
- Choose COMPLICATED for a multi-step workflow with clear inputs, outputs, and constraints.
- Choose COMPLEX for branching workflows, review loops, bundled scripts, or multi-platform save guidance.
- Use the lightest tier that still captures the real workflow clearly.

### Phase 4: Build the SSL Descriptor
Create the following fields from the conversation according to the Hybrid 5W1H + SSL template:

- `name`: a lowercase, hyphenated identifier derived from the core action.
- `description`: use the explicit multi-line format (`WHEN/WHERE/WHO`, `HOW`, `WHY`).
- `who`: who the skill is for.
- `what`: the task the skill accomplishes and concrete side effects.
- `when`: explicit triggers and near-miss boundaries.
- `where`: files, systems, or contexts it applies to.
- `why`: why this workflow is valuable.
- `how`: explicit Structural Workflow phases with review loops.
- `inputs`, `output`, and `constraints`: concrete Logical boundaries and explicitly required tools.

### Phase 5: Generate the Skill Package
1. Write `SKILL.md` using the Hybrid 5W1H + SSL framework.
2. Keep the sections explicit so the next agent can scan the skill quickly.
3. Use imperative instructions, but explain why each step matters.
4. Add real commands, code, configs, or file patterns from the conversation instead of abstract placeholders whenever possible.
5. Apply these Ctx2Skill-inspired quality standards before finalizing the skill:
   - **Actionable, not abstract**: Every instruction must be a concrete step, checklist item, or procedure. Replace vague guidance ("be careful with X") with specific actions ("before committing, run Y and verify Z").
   - **Concise**: Every sentence competes for the model's attention. Challenge each one: "Does this add actionable value?" Remove filler.
   - **Structured for reuse**: Where appropriate, include a pre-answer checklist (what to verify before starting), a response procedure (ordered steps), and self-verification steps (what to check after drafting).
   - **Generalizable**: Write the skill so it applies to similar future problems, not only the exact conversation that produced it. Avoid embedding one-off details that won't transfer.
   - **Complementary**: Before creating a new skill, check whether an existing skill already covers similar ground. If so, propose edits to that skill rather than creating a duplicate.
6. If the conversation produced reusable helpers, recommend a structure like:

   ```text
   <skill-name>/
     SKILL.md
     scripts/
     references/
     assets/
   ```

7. Keep `SKILL.md` under about 500 lines. Move long reference material into `references/` and point to it from the skill.

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

Also check against these Ctx2Skill anti-patterns and fix any that apply:
- **Vague skills**: Does the skill say things like "be more careful" or "pay attention"? Replace with concrete procedures.
- **Narrow skills**: Is the skill written only for this exact conversation? Broaden it so similar future cases benefit too.
- **Duplicate skills**: Does the skill repeat guidance already present in an existing skill in the workspace? Merge or reference instead of repeating.

### Phase 6: Evaluate the Skill via Ctx2Skill Self-Play

Run the Ctx2Skill five-agent self-play loop to test and refine the generated skill. Each round scores the current skill version; the loop ends when the skill passes all probes or the user accepts the current version.

**Before the first round, initialize:**
- `probe_pool.hard = []` — tasks the Reasoner failed
- `probe_pool.easy = []` — tasks the Reasoner passed
- `skill_history = [v1]` — the skill version generated in Phase 5

#### Step 1 — Challenger: generate probing tasks

Take on the Challenger role. Generate 3–5 tasks a future agent must perform when invoking the new skill:
1. Each task must **require** reading and applying the skill — it should not be answerable from general knowledge alone.
2. Include at least two complexity factors per task: specific facts from the skill, format constraints, exact numerical limits, multi-step reasoning, or compliance with behavioral rules.
3. Write 8–12 binary rubrics per task using these type targets:
   - **Content inclusion** (~25%): "The response should include [specific element from the skill]."
   - **Content exclusion** (~20%): "The response should not include [specific thing]."
   - **Format/structure** (~15%): "The response should [format requirement, e.g., use numbered steps]."
   - **Accuracy** (~15%): "The response should correctly state [specific fact from the skill]."
   - **Constraint compliance** (~10%): "The response should meet [exact constraint, e.g., stay under 500 lines]."
   - **Other** (~15%): sequence/ordering, tone/style, or domain-specific logic.
4. Each task must target a **different** aspect of the skill — no two tasks may test the same section.

#### Step 2 — Reasoner: attempt each task

Take on the Reasoner role. Using **only the generated SKILL.md as your guide** (simulate a fresh agent with no memory of the source conversation), attempt each task and produce a response.

#### Step 3 — Judge: score each rubric

Take on the Judge role. For each (task, response) pair, score every rubric as `1` (pass) or `0` (fail). Classify each task:
- **Solved** (all rubrics pass) → add to `probe_pool.easy`.
- **Failed** (any rubric fails) → add to `probe_pool.hard`.

If all tasks are solved, exit the loop — the skill is ready. Otherwise continue to Step 4.

#### Step 4 — Proposer: diagnose failures

Take on the Proposer role. For each failed task:
1. Classify the failure using the Phase 2 taxonomy (content gap, format/structure error, constraint violation, reasoning error, task misunderstanding, system prompt non-compliance).
2. Check whether an existing skill in the workspace already covers this gap — if yes, propose an **edit** to that skill instead of adding to the new one.
3. Produce a single, concrete, generalizable proposal: what rule or procedure, added to the skill, would prevent this failure class across diverse future tasks?
4. Avoid vague proposals ("be more careful"). Specify exact changes ("add a pre-answer checklist item that confirms X before proceeding").

#### Step 5 — Generator: update the skill

Take on the Generator role. Apply the Proposer's proposals to produce an updated SKILL.md:
1. Add the highest-impact proposal first.
2. Keep the skill concise — remove filler when adding new content.
3. Re-run `scripts/validate_skill.py` on the updated skill to confirm template compliance.
4. Append the new version to `skill_history` (e.g., `v2`).
5. Return to Step 1 for the next round.

**If the user wants the bundled review tool**, save tasks and rubrics in `<skill-name>-workspace/evals.json` and launch:

```bash
python <skill-root>/scripts/generate_review.py <skill-name>-workspace/ --skill-name "my-skill"
```

For headless environments:

```bash
python <skill-root>/scripts/generate_review.py <skill-name>-workspace/ --skill-name "my-skill" --static /tmp/review.html
```

Copy downloaded feedback into `<skill-name>-workspace/feedback.json` before the next round.

### Phase 7: Select the Best Version via Cross-Time Replay and Save

After two or more self-play rounds, use the Ctx2Skill Cross-Time Replay mechanism to select the skill version with the best balanced performance across all accumulated probes.

#### Cross-Time Replay
1. Replay every skill version in `skill_history` against the full `probe_pool` (all hard and easy tasks accumulated across all rounds).
2. For each version, compute:
   - `hard_rate` = fraction of `probe_pool.hard` tasks solved
   - `easy_rate` = fraction of `probe_pool.easy` tasks solved
   - `balanced_score` = `hard_rate × easy_rate`
3. Select the version with the highest `balanced_score`. This prevents selecting a version that solved hard probes by over-specializing and regressing on easy ones.
4. If scores are tied, prefer the later version (more up-to-date guidance).

#### Save
1. Save the selected version to the user's target platform.
2. Tell the user which version was selected, what its balanced score was, and what, if anything, still needs manual follow-up.
3. If the loop ran only one round (no replay history), skip Cross-Time Replay and save the current version directly.

## Resources
- `scripts/generate_review.py` to review generated outputs.
- `scripts/validate_skill.py` to check generated skills against the SIMPLE, COMPLICATED, or COMPLEX template tiers.
- `references/ctx2skill-agent-roles.md` — prompt templates for all five Ctx2Skill agent roles (Challenger, Reasoner, Judge, Proposer, Generator) adapted for skill evaluation.
- `references/` for long docs, checklists, or background material.
- `assets/` for templates, configs, or boilerplate files.
- [Ctx2Skill paper](https://arxiv.org/abs/2604.27660) — the self-evolving, multi-agent skill-discovery framework whose 5-agent self-play loop and Cross-Time Replay mechanism are embedded directly into Phase 6 and Phase 7 of this skill.

## Validation
1. Verify the frontmatter is valid and `name` matches the skill folder.
2. Run the manual template checklist, and run `scripts/validate_skill.py` when it is available.
3. Verify the section layout matches the chosen template tier.
4. Verify the examples, commands, and file paths come from the conversation or the current workspace.
5. Verify the skill includes the stop-and-ask rule before returning it to the user.
