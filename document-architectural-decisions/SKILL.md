---
name: document-architectural-decisions
description: >
  WHEN/WHERE/WHO: [Scheduling: Architects, system designers, or agents resolving an architectural tradeoff. Applies to design proposals and RFCs.]
  HOW: [Structural: Use this SKILL to write structured 12-field Architectural Decision Records (ADRs) and alternatives matrices.]
  WHY: [Scheduling: Capturing the "why" behind system design prevents future developers from repeating dead-end paths.]
---

# Document Architectural Decisions

## Common Contract (Load First)

When this skill is activated, first load [skill-common](../skill-common/SKILL.md) and apply the shared conventions it defines: canonical section order, frontmatter rules, anti-pattern guidance, and the Review In Mind loop in [review-in-mind](../skill-common/details/review-in-mind.md). This skill adds only domain-specific rules below.

## Who
Architects, system designers, or coding agents responsible for capturing the reasoning behind major design choices to ensure long-term traceablity, compliance, and developer alignment.

## What
Elicit design issues, catalog and compare design alternatives, and compile a structured 12-field Architectural Decision Record (ADR) including type (Existence, Ban, Property, Executive), state, and downstream implications.

## When
- Triggered by requests like: "document this design decision", "write an ADR for...", "create a decision record...", "log the tradeoffs between X and Y", or "document why we banned dynamic allocation".
- Do not use for documenting minor local refactoring choices, variable naming preferences, or simple unit testing setups unless they carry system-level implications.

## Where
- Input is gathered from the active conversation, codebase constraints, datasheets, or design tickets.
- The output is written to a designated decision folder in the workspace (e.g., `docs/adr/`, `docs/decisions/`, or a new directory specified by the user).

## Why
- Capturing the "why" behind system design prevents future developers from shaking their heads in disbelief and asking "what were they thinking?".
- Explicitly documenting alternatives and arguments prevents circular team discussions and repeating dead-end technical paths.
- Mapping implications helps stakeholders plan schedule impacts, training needs, and downstream requirements revisions.

## Inputs
- **Design Issue Context** (required): The specific problem or requirement being addressed.
- **Proposed Alternatives** (optional): Options under consideration. If missing, the agent must identify at least two viable options.
- **Decision Template Details** (required): Located at [decision-template-details](details/decision-template-details.md).
- **Documenting Software Architectures PDF** (optional): Reference book located at [Documenting Software Architectures](../TMP/Documenting%20Software%20Architectures.pdf).

## Output (Logical Evidence)
- **Architectural Decision Record (ADR)**: A markdown file containing the completed 12-field template.
- **Alternatives Comparison Matrix**: A structured matrix comparing options against technical/business concerns.

## Optimization Readiness
- **Failure Signals**: Alternatives are weak or fake, implications are left blank, the decision type is unclear, or the rationale is too shallow to defend later.
- **Evidence To Collect**: Issue context, alternatives matrix entries, decision fields, downstream implications, and examples of where the chosen alternative beat the others.
- **Safe Mutation Boundaries**: Refine comparison criteria, ADR field prompts, alternative-generation guidance, and validation checks without changing the core decision-record workflow.
- **Acceptance Criteria**: Accept revisions only if the ADR contains viable alternatives, no empty critical fields, a clear decision type, and downstream implications that match the selected option.
- **Rejected Revision Handling**: Record placeholder alternatives, empty-field patterns, and thin rationales so they are not repeated.
- **Transfer Check**: Verify the workflow still works for low-risk local choices and for system-level architecture decisions.
- **Stop Rule**: If the timing, budget, or hardware constraints are unclear or conflicting, stop and ask before documenting the decision.

## Constraints (Logical Boundaries)
- **Viable Options Only**: Do not list weak placeholders as alternatives. All alternatives listed in the comparison matrix must be genuinely viable solutions.
- **No Empty Fields**: The *Implications*, *Assumptions*, and *Argument* fields must never be blank or marked as "N/A."
- **Rigorous Typing**: Every decision must be explicitly categorized under Kruchten's types (Existence, Ban, Property, or Executive).

## One More Thing
If the primary business goals, timing budgets, or physical hardware constraints are unknown or conflicting, stop and ask the user to clarify them before writing the decision record.

---

## How (Structural Workflow)
### 1. Gather the Required Context
*   Identify the core design issue and what triggers it now.
*   Locate any business/technical concerns (e.g., CPU headroom, latency budgets, safety regulations like ISO 26262, or development schedule limits).
*   Verify what software/hardware artifacts will be affected.

### 2. Compare Alternatives
*   Search the reference at [decision-template-details](details/decision-template-details.md) to understand the format.
*   Identify at least two viable design options.
*   Build an **Alternatives Comparison Matrix** mapping the options to the relevant concerns. Use clear evaluations (`Yes`, `No`, `Partial`) and summarize the key tradeoffs (e.g., choosing Option A improves latency but increases RAM consumption).

### 3. Draft the Decision Record
*   Write the decision record using the **12-field template** defined in [decision-template-details](details/decision-template-details.md).
*   Clearly describe the chosen solution and detail the *Argument* (the core logic/tradeoffs driving the choice).
*   Explicitly list the *Implications* (e.g., "requires additional RTOS task configuration", "requires developer training on atomic lock usage").
*   Classify the decision type (Existence, Ban, Property, or Executive) and set its initial state (`Decided` or `Tentative`).

### 4. Validate and Refine
*   Ensure all markdown links to related files, code symbols, or documents are valid.
*   Run these quality checks to prevent common model issues:
    *   **Common Rationalization check**: If you feel tempted to skip documenting alternatives or implications because the choice seems "obvious," stop and remember: *Even obvious decisions carry hidden assumptions. Document at least one alternative and list downstream impacts.*
    *   **Red Flags check**: Verify that the record does not have empty fields, does not suggest unverified tools, and clearly maps to system requirements.

### 5. Report the Outcome Clearly
*   Present the final decision record and comparison matrix in the chat, and save them to the target directory.

## Review In Mind (ReviewInMindGenie)

Execute the common review loop in [review-in-mind](../skill-common/details/review-in-mind.md) before delivering.

Review lens for this skill:
- Does each ADR fill the 12 fields and record type, state, and downstream implications?
- Are alternatives compared with explicit rationale for the chosen solution?
- Is every decision traceable to the design issue it resolves?
