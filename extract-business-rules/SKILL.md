---
name: extract-business-rules
description: >
  WHEN/WHERE/WHO: Business analysts or agents reviewing user stories or PRDs that contain embedded business logic.
  HOW: Use this SKILL to extract policies, laws, and calculations from text and categorize them into a strict Business Rules Taxonomy.
  WHY: Business rules change more frequently than software. Hardcoding a rule as a "feature" creates legacy debt. Separating rules allows for dynamic configuration or rules-engine implementation.
---

# Extract Business Rules

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

## Output
- A catalog of extracted Business Rules, tagged by taxonomy type.

## Constraints
- Business rules are NOT software functions. "The system shall display a warning" is a functional requirement, not a business rule.
- Do not invent rules. If a calculation is implied but not stated, flag it as a question.

## One More Thing
If the input text is purely technical (e.g., "The API must respond in 200ms"), stop and inform the user that these are Non-Functional Requirements, not Business Rules.

## How

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

## Validation
1. Verify that no extracted rule dictates a specific software implementation (e.g., "Must use a dropdown" is invalid).
2. Ensure every rule has a defined taxonomy type.
