---
name: design-ddd-aggregates
description: >
  WHEN/WHERE/WHO: Developers, database designers, or agents designing the object-oriented domain layer of a system.
  HOW: Use this SKILL to strictly apply Vaughn Vernon's 4 Rules of Aggregate Design to shape entities and value objects.
  WHY: Most developers build massive "God Objects" (e.g., an Order object containing all OrderItems, Customer details, and Shipping history). This causes concurrency conflicts and unscalable database transactions. Designing small aggregates referenced by ID ensures transactional safety and high performance.
---

# Design DDD Aggregates (Tactical Design)

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

## Validation
1. Verify no Aggregate holds an object reference to another Aggregate.
2. Verify the Aggregate is as small as possible.
3. Verify that any cross-aggregate updates rely on Domain Events and eventual consistency, not massive single transactions.
