---
name: create-living-documentation
description: >
  WHEN/WHERE/WHO: [Scheduling: Use when: automating specifications, extracting domain glossaries, generating PlantUML/Graphviz architecture diagrams, or creating BDD reconciliation tests. Applies to: codebase architecture, glossary generators, API schemas, and build validation scripts in the workspace]
  HOW: [Structural: Helps with: establishing a single source of truth, avoiding documentation drift, extracting code metadata via AST/annotations, and validating documentation via unit tests]
  WHY: [Scheduling: Prevents documentation drift by validating specs, glossaries, and diagrams against code.]
---

# Create Living Documentation

## Common Contract (Load First)

When this skill is activated, first load [skill-common](../skill-common/SKILL.md) and apply the shared conventions it defines: canonical section order, frontmatter rules, anti-pattern guidance, and the Review In Mind loop in [review-in-mind](../skill-common/details/review-in-mind.md). This skill adds only domain-specific rules below.

## Who
Architects, system developers, or coding agents who need to automate, extract, and verify architectural diagrams, domain glossaries, and system specifications from the live codebase to eliminate documentation drift.

## What
Analyze source code annotations, package structures, and tests; configure single-source extraction scripts; generate dynamic markdown glossaries and PlantUML/Graphviz system diagrams; and implement automated reconciliation/consistency tests to verify documentation accuracy.

## When
- Triggered by requests like: "create a living glossary from these packages...", "automate system diagrams using PlantUML from source...", "design a reconciliation test for this specification...", "extract living specifications from BDD feature files...", or "generate architecture codex from class annotations...".
- Do not use for writing manual documents, wikis, or PDFs, or documenting legacy systems in place without first checking the [document-legacy-codebase](../document-legacy-codebase) skill.

