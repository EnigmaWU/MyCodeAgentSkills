---
name: create-ecosystem-map
description: >
  WHEN/WHERE/WHO: System architects, analysts, or agents defining the scope of a new project.
  HOW: Use this SKILL to extract all upstream and downstream systems from text and render them as a Mermaid.js graph.
  WHY: Failing to identify an integration point early leads to massive architectural rework later. Ecosystem maps define the exact boundary.
---

# Create Ecosystem Map

## Who
System Architects, Business Analysts, and AI Agents. The agent uses this skill to map dependencies and boundaries.

## What
This skill implements the Ecosystem Map from the Requirements Modeling Language (RML). It analyzes requirements text to identify the System Under Design (SUD) and every external system, API, or human actor it interacts with. It outputs a Mermaid.js graph visualizing these relationships.

## When
Invoke this skill during scope definition or early architectural design. Trigger phrases include: "create an ecosystem map," "what systems does this touch," "map the dependencies," or "draw a context diagram."

## Where
Applies to Product Requirements Documents (PRDs), architectural design docs, and system integration plans.

## Why
When teams focus only on the features they are building, they forget the systems they must integrate with. An Ecosystem Map forces the team to acknowledge (and plan for) every data feed, legacy database, and third-party API that touches their system.

## Inputs
- Requirements documents, PRDs, or architecture descriptions.

## Output (Logical Evidence)
- A Mermaid.js graph diagram (Ecosystem Map).
- A list of defined interfaces.

## Constraints (Logical Boundaries)
- Do not map the internal components of the System Under Design. The SUD is a black box in this model. Only map *external* interactions.
- Differentiate between human actors and software systems.

## One More Thing
If the input text describes a purely standalone script with no external inputs or outputs, inform the user that an Ecosystem Map is trivial and unnecessary.

## How (Structural Workflow)
### Phase 1: Identify the Center
1. Identify the **System Under Design (SUD)**. This is the application or service being built or modified. It goes in the center of the map.

### Phase 2: Identify Externals
2. Scan the text for nouns representing external entities:
   - **Upstream Systems:** Systems that send data *to* the SUD.
   - **Downstream Systems:** Systems that receive data *from* the SUD.
   - **Human Actors:** User classes that interact directly with the SUD.

### Phase 3: Define Interfaces
3. For every connection between the SUD and an external entity, define the nature of the data flowing across it (e.g., "Sends Order Data", "Returns Auth Token").

### Phase 4: Visualization
4. Output the map using Mermaid.js `graph` or `flowchart` syntax.

## Resources
- [Ecosystem Map Template](./details/ecosystem-map-template.md)

## Validation
1. Verify the Mermaid syntax is valid.
2. Ensure the SUD is treated as a black box (no internal modules are shown).
3. Ensure every arrow has a label describing the data/interaction.
