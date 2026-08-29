---
name: design-autonomous-ai-interfaces
description: >
  WHEN/WHERE/WHO: Product designers, UX researchers, architects, and AI agents should use this skill when asked to design an autonomous AI interface, agentic product UX, AI copilots that plan or act, human-in-the-loop controls, AI workflow checkpoints, or interfaces for creative and autonomous AI systems. Near-miss: do not use it for backend-only agent implementation, prompt tuning alone, generic UI polish, or non-agentic chat copy unless the request explicitly needs user-facing AI interaction design.
  HOW: Use this COMPLEX SKILL to frame user intent and autonomy level, map capability and orchestration, design input/context capture, expose planning and permissions, manage progress/checkpoints/recovery, shape outputs for verification and onward action, and validate the design against shared-control criteria.
  WHY: Autonomous AI products can become opaque, over-trusting, or over-controlling when input, computation, output, and agent action are not designed as one loop. This skill keeps users oriented, empowered, and able to verify or redirect the system.
---

# Design Autonomous AI Interfaces

## Common Contract (Load First)

When this skill is activated, first load [skill-common](../skill-common/SKILL.md) and apply the shared conventions it defines: canonical section order, frontmatter rules, anti-pattern guidance, and the Review In Mind loop in [review-in-mind](../skill-common/details/review-in-mind.md). This skill adds only domain-specific rules below.

## Who
Product designers, UX researchers, AI product managers, architects, and coding agents designing user-facing AI systems that capture intent, compute or plan behind the scenes, produce outputs, and may act autonomously through tools, agents, or workflows.

## What
Designs an autonomous AI interface as a complete user-control loop: input, computation, output, planning, permissions, checkpoints, recovery, and onward action. The output is a design brief, flow, checklist, or implementation-ready UX specification that shows how users stay informed and in control while the AI assists, plans, or acts.

## When
- Use when the request includes phrases such as "design an autonomous AI interface", "agentic UX", "AI copilot workflow", "human-in-the-loop agent", "AI checkpoints", "AI planning UI", "tool-use permissions", "agent progress and rollback", or "creative/autonomous AI interface".
- Use when an AI feature needs visible planning, capability discovery, context controls, output verification, permission boundaries, or recovery from partial failures.
- Near-miss: do not use for model training, backend orchestration code, prompt engineering alone, or generic visual redesign unless the work includes user-facing AI behavior and control surfaces.

## Where
Applies to product specs, UX flows, prototypes, agentic workflow designs, AI copilots, creative AI tools, enterprise automation, developer agents, and any interface where an AI system interprets user intent, uses hidden computation, returns generated output, or performs multistep autonomous work.

## Why
Autonomous AI interfaces fail when users cannot tell what the system can do, what context it is using, why it is waiting, what it plans to do next, whether an output is trustworthy, or how to stop and recover. This skill converts the book-derived input-computation-output model into a practical design workflow that preserves shared control instead of asking the user to either micromanage or surrender.

## Inputs
- **User Job**: The user's goal, workflow, artifact, decision, or real-world action.
- **AI Role**: Whether the AI should advise, draft, plan, act with approval, or act with monitoring.
- **Capabilities**: Models, tools, data sources, retrieval paths, memory, connected services, and known limits.
- **Risk Profile**: Task stakes, reversibility, duration, cost, privacy sensitivity, compliance obligations, and external side effects.
- **Interface Context**: Platform, modality, UI constraints, existing design system, and expected user expertise.
- **Evidence**: Existing specs, screenshots, workflows, user research, failure reports, or source material when available.

## Output (Logical Evidence)
- An autonomous AI interface design brief or UX specification.
- An intent/capability/orchestration map.
- An input and context-capture model.
- A planning, progress, permissions, checkpoint, and recovery model.
- Output presentation rules for clarity, grounding, verification, actionability, and adjustability.
- A validation checklist or scenario walkthrough proving the design supports shared control.

