# Architectural Decision Documentation Guide

This document contains ready-to-use templates and reference classifications for documenting architectural decisions in accordance with *Documenting Software Architectures: Views and Beyond* (Chapter 6.5) and Philippe Kruchten's decision ontology.

---

## 1. The 12-Field Decision Record Template

Copy and paste this template to log a key architectural decision. Make sure all sections are filled out comprehensively.

```markdown
# Architectural Decision Record: [Decision Name or ID]

| Field | Description |
| :--- | :--- |
| **1. Issue** | State the architectural design issue being addressed. Explain the clear reason why this issue must be resolved now. |
| **2. Decision** | Clearly state the chosen solution. Explain the selection out of the possible positions the architect could have taken. |
| **3. Status** | The lifecycle state of the decision (e.g., `Idea`, `Tentative`, `Decided`, `Approved`, `Challenged`, `Rejected`, `Obsolesced`). |
| **4. Group** | Category label for organizing and filtering decisions (e.g., `data`, `integration`, `presentation`, `concurrency`, `safety`). |
| **5. Assumptions** | Describe underlying assumptions in the environment (cost, schedule, tool availability, staff skill levels) or needs. |
| **6. Alternatives** | List the viable options considered. For complex choices, link to the **Alternatives Comparison Matrix** (see Section 2). |
| **7. Argument** | Detail why the selected position was chosen. Cite trade studies, cost, time to market, or quality attribute evaluations (e.g., ATAM/CBAM). |
| **8. Implications** | List downstream effects: new decisions required, requirement modifications, schedule renegotiations, or staff training needs. |
| **9. Related Decisions** | List related decisions and relationship types (e.g., *constrains*, *enables*, *forbids*, *subsumes*, *overrides*, *conflicts with*). |
| **10. Related Requirements** | Map this decision to business goals or Architecturally Significant Requirements (ASRs) to establish accountability. |
| **11. Affected Artifacts** | List specific components, modules, code files, directories, interfaces, or management budgets/schedules affected. |
| **12. Notes** | Raw notes, feedback, and meeting outcomes discussed during the decision process. |
```

---

## 2. Alternatives Comparison Matrix Template

Use this table when choosing between multiple complex alternatives. Map each option against the technical/business concerns.

| ID | Architectural Concern | Option 1: [Name] | Option 2: [Name] | Option 3: [Name] |
| :--- | :--- | :--- | :--- | :--- |
| **C1** | [e.g., Low-latency response (<50ms)] | Yes / No / Partial | Yes / No / Partial | Yes / No / Partial |
| **C2** | [e.g., Dev schedule (<3 months)] | | | |
| **C3** | [e.g., Static memory footprint limits] | | | |
| **C4** | [e.g., License / Compliance checks] | | | |
| **C5** | [e.g., Minimizes risk of data loss] | | | |

*Provide a brief summary of the tradeoffs under the matrix.*

---

## 3. Philippe Kruchten's Decision Ontology

Use these standard terms in the **Group**, **Decision**, and **Related Decisions** sections to maintain structural rigor:

### A. Kinds of Decisions
*   **Existence decisions** ("ontocrises"): Asserts that a structural or behavioral element will exist in the system.
    *   *Example*: "The network driver is organized into a primary task and an interrupt service handler task."
*   **Ban or nonexistence decisions** ("anticrises"): Explicitly forbids an element or design construct.
    *   *Example*: "The system will *not* use dynamic heap allocation (`malloc`/`free`) after initialization."
*   **Property decisions** ("diacrises"): Overarching traits, design rules, or constraints.
    *   *Example*: "All interrupt handlers must clear their interrupt source flags within 5 microseconds of invocation."
*   **Executive decisions** ("pericrises"): Non-technical constraints driven by business, process, education, or tools.
    *   *Example*: "All module interfaces must be audited and approved by the lead systems architect."

### B. State Machine
*   `Idea`: Brainstorming phase; does not constrain other decided options.
*   `Tentative`: Under evaluation; used to perform "what-if" analyses.
*   `Decided`: The current choice of the architect; must be internally consistent with all other decided decisions.
*   `Approved`: Formally reviewed and signed off by stakeholders or reviewers.
*   `Challenged`: An approved decision currently in jeopardy or under re-evaluation.
*   `Rejected`: Kept in the logs as historical record of a dead end that should not be revisited.
*   `Obsolesced`: Marked moot due to higher-level architectural changes.

### C. Relationship Types
*   **Constrains / Enables**: Decision A limits/makes possible Decision B (e.g., choosing FreeRTOS enables task notifications).
*   **Forbids (Excludes) / Conflicts With**: Decision A is incompatible with Decision B.
*   **Subsumes / Comprises**: Decision A contains or generalizes Decision B.
*   **Overrides**: Decision A is a specific local exception to a universal Decision B.
*   **Is Bound To**: A bidirectional constraint between A and B.
