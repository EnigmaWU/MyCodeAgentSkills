---
name: plan-ai-project-emed
description: >
  WHEN/WHERE/WHO: AI project managers and agents who must create an end-to-end AI
  project plan using the EMED methodology (Exploration, Mobilization, Execution,
  Delivery) from the book "Managing AI Projects".
  HOW: Walk the four EMED phases in order, complete the required templates and
  checklists (use-case discovery, prioritization, data quality, premortem, sprint
  zero, experimentation budget, delivery), and produce a structured project plan.
  WHY: Most AI projects fail from vague scoping and missing gates; EMED turns
  uncertainty into a repeatable, gate-controlled plan.
---

# Plan AI Project with EMED

## Who
AI project managers, scrum masters, product owners, and agents who must turn a
business idea into a realistic, gated AI project plan.

## What
Produce an end-to-end AI project plan organized by the four EMED phases:

- **Exploration**: strategy alignment, use-case discovery/evaluation, data-source
  mapping, premortem, prioritization, pilot scope, EDA, data quality.
- **Mobilization**: infrastructure, tools, team competencies, data culture,
  scientific approach, ethics/legal readiness.
- **Execution**: sprint zero (7 pillars), methodology choice, experimentation
  scoping, user adoption, communication channels.
- **Delivery**: formalized deliverables, knowledge transfer, final readout.

## When
Trigger when the user asks to: "plan an AI project", "create an AI project plan",
"use EMED", "scope an AI initiative", "build the project plan for our AI
initiative", or "prepare an AI project from idea to delivery".

## Where
Works from user-provided business context (goal, organization, team, data
sources, constraints). Produces a plan document in the user's preferred format
(Markdown by default) in the workspace or output location they specify.

## Why
The book reports that most AI failures come from poor alignment, missing data,
and runaway experimentation. EMED front-loads the decisions (exploration +
mobilization) that account for roughly 60-70% of project success, and gates the
rest so the plan stays honest about uncertainty.

## Inputs
- **Business goal/strategy** (required): what the organization is trying to
  achieve (cost leadership, differentiation, or focus per Porter).
- **Candidate use cases** (required): ideas to evaluate, even rough ones.
- **Data sources** (optional but strongly recommended): available systems,
  owners, formats.
- **Team and constraints** (optional): roles available, budget, timeline,
  infrastructure, regulatory context.

## Output (Logical Evidence)
- A structured project plan containing:
  1. Selected use case with value/feasibility rationale.
  2. Data source map and data-quality scorecard.
  3. Premortem risk table with mitigations.
  4. Pilot scope and value objectives/KPIs.
  5. Mobilization checklist (infrastructure, tools, people, ethics).
  6. Sprint zero plan (7 pillars) and methodology choice.
  7. Experimentation budget (who, goal, resource ceiling, thresholds, delay
     impact, blockers).
  8. Delivery plan (deliverables, knowledge transfer, readout).

## Optimization Readiness
- **Failure Signals**: Plan skips a phase or gate; use cases prioritized without
  data feasibility; no premortem; experimentation has no budget or thresholds;
  plan promises fixed dates for experimental outcomes.
- **Evidence To Collect**: User feedback on completeness; which templates were
  confusing; plans that later failed and why.
- **Safe Mutation Boundaries**: Template wording, plan format, and checklist
  phrasing may change. The four EMED phases and their gate rules must remain.
- **Acceptance Criteria**: A revision must produce a plan covering all four
  phases with the required outputs, readable without the book open.
- **Rejected Revision Handling**: Record dropped checklists or failed plan
  structures in the umbrella's `details/validation-log.md`.
- **Transfer Check**: Must work for any AI domain (e.g., retail recommendation,
  health care triage, manufacturing forecasting), not only the book's examples.
- **Stop Rule**: If the business goal or candidate use cases are missing, stop
  and ask instead of inventing them.

## Constraints (Logical Boundaries)
- Prioritize use cases by value vs. complexity; do not let hype select the
  project.
- Define measurable KPIs and a "good enough" performance threshold up front.
- Include explicit experimentation limits (time, budget, compute).
- Integrate responsible AI and compliance checkpoints from exploration onward.
- Do not promise exact delivery dates for model outcomes; use ranges and
  checkpoints.
- **Anti-Pattern Mapping**:
  - MUST NOT skip the premortem.
  - MUST NOT choose a use case without data availability checks.
  - MUST NOT treat the roadmap as a fixed contract.
  - MUST NOT ignore regulatory context (e.g., EU AI Act, GDPR/CCPA, ISO 42001).

## One More Thing
If the business goal, candidate use cases, or required context is missing, stop
and ask the user before drafting the plan.

## How (Structural Workflow)

