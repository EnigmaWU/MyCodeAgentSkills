---
name: implement-agent-reflection
description: >
  WHEN/WHERE/WHO: [Scheduling: Agents or architects designing self-correcting loops for LLM-based tasks where high-quality output is critical.]
  HOW: [Structural: Use this SKILL to set up an Evaluator-Generator loop, explicitly separating the generation logic from the critique logic.]
  WHY: [Scheduling: Single-shot LLM outputs often contain subtle flaws. Reflection forces the agent to critique its own work before returning the final result, dramatically improving quality while preventing infinite token burn.]
---

# Implement Agent Reflection

## Common Contract (Load First)

When this skill is activated, first load [skill-common](../skill-common/SKILL.md) and apply the shared conventions it defines: canonical section order, frontmatter rules, anti-pattern guidance, and the Review In Mind loop in [review-in-mind](../skill-common/details/review-in-mind.md). This skill adds only domain-specific rules below.

## Who
Architects, principal developers, or coding agents designing self-correcting workflows for autonomous systems.

## What
Implement an Evaluator-Generator pattern where an initial output is systematically critiqued by a distinct reflection node, yielding actionable feedback that is fed back into the generator for iterative refinement.

## When
- Triggered by requests like: "add reflection to this agent", "make this prompt self-correcting", or "implement an evaluator-generator loop".
- Do not use for simple deterministic tasks (like basic data formatting) where a single API call is sufficient.

## Where
Applies to LangChain/LangGraph orchestrations, Google ADK topologies, or custom Python agent frameworks.

## Why
Large Language Models excel at critiquing content. By explicitly asking an agent (or a separate model) to critique an initial draft against strict acceptance criteria, the system can self-correct logical errors, hallucinations, and formatting mistakes before the user ever sees them.

## Inputs
- **Base Generator Prompt**: The original instructions for generating the artifact.
- **Evaluation Criteria**: The strict rubric or rules the critique node must enforce.
- **Max Iterations Limit**: A hard limit (e.g., `3`) to prevent infinite looping.

## Output (Logical Evidence)
- **Reflective Orchestration Code**: LangGraph or ADK logic containing distinct `generate` and `reflect` nodes.
- **State Schema**: A schema including a `critique` field and a `retry_count` integer.

## Optimization Readiness
- **Failure Signals**: Reflection loops become open-ended, critique prompts collapse into generic feedback, generator and reflector share the same role framing, or revisions do not measurably improve output quality.
- **Evidence To Collect**: Critique logs, retry counts, before/after drafts, rubric results, and examples where reflection caught or missed specific defects.
- **Safe Mutation Boundaries**: Refine rubric prompts, retry policy wording, state-schema details, and validation examples without changing the core generator-plus-reflector loop.
- **Acceptance Criteria**: Accept revisions only if the workflow enforces a hard iteration limit, uses distinct prompts, and produces drafts that improve against explicit evaluation criteria.
- **Rejected Revision Handling**: Record vague critique styles, ineffective retry behaviors, and rubric gaps so they are not reused blindly.
- **Transfer Check**: Confirm the workflow still works for both formatting corrections and deeper factual or logical critique scenarios.
- **Stop Rule**: If the evaluation rubric or retry ceiling is missing, stop and ask before building a reflection loop.

## Constraints (Logical Boundaries)
- **Hard Iteration Limit**: The workflow MUST include a strictly enforced loop limit. If the `retry_count` hits the limit, the loop must break and return the best effort.
- **Separate Prompts**: The generation and reflection phases must use explicitly different system prompts.

## One More Thing
If the user has not provided the explicit Evaluation Criteria (the "rubric"), stop and ask them what the reflection node should be looking for.

---

## How (Structural Workflow)

### 1. Define the State Schema
- Define a typed state dictionary (or Pydantic model) that holds the `draft_output`, the `critique_feedback`, and a `retry_count`.

### 2. Implement the Generator Node
- Write the node that takes the original prompt and any existing `critique_feedback`.
- If `critique_feedback` exists, the generator must explicitly address the critique in its new draft.

### 3. Implement the Reflection Node
- Write a distinct node that acts as a harsh, objective reviewer.
- Provide the Reflection node with the strict Evaluation Criteria.
- The Reflection node must output two things:
  1. A boolean flag `is_acceptable`.
  2. A string `critique_feedback` containing specific, actionable directives for fixing flaws.

### 4. Wire the Conditional Edge
- Route the Generator to the Reflection node.
- Route the Reflection node:
  - If `is_acceptable == true`, route to `__END__`.
  - If `retry_count >= MAX_RETRIES`, route to `__END__` (or a fallback handler).
  - Otherwise, increment `retry_count` and route back to the Generator.

### 5. Validate the Loop
- Ensure the state schema is correctly passed and mutated at each step.
- Verify that the iteration limit is not off-by-one.

## Review In Mind (ReviewInMindGenie)

Execute the common review loop in [review-in-mind](../skill-common/details/review-in-mind.md) before delivering.

Review lens for this skill:
- Is the evaluator distinct from the generator, with specific and actionable critique feedback?
- Are conditional edges and retry limits correct (no off-by-one, no infinite loop)?
- Would a genuinely bad output fail the evaluator and produce usable feedback?
