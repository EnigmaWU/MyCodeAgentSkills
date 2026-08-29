# Review In Mind (ReviewInMindGenie) — Common Loop

Every skill MUST run this review loop before delivering any artifact. The loop is deterministic-first: objective checks run before subjective judgment.

## Activate the Genie

Before delivering, activate the ReviewInMindGenie: stop authoring, switch to a skeptical reviewer, and critique the artifact as if someone else had produced it.

## The Loop

1. **Review Against Own Rules**: Run every deterministic check first — required fields, schema, syntax, links, and any build/test/lint command this skill defines. Only for what cannot be automated, switch to the skeptical-reviewer persona and judge the output against this skill's `What`, `Constraints (Logical Boundaries)`, and `Validation` criteria; do not assume it passed because it was easy to write.
2. **Classify Findings**: Label each defect as BLOCKER (output unusable), MAJOR (violates a core rule), or MINOR (polish/consistency).
3. **Fix or Escalate**: Fix BLOCKER and MAJOR findings immediately when the fix is unambiguous. After each fix, re-check the affected criteria. If a finding cannot be fixed without new input (missing evidence, conflicting requirements, or a user decision), do not guess — report it as an open question or known gap.
4. **Deliver with a Review Note**: Present the output with a short note: what was checked, what was fixed, and what remains as a known gap. Never present an unreviewed artifact as final.

## Per-Skill Lens

Each skill MUST keep its own `Review lens for this skill:` bullets directly under its `## Review In Mind (ReviewInMindGenie)` heading. The lens MUST be derived from that skill's `What`, `Constraints (Logical Boundaries)`, and `Validation` criteria so the review is domain-specific rather than generic.
