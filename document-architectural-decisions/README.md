# Document Architectural Decisions

An agent skill for documenting critical software and system architecture decisions. It implements the comprehensive 12-field template from *Documenting Software Architectures: Views and Beyond* by Paul Clements et al., and incorporates Philippe Kruchten's decision ontology.

## What Is This

Decisions shape software systems, but their rationale is often lost. This skill enforces rigorous documentation of the "why" behind system design choice—crucial for teams maintaining complex, long-lived architectures, safety-critical systems, or embedded platforms. 

Instead of simple three-section logs, it uses a detailed 12-field structure and requires analyzing:
- **Alternatives**: Viable choices considered and compared using a pros/cons matrix.
- **Arguments & Tradeoffs**: Economic, technical, and quality-attribute rationales.
- **Implications**: Downstream constraints, requirements changes, or training needs.
- **Kruchten's Ontology**: Defining decision type (Existence, Ban, Property, Executive) and lifecycle state.

## Directory Structure

```text
document-architectural-decisions/
  ├── SKILL.md                                 # Level-1: Main skill workflow (COMPLICATED tier)
  ├── README.md                                # Overview and trigger rules
  └── details/                                 
      └── decision-template-details.md         # Level-3: Markdown templates and classification guide
```

## Why This Method Matters

When designing large software systems:
1. **Traceability**: Decisions are explicitly linked to business requirements (ASRs) and affected software artifacts.
2. **Preventing Rework**: Listing assumptions and alternatives heads off redundant discussions and circular design debates.
3. **High-Stakes Rigor**: Safety-critical systems require clear documentation of *nonexistence decisions* (bans on unsafe libraries or language constructs) and *property decisions* (enforced guidelines).

## Usage

Invoke this skill using trigger phrases such as:
* *"document this design decision"*
* *"write an ADR for [Issue]"*
* *"create a decision record using Views and Beyond"*
* *"log the architectural tradeoffs for [Component]"*

The agent will load the templates in `details/` and compile a validated, structured architectural decision record.
