---
name: design-agents-using-patterns
description: 'Use when: designing a multi-agent system, creating routing logic, building self-correcting prompt chains, or adding tool-use and planning capabilities. Helps with: selecting appropriate agentic patterns, structuring coordinator-specialist teams, implementing exception handling, and preventing runaway LLM loops. Applies to: orchestration scripts, agent system designs, and prompt chain configurations in the workspace.'
---

# Design Agents Using Patterns

> [!IMPORTANT]
> **TOP-3 Golden Rules of Agentic Design (Must be followed by all invoking agents):**
> 1. **Loop Safety Boundaries**: Never configure an agent loop (Reflection, Planning, or Exception Recovery) without a hard-coded maximum iteration limit (e.g., max 3 or 5 retries).
>    * *WHY*: Non-deterministic LLM behaviors can result in infinite correction/compilation loops, leading to token exhaustion and extreme API costs.
> 2. **Shell Sandboxing & User Approval**: Never execute write operations, file deletions, or terminal shell commands without running inside a virtualized container (e.g. Docker, dev container) or requesting explicit human user approval.
>    * *WHY*: Autonomous agents carry user-level shell privileges; unconstrained command executions can cause catastrophic system failures or code security violations.
> 3. **Memory Scoping & Event Integrity**: Never mutate the session state directly outside the runner's event processing cycle, and always partition state namespaces using prefixes (`user:`, `app:`, `temp:`).
>    * *WHY*: Direct dictionary mutation bypasses event history logs, making rollbacks and trace audits impossible. Scoping namespaces prevents cross-session variables pollution.
 
## Who
Architects, system developers, or coding agents who need to design and orchestrate reliable, autonomous, and self-correcting agent systems.
 
## What
Analyze functional goals, select the appropriate pattern(s) (e.g., Routing, Reflection, Multi-Agent Collaboration), design the state schema and node topology, build exception handling guards, and implement/verify the code using LangChain/LangGraph or Google ADK.
 
## When
- Triggered by requests like: "design agents using patterns to...", "design a multi-agent system for...", "implement a self-correcting prompt chain for...", "design a router for these sub-agents", or "evaluate the resilience of this agentic architecture".
- Do not use for simple static scripting, simple template prompts that do not involve loops, routing, or tool calls, or basic API calls lacking autonomous logic.

## Where
Applies to orchestration files, state graphs, system architecture documents, and agent scripts in the workspace.

## Why
- Unstructured agent calls are non-deterministic, fragile, and prone to complete failure when tools or APIs fail.
- Agents can enter infinite loops (e.g., failing the same tool over and over) or incur excessive API costs unless explicitly bound by iteration limits and clear exit conditions.
- Standardizing the orchestration structures (using templates for LangChain/LangGraph and Google ADK) keeps the codebase readable, maintainable, and robust.

## Inputs
- **System Goal & Requirements** (required): The specific tasks or workflow the agentic system must complete.
- **Tools & API Specs** (optional): Capabilities and functions the agents can invoke.
- **Pattern Checklists Reference** (required): Located at [pattern-checklists.md](details/pattern-checklists.md).
- **Framework Target** (optional): The target framework (e.g., LangChain/LangGraph, Google ADK, or raw Python).
- **Agentic Design Patterns Book** (optional): Reference book unpacked at [Agentic Design Patterns.epub](../TMP/Agentic%20Design%20Patterns.epub).

## Output
- **Agentic System Architecture Specification**: Visual/textual mapping of agent nodes, state schema, routing rules, and fallback paths.
- **Orchestration Source Code**: Executable code (e.g., using LangChain `RunnableBranch` or Google ADK `Agent`/`SequentialAgent`) that implements the designed topology.
- **Resilience Log**: Documentation detailing loop iteration limits, error handling guards, and fallback conditions.

## Constraints
- **Runaway Loop Protection**: Every agentic loop (Reflection, Planning, or Exception Recovery) must have a strict, hard-coded maximum iteration limit (e.g., maximum 3 or 5 retries) to prevent runaway token spend.
- **No Silent Failures**: All tool errors, API timeouts, or parsing exceptions must be caught, logged, and routed through a defined recovery or escalation path.
- **Schema Validation**: All data passed between agents or tools must be validated against a strict state schema (e.g., Pydantic models or typed state dictionaries).

## One More Thing
If the primary model options, tool schemas, or maximum token/cost budgets are undefined or conflicting, stop and ask the user to clarify before writing the orchestration code.

---

## How

### Phase 1: Analyze & Select Patterns
1. Identify the complexity and requirements of the target system:
   * **Linear & Predictable**: Select *Prompt Chaining*.
   * **Branching & Intent-Driven**: Select *Routing* (LLM-based, semantic, or rule-based).
   * **Resource / Time Intensive**: Select *Parallelization* (fork-join execution).
   * **Quality-Critical**: Select *Reflection & Self-Correction* (evaluator-generator loop).
   * **Complex, Multi-step / Multi-Domain**: Select *Multi-Agent Collaboration* (Coordinator-Specialist or Supervisor architecture) or *Planning*.
2. Review the detailed pattern guidelines and checklist details in [pattern-checklists.md](details/pattern-checklists.md).
3. Draft a conceptual design mapping the workflow.

### Phase 2: Define State Schema & Node Topology
1. Design the **Shared State Schema**:
   * Determine what information must persist across agent nodes (e.g., `user_query`, `history`, `retrieved_docs`, `current_step`, `error_flag`, `retry_count`).
   * Define type definitions and validate using Pydantic or native typing.
2. Define the **Node Topology**:
   * List each agent node (e.g., `Classifier`, `Planner`, `Coder`, `Validator`) and tool-execution node.
   * Define the edge conditions: direct sequential transitions, conditional transitions (routers), and loops (reflection).

### Phase 3: Design Robustness & Exceptions (Chapter 12)
1. Incorporate **Exception Handling and Recovery** rules:
   * **Error Detection**: How does the system catch malformed tool outputs, API status codes, or parsing errors?
   * **Error Handling**: Implement logging of tracebacks, retries for transient errors, and fallback strategies (e.g., delegating to a general fallback handler).
   * **Recovery**: Define rollback logic for state variables and escalation pathways to notify a human operator or return a graceful failure message.
2. Define loop exit conditions: enforce a hard limit on `retry_count` or `iteration_limit`.

### Phase 4: Implement & Verify Orchestration
1. Select the template implementation from [code-examples.md](details/code-examples.md) that matches your framework (Google ADK or LangChain/LangGraph).
2. Write the orchestration code, ensuring the system state is updated cleanly at each node.
3. Validate the implementation:
   * **Common Rationalization Check**: If you think "this tool will never fail, so I don't need a try-except block," stop and remember: *In real-world settings, APIs time out and tools return unexpected schemas. Wrap all tool executions in a try-except structure and handle the failure gracefully.*
   * **Red Flags Check**: Look for missing loop limits, unhandled exceptions, or raw unstructured dictionary mutations without schemas.

---

## Resources
- [pattern-checklists.md](details/pattern-checklists.md) - Actionable checklists for each design pattern.
- [code-examples.md](details/code-examples.md) - Framework templates for Google ADK and LangChain/LangGraph.
- [Agentic Design Patterns.epub](../TMP/Agentic%20Design%20Patterns.epub) - Original reference textbook.

---

## Validation
1. Verify that `SKILL.md` contains frontmatter with `name` and `description`.
2. Verify that all relative links to checklists and code examples are valid and clickable.
3. Verify that every conditional transition and loop in the design includes a defined limit and exit criteria.
4. Verify that there are zero silent failure pathways in the orchestration code.
