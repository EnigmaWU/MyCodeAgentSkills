---
name: manage-ai-stakeholders
description: >
  WHEN/WHERE/WHO: AI project managers and agents who must plan stakeholder
  engagement, expectation management, and adoption for an AI project.
  HOW: Map stakeholders (technical, business, compliance, executives, users),
  design communication cadence and dual-language updates, set realistic
  expectations, plan user adoption, and detect AI-impostor patterns.
  WHY: AI projects live or die by trust and translation; stakeholders with
  inflated expectations or low AI literacy derail delivery.
---

# Manage AI Stakeholders

## Who
AI project managers, scrum masters, product owners, and agents who must align
diverse stakeholders around an AI project.

## What
Produce a stakeholder engagement plan:

- stakeholder map with interests, concerns, and communication needs;
- communication cadence (sprint reviews, weekly summaries, one-on-ones);
- dual-language translation approach (technical <-> business);
- expectation management strategy (probabilistic outcomes, "good enough");
- user adoption plan (UX interviews, testing, demos, training);
- AI-impostor red flags and how to redirect to evidence.

## When
Trigger when the user asks to: "manage AI stakeholders", "set stakeholder
expectations", "deal with a difficult client", "improve AI project
communication", "plan user adoption", or "handle AI hype".

## Where
Works from project context: stakeholder list, project plan, and communication
channels. Output is a stakeholder plan.

## Why
The book positions the AI PM as translator, orchestrator, and expectation
manager: stakeholders speak different languages, AI outcomes are probabilistic,
and hype inflates expectations. A structured plan keeps alignment durable.

## Inputs
- **Stakeholder list** (required or to be identified): executives, clients,
  technical team, compliance, end users.
- **Project context** (required): scope, uncertainty level, key risks.
- **Communication channels** (optional): existing meetings, tools.

## Output (Logical Evidence)
- Stakeholder plan with: role map, per-stakeholder communication approach,
  cadence, expectation-setting tactics, adoption activities, and red-flag
  responses.

## Optimization Readiness
- **Failure Signals**: Plan ignores a stakeholder group; communication is
  one-directional; expectations remain inflated; adoption left to the end;
  plan cannot detect AI-impostor behavior.
- **Evidence To Collect**: Stakeholder feedback; misalignment incidents;
  adoption blockers.
- **Safe Mutation Boundaries**: Communication templates, cadence, and plan
  format may change. Translation, expectation grounding, and early adoption
  must remain.
- **Acceptance Criteria**: A revision must produce a plan covering all
  stakeholder groups with cadence and adoption steps.
- **Rejected Revision Handling**: Record rejected engagement tactics in the
  umbrella's validation log.
- **Transfer Check**: Must work for internal and client projects.
- **Stop Rule**: If the stakeholder list or project context is missing, stop and
  ask.

## Constraints (Logical Boundaries)
- Translate technical results into business language and vice versa; never
  let jargon substitute for understanding.
- Ground expectations in scenarios, thresholds, and trade-offs, not promises.
- Protect the technical team from context switching and external pressure.
- Bring compliance/legal in early, not after development.
- **Anti-Pattern Mapping**:
  - MUST NOT promise 100% accuracy or fixed dates for model outcomes.
  - MUST NOT let "we will explain it in the demo" replace clear communication.
  - MUST NOT dismiss ethical concerns or let vague ethics block progress
    without concrete evidence.

## One More Thing
If the stakeholder list or project context is missing, stop and ask before
building the plan.

## How (Structural Workflow)

### Phase 1: Map stakeholders
1. List stakeholder groups: data scientists/AI engineers, MLOps/DevOps,
   product owners/business, legal/compliance/ethics, sponsors/executives,
   end users.
2. For each: interests, success criteria, concerns, preferred communication
   style, and level of AI literacy.

### Phase 2: Design communication
1. Set cadence: sprint reviews/demos, weekly summaries, one-on-ones/office
   hours, centralized documentation.
2. Prepare dual-language updates: technical summary for engineers, business
   summary for executives/clients.
3. Define escalation paths and decision owners.

### Phase 3: Manage expectations
1. Reframe AI outcomes as probabilistic: scenarios, ranges, thresholds.
2. Educate stakeholders on AI basics (capabilities and limits) and on the
   cost of moving from "good" to "near perfect".
3. Manage hype: tie every claim to a metric or demo.

### Phase 4: Plan adoption
1. Run UX interviews early; build mockups/prototypes.
2. Schedule at least two testing/feedback cycles.
3. Plan demos, training, and human-in-the-loop controls.

### Phase 5: Detect and redirect AI impostors
1. Watch for red flags: dominating without substance, catchphrases, confusing
   fundamentals, blocking with risks, politics, legacy-tool defense, vague
   ethics.
2. Redirect to evidence: metrics, data, requirements, and concrete decisions.

### Phase 6: Validate
1. Confirm every stakeholder group has an engagement approach.
2. Confirm expectation-setting and adoption steps exist.
3. Deliver the plan.

## Validation (Verifiable Rewards)
1. All stakeholder groups are mapped with interests and communication needs.
2. Communication cadence is explicit.
3. Expectation management includes thresholds and scenario framing.
4. Adoption plan includes early user involvement and training.
5. Red-flag list is included and actionable.
