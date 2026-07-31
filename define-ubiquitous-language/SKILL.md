---
name: define-ubiquitous-language
description: >
  WHEN/WHERE/WHO: [Scheduling: Domain experts, developers, or agents analyzing raw business requirements.]
  HOW: [Structural: Use this SKILL to extract a strict Ubiquitous Language glossary for a specific Bounded Context. Reject synonyms, define exact semantics.]
  WHY: [Scheduling: Ambiguous terminology causes translation costs and bugs. The Ubiquitous Language ensures developers and business speak the exact same language.]
---

# Define Ubiquitous Language (Strategic Design)

## Who
Domain Experts, Developers, Product Owners, and AI Agents acting as domain modelers.

## What
Extract, define, and enforce the **Ubiquitous Language** for a specific Bounded Context. The output is a strict glossary where each term has exactly one meaning, and synonyms are explicitly rejected.

## When
Invoke this skill at the beginning of a project, during Event Storming, when reviewing requirements, or when refactoring a legacy codebase to align with the business domain.

Trigger phrases: "Define the ubiquitous language for...", "Extract the glossary", "What is the domain language here?".

## Where
Applies to domain glossaries, requirements documents, and directly naming variables/classes in source code.

## Why
In Domain-Driven Design (DDD), the most critical failure point is the translation gap between business experts and developers. If the business calls it a "Policy" but the code calls it a "Contract", cognitive load increases and bugs occur. The Ubiquitous Language eliminates translations: the language spoken by the business *is* the language written in the code.

## Inputs
- **Raw Business Documents** (required): User stories, meeting transcripts, PRDs, or Event Storming outputs.
- **Target Bounded Context** (required): The linguistic boundary. (e.g., "Billing Context" vs "Shipping Context").

## Output (Logical Evidence)
- A strict **Ubiquitous Language Glossary** mapping Terms to Definitions.
- A list of **Rejected Terms** (synonyms that must not be used).

## Optimization Readiness
- **Failure Signals**: Synonyms remain unresolved, approved terms overlap in meaning, definitions drift outside the target context, or code-facing terms no longer match the business language.
- **Evidence To Collect**: Extracted noun and verb candidates, glossary drafts, rejected-term lists, and examples of terminology conflicts found in code or documents.
- **Safe Mutation Boundaries**: Refine elicitation prompts, glossary formatting, synonym-resolution guidance, and validation examples without changing the core one-term-one-meaning rule inside a bounded context.
- **Acceptance Criteria**: Accept revisions only if the glossary defines distinct approved terms, rejects conflicting synonyms, and keeps the language aligned with the specified bounded context.
- **Rejected Revision Handling**: Record discarded synonyms, ambiguous definitions, and context-crossing term usages so they are not reintroduced.
- **Transfer Check**: Verify the workflow still works for both greenfield glossary creation and cleanup of an already drifting vocabulary.
- **Stop Rule**: If the target context is not clearly defined, stop and ask before standardizing terms that may belong to multiple contexts.

## Constraints (Logical Boundaries)
- **RULE 1: One Meaning Per Context.** Inside a single Bounded Context, a term can have only one meaning. If a term means two different things, you have missed a Bounded Context boundary.
- **RULE 2: No Synonyms.** If "User", "Client", and "Account" all mean the same thing, pick ONE. The others must be actively rejected.
- **RULE 3: Code Must Match.** The exact terms defined in the Ubiquitous Language must be used to name classes, methods, variables, and database tables.

## How (Structural Workflow)
### Phase 1: Elicitation
1. Read the provided raw business documents or Event Storming outputs.
2. Highlight all the **Nouns** (entities, value objects, actors) and **Verbs** (commands, domain events, processes).

### Phase 2: Distillation
3. Identify synonyms (e.g., `Make Payment`, `Process Payment`, `Pay`).
4. Force a decision on the single canonical term to be used in the Ubiquitous Language.
5. Move the remaining synonyms to a "Rejected Terms" list.

### Phase 3: Definition
6. For each accepted term, write a crisp, business-focused definition.
7. Ensure the definition makes sense *only* within the specified Bounded Context (e.g., A "Product" in the Inventory context is defined by its physical weight and dimensions; in the Sales context, it is defined by its price and marketing copy).

### Phase 4: Output the Glossary
8. Format the output as a Markdown table or list.
9. Include three sections:
   - **Context:** The Bounded Context this language applies to.
   - **Ubiquitous Language:** The approved terms (Nouns and Verbs) and their definitions.
   - **Rejected Terms:** The synonyms that developers must NOT use in this context.

## Resources
- [Eric Evans - Domain-Driven Design Reference](https://www.domainlanguage.com/ddd/reference/)

## Validation
1. Verify no two approved terms have the exact same definition.
2. Verify that rejected synonyms are explicitly listed to prevent developers from accidentally using them.
3. Verify that the terms are specific to a single Bounded Context.
