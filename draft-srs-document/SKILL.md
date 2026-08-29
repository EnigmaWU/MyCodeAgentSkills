---
name: draft-srs-document
description: >
  WHEN/WHERE/WHO: [Scheduling: Business analysts, systems engineers, or agents compiling requirements into a final specification.]
  HOW: [Structural: Use this SKILL to map scattered user stories, constraints, and UI notes into the formal IEEE-style SRS template.]
  WHY: [Scheduling: Unstructured documents lead to missing context. The SRS forces teams to state dependencies and quality attributes.]
---

# Draft SRS Document

## Who
Business Analysts, Systems Engineers, and AI Agents. The agent uses this skill to generate a structured, formal requirements baseline.

## What
This skill implements the Software Requirements Specification (SRS) methodology from *Software Requirements (3rd Edition)*. It takes raw inputs (interview transcripts, JIRA tickets, rough PRDs) and maps them into a strict 8-part template:
1. Introduction
2. Overall Description
3. System Features
4. Data Requirements
5. External Interface Requirements
6. Quality Attributes
7. Internationalization
8. Other Requirements

## When
Invoke this skill at the end of the requirements elicitation phase, before handing off to development and QA for implementation and testing. Trigger phrases include: "draft an SRS," "compile these requirements," "create a specification document," or "format this as an SRS."

## Where
Applies to project documentation folders, wikis, or formal contract deliverables.

## Why
A pile of 100 user stories is not a specification. Developers need to know the operating environment (Section 2), the data models (Section 4), and the performance constraints (Section 6). The SRS template forces you to fill in these blanks.

## Inputs
- Raw requirements, user stories, transcripts, or existing vision documents.

## Output (Logical Evidence)
- A markdown document formatted using the SRS Template.

## Optimization Readiness
- **Failure Signals**: Requirements are invented, placeholders are left unmarked, hierarchical numbering breaks, or the draft omits major sections without flagging the gap.
- **Evidence To Collect**: Input classification notes, drafted SRS sections, open-question lists, and examples where the wording was made verifiable instead of vague.
- **Safe Mutation Boundaries**: Refine categorization prompts, section-filling guidance, numbering checks, and gap-analysis rules without changing the core template-driven drafting workflow.
- **Acceptance Criteria**: Accept revisions only if the SRS stays grounded in the source material, uses hierarchical numbering correctly, and marks unrecoverable gaps as `TBD` instead of inventing content.
- **Rejected Revision Handling**: Record invented requirements, poor numbering patterns, and overly generic wording so they are not repeated.
- **Transfer Check**: Verify the workflow still works for partial documents, mixed requirement sources, and feature-heavy specs.
- **Stop Rule**: If the input only contains visuals or missing functional logic, stop and ask before drafting the SRS.

## Constraints (Logical Boundaries)
- Do not invent requirements. If a section of the SRS cannot be filled from the provided input, mark it as `TBD` (To Be Determined) and list it as an open question.
- Write in verifiable, unambiguous language (e.g., replace "fast" with "sub-second response time").

## One More Thing
If the input text only contains UI mockups, stop and inform the user that an SRS requires functional logic and data requirements, not just visual designs.

## How (Structural Workflow)
### Phase 1: Categorization
1. Read the input material and classify every statement: Is it a feature? A constraint? A user class? A performance goal?

### Phase 2: Drafting
2. Populate the SRS Template section by section.
3. For **Section 3: System Features**, group related functional requirements together. Number them logically (e.g., 3.1, 3.1.1).
4. Extract Non-Functional Requirements (NFRs) into **Section 6: Quality Attributes**.

### Phase 3: Gap Analysis
5. Review the drafted SRS. If major sections (like "Data Requirements" or "External Interfaces") are completely empty, highlight this as a risk in your response.

## Resources
- [SRS Template](./details/srs-template.md)

## Review In Mind (ReviewInMindGenie)

Before delivering, activate the ReviewInMindGenie: stop authoring, switch to a skeptical reviewer, and critique the artifact as if someone else had produced it.

1. **Review Against Own Rules**: Re-read the output against this skill's `What`, `Constraints (Logical Boundaries)`, and `Validation` criteria. Check each rule explicitly; do not assume it passed because it was easy to write.
2. **Classify Findings**: Label each defect as BLOCKER (output unusable), MAJOR (violates a core rule), or MINOR (polish/consistency).
3. **Fix or Escalate**: Fix BLOCKER and MAJOR findings immediately when the fix is unambiguous. After each fix, re-check the affected criteria. If a finding cannot be fixed without new input (missing evidence, conflicting requirements, or a user decision), do not guess — report it as an open question or known gap.
4. **Deliver with a Review Note**: Present the output with a short note: what was checked, what was fixed, and what remains as a known gap. Never present an unreviewed artifact as final.

Review lens for this skill:
- Does the SRS cover all 8 required sections with traceable, testable requirements?
- Are requirements free of ambiguous words and implementation-biased constraints?
- Is every stakeholder need mapped to at least one requirement (or explicitly out of scope)?

## Validation
1. Verify that the document uses hierarchical numbering (1.1, 1.2, 3.1.1).
2. Ensure no placeholder text remains unless explicitly marked as `TBD`.
