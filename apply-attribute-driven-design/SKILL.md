---
name: apply-attribute-driven-design
description: >
  WHEN/WHERE/WHO: Software architects or lead developers designing a new feature or greenfield system.
  HOW: Use this SKILL to systematically execute the 7-step ADD 3.0 methodology to map drivers to design patterns.
  WHY: Ensures the architecture handles all constraints and quality attributes instead of just functional requirements.
---

# Apply Attribute-Driven Design (ADD 3.0)

## Who
Software architects, technical leads, and developers responsible for translating requirements into a concrete system design. The agent uses this skill to facilitate structured design iterations.

## What
This skill executes the Attribute-Driven Design (ADD) 3.0 methodology. It produces a documented architectural design by systematically selecting design concepts (patterns/tactics) to satisfy specific architectural drivers.

## When
Invoke this skill after architectural drivers have been defined, and before code implementation begins. Trigger phrases include: "design the architecture," "use ADD 3.0," "create a system design," or "decide on the architecture patterns."

## Where
Applies to technical design documents, ADRs (Architecture Decision Records), and architecture strategy wikis.

## Why
Ad hoc architecture design often ignores non-functional requirements until it's too late. ADD 3.0 enforces a disciplined, iterative approach that guarantees quality attributes (like scalability and security) drive the core structural decisions.

## Inputs
- Architectural Drivers (Use cases, Quality Attribute Scenarios, Constraints).
- Context diagram or system boundaries.

## Output (Logical Evidence)
- Instantiated elements and allocated responsibilities.
- Sketches of architectural views (Logical, Deployment, etc.).
- Recorded design decisions.

## Constraints (Logical Boundaries)
- Do not attempt to design the entire system in one pass; use iterations.
- Base design choices on the drivers, not just preference.

## One More Thing
If the input architectural drivers are missing or vague, stop and ask the user to clarify them before proceeding with the design.

## How (Structural Workflow)
### Phase 1: Preparation
1. **Review Inputs:** Ensure the architectural drivers are prioritized.
2. **Establish the Iteration Goal:** Select a subset of drivers to focus on for this iteration.

### Phase 2: Design and Allocation
3. **Choose Elements to Refine:** Pick the system or sub-system to focus on.
4. **Choose Design Concepts:** Select Reference Architectures, Deployment Patterns, or Tactics that satisfy the selected drivers.
5. **Instantiate and Allocate:** Map the design concepts to concrete elements. Define their responsibilities and how they interface.

### Phase 3: Documentation and Analysis
6. **Sketch Views & Record Decisions:** Create preliminary diagrams and write ADRs for the choices made.
7. **Perform Analysis:** Review the iteration. Did it meet the goal? If not, iterate again.

## Resources
- [ADD 3.0 Checklist](./details/add-3-0-checklist.md)

## Validation
1. Verify that every selected design concept traces back to a specific architectural driver.
2. Ensure interfaces and responsibilities are clearly allocated.
3. Confirm that the iteration goal was met before concluding the skill.