### Phase 1: Exploration
1. Align with strategy: classify the organization's competitive strategy
   (cost leadership / differentiation / focus) and state how the AI use case
   supports it.
2. Conduct use-case discovery: build a table with use case, department,
   internal/external, and project type (GenAI, ML, DL, NLP, etc.).
3. Evaluate each use case: impact, KPIs, available resources (talent, budget,
   sponsor).
4. Map data sources to use cases: catalog data sources (system, asset, contact,
   collection method) and mark availability per use case (✓ / ✗ / TBC).
5. Run a premortem: assume the project failed; list contextual, business, and
   technical risks with mitigations.
6. Prioritize: place use cases on a value vs. feasibility 2x2 matrix; select
   quick wins or strategic projects; drop low-value/high-complexity items.
7. Define pilot scope: limited scope, medium complexity; state value objectives
   (cost reduction, revenue, differentiation).
8. Perform/plan EDA and score data quality (accuracy, completeness,
   consistency, timeliness, relevance, accessibility, validity, uniformity,
   traceability, integrity, reliability).

### Phase 2: Mobilization
1. Define infrastructure: compute (CPU/GPU), cloud vs. on-prem, storage,
   networking, security.
2. Select the tool stack (tracking, documentation, code repositories) — see the
   `select-ai-pm-toolkit` sub-skill if needed.
3. Confirm team competencies: data scientists, data engineers, ML engineers,
   DevOps/MLOps, compliance/ethics; note gaps.
4. Prepare the data culture: acquisition, cleaning, annotation, balanced
   datasets.
5. Adopt the scientific approach: hypotheses, experiments, cross-validation,
   evaluation metrics.
6. Integrate ethical/legal pillars: bias, privacy (GDPR/CCPA), transparency,
   explainability.

### Phase 3: Execution
1. Run sprint zero with the seven pillars: kickoff, work agreements, structured
   schedule, defined methodology, tracking tools, baseline evaluation metrics,
   premortem review.
2. Choose the methodology (recommended hybrid): Kanban for exploration/
   mobilization, two-week "Scrum lite" sprints for execution, one-week sprints
   for wrap-up, Kanban for delivery.
3. Scope each experimentation period by answering: who owns it, what is the
   goal, what is the resource ceiling, what are the performance thresholds,
   what is the delay impact, what is blocked.
4. Plan user adoption: UX interviews, two or more testing/feedback cycles,
   demos and training.
5. Set communication channels: sprint meetings, centralized documentation,
   weekly summaries, targeted one-on-ones.

### Phase 4: Delivery
1. Define formalized deliverables: code repositories, notebooks, technical
   documentation, model cards.
2. Schedule knowledge transfer and training in the final weeks.
3. Prepare the final readout: live demo, success evaluation, lessons learned,
   follow-up proposals.

### Phase 5: Validation
1. Check the plan against the Output list: every required element present.
2. Confirm every risk has a mitigation and every milestone has a gate.
3. Confirm the plan is executable without the book open.
4. Deliver the plan to the user.

## Review In Mind (ReviewInMindGenie)

Before delivering, activate the ReviewInMindGenie: stop authoring, switch to a skeptical reviewer, and critique the artifact as if someone else had produced it.

1. **Review Against Own Rules**: Re-read the output against this skill's `What`, `Constraints (Logical Boundaries)`, and `Validation` criteria. Check each rule explicitly; do not assume it passed because it was easy to write.
2. **Classify Findings**: Label each defect as BLOCKER (output unusable), MAJOR (violates a core rule), or MINOR (polish/consistency).
3. **Fix or Escalate**: Fix BLOCKER and MAJOR findings immediately when the fix is unambiguous. After each fix, re-check the affected criteria. If a finding cannot be fixed without new input (missing evidence, conflicting requirements, or a user decision), do not guess — report it as an open question or known gap.
4. **Deliver with a Review Note**: Present the output with a short note: what was checked, what was fixed, and what remains as a known gap. Never present an unreviewed artifact as final.

Review lens for this skill:
- Do the four EMED phases cover strategy, data, infrastructure, team, ethics, execution, and delivery?
- Is every deliverable owned, sequenced, and gated by an explicit decision?
- Could a team execute the plan without inventing missing details?

## Validation (Verifiable Rewards)
1. Confirm the plan contains all four EMED phases with their required outputs.
2. Confirm the selected use case has a value/feasibility rationale and KPIs.
3. Confirm the premortem table exists with at least one mitigation per risk.
4. Confirm sprint zero and the experimentation budget are explicit.
5. Confirm delivery includes deliverables, knowledge transfer, and readout.

## One More Thing
If any required input is missing or the user's goal conflicts with the EMED
phases (e.g., they need a fixed-date contract), stop and clarify before
proceeding.
