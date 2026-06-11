---
name: apply-oopsi-model
description: >
  WHEN/WHERE/WHO: Business analysts, testers, or agents exploring user journeys or data workflows.
  HOW: Use this SKILL to work backward from the business Outcome, to tangible Outputs, to the Process, down to Scenarios and exact Inputs.
  WHY: Starting with inputs ("When I type 'admin'...") obscures the business goal. Starting with the Outcome ("I want to book a flight") guarantees alignment before writing granular tests.
---

# Apply OOPSI Model

## Who
Business Analysts, Testers, Developers, and AI Agents. The agent uses this skill to deconstruct complex workflows systematically.

## What
This skill implements the OOPSI model (Outcome, Outputs, Process, Scenarios, Inputs). It is a reverse-engineering approach to requirements discovery:
1. **Outcome:** What is the high-level business goal?
2. **Outputs:** What tangible artifacts or system state changes prove the outcome was achieved?
3. **Process:** What steps must be taken to generate those outputs?
4. **Scenarios:** What are the edge cases, business rules, or alternative flows in that process?
5. **Inputs:** What exact data is required to trigger those scenarios?

## When
Invoke this skill when exploring a new Epic, User Story, or complex data flow. Trigger phrases include: "use OOPSI," "work backward from the outcome," "what are the outputs of this feature," or "deconstruct this workflow."

## Where
Applies to Backlog Refinement, Three Amigos sessions, and test planning.

## Why
When teams start by defining inputs (e.g., "Given a user with ID 1234"), they often get bogged down in technical setup and lose sight of the business value. By starting at the Outcome, the team aligns on *why* they are doing the work, and the Inputs become merely the data required to prove the Outcome.

## Inputs
- A User Story, Epic, or high-level feature description.

## Output
- A completed OOPSI framework document.

## Constraints
- Outputs must be tangible and verifiable (e.g., "A confirmation email is sent," "Database record is updated"). "The user feels happy" is an Outcome, not an Output.
- Inputs should be specific data values required to execute the Scenarios.

## One More Thing
If the input text is a non-functional requirement (e.g., "System must support 1000 TPS"), stop and inform the user that OOPSI is designed for functional workflows and data processing.

## How

### Phase 1: Define Outcome and Outputs
1. Identify the **Outcome** (the business goal of the feature).
2. List the tangible **Outputs** that result from a successful (or failed) execution of this feature.

### Phase 2: Map the Process
3. Outline the **Process**—the high-level steps or workflow required to get from start to finish.

### Phase 3: Identify Scenarios
4. Brainstorm the **Scenarios**—what are the different paths through the process? What are the edge cases or business rules?

### Phase 4: Specify Inputs
5. For each scenario, define the exact **Inputs** (data tables, API payloads, or preconditions) needed to trigger that scenario.

## Resources
- [OOPSI Framework](./details/oopsi-framework.md)

## Validation
1. Verify that every Scenario maps to at least one Output.
2. Verify that the Inputs provide enough data to execute the Process.
