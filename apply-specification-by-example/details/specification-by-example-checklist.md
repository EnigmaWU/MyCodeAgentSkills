# Specification by Example Checklist

Use this checklist while applying the skill.

## 1. Goal and Scope Quality

- Verify each feature maps to a business goal and target user outcome.
- Verify boundaries and exclusions are explicit.
- Verify scope describes complete user value, not isolated technical tasks.

## 2. Collaboration Quality

- Verify domain expert, delivery, and test perspectives are represented.
- Verify key assumptions and ambiguities are resolved before implementation.
- Verify collaboration format matches team context (workshop, triad, paired drafting, lightweight review).

## 3. Example Quality

- Verify examples are concrete and use realistic values.
- Verify expected results are explicit and measurable.
- Verify examples remain understandable without hidden oral context.
- Verify edge cases are represented without uncontrolled combinatorial growth.

## 4. Specification Quality

- Verify titles and narratives explain business behavior.
- Verify wording is in domain language, not implementation language.
- Verify specifications are not long procedural scripts.
- Verify nonfunctional constraints are captured when relevant.

## 5. Automation Layer Quality

- Verify automation preserves business wording and intent.
- Verify no business logic is duplicated in automation code.
- Verify checks target stable system boundaries when possible.
- Verify UI checks focus on UI behavior, not all business rules.

## 6. Validation Cadence

- Verify quick checks run frequently.
- Verify slow checks are separated and scheduled.
- Verify flaky checks are tracked and actively reduced.
- Verify CI trend data is reviewed for reliability issues.

## 7. Living Documentation Health

- Verify documentation is generated from executable results.
- Verify organization follows business capabilities or flows.
- Verify naming and language stay consistent across specifications.
- Verify stale or duplicated specifications are refactored regularly.

## Red Flags

- Tool-first discussion before goal and scope clarity
- Frequent rewrites of specifications due to changing interpretation
- Heavy UI-only test strategy for core business rules
- Disabled failing checks with no ownership or remediation plan
- Specifications that stakeholders cannot read or validate
- Domain language drift into framework or implementation jargon

## Common Rationalizations and Rebuttals

- Rationalization: "We can automate later after coding."  
  Rebuttal: Define executable examples early to prevent wrong implementation loops.

- Rationalization: "The UI script already describes behavior."  
  Rebuttal: Scripts describe interaction flow; specification must describe business rules and expected outcomes.

- Rationalization: "We keep flaky tests because everything is flaky anyway."  
  Rebuttal: Reliability is part of feedback quality; isolate and remove instability sources as first-class work.
