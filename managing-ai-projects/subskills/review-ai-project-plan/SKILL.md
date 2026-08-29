---
name: review-ai-project-plan
description: >
  WHEN/WHERE/WHO: AI project managers, sponsors, and agents who must review an
  existing AI project plan against the methodology in "Managing AI Projects"
  (EMED, data quality, metrics, gates, responsible AI).
  HOW: Run the review checklist across strategy, use case, data, metrics,
  experimentation, sprint zero, governance, and delivery; classify findings by
  severity; produce a verdict with concrete fixes.
  WHY: AI plans look plausible but fail on hidden assumptions; a checklist review
  surfaces missing gates and unrealistic expectations before execution.
---

# Review AI Project Plan

## Who
AI project managers, scrum masters, product owners, executives, and agents who
must assess whether an AI project plan is complete, realistic, and aligned with
business value.

## What
Review an AI project plan (document, backlog, roadmap, or slides) against the
book's methodology and return a verdict: PASS, PASS WITH CONDITIONS, or FAIL,
with every finding mapped to a concrete fix.

## When
Trigger when the user asks to: "review my AI project plan", "check if this AI
plan is good", "is this plan ready", "critique our AI project plan", or "validate
this AI initiative".

## Where
Applies to any plan artifact the user provides: Markdown documents, slide decks,
backlogs, roadmaps, or pasted text.

## Why
The book shows that AI projects fail from vague use cases, unstated performance
thresholds, missing data feasibility, and late compliance reviews. A structured
review catches these before money and time are committed.

## Inputs
- **Plan** (required): the AI project plan to review.
- **Context** (optional): organization strategy, team, known constraints.

## Output (Logical Evidence)
- A review report with:
  1. Checklist results (PASS / FAIL / N/A per item).
  2. Findings grouped by severity (BLOCKER / MAJOR / MINOR) with fixes.
  3. Verdict: PASS, PASS WITH CONDITIONS, or FAIL.

## Optimization Readiness
- **Failure Signals**: Review misses missing gates; verdict contradicts findings;
  feedback too vague to act on; plan rewritten instead of reviewed.
- **Evidence To Collect**: Example plans with known defects; user feedback on
  actionability; misclassified findings.
- **Safe Mutation Boundaries**: Checklist wording, severity rules, and report
  format may change. The EMED/data-quality/metrics rules must stay faithful.
- **Acceptance Criteria**: A revision must catch the known defects in at least
  one example plan and keep the verdict consistent with findings.
- **Rejected Revision Handling**: Record rejected checklist items and report
  formats in the umbrella's validation log.
- **Transfer Check**: Must review plans from any AI domain, not only the book's
  examples.
- **Stop Rule**: If the plan cannot be read or the project context is too
  ambiguous, stop and ask.

## Constraints (Logical Boundaries)
- Review only what the plan states; do not fill in missing content.
- Do not rewrite the plan unless asked.
- Every finding must trace to a book rule (EMED phase, data quality factor,
  metric, gate, governance requirement).
- **Anti-Pattern Mapping**:
  - MUST NOT approve a plan without performance thresholds.
  - MUST NOT skip data feasibility when a plan claims ML/DL.
  - MUST NOT accept "we will figure it out during execution" as a reason to pass
    missing gates.

## One More Thing
If the plan is missing or unreadable, stop and ask the user to provide it.

## How (Structural Workflow)

### Phase 1: Ingest
1. Read the plan completely.
2. Identify its scope: use case, expected value, data, timeline, team, metrics,
   gates.

### Phase 2: Run the checklist
1. **Strategy alignment**: Does the plan state the business strategy it serves
   (cost leadership / differentiation / focus) and the expected value (ROI,
   savings, revenue, differentiation)?
2. **Use case**: Is the use case specific, scoped, and justified with KPIs?
3. **Data**: Does the plan map data sources, assess availability/quality
   (volume, joinability, relevance, consistency, clarity, timeliness), and
   address privacy/compliance?
4. **Metrics**: Are success metrics defined (business + technical), with a
   "good enough" threshold agreed by stakeholders?
5. **Experimentation**: Is experimentation budgeted (who, goal, resource
   ceiling, thresholds, delay impact, blockers)? Is there a baseline model
   plan?
6. **Sprint zero**: Does the plan cover kickoff, work agreements, schedule,
   methodology, tracking tools, baseline metrics, premortem?
7. **Governance**: Are ethics/bias, explainability, compliance (e.g., EU AI
   Act, GDPR/CCPA, ISO 42001), and responsible AI checkpoints included from
   the start?
8. **Delivery**: Are deliverables, knowledge transfer, monitoring/retraining,
   and final readout defined?

### Phase 3: Report
1. Group findings:
   - BLOCKER: missing use-case justification, no data feasibility, no metrics
     or thresholds, no premortem, no compliance consideration.
   - MAJOR: vague scope, missing experimentation budget, no sprint zero plan,
     no delivery/knowledge transfer plan.
   - MINOR: unclear wording, missing owner for a task, undocumented assumption.
2. For each finding, state the rule violated and the concrete fix.
3. Produce the verdict: any BLOCKER or unresolved MAJOR -> FAIL; only MINOR ->
   PASS WITH CONDITIONS; all PASS -> PASS.

### Phase 4: Validate
1. Confirm every finding traces to a checklist item.
2. Confirm the verdict matches the findings.
3. Deliver the report.

## Validation (Verifiable Rewards)
1. Every checklist item receives PASS/FAIL/N/A.
2. Every FAIL item has a concrete fix.
3. The verdict is consistent with severity rules.
4. No finding invents content not present in the plan.
