# Design Agents Using Patterns

An agent skill for designing, implementing, and verifying robust agentic system architectures using the 21 patterns from *Agentic Design Patterns: A Hands-On Guide to Building Intelligent Systems* by Antonio Gulli.

## What Is This

This skill guides coding agents and system architects in selecting, designing, and orchestrating intelligent agents. Instead of writing ad-hoc prompts or unconstrained loops, this skill enforces structured patterns—such as Routing, Parallelization, Reflection, Tool Use, Planning, Multi-Agent Collaboration, and Exception Handling/Recovery—to build reliable, deterministic, and self-correcting AI systems.

## TOP-3 Golden Rules of Agentic Design

Developers and agents using this skill must strictly follow these three critical principles:

1.  **Loop Safety Boundaries**
    *   *Rule*: Never build an agentic loop (reflection, self-correction, or planning iteration) without a hard-coded maximum iteration limit (e.g., max 3 or 5 retries) and an explicit, non-agentic fallback handler.
    *   *WHY*: Large language models are non-deterministic. When encountering a compiler block or validation failure, they can oscillate or loop indefinitely trying the same correction. This results in runaway token spend, API rate-limiting, and high monetary cost.
2.  **Shell Sandboxing & User Approval Gates**
    *   *Rule*: Never execute write operations, file deletions, or terminal shell commands without running inside a virtualized sandbox (e.g. Docker container, dev container) or requiring an explicit human-in-the-loop approval gate.
    *   *WHY*: Autonomous coding agents operate with the host machine's user permissions. Destructive commands (e.g., recursive deletes) or security-compromising scripts can run unchecked if they are not constrained by sandboxes or manual verification cards.
3.  **Memory Scoping & Event-driven State Integrity**
    *   *Rule*: Never mutate the session state directly outside the runner's event processing cycle, and always partition state namespaces using prefix scopes (e.g. `user:`, `app:`, `temp:`).
    *   *WHY*: Direct state dictionary mutations bypass the event log, making execution traces impossible to audit or roll back. Cross-session leakage (e.g. user details escaping to global scopes) creates severe data privacy hazards and non-deterministic behavior.

## Directory Structure

```text
design-agents-using-patterns/
  ├── SKILL.md                                 # Level-1: Main skill workflow (COMPLEX tier)
  ├── README.md                                # Overview and usage instructions
  └── details/                                 
      ├── pattern-checklists.md                # Level-2/3: Actionable checklists for core patterns
      └── code-examples.md                     # Level-3: Code examples for LangChain/LangGraph and Google ADK
```

## Why This Method Matters

Building reliable agentic systems requires moving beyond simple linear prompt generation. By structuring LLM interactions with proven patterns, this skill guarantees:
1. **Deterministic Flows**: Enforcing state management, routing, and boundaries to keep execution predictable.
2. **Resilience**: Implementing proactive error detection, fallbacks, retries, and escalation procedures to handle tool failures gracefully.
3. **Loop Bounds & Safety**: Enforcing exit criteria and safety limits to prevent runaway loops, token depletion, or recursive call explosions.
4. **Clean Delegation**: Structuring multi-agent coordinator-specialist teams with clear interfaces, shared state schemas, and distinct responsibilities.

## Usage

When designing, implementing, or reviewing an agentic system, invoke this skill using trigger phrases such as:
* *"design agents using patterns to..."*
* *"design a multi-agent system for [task]"*
* *"implement a self-correcting prompt chain for..."*
* *"design a router for these sub-agents"*
* *"evaluate the resilience of this agentic architecture"*

The agent will read the core checklists in `details/` and write compliant orchestration architectures using standard libraries (such as LangChain/LangGraph or Google ADK).
