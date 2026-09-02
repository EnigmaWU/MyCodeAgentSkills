# WikiSkill Paper Digest

Condensed from **WikiSkill: Compiling Agent Experience into Persistent Knowledge for Skill Evolution** (L. Tang, C. Rashtchian, C.-S. Ferng, A. Tomkins, D.-C. Juan, T. Vu — Google Research / Virginia Tech), arXiv:2608.27454v1, August 2026. The source PDF lives in the user's workspace at `TMP/2608.27454v1(WikiSkill).pdf`.

## Problem

Recent skill-evolution methods (EvoSkill, Trace2Skill, SkillOpt) iterate rollouts → analysis → skill patch → validation gate, but the insights that guide skill development stay scattered across optimization histories. There is no separate, evolving knowledge representation, so rejected ideas get re-proposed and recurring failure modes get rediscovered each iteration.

## Core Idea

Co-evolve skills with a persistent knowledge base (a "wiki") that compiles raw execution experience into structured, compounding knowledge.

## Three-Layer Workspace

| Layer | Directory | Semantics |
| --- | --- | --- |
| Raw | `raw/` | Immutable execution traces (reasoning, tool calls, outputs, final answers). Write once. |
| Wiki | `wiki/` | Pattern pages (`patterns/`), evolution log (`logs.md`), and skill-impact tracker (`skill-impact.md`). Compounding; never reset. |
| Skills | `skills/` | Active procedural skills. Each contains `SKILL.md` plus `PURPOSE.md` linking the skill back to motivating wiki patterns. Reversible via gating. |

## Four Components per Iteration

1. **Inference Agent** — runs rollouts on training tasks with active skills injected into the system prompt. **No wiki access** (see ablation below).
2. **Wiki Maintainer** — samples ~8 traces (≈5 failing + 3 passing, each capped ≈15k chars), performs root-cause analysis, creates/updates pattern pages, refreshes `index.md`, appends to `logs.md`.
3. **Skill Proposer** — ReAct agent given the wiki index, `skill-impact.md`, and a concise pass/fail summary; reads specific patterns and traces on demand; emits exactly **one atomic proposal** (create a skill or patch one skill).
4. **Gating & Rollback** — rolls the candidate out on validation; accepts only if the score strictly exceeds the best-so-far (`R(S') > R_best`); on rejection reverts `skills/` but **never** `wiki/`; the harness then appends diff + score + outcome to `skill-impact.md`. Early-stop at validation 1.0.

## Key Results

- WikiSkill beats the strongest prior method per model by +3.3 to +12.0 points on average across 5 benchmarks (LiveMath, SealQA, SpreadSheetBench, OfficeQA, ALFWorld).
- Gains grow with model scale: +12.3 / +17.5 / +23.9 points for Qwen 4B / 9B / 27B. Skills also compensate for scale: Qwen-9B + WikiSkill (47.4%) beats Qwen-27B without skills (39.4%).
- Skills transfer across model families, and a stronger model's skill can beat a model's self-evolved skill (ALFWorld: 70.2% vs 63.4%). Negative transfer happens when skills encode low-level, model-specific workarounds.
- **Ablation (Gemini-3.5-Flash, 4 benchmarks)**: proposer-with-wiki beats proposer-without-wiki 63.7 vs 48.7 (avg). Inference-agent-with-wiki *degrades* the result to 60.9 — wiki access during rollouts makes traces less informative for skill development.
- Skill refinement continues across iterations: 39–58% of accepted updates happen in iterations 0–1, but 21–48% land mid-run (2–4) and 4–28% late (5–7).
- Wiki patterns accumulate (6–9 created, 7–18 edits on average) while accepted skills stay compact (~45–129 lines depending on model).

## Case Study Pattern (ALFWorld, Qwen-3.6-27B)

Iteration 0: maintainer writes `take-examine-move-loop.md`; proposer's `goal-directed-action` is **rejected** (too abstract). The diff and rejection are preserved in `skill-impact.md`. Iteration 1: proposer creates `break-repetition-loop` with a concrete rule ("Never return an item to its origin"), which is accepted. Iteration 4: new evidence (`multi-operation-loop.md`) motivates a refinement ("Each operation type once per item"), accepted. The wiki — not the current iteration's traces alone — is what made the refinement possible.

## Limitations the Paper Acknowledges

- Skills are fully injected into the prompt; retrieval/triggering is out of scope.
- Strict gating rejects "neutral" proposals that might enable future gains.
- No automated wiki pruning yet (may matter for very long runs).
- No online adaptation within a single very long rollout.

## Companion Paper (Different Problem)

`SKILL.state` (arXiv:2608.26263v2) is complementary but separate: it replaces append-only conversational history with explicit, mutable execution state for long-horizon skill *execution*. WikiSkill is about skill *evolution*; SKILL.state is about skill *runtime*. Do not merge the two into one skill.
