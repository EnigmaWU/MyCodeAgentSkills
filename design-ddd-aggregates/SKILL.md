---
name: design-ddd-aggregates
description: >
  WHEN/WHERE/WHO: [Scheduling: Developers, database designers, or agents designing the object-oriented domain layer of a system.]
  HOW: [Structural: Use this SKILL to strictly apply Vaughn Vernon's 4 Rules of Aggregate Design to shape entities and value objects.]
  WHY: [Scheduling: Designing small aggregates referenced by ID ensures transactional safety and high performance, preventing massive God Objects.]
---

# Design DDD Aggregates (Tactical Design)

## Common Contract (Load First)

When this skill is activated, first load [skill-common](../skill-common/SKILL.md) and apply the shared conventions it defines: canonical section order, frontmatter rules, anti-pattern guidance, and the Review In Mind loop in [review-in-mind](../skill-common/details/review-in-mind.md). This skill adds only domain-specific rules below.

## Who
Developers, Backend Engineers, and AI Agents designing the persistence layer and domain entities of an application.

## What
Apply the strict Tactical Design rules of Domain-Driven Design (DDD) to group Entities and Value Objects into consistency boundaries called **Aggregates**, governed by an **Aggregate Root**.

## When
Invoke this skill when designing database schemas, ORM mappings, or object-oriented domain classes. 

Trigger phrases: "Design the aggregates for...", "Review this domain model for DDD compliance", "Refactor this entity into an aggregate".

## Where
Applies to backend codebases, domain models, entity definitions, and database schema designs.

## Why
Without strict rules, object graphs grow infinitely. If `Order` has a list of `OrderItems`, and `OrderItem` has a reference to `Product`, and `Product` has a reference to `Category`... loading an `Order` might pull half the database into memory. Furthermore, if two users edit the same massive object graph, transaction locks cause performance bottlenecks. Aggregates act as strict transaction boundaries to solve this.

## Inputs
- **Proposed Entities/Data Model** (required): The nouns in the system (e.g., User, Post, Comment).
- **Business Rules/Invariants** (required): The rules that must *always* be true (e.g., "A post cannot have more than 100 comments").

## Output (Logical Evidence)
- A refined domain model with clear boundaries between **Aggregate Roots**, **Entities**, and **Value Objects**.
- Adherence to the 4 rules of Aggregate Design.

## Optimization Readiness
- **Failure Signals**: Aggregates are too large, cross-aggregate object references remain, invariants are diluted, or eventual consistency is ignored in favor of giant transactions.
- **Evidence To Collect**: Proposed aggregates, invariant lists, identity references, domain events, and examples where shrinking the aggregate reduced coupling.
- **Safe Mutation Boundaries**: Refine invariant-hunting prompts, aggregate-shrinking guidance, identity-reference rules, and event-planning cues without changing the core aggregate design constraints.
- **Acceptance Criteria**: Accept revisions only if every aggregate is small, invariants are explicit, cross-aggregate references use IDs, and cross-boundary updates rely on events.
- **Rejected Revision Handling**: Record object-graph sprawl, direct aggregate references, and monolithic transaction patterns so they are not repeated.
- **Transfer Check**: Verify the workflow still works for entity-heavy domains and for systems that require eventual consistency across multiple aggregates.
- **Stop Rule**: If the proposed entities or invariants are unclear, stop and ask before shaping aggregates.

## Constraints (Logical Boundaries)
- **RULE 1: Model True Invariants.** An aggregate is a transaction boundary. Only data that must be strictly, transactionally consistent at the exact same millisecond should be inside the same aggregate.
- **RULE 2: Design Small Aggregates.** An aggregate should contain only the Root Entity and the minimal number of nested Entities/Value Objects needed to enforce the invariants.
- **RULE 3: Reference by Identity.** Aggregates must NOT hold object references (pointers) to other aggregates. They must only hold the ID (String/UUID) of the other aggregate.
- **RULE 4: Eventual Consistency.** If modifying Aggregate A requires modifying Aggregate B, do not update both in the same database transaction. Aggregate A must publish a Domain Event, which Aggregate B listens to and updates itself in a separate transaction.

## How (Structural Workflow)
### Phase 1: Identify the Root and Invariants
1. Analyze the proposed data model and business rules.
2. Identify the **Aggregate Root** (the primary entity that external objects interact with).
3. Identify the **True Invariants** (business rules that cannot be violated, even for a millisecond).

### Phase 2: Shrink the Aggregate
4. Remove any nested entities that do not strictly participate in the invariants.
5. Convert nested entities into **Value Objects** if they have no identity and are entirely replaceable.

### Phase 3: Enforce Identity References
6. Scan the Aggregate's properties.
7. If the Aggregate holds a reference to another Aggregate Root (e.g., `Order` contains a `Customer` object), replace it with a reference by identity (e.g., `Order` contains a `customerId` string).

### Phase 4: Plan Eventual Consistency
8. Review workflows that span multiple Aggregates.
9. Design the **Domain Events** (e.g., `OrderPlaced`) that the primary Aggregate will publish.
10. Design the listeners/policies on the other Aggregates that will react to these events.

## Resources
- [Aggregate Design Rules](./details/aggregate-design-rules.md)

## Review In Mind (ReviewInMindGenie)

Execute the common review loop in [review-in-mind](../skill-common/details/review-in-mind.md) before delivering.

Review lens for this skill:
- Does each aggregate enforce its invariants through a single root, with entities/value objects inside?
- Are references between aggregates by ID only, with explicit consistency boundaries?
- Are oversized aggregates split and transient objects excluded?

## Validation
1. Verify no Aggregate holds an object reference to another Aggregate.
2. Verify the Aggregate is as small as possible.
3. Verify that any cross-aggregate updates rely on Domain Events and eventual consistency, not massive single transactions.