## Optimization Readiness
- **Failure Signals**: Designs rely on a blank prompt box, hide context or tools, expose plans at the wrong granularity, overuse approvals for low-risk actions, skip approval for high-impact actions, make output look authoritative without evidence, or provide only "try again" recovery.
- **Evidence To Collect**: User journey maps, prototype walkthroughs, usability findings, support tickets, agent traces, permission prompts, error states, user edits, rollback events, and examples where users misunderstood AI capability or output confidence.
- **Safe Mutation Boundaries**: Refine trigger wording, phase prompts, checklist items, risk categories, autonomy labels, examples, and detail files without removing the input-computation-output spine or the shared-control validation gate.
- **Acceptance Criteria**: Accept revisions only if the skill still produces designs that name user intent, map capability, show context, define autonomy level, expose planning when stakes require it, manage latency, validate outputs, and preserve pause/edit/resume/rollback paths.
- **Rejected Revision Handling**: Record failed patterns such as generic "ask me anything" flows, opaque agent execution, decorative confidence scores, consent-dark-pattern permissions, and irreversible action shortcuts so future revisions do not reintroduce them.
- **Transfer Check**: Verify the workflow works for at least two different AI interface types, such as a creative drafting assistant and an enterprise automation agent.
- **Stop Rule**: If the user job, AI capabilities, or side-effect risk cannot be determined, stop and ask for the missing context before designing autonomous behavior.

## Constraints (Logical Boundaries)
- Design from the user's job and success outcome first, then map AI capability to that workflow.
- Do not make a blank prompt box carry the whole interaction when implicit context, structured fields, direct manipulation, examples, or clarifying questions would reduce ambiguity.
- Do not hide which context, files, tools, memory, assumptions, or permissions shape the result.
- Do not present fluent output as authoritative unless the interface provides grounding, sources, review paths, or uncertainty handling appropriate to the domain.
- Do not use model-generated confidence percentages as the main trust mechanism.
- Do not flood users with every internal detail. Use progressive disclosure from glanceable state to detailed records.
- Require explicit approval for external, expensive, privacy-sensitive, destructive, or hard-to-reverse actions.
- Preserve recovery paths: pause, edit direction, resume, retry from checkpoint, skip, cancel, branch, and roll back.
- **Anti-Pattern Mapping**: Avoid generic starter prompts, hidden orchestration, passive spinners for long-running work, irreversible agent actions that look like previews, vague errors, and output-only designs with no onward action.

## One More Thing
If the target user, task stakes, tool permissions, or expected AI autonomy are unclear or conflicting, stop and ask before designing the interface.

## How (Structural Workflow)

### Phase 1: Frame the User Job and Autonomy Level
**Input State**: A product idea, AI feature request, user workflow, or interface problem.
1. Name the primary user, the job to be done, the workflow start and end state, and the output or action the user values.
2. Classify the AI role: **Advise**, **Draft**, **Plan**, **Act With Approval**, or **Act With Monitoring**.
3. If the task affects people, money, production systems, private data, legal obligations, or external communication, require human review before meaningful action.
4. If the user only needs a simple answer or non-agentic chat, switch to a simpler UX/prompt workflow and do not add autonomous controls.
**Output State**: A declared user job, success outcome, risk profile, and autonomy level.

### Phase 2: Map Capability, Discovery, and Orchestration
**Input State**: A declared user job and autonomy level.
1. Inventory the model capabilities, tools, data sources, memory, retrieval paths, connected services, and known limitations.
2. Map each capability to a concrete user task. If a capability does not serve the user job, remove it from the primary flow.
3. Design capability discovery through task-specific examples, templates, controls, empty states, and mode labels.
4. Make orchestration intentional, transparent, and recognizable: show what changed when a model, tool, permission, data source, or mode changes.
5. If a required capability is absent or unreliable, design a fallback, escalation path, or refusal state rather than implying unsupported autonomy.
**Output State**: An intent-capability-orchestration map with visible user-facing controls.

### Phase 3: Design Input, Context, and Clarification
**Input State**: A capability map and target workflow.
1. Split intent capture across implicit context, explicit prompts, and direct manipulation.
2. Use the CARE structure for explicit prompts: context, action, results, and examples.
3. Show context that the AI will use, such as selected text, attached files, active workspace, source data, prior turns, or connected tools.
4. Let users add, remove, narrow, replace, or freeze context before expensive or risky computation begins.
5. If ambiguity is high and the cost of being wrong is meaningful, insert a short clarification step. If cost is low, allow execution with editable assumptions.
**Output State**: An input model that captures intent without making the user over-explain everything in text.

### Phase 4: Design Planning, Permissions, and Execution
**Input State**: An input model and AI autonomy level.
1. For multistep, high-stakes, expensive, or long-running work, expose an initial plan before execution.
2. For routine low-risk tasks, allow silent planning but keep progress and recovery visible.
3. Tune plan granularity to task complexity: short tasks need a compact outline; longer workflows need phases, dependencies, branch points, and expandable detail.
4. Define permission prompts at the moment access is needed. Each prompt must state what is accessed, why it is needed, what will happen next, and how access can be revoked.
5. If the agent delegates to tools or other agents, show delegated responsibilities at the level users need to evaluate risk and progress.
**Output State**: A plan and execution model with consent boundaries and visible delegation.

