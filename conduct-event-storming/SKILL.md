---
name: conduct-event-storming
description: >
  WHEN/WHERE/WHO: [Scheduling: Architects, domain experts, product owners, or agents analyzing a new business domain or complex workflow.]
  HOW: [Structural: Use this SKILL to facilitate a Big Picture Event Storming session, discovering Domain Events chronologically, and mapping them to Commands, Actors, and Aggregates.]
  WHY: [Scheduling: Traditional requirements gathering focuses on static data, leading to anemic models. Event Storming focuses on behavior to reveal domain boundaries.]
---

# Conduct Event Storming

## Who
Software Architects, Domain Experts, Product Owners, Business Analysts, and AI Agents acting as facilitators. The agent uses this skill to lead a structured exploration of a business domain using the Event Storming format.

## What
Facilitate a "Big Picture" or "Design-Level" Event Storming session. The output is a chronological flow of business events, the triggers that cause them, the actors involved, and the aggregates (state machines) that enforce business rules.

## When
Invoke this skill at the beginning of a project, when reverse-engineering a legacy system, or when tackling a highly complex, poorly understood business workflow. 

Trigger phrases: "Let's event storm this", "Map out the domain events for...", "What are the events in this subdomain?".

## Where
Applies to system design planning, requirements analysis, and domain discovery discussions. The output is typically captured in a Mermaid graph or markdown list.

## Why
Focusing on data structures (ERDs) early leads to tight coupling and "CRUD-heavy" systems. Event Storming forces participants to think in terms of business behavior (verbs) and timelines, uncovering edge cases and natural boundaries (Bounded Contexts) much earlier in the lifecycle.

## Inputs
- **Business Process/Workflow** (required): The domain to explore (e.g., "E-commerce Checkout", "Loan Origination").
- **Known Actors** (optional): Users or external systems interacting with the workflow.

## Output (Logical Evidence)
- A chronological timeline of **Domain Events**, **Commands**, **Actors**, **Policies**, and **Aggregates**.
- A Mermaid.js flowchart visualizing the Event Storming timeline.

## Optimization Readiness
- **Failure Signals**: Events are not written in past tense, triggers are missing, business behavior is replaced by UI or data-model discussion, or the timeline fails to expose boundaries and bottlenecks.
- **Evidence To Collect**: Event timelines, command-event trigger chains, actor assignments, aggregate clusters, and examples of branching or parallel paths that were discovered.
- **Safe Mutation Boundaries**: Refine facilitation prompts, legend guidance, timeline formatting, and aggregate-clustering cues without changing the core events-first exploration model.
- **Acceptance Criteria**: Accept revisions only if the resulting model starts with events, ties each event to a trigger, and identifies aggregates and possible bounded-context boundaries from the timeline.
- **Rejected Revision Handling**: Record “magic” events, non-past-tense labels, and UI-first discussion patterns so they are not repeated.
- **Transfer Check**: Verify the workflow still works for simple business processes and for branching workflows with policies and external systems.
- **Stop Rule**: If the business process is too vague to name events and triggers reliably, stop and ask before mapping the timeline.

## Constraints (Logical Boundaries)
- **RULE 1: Events First.** Always start by identifying Domain Events. Do not discuss UI, databases, or classes until the timeline of events is complete.
- **RULE 2: Past Tense.** Domain Events MUST be written as verbs in the past tense (e.g., `OrderPlaced`, not `PlaceOrder`).
- **RULE 3: Identify Triggers.** Every event must have a trigger: either a user Command, an external system, time passing, or a Policy.

## How (Structural Workflow)
### Phase 1: Chaotic Exploration (Domain Events)
1. Ask the user to list all the things that happen in the business process.
2. Format these as **Domain Events** (Orange sticky notes) written in past tense.
   - *Example:* `ItemAddedToCart`, `PaymentDeclined`, `OrderShipped`.
3. Arrange them in chronological order from left to right.
4. Identify parallel paths, branching logic, and bottlenecks.

### Phase 2: Enforce the Timeline & Triggers
5. For each Domain Event, ask "What caused this?".
6. Identify the **Commands** (Blue sticky notes) that trigger the events.
   - *Example:* `Submit Payment` (Command) -> `PaymentProcessed` (Event).
7. Identify the **Actors** (Yellow sticky notes) who execute the Commands.
   - *Example:* `Customer` (Actor) -> `Submit Payment` (Command).
8. Identify **External Systems** (Pink sticky notes) that trigger events or receive them.
9. Identify **Policies/Read Models** (Lilac/Green sticky notes) where automatic business logic triggers a command based on an event.
   - *Example:* Policy "When `PaymentDeclined`, trigger `SendFailureEmail` command".

### Phase 3: Identify Aggregates (Design-Level)
10. Group the Command and its resulting Event around the data/state it modifies.
11. Label this state machine as the **Aggregate** (Pale Yellow sticky note).
    - *Example:* `Customer` -> `Submit Payment` -> **PaymentTransaction** (Aggregate) -> `PaymentProcessed`.
12. Look for clusters of Aggregates to identify potential Bounded Context Boundaries.

### Phase 4: Output the Model
13. Document the final flow in a structured markdown list, explicitly using the color-coded legend terminology.
14. Optionally generate a Mermaid.js graph to visualize the Actor -> Command -> Aggregate -> Event flow.

## Resources
- [Event Storming Legend](./details/event-storming-legend.md)

## Validation
1. Verify all Domain Events are past tense.
2. Verify no Domain Event happens "by magic" (it must have a Command, Policy, or External System trigger).
3. Verify Aggregates are named as nouns that represent business concepts.
