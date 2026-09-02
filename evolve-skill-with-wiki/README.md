# Evolve Skill with Wiki

An agent skill for running **WikiSkill-style skill evolution**: improving an agent's procedural `SKILL.md` across many execution runs with a persistent knowledge wiki that compounds what the agent learns.

## What Is This

Most skill maintenance is reactive: a conversation goes off-script and you patch the skill once. This skill is the *proactive* counterpart — a multi-iteration loop where:

1. an agent rolls out on training tasks using the current skills (no wiki access),
2. a wiki maintainer consolidates failing and passing traces into persistent pattern pages,
3. a skill proposer reads the wiki and proposes exactly one atomic skill change,
4. validation gating accepts the change only if the score improves, rolling back the skill but never the wiki.

The method comes from the WikiSkill paper (arXiv:2608.27454, Google Research), which shows this persistent-wiki loop beats one-shot skill-evolution baselines and that accumulated knowledge — not just fresh traces — drives the gains.

## Directory Structure

```text
evolve-skill-with-wiki/
  ├── SKILL.md                                  # Main workflow (COMPLEX tier)
  ├── README.md                                 # English overview
  ├── README_ZH.md                              # Chinese overview
  └── references/
      └── wikiskill-paper-digest.md             # Condensed source-paper method and results
```

The skill's *output* is an evolution workspace such as:

```text
evolution-runs/<task-domain>/
  ├── raw/                                      # immutable execution traces
  ├── wiki/                                     # compounding knowledge (never reset)
  │   ├── patterns/                             # failure modes + successful strategies
  │   ├── patterns/index.md
  │   ├── logs.md                               # chronological history
  │   └── skill-impact.md                       # proposal diff + score + accept/reject
  └── skills/                                   # reversible active skill set
```

## When to Use This vs the Other Skill Skills

| Situation | Skill to use |
| --------- | ------------ |
| Evolve a skill across many rollout runs, with a knowledge base | `evolve-skill-with-wiki` (this skill) |
| Improve a skill from one conversation's evidence | `improve-existing-skill` |
| Capture a brand-new skill from a conversation | `save-as-skill` |
| Design agent memory (user facts, session context) | `build-agent-memory-systems` |

## Usage

Invoke with triggers like:

- "evolve this skill"
- "set up skill evolution for [task domain]"
- "apply WikiSkill"
- "improve this skill from past execution runs"

You must provide (or let the agent set up) a task set with scores, a validation split, and an iteration budget. See `SKILL.md` for the full phased workflow.

## Key Rules the Workflow Enforces

- Skills roll back on validation degradation; the wiki never resets.
- The inference agent never reads the wiki during rollouts — doing so measurably degrades the evolved skill.
- One atomic skill proposal per iteration, gated by a strict validation improvement.
- Every proposal is recorded in `skill-impact.md` (diff, score, outcome) so rejected ideas are not re-proposed.
