# Validation Log: review-c4-model

## Chosen tier
**COMPLICATED** — the workflow has multiple steps (ingest, classify, run checklists,
report, validate), meaningful decision points (diagram type classification, severity
assignment), explicit inputs/outputs, and operating constraints. It is not SIMPLE
(more than one straight-line path) and not COMPLEX (no multi-phase iteration across
multiple artifacts or review loops beyond a single report).

## Source material
*The C4 Model: Visualizing Software Architecture* by Simon Brown (O'Reilly, 2026):
- Chapter 1: diagramming failure patterns.
- Chapter 2: abstractions and diagram types.
- Chapters 3-9: level-specific intent, scope, content, and audience.
- Chapter 10: notation guidance.
- Appendix: Diagram Review Checklist.

## Acceptance gate results
- [x] `SKILL.md`, `README.md`, `README_ZH.md`, and `details/` exist.
- [x] Frontmatter uses the multi-line `description: >` format.
- [x] `SKILL.md` contains all COMPLICATED-template sections: Who, What, When, Where,
  Why, Inputs, Output, Optimization Readiness, Constraints, One More Thing, How,
  Resources, Validation.
- [x] No hallucinated libraries or tools referenced.
- [x] All internal markdown links resolve to existing files.
- [x] Checklist executable from natural language alone (no dependency on the original
  book or diagrams).

## Evidence: worked example
Executed the workflow against the content of the book's Figure 1-1 (a "logical view"
diagram with boxes Risk calculation, Parameter management, Security, Report creation,
Monitoring, Report distribution, Audit).

Expected findings caught:
- FAIL R1/R2: relationships are unlabeled -> BLOCKER.
- FAIL E6: "Security" is a generic/ambiguous element name -> MAJOR.
- FAIL G1: no title stating type/scope -> MAJOR.
- FAIL G3/E7-E10: no key for any notation used -> MAJOR.
- FAIL E12: mixed abstraction level (no explicit types; abstraction ambiguous) ->
  BLOCKER.

Verdict produced: FAIL. Checklist results match the verdict rule (BLOCKER present).

## Transfer check
Applied the General/Elements/Relationships sections to the book's Figure 2-6
(Financial Risk System web application component view — a different system from the
book's main Internet Banking System example). The checklist items applied without
modification, confirming the skill transfers beyond the primary example system.

## Rejected drafting choices
- **Rejected name `c4-diagram-reviewer`** — user explicitly preferred `review-c4-model`.
- **Rejected SIMPLE tier** — classification and severity branching make it more than a
  straight-line checklist.
- **Rejected COMPLEX tier** — no multi-phase iteration or review loops are needed;
  COMPLEX would add unneeded control depth.
- **Rejected including diagram-creation instructions** — scope drift; creation is a
  separate skill family.
- **Rejected JSON-only report format** — human-readable findings with concrete fixes
  are required for actionable reviews.
- **Rejected subjective aesthetics rules** (e.g., "diagram is ugly") — every finding
  must trace to a book rule.
