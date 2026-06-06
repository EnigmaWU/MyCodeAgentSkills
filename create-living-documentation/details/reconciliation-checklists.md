# Reconciliation and Living Documentation Checklists

This document provides checklists for developers and coding agents to curate, automate, and verify living documentation assets.

---

## Section 1: Knowledge Curation Checklists

Dynamic curation involves identifying and highlighting the most important parts of a system while ignoring noise. Use these checkpoints:

- [ ] **Identify the Authoritative Source**: Determine where each piece of information naturally originates.
  * *Code as Authoritative*: Business rules, math calculations, data mappings, type models.
  * *Database Schema as Authoritative*: Database constraints, columns, relational mappings.
  * *Feature Files as Authoritative*: Acceptance criteria, business behavior flows.
  * *Decision Logs as Authoritative*: Structural architecture history, technology choices.
- [ ] **Establish Custom Annotations**: Mark code semantics explicitly when the programming language types are insufficient.
  * Define annotations (e.g., `@Concept`, `@DomainEntity`, `@Policy`) to decorate classes, methods, or packages.
  * Ensure the package name of custom annotations reflects their domain intent (e.g., `com.company.domain.annotations`).
- [ ] **Define Metadata Conventions**: If annotations are not used, establish strict structural patterns.
  * *Naming Conventions*: Suffixing classes with `Policy`, `Validator`, or `Event`.
  * *Directory Conventions*: Keeping all domain logic in a `domain/` directory, separated from `infrastructure/`.
- [ ] **Create Sightseeing Maps**:
  * Write a brief introduction listing the entry point classes or modules.
  * Explain the system metaphors used to represent components (e.g., "The system acts as a conveyor belt...").

---

## Section 2: Living Glossary Checklists

A Living Glossary extracts terms, synonyms, descriptions, and types from source code comments or annotations.

- [ ] **Select Extraction Targets**:
  * Scan only files decorated with core domain annotations (`@Concept`, `@ValueObject`) or matching package namespaces.
  * Filter out framework configurations, utilities, test suites, and boilerplate code (e.g., setters, getters).
- [ ] **Define Term Extraction Rules**:
  * Class names are mapped to term names.
  * Docstrings (Javadoc, docstrings in Python) are parsed for term descriptions.
  * Class attributes represent term properties and relationships.
- [ ] **Segment by Bounded Context**:
  * Group glossary terms by their domain namespace or package.
  * Document conflicting definitions when a single word has different meanings across contexts (e.g., "Account" in Sales vs. Billing).
- [ ] **Output Format & Accessibility**:
  * Generate readable Markdown files.
  * Include a title, descriptive header, and a clear auto-generation timestamp.
  * Embed links back to the source files if the environment supports them.

---

## Section 3: Living Diagram Checklists

Living diagrams are generated dynamically from code structures, ensuring that system boundaries and connections represent reality.

- [ ] **Determine the Narrative ("One Diagram, One Story")**:
  * Do not try to show everything on a single diagram. Decide on a focus (e.g., Hexagonal Architecture ports/adapters, Microservices landscape, or Core Domain interactions).
- [ ] **Scan Relationships**:
  * Identify module imports, class dependencies, interface implementations, and event subscribers.
  * Map these relationships into node connections (e.g., arrows indicating dependency directions).
- [ ] **Generate Visual Syntax**:
  * Output diagrams using high-level text formats (PlantUML `.puml` or Graphviz DOT `.dot`).
  * Apply consistent styling (e.g., clean gray/blue boxes, distinct line styles for sync vs. async calls).
- [ ] **Keep Diagrams Honest**:
  * Ensure diagrams are rebuilt automatically during compilation or CI pipelines.
  * Check for "architectural drift" (e.g., adapter packages importing from each other directly without going through ports). Raise warnings if constraints are breached.

---

## Section 4: BDD & BDD Reconciliation Checklists

Behavior-Driven Development (BDD) links customer scenarios to automated tests. Use these checkpoints:

- [ ] **Write Intent-Revealing Scenario Files**:
  * Feature files (`.feature` written in Gherkin) must describe business behaviors and requirements, not UI details (e.g., use "Given the client has $100" instead of "Given the user clicks the login input").
- [ ] **Verify Step Mappings**:
  * Enforce that every step definition is mapped to code actions.
  * Check for unused steps (dead specs) or unimplemented steps (empty definitions).
- [ ] **Reconcile Feature Specifications**:
  * Ensure that the scenario files are processed by standard test runners (e.g., Cucumber, Behave).
  * Automatically fail the test execution or build phase if any test assertions fail.
- [ ] **Publish Scenario Digests**:
  * Generate clean HTML/Markdown reports summarizing which features passed, failed, or were skipped.
  * Distribute these digests to domain experts and product managers.
