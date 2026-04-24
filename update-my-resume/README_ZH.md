# update-my-resume

在解决完一个问题后，趁细节还新鲜，立刻将你的收获以结构化的方式追加到简历中——同时生成中英文两个版本。

## 这是什么

在经历了一次复杂的调试、一个有挑战性的实现，或任何需要真正思考的任务之后，相关的知识往往会随着对话的结束而消散。本技能从对话中提取已验证的技能收获，并以结构化的方式写入简历条目，覆盖三个核心要素：

1. **遇到了什么问题（WHAT）**
2. **如何一步步解决的（HOW）**
3. **最终收获了什么，以及可复用的证据（WHAT I GOT）**

中英文两条记录将被追加到同一个 `.resume` 文件中，确保你的成长记录在任何语境下都能便捷访问。

## 简历文件位置

技能按以下顺序查找简历文件：

1. 当前项目根目录下的 `.resume`
2. `$HOME/.resume`

如果两者都不存在，技能将自动创建 `$HOME/.resume`，并生成最小化的分区骨架，然后追加新条目。

## 条目格式

**英文分区**

```
--- [YYYY-MM-DD] ---
Problem:  <一句话描述问题>
Approach: <有序步骤，用" → "分隔>
Outcome:  <结果 + 验证证据>
Reuse:    <为何此技能可应用于未来类似场景>
```

**中文分区**

```
--- [YYYY-MM-DD] ---
问题：  <一句话描述问题>
过程：  <有序步骤，用" → "分隔>
收获：  <结果 + 验证证据>
复用性：<为何此技能可应用于未来类似场景>
```

## 何时使用

| 场景 | 是否使用 |
| ---- | -------- |
| 刚解决了一个有难度的 Bug、架构问题或多步骤任务 | ✅ 是 |
| 对话中需要推理、迭代或学习新工具 | ✅ 是 |
| 结果已验证（测试通过、构建成功、输出已确认） | ✅ 是 |
| 简单的一行修复或日常查阅 | ❌ 否 |
| 方案未验证或尚未完成 | ❌ 否——先完成，再使用本技能 |

## 使用方法

### 在 Copilot Chat 中

```text
/update-my-resume
```

智能体会回顾对话，生成结构化的中英文条目，并追加到你的 `.resume` 文件中。

### 触发短语（自动调用）

当你说出以下任意一句话时，技能也会自动激活：

- "update my resume"（更新我的简历）
- "add this to my resume"（把这个加到我的简历里）
- "capture my growth"（记录我的成长）
- "what did I learn today"（我今天学到了什么）
- "record this accomplishment"（记录这次成就）
- "更新我的简历"
- "把这次收获写进简历"
- "记录一下今天学到的东西"

### 示例输出

假设你刚刚调试了一个 Go 并发竞态问题：

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

## 移植到其他智能体

核心技能内容在各智能体间完全相同，只有文件位置和 frontmatter 不同。

### Copilot

将 `SKILL.md` 放置于 `.github/skills/update-my-resume/SKILL.md`。frontmatter 中的 `description` 字段控制 Copilot 何时自动触发。

在 `.github/prompts/update-my-resume.prompt.md` 创建手动触发文件：

```markdown
---
mode: agent
description: '分析当前对话，并将本次收获更新到我的简历中。'
---

遵照 .github/skills/update-my-resume/SKILL.md 中的指令执行。
```

用户在 Copilot Chat 中输入 `/update-my-resume`。

### Cline

添加到 `.clinerules`：

```text
当用户说 "update my resume"、"add this to my resume"、"capture my growth"、
"更新我的简历" 或 "把这次收获写进简历" 时，
读取并遵照 .github/skills/update-my-resume/SKILL.md 执行。
```

### Continue

创建 `.continue/prompts/update-my-resume.prompt`：

```yaml
---
name: update-my-resume
description: "分析当前对话，并将本次收获更新到我的简历中。"
invokable: true
---
```

然后将 `SKILL.md` 正文（frontmatter 以下全部内容）粘贴到该文件中。

### Claude Code

创建 `.claude/commands/update-my-resume.md`：

```markdown
分析当前对话，并将本次收获更新到我的简历中。
遵照 .claude/skills/update-my-resume/SKILL.md 中的指令执行。
```

用户在 Claude Code 的提示中输入 `/update-my-resume`。

## 相关技能

| 技能 | 使用场景 |
| ---- | -------- |
| `save-as-skill` | 对话同时产生了一个值得保存为可复用工作流的技能 |
| `improve-existing-skill` | 应用了某个现有技能，对话中发现了需要改进的地方 |
