# Agentic Design Patterns - Detailed Checklists

This document compiles actionable design rules, checklists, and constraints for the core agentic patterns described in *Agentic Design Patterns: A Hands-On Guide to Building Intelligent Systems*.

---

## 1. Prompt Chaining

Use when executing linear, deterministic workflows where the output of one step is required to construct the input of the next.

### Design Checklist
*   **[ ] Isolation**: Break down the task so that each node has a single, narrow responsibility. Do not make a single prompt generate structure, content, and code all at once.
*   **[ ] State Schema**: Define exactly what data passes between steps. Use structured models (e.g., Pydantic) to validate intermediate outputs before passing them forward.
*   **[ ] Context Minimization**: Ensure step $N$ only receives the necessary output of step $N-1$ and system instructions. Do not dump the entire raw chat history into every step.
*   **[ ] Format Enforcement**: Use structured output parsing (JSON, YAML, or XML tags) at each node to make downstream consumption robust.

### Constraints & Red Flags
*   **Constraint**: Never pass raw, unstructured strings from step to step without validation.
*   **Red Flag**: An intermediate step outputs general conversational text (e.g., "Sure, here is your JSON...") instead of the clean structured schema.

---

## 2. Routing

Use when the system must dynamically choose the next execution path based on intent, classification, or semantic context.

### Design Checklist
*   **[ ] Selector Type**: Choose the right routing mechanism:
    *   *Rule-Based*: Use regex or switch-cases for high speed and absolute determinism (e.g., checking for specific command prefixes).
    *   *LLM-Based*: Use an LLM with structured output mapping (e.g., Enum) for complex intent classification.
    *   *Semantic (Embedding-Based)*: Use vector cosine similarity when routing based on semantic meaning or historical examples.
*   **[ ] Exclusivity**: Ensure router classification options are mutually exclusive to prevent ambiguous decisions.
*   **[ ] Default Path**: Define a clear "unclear" or fallback destination for inputs that do not match any standard category.
*   **[ ] Confidence Threshold**: In semantic or LLM classification, define a threshold below which the router requests clarification or routes to the fallback path.

### Constraints & Red Flags
*   **Constraint**: Do not let a router fail silently. If the intent is unrecognized, route to an escalation/clarification handler.
*   **Red Flag**: The router oscillates or loops between routes because the output categories overlap.

---

## 3. Parallelization

Use when tasks can be processed independently to reduce total execution latency (fork-join or map-reduce).

### Design Checklist
*   **[ ] Concurrency Limits**: Define maximum concurrent workers (e.g., using thread pools or async task limits) to avoid hitting model API rate limits.
*   **[ ] State Isolation**: Ensure workers write to isolated state slices. Workers must not edit the same mutable state variables concurrently.
*   **[ ] Merge Protocol**: Define how the separate outputs are aggregated (e.g., concatenating code files, summing scores, or filtering duplicates).
*   **[ ] Thread Exception Propagation**: Ensure that if one concurrent worker fails or times out, the main coordinator catches the exception, cancels other threads if needed, and applies recovery.

### Constraints & Red Flags
*   **Constraint**: Do not run un-throttled parallel LLM requests without rate-limit retry logic (e.g., exponential backoff).
*   **Red Flag**: The aggregator node blocks indefinitely because one parallel task failed or timed out without raising an error.

---

## 4. Reflection & Self-Correction

Use when the output quality must meet a strict threshold, and the model can analyze and correct its own errors.

### Design Checklist
*   **[ ] Role Separation**: Use two distinct prompts or agents:
    *   *Generator*: Creates the draft (code, text, design).
    *   *Evaluator/Reflector*: Critiques the draft against criteria.
*   **[ ] Concrete Criteria**: Provide the Evaluator with exact, binary check criteria (e.g., "Does the code compile?", "Are there floating-point operations?"). Do not ask the evaluator to just "make the output better."
*   **[ ] Iteration Guard**: Hard-code a maximum reflection loop count (typically 3 to 5). Increment a `retry_count` in the state.
*   **[ ] Exit Strategy**: If the maximum iteration limit is reached without meeting the target score/criteria, route to a fallback (escalate to human or save the best-effort output with warning logs).

### Constraints & Red Flags
*   **Constraint**: Never design a reflection loop without a hard numerical limit.
*   **Red Flag**: The evaluator keeps suggesting modifications and the generator keeps generating new versions, causing an infinite loop.

---

## 5. Tool Use & Planning

Use when the agent must dynamically select external APIs to gather information or take actions in the environment.

### Design Checklist
*   **[ ] Declarative Schema**: Write exact descriptions, argument types, and docstrings for every tool. LLMs rely entirely on these to match intent.
*   **[ ] Tool Call Parsing**: Use structured tool-calling APIs (e.g., Function Calling) rather than parsing raw text prompts.
*   **[ ] Re-planning Loop**: After each tool call, update the agent's plan or state. The agent must evaluate:
    *   Did the tool succeed?
    *   Is the current goal met?
    *   What tool is needed next?
