---
name: apply-architectural-tactics
description: >
  WHEN/WHERE/WHO: [Scheduling: Use when: designing a system architecture, conducting structural design reviews, or mapping quality goals to design decisions. Applies to: architecture design documents, RFCs, and system design specifications]
  HOW: [Structural: Helps with: defining Architecturally Significant Requirements (ASRs), building Quality Attribute Utility Trees, applying Attribute-Driven Design (ADD) steps, selecting SAiP tactics, and executing ATAM tradeoff analysis]
  WHY: [Scheduling: Provides structured workflow execution to prevent errors and ensure standards.]
---

# Apply Architectural Tactics

## Who
Architects, principal engineers, or agents designing systems where quality attributes (Availability, Performance, Security, Modifiability, Testability, Usability, etc.) drive the design choices.

## What
Elicit Architecturally Significant Requirements (ASRs), construct a Quality Attribute Utility Tree, execute the Attribute-Driven Design (ADD) process to select architectural patterns/tactics, and evaluate the architecture using ATAM (Architecture Tradeoff Analysis Method) and CBAM (Cost Benefit Analysis Method).

## When
- Triggered by requests like: "design a system for...", "apply tactics to...", "write a QAS for...", or "evaluate the availability/modifiability of this design."
- Do not use for simple bug fixes, local refactorings, or database schema designs unless they are directly tied to an architectural quality attribute goal.

## Where
Applies to system design documents, RFCs, architecture blueprints, and design files in the current workspace.

## Why
Ensures that architectural design is systematic, driven by measurable quality goals, and backed by proven engineering tactics rather than ad-hoc technology preferences.

## Inputs
- **Functional Requirements** (required): What the system needs to do.
- **Quality Attribute goals** (required): Vague goals (e.g., "high availability", "fast response") that must be codified.
- **Quality Attribute Tactics Reference** (required): Located at [quality-attribute-tactics-and-checklists.md](details/quality-attribute-tactics-and-checklists.md).
- **Software Architecture in Practice PDF** (optional): Located at [references/Software_Architecture_in_Practice.pdf](references/Software_Architecture_in_Practice.pdf).

## Output (Logical Evidence)
- **Utility Tree**: A hierarchical decomposition of quality attributes into concrete scenarios with prioritization.
- **Attribute-Driven Design (ADD) Log**: A breakdown of the design steps, patterns, and tactics chosen.
- **ATAM Evaluation Report**: Sensitivity points, tradeoff points, risks, and non-risks.
- **CBAM Economic Assessment**: Optional ROI ranking of design alternatives.

## Optimization Readiness
- **Failure Signals**: Quality scenarios remain vague, tactics are chosen before measurable goals exist, tradeoffs are undocumented, or design recommendations collapse into framework selection instead of architectural reasoning.
- **Evidence To Collect**: Utility trees, tactic selections, ATAM findings, CBAM comparisons, and examples where quality goals were measurable or remained ambiguous.
- **Safe Mutation Boundaries**: Refine elicitation prompts, tactic-selection guidance, report structure, and validation sequencing without changing the core ASR, ADD, ATAM, and CBAM workflow.
- **Acceptance Criteria**: Accept revisions only if the skill leads to measurable quality scenarios, traceable tactic choices, and explicit tradeoff reporting before implementation technology is selected.
- **Rejected Revision Handling**: Record discarded tactic heuristics, ambiguous scenario templates, and weak tradeoff-reporting patterns so they are not repeated.
- **Transfer Check**: Confirm the revised workflow still supports multiple quality attributes such as availability, performance, and modifiability.
- **Stop Rule**: If architecturally significant requirements or measurable response metrics are missing, stop and ask before recommending tactics.

## Constraints (Logical Boundaries)
- Every Quality Attribute Scenario must have a quantitative, measurable response metric.
- Architectural design must be completed prior to choosing specific frameworks, libraries, or cloud services.

## One More Thing
If the quality requirements are unmeasurable or missing, stop and ask the user to define the targets before choosing tactics.

