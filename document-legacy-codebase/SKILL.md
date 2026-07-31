---
name: document-legacy-codebase
description: >
  WHEN/WHERE/WHO: [Scheduling: Use when: reverse-engineering brownfield systems, mapping legacy code structures, establishing bubble context boundaries, or applying strangler migration patterns. Applies to: legacy libraries, brownfield codebases, boundary interfaces, and migration configurations in the workspace]
  HOW: [Structural: Helps with: extracting fossilized knowledge, superimposing metadata structures via sidecars/decorators, wrapping legacy code in anticontamination layers, and marking deprecated code]
  WHY: [Scheduling: Provides structured workflow execution to prevent errors and ensure standards.]
---

# Document Legacy Codebase

## Who
Architects, system developers, or coding agents who need to analyze, document, isolate, and gradually replace legacy or brownfield codebases without causing regressions.

## What
Perform software archaeology to extract mental models and data flows; define clean boundary interfaces (Bubble Contexts); superimpose external metadata structures (decorators, sidecar files, registries) to document legacy behaviors; and apply strangler patterns with biodegradable annotations to schedule system retirement.

## When
- Triggered by requests like: "document this legacy codebase to map its structures...", "establish a bubble context around this module...", "apply a strangler pattern boundary for migration...", "superimpose a metadata structure on this legacy code...", or "perform software archaeology on this brownfield module...".
- Do not use for documenting brand-new architectures, or greenfield codebases where you should directly apply the [create-living-documentation](../create-living-documentation) skill.

## Where
Applies to legacy directories, brownfield code files, integration APIs, database structures, and boundary adapters in the workspace.

## Why
- Legacy code represents fossilized business knowledge that is often untested and fragile.
- Directly editing legacy code to add documentation or refactor it in place runs an extremely high risk of regression bugs.
- Establishing external metadata layers (superimposed structures) and wrapper boundaries (bubble contexts) allows teams to understand and evolve the system safely.

## Inputs
- **Legacy Source Path** (required): The folder containing legacy/brownfield classes and modules to analyze.
- **Migration Strategy** (optional): The target replacement goal (e.g., Strangler pattern, complete retirement, or bubble context integration).
- **Legacy Checklists Reference** (required): Located at [legacy-checklists.md](details/legacy-checklists.md).
- **Code Examples Reference** (required): Located at [code-examples.md](details/code-examples.md).
- **Textbook PDF**: Cyrille Martraire's *Living Documentation* book located at [ Living Documentation.pdf](../TMP/%20Living%20Documentation.pdf).

## Output (Logical Evidence)
- **Software Archaeology Assessment**: Documentation mapping data flows, critical legacy classes, and known risks.
- **Bubble Context / Adapter Interface**: Wrapper class files that isolate the legacy logic and translate between legacy and modern domain structures.
- **Superimposed Metadata Layer**: Decorators, sidecars, or external JSON/YAML mappings documenting legacy functions without modifying original codebase lines.
- **Biodegradable Deprecation Plan**: Code annotations and retirement timelines designating strangler paths.

## Optimization Readiness
- **Failure Signals**: The workflow proposes invasive legacy changes, misses critical boundary mappings, mixes modern and legacy models directly, or produces documentation that cannot guide safe strangler work.
- **Evidence To Collect**: Archaeology notes, boundary maps, adapter examples, validation tests, and review feedback on whether legacy behavior remained isolated and preserved.
- **Safe Mutation Boundaries**: Refine discovery questions, adapter guidance, metadata examples, and validation checkpoints without changing the core bubble-context and superimposed-structure strategy.
- **Acceptance Criteria**: Accept revisions only if the skill produces isolated wrapper boundaries, documents legacy flows clearly, and preserves legacy execution while enabling modernization planning.
- **Rejected Revision Handling**: Record unsafe direct-modification proposals, weak boundary definitions, and failed isolation patterns so they are not retried blindly.
- **Transfer Check**: Verify the workflow still applies to both documentation-only legacy analysis and adapter-based modernization paths.
- **Stop Rule**: If the legacy boundaries, schemas, or input/output behavior remain too unclear to isolate safely, stop and ask before proposing wrappers or deprecation steps.

## Constraints (Logical Boundaries)
- **Do Not Break Legacy Execution**: Never modify original legacy code lines unless establishing biodegradable annotations or hooks explicitly agreed upon with the user.
- **No In-Place Contamination**: Modern design structures must not be mixed directly with legacy logic; they must remain isolated behind anticontamination adapters (Bubble Contexts).
- **Always Validate Boundaries**: Write unit/integration tests that verify that requests passing through the Bubble Context are translated correctly to and from the legacy model.

## One More Thing
If the legacy codebase has zero unit tests, or if its original domain terms are completely undocumented, stop and ask the user to clarify the core database schemas or system input/output expectations before defining wrapper boundaries.

---

## How (Structural Workflow)
### Phase 1: Software Archaeology & Discovery (Chapter 14)
1. **Audit Fossilized Knowledge**: Scan import graphs, commit logs, and database schemas. Seek out classes that change together frequently.
2. **Document via Investigation Questions**: Answer the key archaeology questions (Who owns this? What APIs are active? What database tables are touched?). Refer to [legacy-checklists.md](details/legacy-checklists.md#section-1-software-archaeology-checklists) for the full checklist.
3. **Draft a Superimposed Structure**: If the legacy code cannot be modified, create external documentation maps (sidecar YAML files or database tables) that classify legacy functions.

### Phase 2: Context Boundaries & Superimposed Structures (Chapter 14)
1. **Define a Bubble Context**: Establish an adapter module that acts as an Anticorruption Layer. Translate the legacy structures into modern domain models.
2. **Decorate with Superimposed Metadata**: For python/javascript codebases, use decorators to wrap legacy classes, adding telemetry, documentation links, or validation checks without modifying original internals. Refer to [code-examples.md](details/code-examples.md#section-1-superimposed-metadata-decorators) for decorator examples.
3. **Map the Superimposed Structures**: Combine the code references with the external registry so the runtime maps legacy actions to modern domain concepts.

### Phase 3: Biodegradable Transformation & Strangler Pattern (Chapter 14)
1. **Apply Strangler Pattern**: Route incoming system requests through a proxy. For implemented modern endpoints, route to the new bubble. For legacy features, route to the old system.
2. **Apply Biodegradable Annotations**: Annotate deprecated components with clear deadlines, replacement class targets, and owners. Refer to checklists in [legacy-checklists.md](details/legacy-checklists.md#section-3-biodegradable-transformation-checklists).
3. **Enforce Legacy Rules**: Add architectural check tests (e.g. using ArchUnit or python custom import assertions) to verify that new code does not import directly from legacy files, violating the bubble. Refer to [code-examples.md](details/code-examples.md#section-2-dependency-validation-tests) for test implementations.

---

## Resources
- [legacy-checklists.md](details/legacy-checklists.md) - Checklists for archaeology, bubble boundaries, and strangler patterns.
- [code-examples.md](details/code-examples.md) - Decorator models, sidecar mapping utilities, and boundary dependency tests.
- [ Living Documentation.pdf](../TMP/%20Living%20Documentation.pdf) - Original textbook.

---

## Validation
1. Verify that the skill configuration aligns with the `document-legacy-codebase` folder.
2. Verify that all relative links to checklists and code examples are valid and clickable.
3. Verify that the Bubble Context wraps the legacy system completely, and that no greenfield code imports the legacy layer directly.
4. Verify that all biodegradable annotations contain: Owner, Expiration Date, and Strangler/Replacement target class.