*   **[ ] Plan Schema**: Structure plans as a sequence of steps (e.g., Pydantic lists) that can be dynamically updated, marked as complete, or rescheduled.

### Constraints & Red Flags
*   **Constraint**: Never invoke a tool with unvalidated parameters. Implement pre-checks on tool inputs (e.g., check range limits, path paths) before sending them to the environment.
*   **Red Flag**: The agent calls a tool with arguments that match placeholder strings (e.g., `user_id="YOUR_USER_ID"`).

---

## 6. Multi-Agent Collaboration

Use when the system goal involves multiple distinct domains of expertise, necessitating specialized sub-agents coordinating together.

### Design Checklist
*   **[ ] Architecture Choice**: Select the correct coordination topology:
    *   *Coordinator-Specialist*: A central hub routes and schedules tasks to specialists.
    *   *Supervisor*: A supervisor evaluates outputs and dictates transitions.
    *   *Peer-to-Peer*: Agents communicate directly via a shared blackboard or message channel.
*   **[ ] Role Isolation**: Give each agent a distinct instruction set, name, and tool list. Do not duplicate responsibilities.
*   **[ ] State Serialization**: Define the global "blackboard" state that all agents read and write. Ensure all updates are atomic.
*   **[ ] Termination Condition**: Define a clear logical state that signifies the collaboration is complete (e.g., `state["task_completed"] == True`).

### Constraints & Red Flags
*   **Constraint**: Do not allow agents to communicate in unmonitored cycles. Keep a communication log and cap the total agent-to-agent interactions.
*   **Red Flag**: Two agents get locked in an argument, exchanging messages repeatedly without updating the system state.

---

## 7. Exception Handling & Recovery

Use to guarantee operational resilience in dynamic, real-world environments.

### Design Checklist
*   **[ ] Proactive Timeout Guards**: Wrap all external service, API, and tool calls in timeouts (e.g., max 10 seconds).
*   **[ ] Transient vs. Permanent Errors**:
    *   *Transient (429 Rate Limit, 503 Service Unavailable)*: Apply automatic retries with exponential backoff and jitter.
    *   *Permanent (404 Not Found, 400 Bad Request, Syntax Error)*: Immediately route to fallback logic or alternative tools.
*   **[ ] State Rollback**: Before performing a complex multi-step tool operation, take a snapshot of the shared state. If the operation fails, restore the snapshot to prevent state corruption.
*   **[ ] Fallback Handlers**: Provide a simpler, robust fallback agent or mechanism (e.g., if a precise location API fails, fallback to a general area API).
*   **[ ] Escalation Protocol**: Define a clear transition to a Human-in-the-Loop state when automated recovery fails.

### Constraints & Red Flags
*   **Constraint**: Never catch generic exceptions (`except Exception:`) without logging the trace and updating the system state (`state["error_flag"] = True`).
*   **Red Flag**: The orchestrator crashes, leaving background tasks or file writes in a half-completed, locked state.

---

## 8. Coding Agents (CodeAgents)

Use when building systems that edit source code, execute shell commands, run tests, or collaborate in multi-agent software engineering pipelines (e.g., configurations like Copilot, Cline, Continue, or OpenCode).

### Design Checklist
*   **[ ] Dynamic Signal Curation (Copilot-Style)**:
    *   *Active vs. Passive Signals*: Prioritize active cursor window bounds (e.g., prefix/suffix lines of cursor position) and append passive signals (recently edited files, imports, dependencies) to curate target prompt context.
    *   *Cache-Backed Tabs*: Scan neighboring tabs inside the IDE for code snippets related to the active file, utilizing local caching to reduce prompt generation latency to zero.
    *   *Semantic Workspace Search*: Build a vector indexing pipeline for codebase-wide queries (like `@workspace` or `#codebase`) to retrieve relevant files outside the active document.
    *   *Persistent Instruction Hooks*: Support project-level guidelines files (e.g., `.github/copilot-instructions.md`) to automatically inject coding rules and architecture decisions into the prompt prefix.
*   **[ ] Interactive Tool Policies & Terminal Integration (Cline/Continue-Style)**:
    *   *Granular Tool Policies*: Configure explicit permissions for each tool category (e.g. read operations can be auto-approved, but terminal shell executions and write operations must prompt the user via an approval gate).
    *   *Terminal Output Capture*: Hook into the IDE's integrated terminal shell integration to stream stdout/stderr back into the model's environment context, allowing self-correction of compiler or test errors.
    *   *Context Boundaries & `.clineignore`*: Implement ignore filters (e.g. `.clineignore`) to prevent the agent from reading or writing sensitive credentials, local `.env` files, or git configuration files.
    *   *Configuration Standard (Continue config.yaml)*: Standardize configuration using project-level `.continuerc.json` or global `config.yaml` blocks, using Model Context Protocol (MCP) servers to expose custom APIs and HTTP context providers.
