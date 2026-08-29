---
name: estimate-ai-roadmap
description: >
  WHEN/WHERE/WHO: AI project managers and agents who must estimate effort or build
  a realistic AI project roadmap despite high uncertainty.
  HOW: Decompose work into estimable units, use time-boxed spikes for unknowns,
  involve technical experts, add explicit buffers, sequence work into milestones
  with gates, and communicate the roadmap as directional rather than contractual.
  WHY: AI estimates fail when uncertainty is hidden; spikes, decomposition, and
  buffers make estimates credible and renegotiation rare.
---

# Estimate AI Roadmap

## Who
AI project managers, tech leads, and agents who must size AI work, sequence it,
and present credible plans to stakeholders.

## What
Produce an AI roadmap with:

- decomposed, estimable backlog items;
- time-boxed spikes for research/unknowns;
- expert-informed estimates;
- explicit task- and project-level buffers;
- milestone gates and decision points;
- communication guidance that frames the roadmap as directional.

## When
Trigger when the user asks to: "estimate this AI project", "build a roadmap",
"how long will this take", "plan the AI sprints", "create a timeline", or "size
the AI work".

## Where
Works from the project plan/backlog and team input. Output is a roadmap document
in the user's preferred format.

## Why
The book observes that "fear of roadmapping" is universal: estimates are treated
as commitments, and AI uncertainty makes commitments scary. This workflow makes
uncertainty visible and acceptable.

## Inputs
- **Project plan or backlog** (required): use cases, phases, tasks.
- **Team composition** (required): roles and availability.
- **Known constraints** (optional): deadlines, budget, infrastructure.

## Output (Logical Evidence)
- Roadmap containing: decomposed tasks with point estimates, spikes with time
  boxes, buffer allocations, milestone gates, dependency map, and risk notes.

## Optimization Readiness
- **Failure Signals**: Estimates without decomposition; no spikes for unknowns;
  hidden buffers; roadmap treated as a promise; team not consulted.
- **Evidence To Collect**: Estimates vs. actuals; stakeholder reactions; spikes
  that were misused.
- **Safe Mutation Boundaries**: Estimation units, buffer policy, and roadmap
  format may change. Spikes and expert involvement must remain.
- **Acceptance Criteria**: A revision must produce a roadmap with decompositions,
  spikes, buffers, and gates for a new project.
- **Rejected Revision Handling**: Record failed estimation approaches in the
  umbrella's validation log.
- **Transfer Check**: Must work for different AI project types (ML, GenAI,
  RAG, agents).
- **Stop Rule**: If the plan/backlog or team details are missing, stop and ask.

## Constraints (Logical Boundaries)
- Estimates are ranges or story points, never false precision.
- Buffers must be explicit and justified, not hidden padding.
- Roadmaps are directional plans, not contracts; say so in the output.
- Involve technical experts in every estimate; do not estimate alone.
- **Anti-Pattern Mapping**:
  - MUST NOT commit to a fixed date for experimental outcomes.
  - MUST NOT skip spikes when key assumptions are unvalidated.
  - MUST NOT hide buffer inside individual estimates to "protect" them.

## One More Thing
If the backlog, team, or constraints are missing, stop and ask before estimating.

## How (Structural Workflow)

### Phase 1: Decompose
1. Break the project into phases (EMED) and then into small, estimable backlog
   items: data acquisition, feature engineering, model evaluation, integration,
   documentation.
2. For any item whose outcome is unknown (data quality, model feasibility,
   tooling), create a time-boxed spike (e.g., 3-5 days) with a concrete output:
   findings, recommendation, or prototype.

### Phase 2: Estimate with Experts
1. Convene data scientists, ML/AI engineers, and data engineers.
2. Estimate each decomposed item using a consistent unit (story points or
   days).
3. Record assumptions behind each estimate.

### Phase 3: Add Buffers
1. Add task-level buffers for experimentation/rework (e.g., 20-30% on model
   tasks).
2. Add a project-level buffer for unknowns; state it explicitly in the roadmap.

### Phase 4: Sequence and Gate
1. Order work by dependencies and value; group into sprints (recommended:
   two-week sprints during execution).
2. Define milestone gates: data ready, baseline model, target metric reached,
   go/no-go for production, launch.
3. Mark decision points where the plan may pivot based on results.

### Phase 5: Communicate
1. Present the roadmap as directional: current assumptions, known risks, and
   probable ranges.
2. Explain trade-offs, potential pivots, and why estimates are probabilistic.

### Phase 6: Validate
1. Confirm every item is estimable and has an owner.
2. Confirm spikes and buffers are visible.
3. Confirm gates and decision points exist.
4. Deliver the roadmap.

## Review In Mind (ReviewInMindGenie)

Before delivering, activate the ReviewInMindGenie: stop authoring, switch to a skeptical reviewer, and critique the artifact as if someone else had produced it.

1. **Review Against Own Rules**: Re-read the output against this skill's `What`, `Constraints (Logical Boundaries)`, and `Validation` criteria. Check each rule explicitly; do not assume it passed because it was easy to write.
2. **Classify Findings**: Label each defect as BLOCKER (output unusable), MAJOR (violates a core rule), or MINOR (polish/consistency).
3. **Fix or Escalate**: Fix BLOCKER and MAJOR findings immediately when the fix is unambiguous. After each fix, re-check the affected criteria. If a finding cannot be fixed without new input (missing evidence, conflicting requirements, or a user decision), do not guess — report it as an open question or known gap.
4. **Deliver with a Review Note**: Present the output with a short note: what was checked, what was fixed, and what remains as a known gap. Never present an unreviewed artifact as final.

Review lens for this skill:
- Are backlog items decomposed and estimable, with explicit spikes and buffers?
- Are milestone gates and decision points placed where uncertainty is highest?
- Is the roadmap framed as directional, with confidence ranges instead of false precision?

## Validation (Verifiable Rewards)
1. Roadmap contains decomposed, estimable items with owners.
2. At least one spike exists for every unvalidated assumption.
3. Buffers are explicit at task and project level.
4. Milestone gates and go/no-go points are defined.
5. The roadmap states it is directional and subject to revision.
