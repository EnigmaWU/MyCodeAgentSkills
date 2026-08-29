---
name: design-architecture-viewpoints
description: >
  WHEN/WHERE/WHO: [Scheduling: Use when: defining the structural views of a system, documenting system architecture, or aligning stakeholder expectations. Applies to: software architecture descriptions, system design documents, and RFCs]
  HOW: [Structural: Helps with: identifying stakeholders and scenarios, selecting viewpoints, drafting views (Context, Functional, Information, Concurrency, Development, Deployment, Operational), applying perspectives, and checking inter-view consistency]
  WHY: [Scheduling: Provides structured workflow execution to prevent errors and ensure standards.]
---

# Design Architecture Viewpoints

## Common Contract (Load First)

When this skill is activated, first load [skill-common](../skill-common/SKILL.md) and apply the shared conventions it defines: canonical section order, frontmatter rules, anti-pattern guidance, and the Review In Mind loop in [review-in-mind](../skill-common/details/review-in-mind.md). This skill adds only domain-specific rules below.

## Who
Architects, system designers, or agents responsible for documenting and verifying system-level designs for diverse stakeholders.

## What
Identify system stakeholders and scenarios, select and draft architectural viewpoints from the Rozanski-Woods catalog, apply cross-cutting perspectives, and perform inter-view consistency checking.

## When
- Triggered by requests like: "document the architecture views of...", "identify stakeholders for...", "create a deployment/operational view for...", or "apply rozanski-woods perspectives to...".
- Do not use for writing code, writing simple tests, or documenting single-function interfaces unless they have system-level architectural implications.

## Where
Applies to system architecture documentation, design proposals, stakeholder alignment matrices, and deployment/concurrency blueprints.

## Why
Ensures that system documentation is comprehensive, targets all relevant stakeholders, and is internally consistent across different views (e.g., code structure vs physical nodes).

## Inputs
- **System Description** (required): Functional components and high-level goals.
- **Stakeholder List** (optional): Users, developers, operators, or business sponsors.
- **Viewpoints and Perspectives Reference** (required): Located at [viewpoints-and-perspectives-reference](details/viewpoints-and-perspectives-reference.md).
- **Software Systems Architecture PDF** (optional): Located at [Software_Systems_Architecture](references/Software_Systems_Architecture.pdf).

## Output (Logical Evidence)
- **Stakeholder-to-Viewpoint Matrix**: Mapping stakeholders to their primary viewpoints of interest.
- **Viewpoint Catalog**: Completed architectural views (Context, Functional, Deployment, etc.).
- **Perspective Checksheets**: Validation logs for cross-cutting perspectives (Security, Performance, Availability, Evolution).
- **Consistency Log**: Alignment verification between views.

## Optimization Readiness
- **Failure Signals**: Stakeholders are omitted, viewpoint selection is incomplete, cross-view inconsistencies are unresolved, or the document treats one view as sufficient for the whole architecture.
- **Evidence To Collect**: Stakeholder matrices, viewpoint catalogs, perspective checksheets, and consistency logs that show where views aligned or conflicted.
- **Safe Mutation Boundaries**: Refine stakeholder-classification prompts, viewpoint-selection guidance, perspective checks, and consistency rules without changing the core view-based architecture workflow.
- **Acceptance Criteria**: Accept revisions only if the architecture covers the relevant stakeholder concerns, drafts multiple views, and documents consistency checks between them.
- **Rejected Revision Handling**: Record missing-view mistakes, skipped perspectives, and inconsistent mapping patterns so they are not repeated.
- **Transfer Check**: Verify the workflow still works for both compact systems and systems with several stakeholder groups and cross-cutting concerns.
- **Stop Rule**: If the primary stakeholders are unknown, stop and ask before drafting viewpoints.

## Constraints (Logical Boundaries)
- Every drafted view must specify which stakeholder concern it addresses.
- Logical components must be explicitly mapped to physical deployment nodes in the Deployment view.

## One More Thing
If anything is unclear, missing, or conflicting (especially if the primary stakeholders are unknown), stop and ask the user before proceeding.

## How (Structural Workflow)
### Phase 1: Identify Stakeholders and Scenarios (SSA Ch 9, 10)
1. Categorize stakeholders using the Rozanski-Woods classes:
   * **Acquirers**: Oversee the procurement and business goals.
   * **Assessors**: Verify compliance with standards, safety, and security.
   * **Communicators**: Explain the architecture to other stakeholders.
   * **Developers**: Build, test, and implement the system.
   * **Maintainers**: Modify and evolve the system post-release.
   * **Operators**: Deploy, monitor, and run the system.
   * **Providers**: Supply third-party hardware, software, or APIs.
   * **Support**: Guide and help users with problems.
   * **Users**: Directly interact with the running system.
