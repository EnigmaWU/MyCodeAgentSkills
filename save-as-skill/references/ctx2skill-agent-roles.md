# Ctx2Skill Agent Roles for Skill Evaluation

This document adapts the five Ctx2Skill agent roles
([paper](https://arxiv.org/abs/2604.27660)) for use in the
`save-as-skill` self-play evaluation loop (Phase 6).

When following `SKILL.md` Phase 6, the agent executing `save-as-skill`
takes on each role in turn — Challenger, Reasoner, Judge, Proposer,
Generator — to iteratively test and improve the generated skill before
saving it.

---

## Challenger

**Purpose:** Generate diverse, context-grounded probing tasks and rubrics
that test whether a future agent can apply the new skill correctly.

**Prompt template (adapt to the skill under evaluation):**

> You are a benchmark design expert specializing in evaluating
> whether a skill document correctly guides an agent.
>
> Given the generated skill (SKILL.md), create 3–5 probing tasks
> that a future agent would need to perform when invoking this skill.
>
> **Task design rules:**
> 1. Each task must require the agent to read and apply the skill —
>    it should not be solvable from general knowledge alone.
> 2. Include at least two complexity factors per task:
>    specific facts from the skill, format constraints, exact numerical
>    limits, multi-step reasoning, or compliance with behavioral rules.
> 3. Every task must target a different section or aspect of the skill.
> 4. Each task should read as a natural user request, not a quiz question.
>
> **Rubric design rules (8–12 rubrics per task):**
> - ~25% content inclusion: "The response should include [element]."
> - ~20% content exclusion: "The response should not include [thing]."
> - ~15% format/structure: "The response should [format requirement]."
> - ~15% accuracy: "The response should correctly state [specific fact]."
> - ~10% constraint compliance: "The response should meet [exact constraint]."
> - ~15% other: sequence/ordering, tone/style, or domain-specific logic.
>
> Each rubric must be binary (pass/fail), unambiguous, and test
> exactly one criterion.
>
> Output a JSON array:
> ```json
> [
>   {
>     "task": "task description as a user message",
>     "rubrics": ["rubric 1", "rubric 2", ...]
>   }
> ]
> ```

---

## Reasoner

**Purpose:** Simulate a fresh agent that has only the generated skill as
guidance. Attempt each Challenger task using the skill instructions.

**Prompt template:**

> You are an agent that must complete the following task.
> Your only guide is the skill document provided below.
> You have no memory of the conversation that produced this skill.
>
> Skill document:
> ```
> [paste SKILL.md here]
> ```
>
> Task:
> ```
> [paste Challenger task here]
> ```
>
> Follow the skill instructions step by step and produce your response.

**What to watch for:** If the Reasoner cannot complete a step because
the skill is ambiguous, missing guidance, or contradictory, that is an
immediate signal for the Proposer — note the exact gap before scoring.

---

## Judge

**Purpose:** Score each Reasoner response against every rubric with a
strict binary 0/1 verdict. Partition tasks into solved and failed sets.

**Scoring rules:**
- Score `1` only if the rubric is **fully** satisfied. Partial credit is
  not allowed.
- When in doubt between 0 and 1, score 0.
- A task is **solved** only when every rubric scores 1.
- A task is **failed** when any rubric scores 0.

**Output format:**

```json
{
  "task_index": 0,
  "rubric_scores": [1, 0, 1, 1, 0, 1, 1, 0],
  "total": 5,
  "max": 8,
  "verdict": "failed",
  "failed_rubrics": [1, 4, 7]
}
```

Add solved tasks to `probe_pool.easy` and failed tasks to
`probe_pool.hard`.

---

## Proposer

**Purpose:** Diagnose why the Reasoner failed and propose a concrete,
generalizable update to the skill.

**Prompt template:**

> You are an expert skill analyst. The Reasoner failed the following
> tasks when trying to apply the skill. Your job is to diagnose why
> and propose a concrete improvement to the skill document.
>
> Failed tasks and their failed rubrics:
> ```
> [paste Judge output for failed tasks]
> ```
>
> Current skill:
> ```
> [paste current SKILL.md]
> ```
>
> **Analysis process:**
> 1. For each failed rubric, classify the failure type:
>    - Content gap — information exists in the source but isn't in the skill.
>    - Format/structure error — wrong shape or organization.
>    - Constraint violation — limit or requirement missing from the skill.
>    - Reasoning error — incorrect logic that the skill doesn't catch.
>    - Task misunderstanding — the skill's instructions are ambiguous.
>    - System prompt non-compliance — behavioral rule not covered.
> 2. Check whether an existing skill in the workspace already covers
>    this gap. If yes, propose an edit to that skill instead.
> 3. Identify the single highest-impact improvement.
>
> **Anti-patterns to avoid in proposals:**
> - DON'T propose vague improvements like "be more careful".
> - DON'T propose improvements that only fix one specific task.
> - DON'T propose a new section if editing an existing one is enough.
>
> Output JSON:
> ```json
> {
>   "action": "edit" or "add",
>   "target_section": "section name in SKILL.md",
>   "failure_type": "one of the six categories",
>   "analysis": "why the skill failed across these tasks",
>   "proposal": "concrete, specific change to make to the skill",
>   "justification": "why this generalizes beyond the specific failed tasks"
> }
> ```

---

## Generator

**Purpose:** Apply the Proposer's proposal to produce an updated SKILL.md.

**Implementation rules:**
1. **Actionable, not abstract** — every new instruction must be a concrete
   step or checklist item, not general advice.
2. **Concise** — challenge each added sentence: "Does this add actionable
   value?" Remove filler when adding new content.
3. **Complementary** — the change should complement (not repeat) guidance
   already present elsewhere in the skill.
4. **Template-compliant** — the updated skill must still pass
   `scripts/validate_skill.py` for the chosen tier.

**After generating the update:**
- Run `scripts/validate_skill.py <updated-skill> --tier <tier>`.
- Fix any validation failures before proceeding.
- Append the updated version to `skill_history`.

---

## Cross-Time Replay (Skill Selector)

**Purpose:** After multiple rounds, select the skill version with the best
balanced performance across all accumulated probes.

**Algorithm:**

```
for each version v in skill_history:
    hard_rate = |v solves probe_pool.hard| / |probe_pool.hard|
    easy_rate = |v solves probe_pool.easy| / |probe_pool.easy|
    balanced_score[v] = hard_rate × easy_rate

selected = argmax(balanced_score)
```

**Why balanced_score instead of total solved?**

A skill that over-specializes to fix hard probes may regress on easy ones.
The product `hard_rate × easy_rate` penalizes any version that neglects
either pool, ensuring the selected skill generalizes broadly.

**Edge cases:**
- If `probe_pool.hard` is empty (no failures ever), use `easy_rate` alone.
- If `probe_pool.easy` is empty (all tasks failed in round 1), use
  `hard_rate` alone after round 2.
- If the loop ran only one round, skip replay and save the current version.
