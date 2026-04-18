---
name: blog-topic-discover
description: 'Use when: a task is completed, a goal is met, or the user asks to review recent work for blog ideas. Helps with: extracting insights, mistakes, new methods, and topics from recent git commits and chat logs to brainstorm blog posts. Applies to: post-task reflection and developer branding.'
---

# Blog Topic Discover

## Who
Developers, dev-rels, and engineers who want to extract valuable learning experiences, mistakes, or novel methods from their recent work to write technical blog posts.

## What
Reviews the trajectory of a recently completed task "from start to end". By analyzing git commits, file changes, and critically, the **conversation history between the code agent and the user/LLM**, it identifies what was changed. It assesses how the problem was iteratively understood and solved through dialogue, how the solution was effectively verified, highlights the right/wrong decisions made along the way, applies any new ideas or methods, and proposes compelling topics for technical blog posts.

## When
- The user declares a task or milestone complete.
- The user asks "what should I write about this?" or "give me blog ideas".
- The user explicitly invokes the `blog-topic-discover` skill after a coding session.

## Where
- The analysis is output to the chat or saved as a markdown summary file (e.g., `blog_ideas.md`) in the workspace, depending on user preference.

## Why
- Turning daily coding challenges and mistakes into shared knowledge helps build personal branding and team documentation.
- The context of "why" decisions were made is freshest right after a task is completed.
- Mining git histories and chat logs uncovers deeper insights than just looking at the final code.

## Inputs
- **Timeframe / Start Point** (required): A commit hash, timestamp, or logical starting point (e.g., "since yesterday", "for the last 5 commits", "this conversation").
- **Final Goal** (optional): What the original objective was.

## Output
Generate a complete, gracefully structured blog post draft using the following specific artistic template:

```markdown
# <Catchy Blog Title>

**【缘起性不空】(Origin)**
<Context of the task, why it started, and the initial goal.>

**【臆想不糊象】(Imagination)**
<Initial thoughts on the approach, the assumptions made before hitting reality.>

**【问题心中起】(Inquiry)**
<The main problem encountered, the bug hit, or the puzzle that needed solving. How the conversation between the agent and user clarified the true problem.>

**【求解不甚解】(Exploration)**
<The collaboration and struggle. The back-and-forth dialogue, the wrong decisions pivoted away from, and how the final solution was reached and effectively verified.>

**【反思更人类】(Reflection)**
<The "human" takeaway. Why did we make those mistakes? What does it say about our workflow or mindset?>

**【洞见显智慧】(Insight)**
<The core technical or methodological lesson learned. Novel tools, methods, or architectural patterns applied.>
*(Include a `mermaid` diagram here to visually explain the core logic, flow, or architectural change for clear and easy understanding)*

**【新问开新局】(Evolution)**
<What new questions this raises, or what the next logical steps are.>

—— by 术子米德@<Current Date, e.g., 2026年x月z日>
（备注：问题是真的，过程也是真的，内容都是生成的）
```

## Constraints
- Base the findings strictly on the provided git diffs, commits, and recent conversation logs. Do not fabricate challenges.
- Focus on the *journey* (the "why" and "how") rather than just a dry changelog (the "what").
- Be honest about mistakes or wrong decisions—these make the best blog posts.
- **Visuals**: Always include at least one `mermaid` diagram to make complex paths or architectures easier to understand.

## One More Thing
If the timeframe or start point for the review is unclear, ask the user to clarify how far back to look before proceeding.

## How

### Phase 1: Discovery & Context Gathering
1. Ask or determine the starting point for the review (e.g., specific commit, start of the chat).
2. Gather the logs: use git tools (`git log`, `git diff`) or review the conversation history to reconstruct the timeline from the start point to the end point.
3. Identify the original goal versus the final outcome.

### Phase 2: Analysis & Extraction
1. Extract the **Journey**: What were the major milestones or pivots?
2. Extract the **Decisions & Collaboration**: Where did the approach change? How did the conversation history shape the final understanding of the problem? What bugs were hit, how were they solved collaboratively, and how was the solution effectively verified? Were there "wrong" decisions that had to be backed out?
3. Extract the **Novelty**: What new techniques, tools, or methods were uniquely applied here?

### Phase 3: Brainstorming & Output
1. Synthesize the extracted analysis and journey.
2. Use the provided artistic blog template ([Origin], [Imagination], etc.) to draft a full, engaging blog post that highlights the problem-solving and collaboration process.
3. Present the drafted blog post to the user for review.
