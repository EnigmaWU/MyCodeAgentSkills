---
name: build-business-objectives-model
description: >
  WHEN/WHERE/WHO: [Scheduling: Product owners or agents analyzing project kickoff documents or vision statements.]
  HOW: [Structural: Use this SKILL to map subjective Business Problems to quantifiable Business Objectives, and derive the Product Concept.]
  WHY: [Scheduling: Avoids the trap of building features no one needs. If a feature doesn't trace back to a BOM objective, it shouldn't be built.]
---

# Build Business Objectives Model

## Who
Product Owners, Business Analysts, and AI Agents. The agent uses this skill to anchor a project's scope in measurable value.

## What
This skill implements the Business Objectives Model (BOM) from the Requirements Modeling Language (RML). It systematically extracts:
1. **Business Problems:** What is wrong today?
2. **Business Objectives:** What quantifiable metric proves we fixed the problem?
3. **Product Concept:** What is the high-level solution?
4. **Guiding Principles:** What rules govern the solution?

## When
Invoke this skill at the absolute beginning of a project (Phase 0), before writing any user stories or feature lists. Trigger phrases include: "extract business objectives," "build a BOM," "what is the product concept," or "analyze this kickoff document."

## Where
Applies to project charters, vision documents, and executive stakeholder transcripts.

## Why
Stakeholders often jump straight to "We need an AI chatbot." If you don't ask *why*, you might build a chatbot when what they really needed was a better search bar. The BOM forces the extraction of the underlying *Problem* (e.g., "Customer service wait times are too high") before committing to the *Product Concept*.

## Inputs
- Project charters, vision documents, or interview transcripts.

## Output (Logical Evidence)
- A completed Business Objectives Model document.

## Optimization Readiness
- **Failure Signals**: Features are mistaken for business problems, objectives lack measurable outcomes, product concepts are accepted without root-cause clarity, or guiding principles are invented rather than sourced.
- **Evidence To Collect**: Problem statements, objective mappings, missing-metric questions, product concepts, and reviewer feedback on whether the BOM stays tied to business intent.
- **Safe Mutation Boundaries**: Refine problem-extraction prompts, objective templates, and formatting guidance without changing the core requirement to connect problems, objectives, and product concept explicitly.
- **Acceptance Criteria**: Accept revisions only if every objective maps back to a business problem, missing metrics are flagged instead of fabricated, and the BOM separates problem, objective, concept, and principles clearly.
- **Rejected Revision Handling**: Record feature-list-only interpretations, invented metrics, and orphan objectives so they are not reused.
- **Transfer Check**: Verify the workflow still works for executive charters, stakeholder interviews, and vision documents with uneven detail.
- **Stop Rule**: If the source material contains only solution ideas or feature lists with no identifiable business problem, stop and ask before drafting the BOM.

## Constraints (Logical Boundaries)
- Do not invent metrics. If an objective is not quantifiable in the source text, flag it as a question (e.g., "[Insert metric here - requires stakeholder input]").
- Ensure there is a 1:1 or 1:N mapping from Problems to Objectives. An objective without a problem is invalid.

## One More Thing
If the input text is just a list of features (e.g., "Build a login page, build a cart"), stop and ask the user what the overarching business problem is before proceeding.

## How (Structural Workflow)
### Phase 1: Problem Extraction
1. Read the input text and extract the core **Business Problems**. These are negative statements about the current state (e.g., "Costs are too high," "Revenue is dropping," "Manual entry takes too long").

### Phase 2: Objective Definition
2. For each Business Problem, extract or infer the corresponding **Business Objective**.
3. Ensure every Business Objective is quantifiable (e.g., "Reduce manual entry time by 50% by Q3"). If the text lacks a metric, mark it for follow-up.

### Phase 3: Product Concept and Principles
4. Extract the **Product Concept**. This is the high-level summary of the solution being proposed.
5. Extract **Guiding Principles**. These are constraints or rules (e.g., "Must be mobile-first," "Do not disrupt the legacy database").

### Phase 4: Formatting
6. Output the extracted data using the BOM Template structure.

## Resources
- [BOM Template](./details/bom-template.md)

## Review In Mind (ReviewInMindGenie)

Before delivering, activate the ReviewInMindGenie: stop authoring, switch to a skeptical reviewer, and critique the artifact as if someone else had produced it.

1. **Review Against Own Rules**: Re-read the output against this skill's `What`, `Constraints (Logical Boundaries)`, and `Validation` criteria. Check each rule explicitly; do not assume it passed because it was easy to write.
2. **Classify Findings**: Label each defect as BLOCKER (output unusable), MAJOR (violates a core rule), or MINOR (polish/consistency).
3. **Fix or Escalate**: Fix BLOCKER and MAJOR findings immediately when the fix is unambiguous. After each fix, re-check the affected criteria. If a finding cannot be fixed without new input (missing evidence, conflicting requirements, or a user decision), do not guess — report it as an open question or known gap.
4. **Deliver with a Review Note**: Present the output with a short note: what was checked, what was fixed, and what remains as a known gap. Never present an unreviewed artifact as final.

Review lens for this skill:
- Is every business problem paired with a quantifiable objective and measurable success metric?
- Does the product concept trace to the objective, and do guiding principles govern scope?
- Would a feature not traceable to a BOM objective be excluded?

## Validation
1. Verify that every Business Problem is addressed by at least one Business Objective.
2. Ensure every Business Objective includes a measurable success metric.
