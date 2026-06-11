# Context Mapping Patterns

When integrating Bounded Contexts, you must define the relationship. It is rarely a relationship between equals; usually, there is an **Upstream (U)** context (the source of truth) and a **Downstream (D)** context (the consumer).

Use these standard DDD patterns to describe how the models interact.

## 1. Anti-Corruption Layer (ACL)
**Type:** Downstream protection.
The downstream team builds a strict translation layer to isolate their clean domain model from the messy or legacy upstream model.
* **When to use:** When the upstream model is poorly designed, legacy, or highly unstable, and the downstream is a Core Subdomain that must remain pure.
* **Cost:** High (requires building and maintaining translation logic).

## 2. Open Host Service (OHS) / Published Language (PL)
**Type:** Upstream accommodation.
The upstream team creates a well-documented, standardized, and versioned public API (the Published Language) specifically designed for external consumers, protecting its internal model from being exposed.
* **When to use:** When the upstream context has many downstream consumers (e.g., Stripe, Twilio).
* **Cost:** High for upstream (requires maintaining backwards compatibility and versioning).

## 3. Conformist
**Type:** Downstream submission.
The downstream team completely abandons their own domain model and blindly adopts the upstream model exactly as it is.
* **When to use:** When the upstream team provides no OHS, has zero incentive to cooperate, and building an ACL is too expensive. (e.g., integrating with a rigid third-party API where you just use their exact JSON structure in your code).

## 4. Partnership
**Type:** Symmetric cooperation.
Two teams coordinate their release schedules and closely align their models. If one fails, they both fail.
* **When to use:** Only when two contexts are highly dependent on each other and the teams have excellent communication. Often a smell of tight coupling.

## 5. Shared Kernel
**Type:** Shared ownership.
Two or more teams share a small, specific subset of the domain model (e.g., a shared code library or database table).
* **When to use:** When duplication is too costly. It requires CI/CD and strict agreement because any change to the kernel affects all consumers.

## 6. Separate Ways
**Type:** No integration.
The teams decide that the cost of integration is higher than the value it provides. They build duplicate functionality independently.
* **When to use:** When integration brings little value or when dealing with Generic subdomains where off-the-shelf solutions are cheap.
