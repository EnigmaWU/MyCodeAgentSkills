---
name: design-agent-perception-layers
description: >
  WHEN/WHERE/WHO: [Scheduling: Use when designing the context-gathering tools (Abilities) for an autonomous agent, especially when mixing fast APIs and slow UI interactions.]
  HOW: [Structural: Use this SKILL to separate "Fast Thinking" (API queries) from "Slow Thinking" (UI vision tools), forcing the agent to use the fastest possible method for perception.]
  WHY: [Scheduling: Agents interacting with UIs are slow, expensive, and brittle. Blended perception layers optimize token usage and execution speed by relying on underlying APIs for context.]
---

# Design Agent Perception Layers

## Common Contract (Load First)

When this skill is activated, first load [skill-common](../skill-common/SKILL.md) and apply the shared conventions it defines: canonical section order, frontmatter rules, anti-pattern guidance, and the Review In Mind loop in [review-in-mind](../skill-common/details/review-in-mind.md). This skill adds only domain-specific rules below.

## Who
AI Agents, Tool Engineers, and System Architects building multi-modal autonomous systems.

## What
Adapts the classic "Blended Testing" paradigm into an agentic context gathering strategy. It forces the separation of "Fast Thinking" (API queries and database reads) from "Slow Thinking" (Browser interaction, Vision Models, UI clicking), ensuring agents always use the fastest and cheapest method to perceive their environment.

## When
Invoke this skill when defining the toolset for an agent, when optimizing an agent that is too slow or consumes too many tokens, or when designing tools for an agent to "look around" a system.
*Near-miss*: Do not use this if the agent only has one method of interacting with the system (e.g., a purely CLI-based agent).

## Where
Applies to the tool-binding phase of agent architecture, specifically when implementing `Abilities` in the Agentic Screenplay Model.

## Why
In classic SE, Blended Testing speeds up test execution by using APIs to bypass slow UI setups. In Agentic SE, this is a matter of survival. Vision-based UI interaction is token-heavy and slow. If an agent needs to know "Does user X exist?", doing so via an API call takes milliseconds and 100 tokens. Doing so by opening a browser, logging in, navigating to an admin panel, and taking a screenshot takes minutes and 10,000+ tokens.

## Inputs
- **Agent Task**: The goal the agent needs to achieve.
- **Available Interfaces**: The APIs, databases, CLIs, and UIs available to the agent.

## Output (Logical Evidence)
- A mapped separation of **Fast Perception** tools (APIs/Databases) and **Slow Perception** tools (UI/Vision).
- A strictly enforced execution order (Fast first, Slow only for final validation).

## Optimization Readiness
- **Failure Signals**: The workflow falls back to UI too early, setup steps remain bound to slow tools, equivalent APIs are ignored, or the final execution order does not enforce Fast First.
- **Evidence To Collect**: Tool-mapping tables, example task breakdowns, latency comparisons, and cases where slow-path usage was necessary or avoidable.
- **Safe Mutation Boundaries**: Refine interface categorization rules, task-to-tool mapping guidance, and hierarchy prompts without changing the core Fast Perception versus Slow Perception split.
- **Acceptance Criteria**: Accept revisions only if the skill consistently routes setup and state inspection to fast interfaces and reserves slow tools for genuinely unavoidable or final visual checks.
- **Rejected Revision Handling**: Record weak categorization heuristics, premature UI fallbacks, and missing-backend-access assumptions so they are not retried blindly.
- **Transfer Check**: Verify the workflow still works across API-heavy, CLI-heavy, and mixed UI automation systems.
- **Stop Rule**: If no fast interfaces exist or their scope is unclear, stop and ask before claiming a blended perception strategy.

## Constraints (Logical Boundaries)
- **Fast First**: The agent MUST exhaust all Fast Perception tools before falling back to Slow Perception tools.
- **Anti-Pattern Mapping**: 
  1. DO NOT give an agent a generic `OpenBrowser` tool without also providing specific, fast `QueryAPI` tools for the same data.
  2. DO NOT use UI tools for pre-condition setup. (e.g., If the agent needs a test user, it must create it via API, not via the UI registration form).
  3. DO NOT allow the agent to use UI tools to read structured data if an API endpoint exists that provides the exact same data.

## One More Thing
If the system under test does not expose backend APIs or databases and relies entirely on UI interaction, stop and inform the user that blended perception is impossible and execution will be slow.

## How (The 4-Phase Refinement Protocol)
<Use imperative state-machine logic. Every phase must explicitly define branching (If/Then/Else).>

### Phase 1: Interface Discovery
**Input State**: A list of available system interfaces.
1. Categorize every interface into `Fast` (APIs, Databases, CLIs, raw logs) or `Slow` (Web Browsers, Vision Models, RPA tools).
2. *Branch*: If no `Fast` interfaces exist, pause and request backend access from the system owners.
**Output State**: A categorized interface list.

### Phase 2: Map Preconditions to Fast Tools
**Input State**: An Agent Task requiring preconditions.
1. Analyze the `Given` clauses (the preconditions) of the agent's task.
2. Assign exclusively `Fast` tools to fulfill these preconditions. 
3. *Branch*: If a precondition can only be fulfilled via a `Slow` tool, flag it as a critical performance bottleneck.
**Output State**: A Fast-Execution plan for setup.

### Phase 3: Map Core Actions and Validations
**Input State**: The `When` (Action) and `Then` (Validation) clauses of the task.
1. Assign the appropriate tool to the `When` clause. If the goal is to test the UI, use the `Slow` tool. If the goal is to execute a backend process, use the `Fast` tool.
2. For the `Then` clause (the Verifiable Reward), assign a `Fast` tool to verify backend state changes, and a `Slow` tool *only* if visual verification is strictly required.
**Output State**: A blended execution strategy.

### Phase 4: Enforce the Perception Hierarchy
**Input State**: A blended execution strategy.
1. Wrap the agent's tool prompts with the Perception Hierarchy constraint: "You must use API/DB tools to gather context. You may only use the Browser tool to perform the final action or if explicitly instructed."
2. Inject this constraint into the agent's system prompt.
**Output State**: An optimized, token-efficient agent architecture.

## Review In Mind (ReviewInMindGenie)

Execute the common review loop in [review-in-mind](../skill-common/details/review-in-mind.md) before delivering.

Review lens for this skill:
- Does the design force fast, cheap perception before slow, expensive tools?
- Are the routing rules deterministic (which input triggers which perception path)?
- Is there a fallback when fast perception fails or is insufficient?

## Validation (Verifiable Rewards)
1. Verify that all setup and teardown tasks are mapped to Fast Perception tools.
2. Verify that the agent's system prompt explicitly enforces the Fast First constraint.
3. If verification passes, output the Tool Binding Strategy in Markdown format.
