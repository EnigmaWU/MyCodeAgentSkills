---
name: elicit-requirements-models
description: >
  WHEN/WHERE/WHO: [Scheduling: Business analysts, agents, or developers reviewing complex user stories or PRDs.]
  HOW: [Structural: Use this SKILL to parse text requirements into Mermaid.js visual models (state/flow diagrams) to identify missing logic.]
  WHY: [Scheduling: Flat text hides missing edge cases and logical dead-ends. Visual modeling exposes these gaps before code is written.]
---

# Elicit Requirements Models

## Who
Business analysts, system architects, developers, and AI agents. The agent uses this skill to critique requirements for completeness.

## What
This skill parses unstructured or flat text requirements and converts them into structured visual models (e.g., State Transition Diagrams, Data Flow Diagrams) using Mermaid.js syntax. It then analyzes the generated model to identify "missing arrows" (unhandled edge cases or missing requirements).

## When
Invoke this skill during the requirements analysis phase, before architectural design or coding begins. Trigger phrases include: "model these requirements," "draw a state diagram for this," "are we missing any edge cases," or "visualize this user story."

## Where
Applies to User Stories, Product Requirements Documents (PRDs), and business rule lists.

## Why
Human language is inherently ambiguous and linear. When describing a system, stakeholders often only describe the "happy path." By forcing text into a strict visual model, dead-ends, unhandled errors, and missing transitions become immediately obvious.

## Inputs
- Raw text requirements or user stories.
- Existing system context (optional).

## Output (Logical Evidence)
- A Mermaid.js diagram block representing the logic.
- A list of "Missing Requirements" discovered by analyzing the model.

## Constraints (Logical Boundaries)
- Do not invent logic to fill gaps; explicitly highlight the gaps as questions for the stakeholder.
- Keep models scoped to the provided text to avoid diagram bloat.

## One More Thing
If the input text is purely cosmetic (e.g., "Change the button to blue") and contains no logic, state, or flow, inform the user that visual modeling is not applicable.

## How (Structural Workflow)
### Phase 1: Model Selection
1. Analyze the text to determine the dominant logic:
   - If it describes an object changing status over time -> **State Transition Diagram**.
   - If it describes a sequence of user/system actions -> **Flowchart / Activity Diagram**.
   - If it describes how the system interacts with external actors -> **Context Diagram**.

### Phase 2: Translation to Visual Model
2. Extract the entities, states, actors, or steps from the text.
3. Draft the model using Mermaid.js syntax.

### Phase 3: Gap Analysis
4. Visually trace the model to find gaps:
   - Are there states with no exit path?
   - Are there decisions (diamonds) with only one outgoing arrow?
   - What happens on failure/timeout at each step?
5. Generate a list of clarifying questions for the missing requirements.

## Resources
- [Mermaid Modeling Templates](./details/mermaid-modeling-templates.md)

## Validation
1. Verify the Mermaid diagram renders correctly without syntax errors.
2. Ensure the gap analysis explicitly references specific missing transitions or unhandled states from the diagram.
