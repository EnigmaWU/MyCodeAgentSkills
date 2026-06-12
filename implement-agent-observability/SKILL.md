---
name: implement-agent-observability
description: >
  WHEN/WHERE/WHO: [Scheduling: Developers or DevOps engineers deploying autonomous agents to production who need to monitor costs and behavior.]
  HOW: [Structural: Use this SKILL to inject trace IDs, token tracking, and structured logging into all agent tool calls and state transitions.]
  WHY: [Scheduling: Agents are non-deterministic black boxes. Without observability, debugging an infinite loop or a hallucinated tool call in production is impossible.]
---

# Implement Agent Observability

## Who
Developers, DevOps engineers, and coding agents preparing to move autonomous LLM systems from prototype into production environments.

## What
Design and implement structured trace logging, token counting, cost tracking, and loop-detection limits across the entire agentic system architecture.

## When
- Triggered by requests like: "add observability to this agent", "track tokens for this LangGraph", "how do I debug this agent?", or "implement agent logging".
- Mandatory before deploying any agentic loop that executes tools or incurs variable API costs.

## Where
Applies to orchestration frameworks, LLM client wrappers, and tool execution decorators in the workspace.

## Why
When a traditional app crashes, you get a stack trace. When an agent fails, it might quietly burn $5 in API costs running the same failed `git` command 500 times. Implementing deep observability (like LangSmith, OpenTelemetry, or custom structured logging) is the only way to debug autonomous behavior and prevent financial runaway.

## Inputs
- **Current Architecture**: The orchestration framework being used.
- **Monitoring Stack**: The target logging system (e.g., Datadog, LangSmith, local JSON lines).

## Output (Logical Evidence)
- **Instrumentation Code**: Wrappers, callbacks, or decorators injected into the agent graph.
- **Telemetry Schema**: The specific metadata logged per event (Trace ID, Step, Token Usage, Tool Status).

## Constraints (Logical Boundaries)
- **PII Scrubbing**: Ensure sensitive user prompts or environment variables (like API keys) are masked before they are sent to the telemetry backend.
- **Strict Parent-Child Tracing**: Every sub-agent call or tool execution MUST carry the `trace_id` of the root user request to allow full waterfall reconstruction.

## One More Thing
If the requested agent logic does not have a strict `max_iterations` counter built into its state schema, stop and force the implementation of loop limits before adding observability.

---

## How (Structural Workflow)

### 1. Establish the Trace ID Hierarchy
- Generate a unique `RunID` or `TraceID` at the absolute start of the user request.
- Pass this ID down into the state schema so every node, sub-agent, and tool has access to it.

### 2. Wrap LLM Calls
- Implement callbacks or use built-in handlers (like LangChain's `BaseCallbackHandler`) to intercept every LLM request and response.
- Log the exact prompt sent, the raw response received, and the `usage` metadata (Prompt Tokens, Completion Tokens, Total Cost).

### 3. Decorate Tool Executions
- Wrap every tool function with a logging decorator.
- The log MUST capture: Tool Name, Input Arguments (scrubbed), Execution Time (latency), and the Output/Exception returned.
- Example structure: `[TRACE_ID][TOOL][START] name=search_web args={"query": "React 19"}` -> `[TRACE_ID][TOOL][END] status=success duration=1.2s`

### 4. Implement State Transition Logging
- If using a DAG orchestrator (like LangGraph), log every state mutation.
- "Node X completed. Next Node: Y. State updated with 2 new messages." This allows developers to replay the exact graph traversal.

### 5. Validate the Telemetry
- Run a simulated failure (e.g., pass a bad argument to a tool intentionally).
- Verify that the trace correctly captures the LLM decision, the tool failure, and the LLM's recovery attempt, all linked under a single Trace ID.
