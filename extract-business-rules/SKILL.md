---
name: extract-business-rules
description: >
  WHEN/WHERE/WHO: [Scheduling: Business analysts or agents reviewing user stories or PRDs that contain embedded business logic.]
  HOW: [Structural: Use this SKILL to extract policies, laws, and calculations from text and categorize them into a strict Business Rules Taxonomy.]
  WHY: [Scheduling: Separating rules allows for dynamic configuration. Hardcoding a rule as a feature creates legacy debt.]
---

# Extract Business Rules

## Common Contract (Load First)

When this skill is activated, first load [skill-common](../skill-common/SKILL.md) and apply the shared conventions it defines: canonical section order, frontmatter rules, anti-pattern guidance, and the Review In Mind loop in [review-in-mind](../skill-common/details/review-in-mind.md). This skill adds only domain-specific rules below.

## Who
Business Analysts, Product Owners, and AI Agents. The agent uses this skill to decouple business logic from functional requirements.

## What
This skill implements the Business Rules methodology from *Software Requirements (3rd Edition)*. It scans requirements text, identifies statements that dictate business behavior (rather than software behavior), and classifies them into one of five categories:
1. **Facts:** True statements about the business domain.
2. **Constraints:** Rules that restrict actions.
3. **Action Enablers:** Conditions that trigger actions.
4. **Inferences:** Derived truths based on conditions.
5. **Computations:** Mathematical formulas.

## When
Invoke this skill during requirements analysis, when reviewing user stories, or when reverse-engineering legacy code. Trigger phrases include: "extract business rules," "find the rules in this text," "decouple the logic," or "what are the policies here."

## Where
Applies to User Stories, PRDs, acceptance criteria, and interview transcripts.

## Why
If a user story says, "The system shall charge 7% tax for state residents," the *functional requirement* is to calculate tax. The *business rule* is the 7% rate. If you don't separate them, the developer hardcodes `0.07`, and when the law changes, the code breaks.

## Inputs
- PRDs, User Stories, or transcripts containing business logic.

## Output (Logical Evidence)
- A catalog of extracted Business Rules, tagged by taxonomy type.

## Optimization Readiness
- **Failure Signals**: Software behavior is mistaken for a business rule, implied calculations stay unflagged, taxonomy labels are missing, or the extraction invents policy details.
- **Evidence To Collect**: Rule catalogs, taxonomy assignments, implied-functional-requirement notes, and examples where the extracted rule clearly separated business logic from software behavior.
- **Safe Mutation Boundaries**: Refine extraction prompts, taxonomy guidance, implied-requirement notes, and output formatting without changing the core rule-extraction workflow.
- **Acceptance Criteria**: Accept revisions only if each rule is categorized correctly, no software implementation details leak into the rule list, and uncertain calculations are surfaced as questions.
- **Rejected Revision Handling**: Record implementation-style statements, unsupported rule inferences, and ambiguous taxonomies so they are not repeated.
- **Transfer Check**: Verify the workflow still works for user stories, PRDs, and legacy-code reverse engineering.
- **Stop Rule**: If the input is purely technical or non-functional, stop and redirect before extracting business rules.

## Constraints (Logical Boundaries)
- Business rules are NOT software functions. "The system shall display a warning" is a functional requirement, not a business rule.
- Do not invent rules. If a calculation is implied but not stated, flag it as a question.

## One More Thing
If the input text is purely technical (e.g., "The API must respond in 200ms"), stop and inform the user that these are Non-Functional Requirements, not Business Rules.

## How (Structural Workflow)
### Phase 1: Rule Extraction
1. Read the input text and identify any statements that represent corporate policies, government regulations, industry standards, or mathematical calculations.
2. Extract these statements, separating them from the software features that might implement them.

### Phase 2: Classification
3. Classify each extracted rule into one of the five categories defined in the Business Rules Taxonomy (Fact, Constraint, Action Enabler, Inference, Computation).

### Phase 3: Formatting
4. Output the extracted rules in a structured list or table, including an ID, Type, and the Rule Definition.
5. If a rule implies a functional requirement (e.g., "A user must be 18 to register" implies the system needs to ask for a birthdate), note the implied functional requirement.

## Resources
- [Business Rules Taxonomy](./details/business-rules-taxonomy.md)

## Review In Mind (ReviewInMindGenie)

Execute the common review loop in [review-in-mind](../skill-common/details/review-in-mind.md) before delivering.

Review lens for this skill:
- Is each extracted rule classified correctly (fact/constraint/enabler/inference/computation)?
- Does the rule text preserve the original business intent and scope?
- Are software-implementation details excluded from business rules?

## Validation
1. Verify that no extracted rule dictates a specific software implementation (e.g., "Must use a dropdown" is invalid).
2. Ensure every rule has a defined taxonomy type.
