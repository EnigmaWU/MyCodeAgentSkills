# Aggregate Design Rules

An Aggregate is a cluster of domain objects that can be treated as a single unit for data changes. Every Aggregate has a root and a boundary. The boundary defines what is inside the Aggregate. The root is a single, specific Entity contained in the Aggregate.

When designing or reviewing Aggregates, enforce these four strict rules defined by Vaughn Vernon in *Implementing Domain-Driven Design*.

## Rule 1: Model True Invariants in Consistency Boundaries
A **True Invariant** is a business rule that must *always* be consistent.
* If Rule A states "An order must not exceed $10,000", then the Order and its OrderItems must be updated in the exact same database transaction. Therefore, `OrderItem` belongs inside the `Order` aggregate.
* Do not put entities in the same aggregate just for convenience. Only put them together if they must be strongly consistent.

## Rule 2: Design Small Aggregates
Large aggregates degrade performance and scalability.
* If multiple users try to update different parts of a massive "God Object" (e.g., `User` aggregate containing `Profile`, `Posts`, `Comments`), they will constantly hit optimistic concurrency exceptions or database locks.
* Keep aggregates as small as possible. If an entity does not participate in a true invariant with the root, kick it out and make it its own Aggregate Root.
* *Hint:* Many aggregates consist of only a single Entity and a few Value Objects.

## Rule 3: Reference Other Aggregates by Identity
Do not use object references (pointers) between aggregates.
* **BAD:** `Order` contains a reference to `Customer customer;`
* **GOOD:** `Order` contains a reference to `String customerId;`
* **Why:** Object references encourage developers to modify the external aggregate from within the current one (e.g., `order.getCustomer().setStatus("VIP")`), completely violating transaction boundaries and loading massive object graphs into memory.

## Rule 4: Use Eventual Consistency Outside the Boundary
If executing a command on Aggregate A requires a state change in Aggregate B, do not update both in the same transaction.
* **BAD:** A database transaction that updates `Order` and `Customer` simultaneously.
* **GOOD:** `Order` updates itself and publishes an `OrderCreated` Domain Event. A separate event handler listens to `OrderCreated` and updates the `Customer` aggregate in a completely separate database transaction.
* **Why:** This ensures high availability and scalability. If the `Customer` database is temporarily slow, the `Order` still succeeds.
