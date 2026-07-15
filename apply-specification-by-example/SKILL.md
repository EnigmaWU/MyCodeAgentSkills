---
name: apply-specification-by-example
description: >
  WHEN/WHERE/WHO: [Scheduling: Product owners, BAs, testers, developers, and agents aligning requirements with delivery.] 
  HOW: [Structural: Use this SKILL to derive scope from goals, specify collaboratively with examples, refine for clarity, automate validation, and evolve living documentation.] 
  WHY: [Scheduling: Reduces rework and ambiguity by turning requirements into executable, trustworthy documentation.]
---

# Apply Specification by Example

## Who
Product owners, business analysts, testers, developers, and AI coding agents who need to deliver the right behavior with less ambiguity and less rework.

## What
This skill applies Specification by Example as a repeatable workflow: collaborate on requirements, express rules through concrete examples, turn those examples into executable checks, and maintain living documentation.

## When
Invoke this skill when requests include terms like:
- "align requirements and tests"
- "write executable acceptance criteria"
- "use examples for specification"
- "improve requirement quality"
- "reduce rework from unclear stories"

Use this skill before implementation begins, or while stabilizing an existing delivery process with frequent misunderstandings.

## Where
Applies to:
- Story and requirement artifacts
- Acceptance criteria and example tables
- Automation suites for executable specifications
- Living documentation outputs in docs or reports

## Why
Teams often fail not because coding is hard, but because understanding is inconsistent. This skill creates shared understanding early, keeps validation close to delivery, and preserves knowledge in documentation that remains current through execution.

## Inputs
- Business outcomes and scope context (required)
- Candidate stories/features (required)
- Stakeholders available for clarification (required)
- Existing acceptance tests or scripts (optional)
- Existing automation/reporting stack (optional)

## Output (Logical Evidence)
- A scoped set of feature specifications written with concrete examples
- Executable checks that validate behavior without changing business intent
- Living documentation that reflects current system behavior
- A short risk list (ambiguities, unstable checks, missing examples)

## Constraints (Logical Boundaries)
- Start from business goals and expected outcomes, not from tool capabilities.
- Keep specifications in domain language; do not couple them to implementation details.
- Do not convert long procedural UI scripts into "specifications".
- Do not duplicate business rules in the automation layer.
- Keep examples precise, realistic, and comprehensible; avoid combinatorial explosions.
- Validate frequently and classify checks by feedback speed.
- Anti-Pattern Mapping:
  - Forbidden: "tool-first adoption", "record-and-playback test strategy", "UI-only business rule validation", "unstable flaky checks normalized as acceptable".

## One More Thing
If goals, stakeholders, or sign-off expectations are unclear, stop and ask the user to clarify before drafting or automating specifications.

## How (Structural Workflow)
### Phase 1: Derive Scope from Goals
1. Capture the target business outcome and beneficiaries.
2. Convert high-level goals into a candidate feature scope.
3. Identify boundaries, exclusions, and value assumptions.
4. Confirm that scope describes complete user-facing outcomes, not isolated technical tasks.

### Phase 2: Specify Collaboratively
1. Choose collaboration format based on team context (workshop, small triad, paired drafting, or lightweight iterative reviews).
2. Draft a small set of examples together with domain experts.
3. Resolve ambiguity through questions on intent, edge cases, and expected outputs.
4. Freeze a first-pass specification only when stakeholders agree on behavior.

### Phase 3: Illustrate and Refine with Examples
1. Ensure each example is concrete and testable.
2. Replace vague categories with explicit values where possible.
3. Keep examples business-focused and self-explanatory.
4. Refine titles and short narrative so specifications can be understood without oral context.
5. Add nonfunctional examples when relevant (for example: latency thresholds, workflow timing, data consistency).

### Phase 4: Automate Validation Without Changing Intent
1. Implement an automation layer that maps examples to system interactions.
2. Keep business wording stable while evolving underlying automation code.
3. Automate near system boundaries where checks are meaningful and stable.
4. Avoid re-implementing product logic in test code.
5. Partition checks by speed and reliability to support fast feedback cycles.

### Phase 5: Validate Frequently and Manage Reliability
1. Run quick packs continuously and slower packs on scheduled gates.
2. Track flaky checks and remove instability sources first.
3. Maintain a separate known-failures workflow if needed, with transparent ownership.
4. Use CI history to identify and prioritize unreliable checks.

### Phase 6: Evolve Living Documentation
1. Publish executable specification results as readable documentation.
2. Organize documentation by business capability or workflow, not by tool internals.
3. Standardize language and naming across teams.
4. Review documentation drift every iteration and refactor stale specs.

## Resources
- [Specification by Example Checklist](./details/specification-by-example-checklist.md)

## Validation (Verifiable Rewards)
1. Verify every specification links to a business goal and explicit expected outputs.
2. Verify examples are concrete, domain-readable, and executable.
3. Verify automation does not duplicate business logic and is not primarily UI-fragile.
4. Verify documentation output is generated from execution and organized for stakeholder use.
5. Verify unresolved ambiguities and reliability risks are explicitly reported.
