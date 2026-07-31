---
name: analyze-with-tactics-questionnaires
description: >
  WHEN/WHERE/WHO: [Scheduling: Reviewers, architects, or agents analyzing a proposed or existing architecture.]
  HOW: [Structural: Use this SKILL to systematically evaluate the design against targeted Quality Attribute questionnaires (e.g., Availability, Security).]
  WHY: [Scheduling: Uncovers hidden architectural risks and missing tactics before implementation.]
---

# Analyze with Tactics Questionnaires

## Who
Architecture reviewers, technical leads, and QA engineers. The agent uses this skill to critique designs systematically.

## What
This skill executes a structured architectural analysis using Tactics-Based Questionnaires. It evaluates how well an architecture supports a specific Quality Attribute by checking if necessary tactics (like fault detection, authorization, or resource management) are present.

## When
Invoke this skill during design reviews, architectural assessments, or when auditing legacy systems. Trigger phrases include: "review this architecture for security," "analyze availability," or "run a tactics questionnaire."

## Where
Applies to Architecture Decision Records (ADRs), system design documents, and architecture diagrams.

## Why
Free-form reviews often miss edge cases. Tactics-based questionnaires force the reviewer to ask uncomfortable but necessary questions (e.g., "How does the system recover from state corruption?") based on established architectural theory.

## Inputs
- The architecture design or ADRs.
- The target Quality Attribute(s) to analyze (e.g., Availability, Modifiability).

## Output (Logical Evidence)
- A gap analysis report highlighting missing tactics or unaddressed risks.
- Recommendations for architectural improvements.

## Optimization Readiness
- **Failure Signals**: Reviews stay too generic, targeted tactics are skipped, unsupported findings lack evidence, or the analysis drifts across too many quality attributes at once.
- **Evidence To Collect**: Completed questionnaire answers, gap reports, cited architecture evidence, and reviewer feedback on missed or overstated risks.
- **Safe Mutation Boundaries**: Refine trigger phrases, reporting structure, questionnaire-loading guidance, and evidence requirements without changing the core tactic-driven review workflow.
- **Acceptance Criteria**: Accept revisions only if the skill produces attribute-focused findings, ties each gap to design evidence, and yields recommendations that map back to the questionnaire.
- **Rejected Revision Handling**: Record weak prompts, unsupported finding patterns, and over-broad review shapes so they are not reintroduced blindly.
- **Transfer Check**: Verify the workflow still works for at least two different quality attributes, such as security and availability.
- **Stop Rule**: If the target quality attribute or source architecture evidence is missing, stop and ask before broadening the review.

## Constraints (Logical Boundaries)
- Do not attempt to evaluate every single quality attribute at once; focus on the top 1 or 2 highest priority ones.
- Justify every identified gap with evidence (or lack of evidence) from the design document.

## One More Thing
If the target Quality Attribute is not specified, stop and ask the user which attribute they want to analyze.

## How (Structural Workflow)
### Phase 1: Preparation
1. Identify the target Quality Attribute(s) for the review based on the system's business drivers.
2. Load the corresponding Tactics-Based Questionnaire.

### Phase 2: Analysis Execution
3. Review the architecture documents.
4. For each question in the questionnaire, determine if the architecture addresses it:
   - Supported: The architecture uses an appropriate tactic.
   - Unsupported: The tactic is missing.
   - Not Applicable: The tactic is irrelevant to this system's context.

### Phase 3: Reporting
5. Compile the unsupported tactics into an Architecture Risk Report.
6. Propose specific design modifications or new ADRs to mitigate the identified risks.

## Resources
- [Tactics Questionnaires](./details/tactics-questionnaires.md)

## Validation
1. Verify that all questions in the targeted questionnaire were explicitly answered.
2. Ensure that "Unsupported" findings are backed by an explanation of the risk.
