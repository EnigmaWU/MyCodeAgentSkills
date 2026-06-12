---
name: define-architectural-drivers
description: >
  WHEN/WHERE/WHO: [Scheduling: System analysts or architects analyzing raw product requirements before design begins.]
  HOW: [Structural: Use this SKILL to extract and formalize unstructured requirements into the four types of architectural drivers.]
  WHY: [Scheduling: Architecture cannot be designed without clear constraints and prioritized quality attribute scenarios.]
---

# Define Architectural Drivers

## Who
System analysts, product owners, and architects. The agent uses this skill to translate business language into architectural constraints.

## What
This skill extracts and formalizes unstructured product requirements into strict Architectural Drivers. It outputs a structured document detailing Design Purpose, Quality Attribute Scenarios, Primary Functionality, and Architectural Concerns.

## When
Invoke this skill at the very beginning of a project, before any architectural design (ADD 3.0) occurs. Trigger phrases include: "extract drivers," "formalize requirements," "write quality attribute scenarios," or "prepare for architecture design."

## Where
Applies to raw Product Requirements Documents (PRDs), user story backlogs, and stakeholder interview transcripts.

## Why
If an architect tries to design a system based purely on "it needs to be fast and secure," the resulting architecture will be flawed. This skill forces those vague requirements into testable Quality Attribute Scenarios (e.g., "Under peak load, 99% of requests complete in <200ms").

## Inputs
- Raw requirements documents (PRD, user stories).
- Business goals.

## Output (Logical Evidence)
- A completed Architectural Drivers Document.

## Constraints (Logical Boundaries)
- Do not invent drivers; infer them only from the provided inputs.
- Quality Attributes must be written as 6-part scenarios (Source, Stimulus, Artifact, Environment, Response, Response Measure).

## One More Thing
If the input lacks sufficient detail to create testable response measures (e.g., "fast"), stop and ask the user to provide specific SLA targets.

## How (Structural Workflow)
### Phase 1: Context Extraction
1. Extract the **Design Purpose**: Why are we designing this architecture? (e.g., greenfield project, extending a legacy system, improving performance).
2. Extract the **Primary Functionality**: Identify the top 3-5 core use cases the system must support.

### Phase 2: Constraint and Concern Identification
3. Identify **Constraints**: List technical, business, and timeline limitations (e.g., "Must use AWS," "Must launch by Q3").
4. Identify **Architectural Concerns**: Note internal technical goals (e.g., "Establish a CI/CD pipeline," "Use microservices").

### Phase 3: Formalizing Quality Attributes
5. Scan for non-functional requirements (speed, safety, uptime, adaptability).
6. Convert vague statements into formal Quality Attribute Scenarios. Each scenario must have a measurable response.

### Phase 4: Prioritization
7. Rank the scenarios and use cases based on business value and architectural risk.

## Resources
- [Driver Extraction Template](./details/driver-extraction-template.md)

## Validation
1. Verify that at least one Quality Attribute Scenario is defined.
2. Ensure that every scenario has a quantifiable "Response Measure".
