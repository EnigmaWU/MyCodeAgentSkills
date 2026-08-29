# Common Spine: Canonical Section Order

Every skill in this repository follows this level-2 section order unless the skill explicitly documents a reason to deviate:

1. `## Common Contract (Load First)` — activation reference to `skill-common`.
2. `## Who` — who uses the skill or who the work is for.
3. `## What` — what the skill does and its concrete outcome.
4. `## When` — exact trigger conditions and near-misses.
5. `## Where` — files, folders, systems, or contexts the skill applies to.
6. `## Why` — value, risks, and reason the workflow is worth reusing.
7. `## Inputs` — required and optional inputs (COMPLICATED/COMPLEX).
8. `## Output (Logical Evidence)` — expected deliverables and declared side effects.
9. `## Optimization Readiness` — failure signals, evidence, mutation boundaries, acceptance criteria, rejected revision handling, transfer check, stop rule.
10. `## Constraints (Logical Boundaries)` — invariants, required tools, and anti-pattern mapping.
11. `## One More Thing` — the standard stop-and-ask closing rule.
12. `## How (Structural Workflow)` — deterministic, phased, state-machine execution steps.
13. `## Review In Mind (ReviewInMindGenie)` — heading plus the reference to `skill-common/details/review-in-mind.md` and the skill's own review lens.
14. `## Resources` — linked details, references, scripts, and assets (COMPLEX).
15. `## Validation (Verifiable Rewards)` — strict checks that prove success before delivery.

## Tier Rules
- SIMPLE: one straight-line workflow; may omit Inputs/Output/Resources but keeps the common spine sections.
- COMPLICATED: one main flow plus decision points; keeps Inputs, Output, Constraints, and Validation.
- COMPLEX: phased, branching, review loops, bundled resources; keeps all sections above.

Do not upgrade a tier because a topic is important; upgrade it because the execution logic is deeper.
