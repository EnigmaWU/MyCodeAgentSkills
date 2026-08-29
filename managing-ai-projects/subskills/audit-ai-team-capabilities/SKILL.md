---
name: audit-ai-team-capabilities
description: >
  WHEN/WHERE/WHO: AI project managers and agents who must analyze AI team gaps,
  build a capability heatmap, and define an upskilling plan.
  HOW: Score the team across capability areas and roles, identify gap clusters,
  apply the signal-adapt-embed-monitor learning loop, and produce prioritized
  actions.
  WHY: AI team failures are usually missing bridges between roles, not missing
  people; a heatmap makes gaps visible without blaming individuals.
---

# Audit AI Team Capabilities

## Who
AI project managers, tech leads, and agents evaluating AI team readiness before
or during a project.

## What
Produce a capability audit:

- capability heatmap (capability areas x roles, maturity ratings);
- gap cluster analysis (reproducibility, data stewardship, responsible AI,
  human-centered design);
- learning-loop actions (signal, adapt, embed, monitor);
- prioritized upskilling/hiring recommendations.

## When
Trigger when the user asks to: "audit our AI team", "analyze AI team gaps",
"build a capability heatmap", "find team skill gaps", or "plan AI upskilling".

## Where
Works from the team roster and evidence of current practices. Output is a
heatmap + action plan.

## Why
The book shows that AI teams grow around immediate needs and develop invisible
structural gaps; a heatmap evaluates functions, not people, and turns gaps into
growth via a continuous learning loop.

## Inputs
- **Team roster/roles** (required): data science, MLOps/engineering,
  product/design, responsible AI/compliance, etc.
- **Evidence of practices** (required): how data, experiments, deployment,
  governance, and user feedback are handled today.

## Output (Logical Evidence)
- Heatmap table with maturity ratings (Weak / Developing / Mature / Strong).
- Gap clusters with risk implications.
- Action plan: micro-changes, documentation/artifacts, and monitoring signals.

## Optimization Readiness
- **Failure Signals**: Heatmap blames individuals; gaps listed without actions;
  no monitoring step; audit ignores responsible AI.
- **Evidence To Collect**: Real team audits; feedback on actionability.
- **Safe Mutation Boundaries**: Heatmap dimensions, rating scale, and action
  templates may change. The function-based, non-blaming approach must remain.
- **Acceptance Criteria**: A revision must produce a heatmap with gap clusters
  and concrete actions.
- **Rejected Revision Handling**: Record rejected heatmap dimensions in the
  umbrella's validation log.
- **Transfer Check**: Must work for ML, GenAI, and mixed teams.
- **Stop Rule**: If the roster or evidence is missing, stop and ask.

## Constraints (Logical Boundaries)
- Evaluate capability areas, never individuals.
- Cover at least: data quality/stewardship, experimentation/traceability,
  prompt/model behavior, deployment/monitoring, responsible AI, user feedback.
- Every gap must map to at least one action.
- **Anti-Pattern Mapping**:
  - MUST NOT skip responsible AI in the audit.
  - MUST NOT propose large restructures as the first fix; prefer micro
    adaptations.
  - MUST NOT treat the audit as a one-time event; include monitoring.

## One More Thing
If the roster or evidence of practices is missing, stop and ask before
auditing.

## How (Structural Workflow)

### Phase 1: Build the heatmap
1. List capability areas (data quality, experimentation, prompt/model
   behavior, deployment, responsible AI, user feedback).
2. List roles (data science, MLOps/engineering, product/design, RAI/compliance).
3. Rate each cell: Weak / Developing / Mature / Strong, using evidence only.

### Phase 2: Find gap clusters
1. Identify weak cells and group them into clusters: reproducibility,
   data stewardship, responsible AI, human-centered design.
2. Trace how clusters create compound risks (e.g., no versioning -> compliance
   issue; late compliance -> release block).

### Phase 3: Plan the learning loop
1. **Signal**: state what each gap is revealing about the system.
2. **Adapt**: define micro-changes (version prompt templates, add a one-page
   ethical check, link feedback to experiments).
3. **Embed**: turn each change into a living artifact (checklist, retrospective
   insight, documented process).
4. **Monitor**: define signals to watch so gaps resurface visibly.

### Phase 4: Validate
1. Confirm every gap has an action and an owner.
2. Confirm the plan includes monitoring.
3. Deliver the audit.

## Review In Mind (ReviewInMindGenie)

Before delivering, activate the ReviewInMindGenie: stop authoring, switch to a skeptical reviewer, and critique the artifact as if someone else had produced it.

1. **Review Against Own Rules**: Re-read the output against this skill's `What`, `Constraints (Logical Boundaries)`, and `Validation` criteria. Check each rule explicitly; do not assume it passed because it was easy to write.
2. **Classify Findings**: Label each defect as BLOCKER (output unusable), MAJOR (violates a core rule), or MINOR (polish/consistency).
3. **Fix or Escalate**: Fix BLOCKER and MAJOR findings immediately when the fix is unambiguous. After each fix, re-check the affected criteria. If a finding cannot be fixed without new input (missing evidence, conflicting requirements, or a user decision), do not guess — report it as an open question or known gap.
4. **Deliver with a Review Note**: Present the output with a short note: what was checked, what was fixed, and what remains as a known gap. Never present an unreviewed artifact as final.

Review lens for this skill:
- Is the capability heatmap evidence-backed (roles × capability areas with maturity ratings)?
- Are gap clusters tied to concrete learning-loop actions with owners?
- Are upskilling/hiring recommendations prioritized and feasible?

## Validation (Verifiable Rewards)
1. Heatmap covers the required capability areas and roles.
2. Ratings are based on stated evidence.
3. Gap clusters map to compound risks.
4. Every gap has a micro-change, artifact, and monitoring signal.
