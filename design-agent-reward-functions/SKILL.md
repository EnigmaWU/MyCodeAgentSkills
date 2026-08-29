---
name: design-agent-reward-functions
description: >
  WHEN/WHERE/WHO: [Scheduling: Use when designing the exit criteria and validation logic for an autonomous AI agent's execution loop.]
  HOW: [Structural: Use this SKILL to translate classic BDD Gherkin scenarios into Verifiable Reward Functions that act as hard constraints.]
  WHY: [Scheduling: Autonomous agents suffer from reasoning drift and hallucinations. Explicit Given/When/Then boundary checks prevent runaway execution.]
---

# Design Agent Reward Functions

## Common Contract (Load First)

When this skill is activated, first load [skill-common](../skill-common/SKILL.md) and apply the shared conventions it defines: canonical section order, frontmatter rules, anti-pattern guidance, and the Review In Mind loop in [review-in-mind](../skill-common/details/review-in-mind.md). This skill adds only domain-specific rules below.

## Who
AI Agents, Test Engineers, and System Architects building autonomous execution loops.

## What
Elevates classic BDD Gherkin into strict boundary constraints (Reward Functions) for autonomous agents. It forces the creation of deterministic `Given/When/Then` checks that act as the exact exit criteria for an agent, ensuring it stops executing once the goal is achieved, and preventing it from hallucinating success.

## When
Invoke this skill when defining the "Done" state for an agentic task, when an agent loop is suffering from infinite recursion, or when you need to formally specify the success criteria for an autonomous workflow.
*Near-miss*: Do not use this to write UI testing scripts (use `write-declarative-executable-specifications` instead).

## Where
Applies to the validation phase of an agentic workflow, typically within the `Evaluation` or `Verification` node of a state machine (e.g., LangGraph).

## Why
In classic SE, Gherkin was a communication tool for humans. In Agentic SE, Gherkin is the mathematical boundary that stops an agent from drifting. Without a Verifiable Reward Function, an agent relies on internal self-reflection to determine success, which is highly prone to hallucination.

## Inputs
- **Agent Task**: The goal the agent is attempting to achieve.
- **System State**: The expected state of the system after execution.

## Output (Logical Evidence)
- A deterministic `Given/When/Then` scenario.
- A mapped set of programmatic checks (the "Verifiable Reward") that correspond to the `Then` clauses.

## Optimization Readiness
- **Failure Signals**: Reward definitions remain subjective, `Then` clauses cannot be observed programmatically, the agent is allowed to self-certify success, or the scenario omits critical preconditions.
- **Evidence To Collect**: Given/When/Then scenarios, mapped checks, failed validations, and examples where a reward function caught or missed execution drift.
- **Safe Mutation Boundaries**: Refine scenario wording, reward-mapping guidance, and deterministic check examples without changing the core requirement that success be externally verifiable.
- **Acceptance Criteria**: Accept revisions only if every success condition maps to observable evidence and the workflow rejects subjective or purely LLM-based validation.
- **Rejected Revision Handling**: Record weak `Then` clauses, pseudo-deterministic checks, and self-evaluation shortcuts so they are not repeated.
- **Transfer Check**: Verify the workflow still works for file, API, and database state changes rather than only one verification medium.
- **Stop Rule**: If the task goal cannot be tied to programmatic evidence, stop and tell the user the workflow lacks a safe reward function.

## Constraints (Logical Boundaries)
- **Observable Evidence**: Every `Then` clause MUST correspond to an observable state change in the system (e.g., a file written, a database row added, an API 200 OK response).
- **Anti-Pattern Mapping**: 
  1. DO NOT use subjective or qualitative `Then` clauses (e.g., `Then the code should be clean`).
  2. DO NOT allow the agent to evaluate its own success purely via an LLM call. The reward MUST be verified by a deterministic tool or script.

## One More Thing
If the expected outcomes cannot be programmatically verified, stop and inform the user that the task lacks a Verifiable Reward and is unsafe for autonomous execution.

## How (The 4-Phase Refinement Protocol)
<Use imperative state-machine logic. Every phase must explicitly define branching (If/Then/Else).>

### Phase 1: Define the Context (Given)
**Input State**: An Agent Task.
1. Determine the necessary preconditions for the agent to begin execution.
2. Formulate these as `Given` statements.
**Output State**: A deterministic starting state.

### Phase 2: Define the Action (When)
**Input State**: Preconditions defined.
1. Define the specific action or sequence of actions the agent will perform.
2. Formulate this as a `When` statement. Ensure it describes *what* the agent does, not *how* it does it.
**Output State**: The core action defined.

### Phase 3: Define the Verifiable Reward (Then)
**Input State**: Action defined.
1. Identify the observable, programmatic evidence that proves the action was successful.
2. Formulate these as `Then` statements.
3. *Branch*: If a `Then` statement relies on subjective evaluation (e.g., an LLM checking its own work), reject it and demand a deterministic check.
**Output State**: A set of Verifiable Rewards.

### Phase 4: Construct the Exit Condition
**Input State**: Verifiable Rewards defined.
1. Wrap the `Then` statements into a script or tool that returns a boolean `True/False` (or a specific score).
2. Inject this script into the agent's evaluation loop as the hard exit condition.
**Output State**: A hardened agent execution loop protected against reasoning drift.

## Review In Mind (ReviewInMindGenie)

Execute the common review loop in [review-in-mind](../skill-common/details/review-in-mind.md) before delivering.

Review lens for this skill:
- Are reward functions strict Given/When/Then checks that can be evaluated deterministically?
- Do they include stop conditions that prevent hallucinated success?
- Is there an exit criterion for every terminal state (success, failure, retry)?

## Validation (Verifiable Rewards)
1. Verify that all `Then` statements can be executed by a deterministic script without human or LLM intervention.
2. If verification passes, output the Verifiable Reward Function definition.
