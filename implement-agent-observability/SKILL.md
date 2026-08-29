---
name: implement-agent-observability
description: >
  WHEN/WHERE/WHO: [Scheduling: Developers or DevOps engineers deploying autonomous agents to production who need to monitor costs and behavior.]
  HOW: [Structural: Use this SKILL to inject trace IDs, token tracking, and structured logging into all agent tool calls and state transitions.]
  WHY: [Scheduling: Agents are non-deterministic black boxes. Without observability, debugging an infinite loop or a hallucinated tool call in production is impossible.]
---

# Implement Agent Observability

## Common Contract (Load First)

When this skill is activated, first load [skill-common](../skill-common/SKILL.md) and apply the shared conventions it defines: canonical section order, frontmatter rules, anti-pattern guidance, and the Review In Mind loop in [review-in-mind](../skill-common/details/review-in-mind.md). This skill adds only domain-specific rules below.

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

## Optimization Readiness
- **Failure Signals**: Traces cannot reconstruct a full run, telemetry leaks secrets, tool and sub-agent events lose the root trace ID, or observability is added without loop limits and simply records runaway behavior.
- **Evidence To Collect**: Sample traces, scrubbed payloads, parent-child run graphs, cost logs, and examples of failures that observability did or did not explain.
- **Safe Mutation Boundaries**: Refine event schemas, logging wrappers, scrubbing rules, and dashboard/reporting examples without changing the core trace propagation and instrumentation requirements.
- **Acceptance Criteria**: Accept revisions only if a single request can be reconstructed end to end, sensitive fields are masked, and loop or cost anomalies become observable quickly.
- **Rejected Revision Handling**: Record telemetry fields that exposed too much data, tracing gaps, and noisy logging patterns so they are not repeated.
- **Transfer Check**: Verify the workflow still works across local logs, tracing backends, and mixed sub-agent/tool execution paths.
- **Stop Rule**: If loop limits, trace propagation, or PII scrubbing cannot be guaranteed, stop and fix those boundaries before broadening telemetry.

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

## Review In Mind (ReviewInMindGenie)

Execute the common review loop in [review-in-mind](../skill-common/details/review-in-mind.md) before delivering.

Review lens for this skill:
- Do traces capture decision, tool call, state transition, token cost, and loop count under one trace ID?
- Are sensitive inputs scrubbed and are latency/cost metrics real rather than placeholders?
- Would a simulated failure be diagnosable end to end from the logs?
