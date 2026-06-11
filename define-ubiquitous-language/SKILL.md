---
name: define-ubiquitous-language
description: >
  WHEN/WHERE/WHO: Domain experts, developers, or agents analyzing raw business requirements.
  HOW: Use this SKILL to extract a strict Ubiquitous Language glossary for a specific Bounded Context. Reject synonyms, define exact semantics, and enforce these terms in all code, tests, and documentation.
  WHY: Ambiguous terminology causes translation costs and bugs. If the business says "Guest" but the code says "Visitor", the mental model breaks. The Ubiquitous Language ensures developers and domain experts speak the exact same language.
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

## Output
- A strict **Ubiquitous Language Glossary** mapping Terms to Definitions.
- A list of **Rejected Terms** (synonyms that must not be used).

## Constraints
- **RULE 1: One Meaning Per Context.** Inside a single Bounded Context, a term can have only one meaning. If a term means two different things, you have missed a Bounded Context boundary.
- **RULE 2: No Synonyms.** If "User", "Client", and "Account" all mean the same thing, pick ONE. The others must be actively rejected.
- **RULE 3: Code Must Match.** The exact terms defined in the Ubiquitous Language must be used to name classes, methods, variables, and database tables.

## How

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