*   **[ ] Persona Teams & Environment Sandboxing (OpenCode/OpenHands-Style)**:
    *   *Secure Docker Sandboxing*: Execute arbitrary commands inside a virtualized environment or Docker container to isolate the local host system from destructive shell commands.
    *   *Explicit Persona Separation*: Assign distinct tasks to role-specific agents (e.g., `Scaffolder` for feature generation, `TestEngineer` for writing test suites, and `ProcessAgent` for critique and code review).

### Constraints & Red Flags
*   **Constraint**: Never execute shell commands locally without sandboxing (e.g., dev containers, Docker) unless the user has explicitly toggled manual confirmation or "YOLO" mode.
*   **Constraint**: Never allow an agent to read or write credentials or `.env` files. Enforce a strict ignore filter.
*   **Red Flag**: An agent modifies a file and introduces compile-time warnings or test failures, but attempts to continue execution without reverting or correcting the code.
*   **Red Flag**: The agent gets stuck in a loop of running a command, encountering an error, making the same correction, and running the command again.

---

## 9. Memory Management

Use when designing agents that must maintain context, user preferences, session history, and persistent knowledge bases across single or multiple interaction turns.

### Design Checklist
*   **[ ] Short-Term Contextual Memory**:
    *   *Token Budgeting*: Monitor context window consumption. Summarize older conversation turns once token thresholds are reached.
    *   *Sliding Buffer*: Keep only the last $N$ turns of raw chat messages in the immediate prompt, compressing previous logs.
*   **[ ] Scoped State Memory (Scratchpad)**:
    *   *Prefix Scoping*: Standardize state dictionary keys using prefix namespaces:
        *   `user:`: Associates and persists data with a user ID across multiple session chat threads.
        *   `app:`: Shares configuration or static application data among all users.
        *   `temp:`: Stores ephemeral variables valid only for the current execution turn (discarded after use).
    *   *State-Delta Mutators*: Ensure state changes are encapsulated inside defined tool execution scopes rather than mutated arbitrarily outside the runner event processing cycle.
*   **[ ] Long-Term Persistent Memory**:
    *   *Database Selection*: Pick the appropriate storage service for sessions (e.g., `InMemorySessionService` for ephemeral tests vs. `DatabaseSessionService`/SQLAlchemy for persistent SQLite/PostgreSQL setups).
    *   *Semantic Embedding Store*: Index long-term facts, user profiles, or documents into a vector database for semantic retrieval based on input similarity matching.

### Constraints & Red Flags
*   **Constraint**: Never directly modify the `session.state` dictionary after retrieving a session. All state updates must occur via `LlmAgent.output_key` or `EventActions.state_delta` to ensure changes are logged in the session's event history.
*   **Constraint**: Ephemeral variables must be prefixed with `temp:` and deleted or ignored before persisting the session object to database storage.
*   **Red Flag**: Shared application state keys (`app:`) are mutated dynamically by user-specific tasks, causing cross-session state corruption.

---

## 10. Model Context Protocol (MCP)

Use when exposing resources, prompts, and tools from external servers to the agent using a standard transport and communication protocol.

### Design Checklist
*   **[ ] Transport & JSON-RPC Schema**:
    *   Verify that the client-server communication complies with the MCP JSON-RPC 2.0 schema (e.g. notifications, request/response models).
*   **[ ] Resource URI Management**:
    *   Expose context documents (codebases, databases, API specs) as standard URIs (e.g. `file://`, `postgres://`).
*   **[ ] Declarative Tools Mapping**:
    *   Map external tool calls to declarative schemas with clear JSON schema arguments.

### Constraints & Red Flags
*   **Constraint**: Never expose tools that modify system files without specifying explicit manual confirmation parameters in the client.
*   **Red Flag**: The client blocks indefinitely waiting for an MCP tool response due to a missing timeout limit.

---

## 11. Guardrails & Safety Patterns

Use to validate system inputs/outputs, prevent prompt injection, and enforce formatting constraints at the boundaries of model communication.

### Design Checklist
*   **[ ] Input Sanitization**:
    *   Filter user prompts to detect and strip system override keys or malicious instructions.
*   **[ ] Output Structure Validation**:
    *   Enforce structural parser checks (e.g., Pydantic schema validation or regex checks) before utilizing the model's generated data in tool calls.
*   **[ ] Content Classification (Safety filters)**:
    *   Use lightweight classifiers to check if system responses contain harmful or unsafe content before rendering them to the user.

### Constraints & Red Flags
*   **Constraint**: Never feed raw LLM output into a command shell or system execution tool without running output sanitization checks (e.g., stripping unexpected chain characters or command suffixes).
*   **Red Flag**: The agent bypasses validation steps because it encountered a format error and returned raw text.




