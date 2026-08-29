---
name: orchestrate-multi-agent-collaboration
description: >
  WHEN/WHERE/WHO: [Scheduling: Agents or architects designing systems where distinct domain experts must collaborate to produce a final result.]
  HOW: [Structural: Use this SKILL to design a Supervisor or Coordinator-Specialist topology, defining clear message passing and state boundaries.]
  WHY: [Scheduling: A single prompt cannot hold deep expertise across multiple conflicting domains (e.g., Security vs. Performance). Multi-agent patterns separate concerns.]
---

# Orchestrate Multi-Agent Collaboration

## Who
Architects, AI engineers, or coding agents designing multi-agent systems for complex domains requiring varied expertise.

## What
Design a collaborative topology (e.g., Supervisor-Worker, Hierarchical Teams, or Peer-to-Peer Debate) where distinct agents with specialized system prompts and tools interact to achieve a joint objective.

## When
- Triggered by requests like: "build a multi-agent system", "design a supervisor architecture", or "create a team of agents".
- Use when the problem requires conflicting perspectives (e.g., a "Coder" agent and a "Security Reviewer" agent).

## Where
Applies to agent orchestration code (LangGraph, AutoGen, CrewAI, or ADK).

## Why
Generalist agents degrade in performance when given too many tools and too many competing instructions. By giving distinct "personas" to different agents (one for writing code, one for testing, one for documentation), the system performs vastly better. The Supervisor pattern ensures these experts don't talk over each other in an infinite loop.

## Inputs
- **System Goal**: The overall task to complete.
- **Agent Roster**: The list of desired specialists (e.g., Researcher, Coder, Reviewer).

## Output (Logical Evidence)
- **Topology Map**: A visual or structured definition of how agents communicate.
- **Orchestration Code**: The implementation of the Supervisor router and the Specialist nodes.

## Optimization Readiness
- **Failure Signals**: Specialists overlap responsibilities, routing loops repeat without progress, shared state becomes inconsistent, or the team design grows flat and unmanageable.
- **Evidence To Collect**: Routing traces, agent prompts, state transitions, loop counts, and examples of handoffs that succeeded or caused debate cycles.
- **Safe Mutation Boundaries**: Refine role definitions, supervisor options, state-schema details, and escalation rules without changing the core supervisor-plus-specialist collaboration model.
- **Acceptance Criteria**: Accept revisions only if the design yields clear role boundaries, finite collaboration loops, and a shared state that supports predictable handoffs.
- **Rejected Revision Handling**: Record duplicate role designs, weak router choices, and failed debate-loop controls so they are not reused blindly.
- **Transfer Check**: Confirm the workflow still supports both small specialist teams and hierarchical multi-supervisor designs.
- **Stop Rule**: If the roster, state ownership, or finish conditions are unclear, stop and resolve them before adding more agents.

## Constraints (Logical Boundaries)
- **No Infinite Debates**: Peer-to-peer or reflection loops between agents MUST have a strict turn limit (e.g., max 3 rounds of back-and-forth).
- **Single Source of Truth**: There must be a shared state object that tracks the conversation history and the current artifacts.

## One More Thing
If the user asks for more than 5 distinct agents in a single flat team, pause and suggest a hierarchical design (multiple supervisors) to prevent context window explosion and routing chaos.

---

## How (Structural Workflow)

### 1. Define the Agent Roster and Prompts
- Identify the exact roles needed.
- Write highly focused, narrow system prompts for each specialist. Do not give the Coder instructions about formatting documentation; leave that to the Documenter.

### 2. Design the State Schema
- Define a shared state (e.g., a dictionary holding `messages`, `current_artifact`, and `next_speaker`).

### 3. Implement the Supervisor (Router) Node
- The Supervisor is an LLM node (or strict rule-engine) responsible for looking at the current state and deciding *who speaks next*.
- The Supervisor must have a strict set of options (e.g., `["Coder", "Reviewer", "FINISH"]`).

### 4. Implement the Specialist Nodes
- Each Specialist reads the shared state, performs its task, and appends its output to the `messages` list.
- A Specialist does not decide who goes next; it only passes control back to the Supervisor.

### 5. Wire the Graph
- Connect all Specialists back to the Supervisor.
- Add a conditional edge from the Supervisor to the chosen Specialist, or to the `__END__` node if the task is complete.

## Review In Mind (ReviewInMindGenie)

Before delivering, activate the ReviewInMindGenie: stop authoring, switch to a skeptical reviewer, and critique the artifact as if someone else had produced it.

1. **Review Against Own Rules**: Re-read the output against this skill's `What`, `Constraints (Logical Boundaries)`, and `Validation` criteria. Check each rule explicitly; do not assume it passed because it was easy to write.
2. **Classify Findings**: Label each defect as BLOCKER (output unusable), MAJOR (violates a core rule), or MINOR (polish/consistency).
3. **Fix or Escalate**: Fix BLOCKER and MAJOR findings immediately when the fix is unambiguous. After each fix, re-check the affected criteria. If a finding cannot be fixed without new input (missing evidence, conflicting requirements, or a user decision), do not guess — report it as an open question or known gap.
4. **Deliver with a Review Note**: Present the output with a short note: what was checked, what was fixed, and what remains as a known gap. Never present an unreviewed artifact as final.

Review lens for this skill:
- Is the collaboration topology justified by the joint objective rather than a default pattern?
- Are roles, tools, message schemas, and termination conditions explicit?
- Would the routing prevent loops and deadlocks as written?
