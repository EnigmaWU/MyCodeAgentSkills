---
name: managing-ai-projects
description: >
  WHEN/WHERE/WHO: Software architects, project managers, and agents who must plan,
  review, estimate, or run AI projects using the EMED methodology and practical
  guidance from the book "Managing AI Projects" by González Sánchez and Jain
  Runtasewee.
  HOW: Route the request to the matching sub-skill in subskills/ (plan, review,
  estimate, model selection, evaluation, stakeholders, team audit, or toolkit),
  read that sub-skill's SKILL.md, and execute its workflow.
  WHY: AI projects fail from vague scoping, unrealistic expectations, and weak
  governance; structured, book-derived workflows make AI delivery repeatable.
---

# Managing AI Projects

## Common Contract (Load First)

When this skill is activated, first load [skill-common](../skill-common/SKILL.md) and apply the shared conventions it defines: canonical section order, frontmatter rules, anti-pattern guidance, and the Review In Mind loop in [review-in-mind](../skill-common/details/review-in-mind.md). This skill adds only domain-specific rules below.

## Who
AI project managers, scrum masters, product owners, technical leads, and agents
supporting AI delivery teams. Also useful for executives and coaches who need
structured, field-tested processes for AI initiatives.

## What
An umbrella skill that routes AI project management work to one of eight focused
sub-skills, each derived from the book *Managing AI Projects* (O'Reilly) and its
EMED methodology (Exploration, Mobilization, Execution, Delivery):

1. `subskills/plan-ai-project-emed/` — create an end-to-end AI project plan.
2. `subskills/review-ai-project-plan/` — review an existing AI project plan.
3. `subskills/estimate-ai-roadmap/` — estimate effort and build a realistic AI
   roadmap.
4. `subskills/select-ai-model-approach/` — choose the model family and approach.
5. `subskills/evaluate-ai-model-readiness/` — run the evaluation/validation gate.
6. `subskills/manage-ai-stakeholders/` — plan stakeholder engagement and
   expectations.
7. `subskills/audit-ai-team-capabilities/` — analyze team gaps and build an
   upskilling plan.
8. `subskills/select-ai-pm-toolkit/` — select tools for managing AI projects.

## When
Trigger when the user asks to:

- "plan an AI project" / "create an AI project plan"
- "review or check my AI project plan"
- "estimate or build a roadmap for an AI project"
- "which AI model should we use" / "help me choose the AI approach"
- "is the model ready" / "evaluate or validate the model"
- "manage AI stakeholders" / "set stakeholder expectations"
- "analyze our AI team gaps" / "audit AI team capabilities"
- "which AI project tools should we use" / "build an AI PM toolkit"
- "use the EMED methodology" or "how should we manage this AI project?"

Do NOT use for: generic non-AI project management, coding the AI models
themselves, or summarizing the book without a concrete task.

## Where
This skill lives at the workspace root as `managing-ai-projects/`. Sub-skills live
in `subskills/<name>/` and each has its own `SKILL.md` with full instructions.
Read the selected sub-skill's `SKILL.md` before executing its workflow.

## Why
AI projects are uncertain, data-dependent, and stakeholder-heavy. The book
codifies a repeatable method (EMED), checklists (use-case discovery, premortem,
data quality, metrics, sprint zero), and role guidance that converts this theory
into executable agent workflows. Keeping them under one umbrella makes discovery
and routing simple while keeping each sub-skill focused and small.

## Inputs
- **Request** (required): what the user wants done (plan, review, estimate,
  model choice, evaluation, stakeholders, team audit, or toolkit).
- **Project context** (required by most sub-skills): business goal, use case,
  data sources, team, constraints, metrics, or existing plan/roadmap.
- **Files** (optional): existing project plans, backlogs, roadmaps, or
  documentation.

## Output (Logical Evidence)
- The selected sub-skill's deliverable: project plan, review report, roadmap,
  model recommendation, readiness decision, stakeholder plan, capability
  heatmap, or toolkit recommendation.
- The umbrella itself produces no output beyond the routing decision and the
  selected sub-skill's result.

## Optimization Readiness
- **Failure Signals**: Wrong sub-skill chosen for a request; sub-skill workflows
  too vague to execute; routing table missing a common request (e.g., "write the
  project charter"); outputs that contradict the book's methodology.
- **Evidence To Collect**: Real user requests and the sub-skill that was chosen;
  feedback that a sub-skill was hard to follow; cases where two sub-skills
  overlap (e.g., plan vs. review).
- **Safe Mutation Boundaries**: Routing table wording, sub-skill trigger phrases,
  and output formats may change. The EMED phases and book-derived rules must
  remain faithful to the source.
- **Acceptance Criteria**: Every common request type maps to exactly one
  sub-skill; each sub-skill passes `quick_validate.py`; a revision must not
  break existing sub-skill links.
- **Rejected Revision Handling**: Record wrong routing decisions and rejected
  trigger phrases in `details/validation-log.md`.
- **Transfer Check**: The umbrella must route requests for projects in a domain
  not used during extraction (e.g., a retail recommendation system or a health
  care pilot), not just the book's examples.
- **Stop Rule**: If a request does not clearly map to a sub-skill, or the
  required project context is missing, stop and ask the user instead of guessing.

## Constraints (Logical Boundaries)
- The umbrella does not duplicate sub-skill instructions; it routes and then
  delegates.
- Do not invent book rules; every directive in a sub-skill must trace to the
  book's methodology (EMED, ADRIAN, sprint zero, premortem, data quality, etc.).
- Do not promise fixed delivery dates or guaranteed model performance; AI
  outcomes are probabilistic and must be framed with thresholds and buffers.
- **Anti-Pattern Mapping**:
  - MUST NOT skip the premortem or go/no-go gates when producing a plan.
  - MUST NOT treat "good enough" performance as a fixed, unstated number.
  - MUST NOT recommend hallucinated tools; tool names come from the book or the
    user's organization.
  - MUST NOT let hype replace measurable value criteria (ROI, KPIs, metrics).

## How (Structural Workflow)

### Phase 1: Classify the Request
Read the user request and map it to exactly one sub-skill:

| If the user asks to... | Use sub-skill |
| --- | --- |
| create/plan a project, use EMED end-to-end | `plan-ai-project-emed` |
| review/critique an existing AI project plan | `review-ai-project-plan` |
| estimate effort, build/adjust a roadmap, handle uncertainty | `estimate-ai-roadmap` |
| choose a model/approach, build vs. leverage, explainability | `select-ai-model-approach` |
| evaluate/validate readiness, metrics, go/no-go | `evaluate-ai-model-readiness` |
| manage stakeholders, expectations, adoption, difficult clients | `manage-ai-stakeholders` |
| analyze team gaps, capability heatmap, upskilling | `audit-ai-team-capabilities` |
| pick tools/platforms/vendors, build a PM toolkit | `select-ai-pm-toolkit` |

If the request spans multiple sub-skills (e.g., "plan and review"), run them in
sequence and combine the outputs. If no sub-skill fits, stop and ask.

### Phase 2: Load the Sub-skill
1. Read `subskills/<selected>/SKILL.md` completely.
2. Gather the inputs the sub-skill requires (project context, files, constraints).
3. If a required input is missing, stop and ask the user.

### Phase 3: Execute
1. Run the sub-skill's workflow exactly as written.
2. Produce the sub-skill's deliverable.

### Phase 4: Validate
1. Run the sub-skill's Validation section.
2. Confirm the output is executable from natural language alone and does not
   require the book to be open.
3. Report the deliverable and any follow-up work.

## Resources
- [SKILL](subskills/plan-ai-project-emed/SKILL.md)
  — EMED project planning (COMPLEX)
- [SKILL](subskills/review-ai-project-plan/SKILL.md)
  — plan review (COMPLICATED)
- [SKILL](subskills/estimate-ai-roadmap/SKILL.md)
  — estimation and roadmaps (COMPLICATED)
- [SKILL](subskills/select-ai-model-approach/SKILL.md)
  — model selection (COMPLICATED)
- [SKILL](subskills/evaluate-ai-model-readiness/SKILL.md)
  — readiness gates (COMPLICATED)
- [SKILL](subskills/manage-ai-stakeholders/SKILL.md)
  — stakeholders (COMPLICATED)
- [SKILL](subskills/audit-ai-team-capabilities/SKILL.md)
  — team gaps (SIMPLE)
- [SKILL](subskills/select-ai-pm-toolkit/SKILL.md)
  — tooling (COMPLICATED)
- [validation-log](details/validation-log.md) — tier choices and
  acceptance evidence

## Review In Mind (ReviewInMindGenie)

Execute the common review loop in [review-in-mind](../skill-common/details/review-in-mind.md) before delivering.

Review lens for this skill:
- Does the routing map the request to the right sub-skill, or explicitly report the gap?
- Are near-miss requests redirected or rejected instead of being mis-routed?
- Is the chosen sub-skill actually the one that produces the requested deliverable?

## Validation (Verifiable Rewards)
1. Confirm every sub-skill directory exists and passes `quick_validate.py`.
2. Confirm each routing row in Phase 1 points to an existing sub-skill.
3. Confirm the selected sub-skill's SKILL.md was read before execution.
4. Confirm the delivered output matches the sub-skill's declared Output section.
5. Confirm no hallucinated tools, dates, or performance guarantees appear in the
   output.

## One More Thing
If anything is unclear, missing, or conflicting — the request does not map to a
sub-skill, project context is absent, or the user wants something the book does
not cover — stop and ask the user before proceeding.
