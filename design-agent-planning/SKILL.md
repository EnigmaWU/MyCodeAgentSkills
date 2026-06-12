---
name: design-agent-planning
description: >
  WHEN/WHERE/WHO: [Scheduling: Agents or architects designing systems capable of handling complex, multi-step tasks that require forward thinking.]
  HOW: [Structural: Use this SKILL to implement ReAct (Reason + Act) or Plan-and-Solve workflows, decoupling task decomposition from task execution.]
  WHY: [Scheduling: LLMs struggle with long horizons. Explicit planning breaks a massive goal into digestible, verifiable steps, drastically reducing failure rates on complex tasks.]
---

# Design Agent Planning

## Who
Architects, AI engineers, or coding agents building orchestrations that must solve complex, multi-step goals autonomously.

## What
Design and implement a Planning pattern where a Planner agent explicitly decomposes a high-level goal into a sequence of atomic sub-tasks (a Plan) before any execution begins.

## When
- Triggered by requests like: "design a planning agent", "implement a plan-and-solve workflow", or "use ReAct to solve this multi-step problem".
- Do not use for linear, single-step tasks (e.g., translation, summarization).

## Where
Applies to agent orchestration code, especially frameworks supporting directed acyclic graphs (DAGs) like LangGraph or explicit loop chains.

## Why
Without a plan, agents often suffer from "context drift" or get stuck in repetitive tool-calling loops because they lose track of the overarching goal. Explicit planning forces the agent to generate a "roadmap", making the subsequent execution steps highly focused and much less prone to hallucination.

## Inputs
- **High-Level Goal**: The complex task to solve.
- **Available Tools/Specialists**: The capabilities the planner can delegate to.

## Output (Logical Evidence)
- **Planner Orchestration Code**: Code that implements a Planner node, an Executor loop, and a Replanner (if dynamic).
- **Plan Schema**: A Pydantic model or TypedDict defining a list of `SubTask` objects.

## Constraints (Logical Boundaries)
- **Atomic Sub-tasks**: The Planner must break tasks down into steps that can be completed by a single tool call or a single specialist agent.
- **State Validation**: The plan must be stored in the state explicitly so the Executor can cross them off one by one.

## One More Thing
If it is unclear what tools the agent has access to, stop and ask the user to clarify the tools before designing the planner.

---

## How (Structural Workflow)

### 1. Define the Plan Schema
- Create a strict schema for the plan (e.g., a `Plan` object containing a list of `steps`, where each step has a `description` and a `status`).

### 2. Implement the Planner Node
- Write the system prompt for the Planner. It must understand the High-Level Goal and the available tools.
- Force the Planner to output structured JSON matching the Plan Schema.

### 3. Implement the Executor Node(s)
- The Executor node looks at the current state, picks the *next incomplete step* from the plan, and attempts to execute it.
- After execution, the Executor updates the state to mark the step as complete and appends the result to a `scratchpad` or `memory`.

### 4. (Optional) Implement the Replanner
- For highly dynamic environments, implement a Replanner node that evaluates the execution results. If an execution failed or new information was discovered, the Replanner alters the remaining steps in the plan.

### 5. Wire the Workflow
- Route: Planner -> Executor.
- Route: Executor -> Replanner (or loop back to Executor if static).
- Add conditional edges to exit when all steps in the plan are marked complete.