### Phase 5: Design Progress, Checkpoints, and Recovery
**Input State**: A plan and execution model.
1. Match latency feedback to duration and stakes: immediate results for subsecond work, status for short delays, and progress with estimates or step state for long-running work.
2. Layer progress communication: notification, overview status, detailed step view, and full record or trace.
3. Add checkpoints before plan approval, assumption lock-in, external action, irreversible change, low-confidence branch, or major artifact transition.
4. At each checkpoint, show what was done, what is pending, what the system is waiting for, and what options the user has.
5. Preserve rollback or branching for evolving artifacts such as documents, dashboards, code, workflows, or generated media.
6. If an error occurs, state what happened, what work was preserved, what is blocked, and what the user can do next.
**Output State**: A progress and recovery model that keeps long-running autonomy understandable and interruptible.

### Phase 6: Design Outputs and Onward Action
**Input State**: A completed or intermediate AI result.
1. Shape outputs to be clear, verifiable, grounded, actionable, and adjustable.
2. Choose presentation structures that match the task: summary, comparison, table, canvas, diff, preview, generated artifact, recommendation, or step-by-step plan.
3. Separate draft, preview, send, publish, commit, delete, and external-share actions visually and behaviorally.
4. Provide citations, source links, provenance, comparison views, review-before-act flows, or human approval where objective claims or real-world effects matter.
5. Let users revise selected parts, regenerate variants, compare versions, accept partial outputs, or turn output edits into the next input.
**Output State**: An output and action model that supports trust, editing, verification, and continuation.

### Phase 7: Validate with Scenarios and Iterate
**Input State**: A candidate autonomous AI interface design.
1. Run the checklist in [validation-checklist](details/validation-checklist.md) against the candidate design.
2. Walk through at least four scenarios: happy path, ambiguous input, tool/permission failure, and high-risk or irreversible action.
3. If validation fails and the failure is local, revise the corresponding phase and rerun the same checklist.
4. If two validation loops fail for the same missing capability, unclear risk boundary, or impossible recovery path, stop and ask for product or technical clarification.
**Output State**: A validated design brief or a clearly stated blocker with the missing decision.

## Resources
- [principles](details/principles.md) - Core principles and the input-computation-output control loop.
- [intent-capability-orchestration](details/intent-capability-orchestration.md) - Capability discovery, orchestration, and configuration guidance.
- [input-patterns](details/input-patterns.md) - Implicit context, explicit prompting, direct manipulation, and CARE prompts.
- [agentic-workflow-patterns](details/agentic-workflow-patterns.md) - Planning, delegation, branching, and autonomy-level patterns.
- [progress-checkpoints-permissions](details/progress-checkpoints-permissions.md) - Latency, progress, checkpoints, rollback, and permissions.
- [output-validation-and-recovery](details/output-validation-and-recovery.md) - Output design, grounding, verification, action, and recovery.
- [validation-checklist](details/validation-checklist.md) - Operational checklist for scenario review.

## Review In Mind (ReviewInMindGenie)

Execute the common review loop in [review-in-mind](../skill-common/details/review-in-mind.md) before delivering.

Review lens for this skill:
- Does the design close the full loop: input, computation, output, planning, permissions, checkpoints, recovery, onward action?
- Are permission gates and checkpoints placed before every risky mutation?
- Would a user remain informed and in control at every stage?

## Validation (Verifiable Rewards)
1. Verify the design names the user job, success outcome, AI role, autonomy level, and risk profile.
2. Verify every AI capability, tool, context source, memory source, and permission appears in the intent-capability-orchestration map.
3. Verify users can see and adjust the context the system uses before costly or risky computation begins.
4. Verify multistep or high-stakes workflows expose a plan, checkpoints, permission prompts, and interruption paths.
5. Verify latency feedback explains progress at the right level without exposing irrelevant internal noise.
6. Verify outputs are clear, grounded, verifiable, actionable, adjustable, and visually distinct from irreversible actions.
7. Verify the design supports pause, edit direction, resume, retry, cancel, branch, and rollback wherever autonomous work can go off course.
8. Verify at least four scenarios pass: happy path, ambiguous input, tool/permission failure, and high-risk or irreversible action.
