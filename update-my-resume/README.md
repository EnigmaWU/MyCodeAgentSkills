# update-my-resume

Capture what you learned from a solved problem and append it to your resume — in both English and Chinese — immediately while the details are fresh.

## What Is This

After a hard debugging session, a complex implementation, or any task that required real reasoning, the knowledge tends to disappear when the conversation ends. This skill extracts the demonstrated competency and writes a structured, verifiable resume entry that covers:

1. **WHAT problem** was encountered
2. **HOW** you approached it, step by step
3. **WHAT you gained** and evidence that it is useful and repeatable

Both an English and a Chinese entry are written to the same `.resume` file, keeping your record accessible for opportunities in any language context.

## Resume File Location

The skill looks for the resume file in this order:

1. `.resume` in the current project root
2. `$HOME/.resume`

If neither exists, the skill creates `$HOME/.resume` with a minimal section skeleton before appending the new entry.

## Entry Format

**English section**

```
--- [YYYY-MM-DD] ---
Problem:  <one-sentence problem statement>
Approach: <ordered steps, separated by " → ">
Outcome:  <result + verification evidence>
Reuse:    <why this skill applies to future situations>
```

**Chinese section**

```
--- [YYYY-MM-DD] ---
问题：  <一句话描述问题>
过程：  <有序步骤，用" → "分隔>
收获：  <结果 + 验证证据>
复用性：<为何此技能可应用于未来类似场景>
```

## When to Use This

| Situation | Use this skill? |
| --------- | --------------- |
| Just solved a non-trivial bug, architecture problem, or multi-step task | ✅ Yes |
| Conversation required reasoning, iteration, or learning a new tool | ✅ Yes |
| Outcome is verified (test passes, build succeeds, output confirmed) | ✅ Yes |
| Trivial one-liner or routine lookup | ❌ No |
| Solution is unverified or incomplete | ❌ No — finish first, then run this skill |

## Usage

### In Copilot Chat

```text
/update-my-resume
```

The agent reviews the conversation, writes structured EN and ZH entries, and appends them to your `.resume` file.

### Trigger phrases (auto-invocation)

The skill also activates when you say:

- "update my resume"
- "add this to my resume"
- "capture my growth"
- "what did I learn today"
- "record this accomplishment"

### Example output

After a session where you debugged a Go race condition:

```
--- [2026-04-24] ---
Problem:  Intermittent panics in a Go service caused by concurrent writes to a shared map under load.
Approach: Ran with -race flag to reproduce reliably → identified shared map via pprof → replaced with sync.Map → re-ran load test at 10× normal traffic.
Outcome:  Zero panics across 10× load test. Fix merged and verified in staging.
Reuse:    Applicable to any Go service with shared mutable state accessed by multiple goroutines.
```

```
--- [2026-04-24] ---
问题：  Go 服务中因高并发写入共享 map 导致间歇性 panic。
过程：  加 -race 标志稳定复现 → 用 pprof 定位共享 map → 替换为 sync.Map → 以 10 倍流量重跑负载测试。
收获：  负载测试零 panic，修复已合入并在 staging 验证通过。
复用性：适用于所有存在多 goroutine 共享可变状态的 Go 服务。
```

## Porting to Other Agents

The core skill content is identical across agents. Only the file location and frontmatter differ.

### Copilot

Place `SKILL.md` at `.github/skills/update-my-resume/SKILL.md`. The `description` frontmatter field controls when Copilot triggers the skill automatically.

Create a manual trigger at `.github/prompts/update-my-resume.prompt.md`:

```markdown
---
mode: agent
description: 'Analyze this conversation and update my resume with what I learned.'
---

Follow the instructions in .github/skills/update-my-resume/SKILL.md
```

User types `/update-my-resume` in Copilot Chat.

### Cline

Add to `.clinerules`:

```text
When the user asks to "update my resume", "add this to my resume", "capture my growth",
or "what did I learn today",
read and follow .github/skills/update-my-resume/SKILL.md
```

### Continue

Create `.continue/prompts/update-my-resume.prompt`:

```yaml
---
name: update-my-resume
description: "Analyze this conversation and update my resume with what I learned."
invokable: true
---
```

Then paste the body of `SKILL.md` (everything below the frontmatter) into the file.

### Claude Code

Create `.claude/commands/update-my-resume.md`:

```markdown
Analyze the current conversation and update my resume with what I learned.
Follow the instructions in .claude/skills/update-my-resume/SKILL.md
```

User types `/update-my-resume` in Claude Code's prompt.

## Related Skills

| Skill | When to use it |
| ----- | -------------- |
| `save-as-skill` | The conversation also produced a reusable workflow worth preserving as a skill |
| `improve-existing-skill` | An existing skill was applied and the conversation revealed improvements |