## Where
Applies to source code directories (Java, Python, C#, etc.), AST parsing scripts, build workflows, and test files in the workspace.

## Why
- Traditional documentation is expensive to maintain, drifts instantly from the code, and loses its credibility.
- Code structures, types, and annotations are rich sources of design intent that the compiler and IDEs understand.
- Living documentation keeps specs, glossaries, and diagrams in lock-step with implementation by verifying them through standard test runners.

## Inputs
- **Codebase Source Path** (required): The folder containing classes, types, and annotations to be documented.
- **Extraction Target** (required): The type of living document to create (e.g., glossary, system diagram, decision log, or contract specifications).
- **Reconciliation Checklists Reference** (required): Located at [reconciliation-checklists](details/reconciliation-checklists.md).
- **Code Examples Reference** (required): Located at [code-examples](details/code-examples.md).
- **Textbook PDF**: Cyrille Martraire's *Living Documentation* book located at [Living Documentation](../TMP/%20Living%20Documentation.pdf).

## Output (Logical Evidence)
- **Living Glossary/Specification**: Dynamically generated Markdown files documenting system terms, roles, and rules.
- **Living Diagram**: Generated SVG/PNG/Text diagrams (PlantUML or Graphviz DOT) rendering class topologies or package relationships.
- **Reconciliation Test Suite**: Automated unit tests (e.g., Python `unittest` or JUnit tests) that assert the consistency of source structures with generated documentation or metadata.

## Optimization Readiness
- **Failure Signals**: Extraction becomes manual copy-paste, documentation drifts from code, reconciliation tests do not fail on mismatches, or the output omits a buildable source-of-truth pipeline.
- **Evidence To Collect**: Generated docs, extraction scripts, reconciliation tests, and examples where source changes did or did not trigger the expected verification failure.
- **Safe Mutation Boundaries**: Refine extraction conventions, diagram-generation guidance, validation scripting, and glossary formatting without changing the core live-extraction and consistency-check workflow.
- **Acceptance Criteria**: Accept revisions only if the generated docs are sourced programmatically, diagrams stay tied to code, and reconciliation tests fail on divergence instead of silently passing.
- **Rejected Revision Handling**: Record hand-transcribed summaries, missing-failure cases, and weak extraction boundaries so they are not repeated.
- **Transfer Check**: Verify the workflow still works for glossary generation, diagram generation, and contract checks across multiple languages or frameworks.
- **Stop Rule**: If the scope, annotations, or output directories are ambiguous, stop and ask before wiring extraction scripts.

## Constraints (Logical Boundaries)
- **Zero Manual Copy-Paste**: Never manually transcribe business properties or structural rules from code to documentation files. All structured summaries must be extracted programmatically.
- **No Silent Extraction Failures**: If an AST parsing script or custom Doclet fails to parse a code file, it must abort the build or fail the test, rather than generating an empty or partial output.
- **Always Test Consistency**: Every living document must be backed by a reconciliation test or contract check that alerts developers of mismatches.

## One More Thing
If target annotations, package names, or document output directories are ambiguous or undefined, stop and ask the user to specify the exact scope before running AST parsers or creating extraction scripts.

---

## How (Structural Workflow)
### Phase 1: Curation & Curation Scoping (Chapter 5)
1. **Identify the Core**: Determine what parts of the system represent the core domain knowledge (e.g., domain models, business policies, external API contracts). Do not waste time extracting boilerplate (e.g., getters/setters, frameworks).
2. **Define Conventions and Annotations**: Select or create clear annotations (e.g., `@Concept`, `@DomainService`, or specific Python decorators) to mark authoritative knowledge in source code. Refer to [reconciliation-checklists](details/reconciliation-checklists.md#section-1-knowledge-curation-checklists) for details.
3. **Plan Guided Tours**: Map out structural entry points (sightseeing maps) to guide new developers through the codebase.

### Phase 2: Automation & Documentation Generation (Chapter 6)
1. **Build a Single-Source Publisher**: Set up code extraction scripts using Python's `ast` module or Java's custom Doclet/annotation processors.
2. **Generate Living Glossaries**: Extract terms, descriptions, and types from docstrings and custom annotations. Format the output as a readable Markdown table or document.
3. **Generate Living Diagrams**: Parse dependency paths, classes, and packages to output PlantUML (`.puml`) or Graphviz (`.dot`) diagrams. Integrate these generations into the build or pre-commit workflow. Refer to templates in [code-examples](details/code-examples.md#section-2-living-diagram-generator-examples).

### Phase 3: Reconciliation & Continuous Verification (Chapter 3)
1. **Implement Reconciliation Tests**: Write unit tests that dynamically parse both the source code and the generated documentation files to assert that every marked entity is documented, and that no outdated entries exist.
2. **Write Published Contract Checks**: For external APIs or database schemas, write verification tests comparing code-declared DTOs/models against the active specification schema. Refer to templates in [code-examples](details/code-examples.md#section-3-reconciliation-test-examples).
3. **Establish Red Flags Checks**: Verify that compilation or test runs fail if any part of the extracted specs deviates from the code.

---

## Resources
- [reconciliation-checklists](details/reconciliation-checklists.md) - Checklists for glossaries, BDD specifications, and diagrams.
- [code-examples](details/code-examples.md) - Parse code scripts, PlantUML templates, and reconciliation test samples.
- [Living Documentation](../TMP/%20Living%20Documentation.pdf) - Original textbook.

---

## Review In Mind (ReviewInMindGenie)

Execute the common review loop in [review-in-mind](../skill-common/details/review-in-mind.md) before delivering.

Review lens for this skill:
- Does each generated artifact trace to real source code or tests rather than assumptions?
- Are extraction scripts and reconciliation tests reproducible and committed with the docs?
- Would stale-documentation drift be detected by the automated checks?

## Validation
1. Verify that the skill configuration matches the `create-living-documentation` folder name.
2. Verify that all relative links to checklists and code examples are valid and clickable.
3. Verify that the generated documentation features a clearly stated generation date or build timestamp, pointing to the source repository.
4. Verify that the reconciliation test suite fails explicitly when a documented code element is modified or removed without updating the corresponding spec rules.
