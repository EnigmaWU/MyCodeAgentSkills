---
name: define-bounded-contexts
description: >
  WHEN/WHERE/WHO: [Scheduling: Software architects, domain experts, or agents splitting a monolith or designing a microservices architecture.]
  HOW: [Structural: Use this SKILL to partition the system into Subdomains and map the integration contracts using Context Mapping patterns.]
  WHY: [Scheduling: Explicitly defining Bounded Contexts prevents big balls of mud caused by ambiguous terminology across domains.]
---

# Define Bounded Contexts (Strategic Design)

## Who
Software Architects, Domain Experts, and AI Agents acting as architectural consultants.

## What
Execute the Strategic Design phase of Domain-Driven Design (DDD). The output is a categorization of the problem space into Subdomains, and the solution space into Bounded Contexts with explicitly defined relationships (Context Maps).

## When
Invoke this skill when breaking down a monolith, defining microservice boundaries, deciding whether to build vs. buy, or integrating with legacy/external systems.

Trigger phrases: "Define bounded contexts for...", "How should we split these microservices?", "Map the subdomains".

## Where
Applies to system architecture documents, RFCs, and integration specifications.

## Why
A unified data model spanning the entire enterprise always fails. Words are ambiguous (e.g., "Customer" means a lead to Marketing, but a ledger account to Billing). Bounded Contexts provide explicit linguistic boundaries where a domain model has strict, unambiguous meaning (the Ubiquitous Language).

## Inputs
- **Business Domain** (required): The overarching business area to analyze.
- **Identified Aggregates/Events** (optional): Output from Event Storming if available.

## Output (Logical Evidence)
- **Subdomain Categorization**: Core, Supporting, and Generic subdomains.
- **Bounded Context Map**: Explicit boundaries and their integration patterns (ACL, OHS, Conformist, etc.).

## Constraints (Logical Boundaries)
- **RULE 1: Linguistic Boundary.** A Bounded Context is a linguistic boundary. A model inside one context must not be corrupted by concepts from outside.
- **RULE 2: Core Domain Focus.** The Core Domain is where the business makes its money. It must be built in-house. Generic subdomains (like Identity or Invoicing) should be outsourced or bought if possible.
- **RULE 3: Text-First Execution.** The workflow must be executable from natural-language context definitions even without diagram tooling.
- **RULE 4: Diagram Optionality.** Context maps may be represented as structured text tables when Mermaid output is unavailable.

## How (Structural Workflow)
### Phase 1: Problem Space (Subdomains)
1. Analyze the overarching business domain and break it into sub-parts.
2. Classify each part into one of three Subdomains:
   - **Core Subdomain:** The secret sauce. What makes the business unique. (Must build in-house, highest quality).
   - **Supporting Subdomain:** Necessary for the business, but not a competitive advantage. (Build in-house, but don't over-engineer).
   - **Generic Subdomain:** Problems that every business has. (Buy off-the-shelf or use open-source: e.g., Auth, Payments).

### Phase 2: Solution Space (Bounded Contexts)
3. Define the **Bounded Contexts** that will implement these subdomains. (Ideally, 1:1 mapping, but legacy systems often span multiple).
4. Define the **Ubiquitous Language** for each context. Explicitly state how concepts differ between contexts (e.g., Context A: `User(id, email)` vs. Context B: `Customer(id, credit_score)`).

### Phase 3: Context Mapping (Integration)
5. Identify where Bounded Contexts need to share data or trigger actions.
6. For each integration point, explicitly assign a **Context Mapping Pattern** from the list below:
   - **Anti-Corruption Layer (ACL):** The downstream context translates the upstream model to protect itself.
   - **Open Host Service (OHS) / Published Language (PL):** The upstream context provides a stable, public API meant for multiple consumers.
   - **Conformist:** The downstream context blindly accepts the upstream model (often used when upstream has no incentive to change).
   - **Partnership / Shared Kernel:** Teams cooperate closely or share a common code library (use sparingly).

### Phase 4: Output the Map
7. Document the Subdomains and Context Map.
8. Optionally generate a Mermaid.js diagram illustrating the contexts, data flow direction (U = Upstream, D = Downstream), and the mapping patterns applied.

## Resources
- [Context Mapping Patterns](./details/context-mapping-patterns.md)

## Validation
1. Verify that no single model (e.g., a massive `User` object) spans multiple contexts.
2. Verify that every integration line specifies an Upstream (U) and Downstream (D) relationship, along with a specific integration pattern (e.g., ACL, OHS).