2. Elicit and prioritize scenarios:
   * **Use Case Scenarios**: Normal system behaviors.
   * **Growth Scenarios**: Scalability, volume, or business expansion.
   * **Exploratory Scenarios**: Unexpected changes (e.g., loss of a supplier, major framework migration).

### Phase 2: Select and Draft Viewpoints (SSA Part III)
Select and document the views required to describe the system structure. Refer to the structured reference at [viewpoints-and-perspectives-reference](details/viewpoints-and-perspectives-reference.md) (or consult the original PDF at [Software_Systems_Architecture](references/Software_Systems_Architecture.pdf)) for the viewpoints. Apply the detailed models and checklists from the corresponding Level-3 files:
* **Context View (Ch 16)**: Scope, boundaries, external interfaces. Details in [viewpoints-and-perspectives-reference](details/viewpoints-and-perspectives-reference.md).
* **Functional View (Ch 17)**: Component structures and behavioral interactions. Details in [functional-viewpoint-details](details/functional-viewpoint-details.md).
* **Information View (Ch 18)**: Data models, lifecycle, flow. Details in [viewpoints-and-perspectives-reference](details/viewpoints-and-perspectives-reference.md).
* **Concurrency View (Ch 19)**: Process/thread mappings, synchronization primitives. Details in [viewpoints-and-perspectives-reference](details/viewpoints-and-perspectives-reference.md).
* **Development View (Ch 20)**: Package structure, module layout, build processes. Details in [viewpoints-and-perspectives-reference](details/viewpoints-and-perspectives-reference.md).
* **Deployment View (Ch 21)**: Physical infrastructure, hardware nodes, network topologies. Details in [deployment-viewpoint-details](details/deployment-viewpoint-details.md).
* **Operational View (Ch 22)**: Installation, backup, monitoring. Details in [viewpoints-and-perspectives-reference](details/viewpoints-and-perspectives-reference.md).

### Phase 3: Apply Architectural Perspectives (SSA Part IV)
Refine the views by applying cross-cutting quality perspectives. Refer to the corresponding Level-3 guides:
* **Security (Ch 25)**: Threat modeling, access control, encryption. Details in [security-perspective-details](details/security-perspective-details.md).
* **Performance & Scalability (Ch 26)**: Latency budgets, load modeling. Details in [performance-perspective-details](details/performance-perspective-details.md).
* **Availability & Resilience (Ch 27)**: Single points of failure, recovery times. Details in [viewpoints-and-perspectives-reference](details/viewpoints-and-perspectives-reference.md).
* **Evolution (Ch 28)**: Extensibility, backward compatibility. Details in [viewpoints-and-perspectives-reference](details/viewpoints-and-perspectives-reference.md).

### Phase 4: Check Inter-View Consistency (SSA Ch 23)
Perform pairwise checks between views to resolve conflicts:
1. **Context vs Functional**: Verify all external systems in the Context view map to interfaces in the Functional view.
2. **Functional vs Development**: Verify every logical component in the Functional view maps to a module or package in the Development view.
3. **Functional vs Concurrency**: Verify component runtime execution maps to processes/threads in the Concurrency view.
4. **Concurrency vs Deployment**: Verify process/thread deployments map to physical nodes in the Deployment view.
5. **Deployment vs Operational**: Verify physical configurations in the Deployment view have monitoring and administration procedures in the Operational view.

## Resources
- [viewpoints-and-perspectives-reference](details/viewpoints-and-perspectives-reference.md) - Primary reference for viewpoints and perspectives.
- [Software_Systems_Architecture](references/Software_Systems_Architecture.pdf) - Original textbook.
- [functional-viewpoint-details](details/functional-viewpoint-details.md) - Level-3 Functional viewpoint details.
- [deployment-viewpoint-details](details/deployment-viewpoint-details.md) - Level-3 Deployment viewpoint details.
- [security-perspective-details](details/security-perspective-details.md) - Level-3 Security perspective details.
- [performance-perspective-details](details/performance-perspective-details.md) - Level-3 Performance perspective details.

## Review In Mind (ReviewInMindGenie)

Execute the common review loop in [review-in-mind](../skill-common/details/review-in-mind.md) before delivering.

Review lens for this skill:
- Are viewpoints selected for real stakeholders and concerns, with cross-cutting perspectives applied?
- Do the drafted viewpoints cover the required concerns without gaps?
- Is inter-view consistency verified (the same facts appear consistently across views)?

## Validation
1. Verify the Stakeholder-to-Viewpoint Matrix contains at least 3 stakeholder categories.
2. Verify at least 3 viewpoints are drafted (e.g., Context, Functional, Deployment).
3. Verify that Concurrency, Development, and Deployment views have pairwise consistency checks documented in the Consistency Log.