## How (Structural Workflow)
### Phase 1: Elicit ASRs and Build a Utility Tree (SAiP Ch 16)
1. Read the functional and business requirements to extract **Architecturally Significant Requirements (ASRs)**.
2. Build a **Utility Tree** to organize quality goals:
   * **Root**: Utility.
   * **Branch 1 (Quality Attributes)**: Availability, Modifiability, Performance, Security, Testability, Usability.
   * **Branch 2 (Sub-categories)**: e.g., Performance -> Latency, Performance -> Throughput; Availability -> Detection, Recovery.
   * **Leaf Nodes (Scenarios)**: Concrete 6-part scenarios (Source, Stimulus, Artifact, Environment, Response, Response Measure).
3. Prioritize each leaf scenario on a two-dimensional grid: **(Business Value, Architectural Difficulty)** using High (H), Medium (M), and Low (L) rankings (e.g., `(H, H)` or `(H, M)`).
4. Focus design efforts on the highest-priority scenarios.

### Phase 2: Design Using Attribute-Driven Design (ADD 3.0) (SAiP Ch 17)
For the system element to be designed:
1. **Identify the design target**: Determine which subsystem or element is being decomposed.
2. **Review design inputs**: Select the ASRs from the Utility Tree that apply to this target.
3. **Generate design concepts**:
   * Search the structured reference at [quality-attribute-tactics-and-checklists.md](details/quality-attribute-tactics-and-checklists.md) (or consult the original PDF at [references/Software_Architecture_in_Practice.pdf](references/Software_Architecture_in_Practice.pdf)) for appropriate tactics.
   * Apply the detailed design checklists from the corresponding Level-3 files:
     * *Availability (Ch 5)*: Search the checklist at [availability-checklist-details.md](details/availability-checklist-details.md).
     * *Performance (Ch 8)*: Search the checklist at [performance-checklist-details.md](details/performance-checklist-details.md).
     * *Security (Ch 9)*: Search the checklist at [security-checklist-details.md](details/security-checklist-details.md).
     * *Modifiability (Ch 7)*: Search the checklist at [modifiability-checklist-details.md](details/modifiability-checklist-details.md).
     * *Interoperability, Testability, Usability*: See the summary reference at [quality-attribute-tactics-and-checklists.md](details/quality-attribute-tactics-and-checklists.md).
   * Select architectural patterns (e.g., Microservices, Layers, Publish-Subscribe) that bundle these tactics.
4. **Instantiate elements**: Allocate functional responsibilities to the components.
5. **Define interfaces**: Specify communication protocols, APIs, and data structures.
6. **Verify the design**: Run thought experiments and checklists against the target QAS.

### Phase 3: Evaluate Tradeoffs and Risks (ATAM) (SAiP Ch 21)
Evaluate the proposed design against the high-priority scenarios:
1. Identify **Sensitivity Points**: Design decisions critical to achieving a specific quality attribute (e.g., "The database write replication factor is highly sensitive for availability").
2. Identify **Tradeoff Points**: Decisions that affect multiple quality attributes (e.g., "Encrypting message payloads improves security but increases latency, affecting performance").
3. Document **Risks**: Architectural decisions that could lead to undesirable consequences (e.g., "Single database node is a single point of failure under load").
4. Document **Non-risks**: Documented, safe decisions that guarantee constraints are met.

### Phase 4: Analyze Economics (CBAM) (SAiP Ch 23)
If multiple design alternatives exist:
1. Estimate the cost to implement each tactic.
2. Estimate the utility/benefit of the quality attribute improvements for each tactic.
3. Calculate the Return on Investment (ROI = Utility / Cost).
4. Recommend the design alternative with the highest ROI.

## Resources
- [quality-attribute-tactics-and-checklists.md](details/quality-attribute-tactics-and-checklists.md) - Primary reference for tactics and design checklists.
- [Software_Architecture_in_Practice.pdf](references/Software_Architecture_in_Practice.pdf) - Original textbook.
- [availability-checklist-details.md](details/availability-checklist-details.md) - Level-3 Availability checklist.
- [performance-checklist-details.md](details/performance-checklist-details.md) - Level-3 Performance checklist.
- [security-checklist-details.md](details/security-checklist-details.md) - Level-3 Security checklist.
- [modifiability-checklist-details.md](details/modifiability-checklist-details.md) - Level-3 Modifiability checklist.

## Validation
1. Verify the Utility Tree contains at least 3 prioritized scenarios with 6-part definitions.
2. Verify every selected tactic maps directly to an ASR from the Utility Tree.
3. Verify that Sensitivity Points, Tradeoff Points, Risks, and Non-risks are documented in ATAM format.
