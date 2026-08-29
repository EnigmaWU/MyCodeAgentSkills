---
name: build-agent-memory-systems
description: >
  WHEN/WHERE/WHO: [Scheduling: Agents or developers designing memory layers for autonomous agents that must retain context across sessions.]
  HOW: [Structural: Use this SKILL to configure short-term working memory, semantic vector stores, and episodic event logs to avoid LLM amnesia.]
  WHY: [Scheduling: Without persistent memory, an agent starts from zero every message. A structured memory system allows deep personalization and context awareness over long time horizons.]
---

# Build Agent Memory Systems

## Common Contract (Load First)

When this skill is activated, first load [skill-common](../skill-common/SKILL.md) and apply the shared conventions it defines: canonical section order, frontmatter rules, anti-pattern guidance, and the Review In Mind loop in [review-in-mind](../skill-common/details/review-in-mind.md). This skill adds only domain-specific rules below.

## Who
Architects, principal developers, or AI engineers designing autonomous systems that require deep personalization or long-running context.

## What
Design and implement a multi-tiered memory architecture for agents, including Short-Term (working/scratchpad) memory, Long-Term (semantic/vector) memory, and Episodic (event/history) memory.

## When
- Triggered by requests like: "add memory to this agent", "how do I persist context?", or "design an agent memory system".
- Use when an agent must remember facts from past sessions or retrieve relevant domain knowledge dynamically.

## Where
Applies to backend agent orchestration, state schemas, and database configurations (e.g., Vector DBs, SQL history logs).

## Why
LLMs are stateless. The "context window" is too small to fit an entire user's history or a massive codebase. By injecting only the *relevant* memories dynamically via RAG (Retrieval-Augmented Generation) and summarizing older context, the agent remains highly capable without hitting token limits or context degradation.

## Inputs
- **Memory Requirements**: What specifically needs to be remembered (user facts, code snippets, tool outcomes)?
- **Scale and Latency**: How fast must retrieval happen, and how large is the dataset?

## Output (Logical Evidence)
- **Memory Architecture Design**: A mapping of data types to short-term or long-term storage mechanisms.
- **RAG & Summarization Logic**: The code logic that manages when to write to memory and when/how to retrieve from it.

## Optimization Readiness
- **Failure Signals**: The design overfills the context window, mixes memory namespaces, retrieves irrelevant history, or lacks a clear rule for when to summarize versus retrieve.
- **Evidence To Collect**: Retrieval traces, summarization outputs, latency measurements, token-usage trends, and examples of useful versus noisy recalled memories.
- **Safe Mutation Boundaries**: Refine storage partitioning, retrieval heuristics, summarization thresholds, and memory examples without changing the core short-term, episodic, and long-term memory split.
- **Acceptance Criteria**: Accept revisions only if the design preserves token budget, isolates tenant state correctly, and retrieves relevant memory with clear write and recall rules.
- **Rejected Revision Handling**: Record failed chunking strategies, noisy retrieval patterns, and unsafe namespace designs so they are not retried blindly.
- **Transfer Check**: Confirm the workflow still works for both lightweight conversation persistence and larger semantic-memory architectures.
- **Stop Rule**: If the required retrieval scale, latency target, or memory type is still unclear, stop and ask before choosing storage and summarization strategy.

## Constraints (Logical Boundaries)
- **Token Budget Protection**: Never blindly append all past messages into the context window. Old messages MUST be summarized or evicted to maintain a safe token buffer.
- **State Partitioning**: Strictly partition memory namespaces (e.g., `user_123` vs `system_global`) to prevent cross-tenant data leakage.

## One More Thing
If the user hasn't specified whether they need Semantic Search (Vector DB) or just simple conversation persistence (SQL/NoSQL), pause and ask them about the scale of data they expect to handle.

---

## How (Structural Workflow)

### 1. Define the Short-Term Memory (Scratchpad)
- Design the state schema (e.g., in LangGraph) to hold the *immediate* context of the current task.
- Ensure the state schema resets or truncates upon task completion.

### 2. Implement the Episodic Memory (Conversation History)
- Configure an append-only log (e.g., SQLite, Postgres, or Redis) to store raw message exchanges.
- Implement a **Summarizer Agent**: A background process that triggers when the message history exceeds `N` tokens. The Summarizer squashes the history into a dense `<summary>` block and clears the raw messages, leaving only the summary and the last 3 turns.

### 3. Implement the Semantic/Long-Term Memory (Vector/Knowledge Graph)
- Determine the extraction trigger: When the agent learns a "core fact" (e.g., user preference or global architecture rule), it explicitly calls a `save_memory` tool.
- The `save_memory` tool chunks the text, embeds it, and saves it to a Vector Database (like Chroma, Pinecone, or pgvector).

### 4. Wire the Retrieval Mechanism
- At the start of the agent's turn (or via a specific `search_memory` tool), the agent queries the Vector DB based on the current context.
- The retrieved results are injected directly into the system prompt's `<relevant_context>` section.

### 5. Validate the Memory Lifecycle
- Ensure the extraction tool actually runs (test it).
- Verify that the Summarizer successfully truncates the history without losing the core user intent.

## Review In Mind (ReviewInMindGenie)

Execute the common review loop in [review-in-mind](../skill-common/details/review-in-mind.md) before delivering.

Review lens for this skill:
- Do short-term, long-term, and episodic memories have distinct stores, triggers, and retrieval paths?
- Is there a validation step proving extraction and retrieval actually work?
- Are privacy, retention, and eviction rules explicit?
