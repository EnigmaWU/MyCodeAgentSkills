# design-tool-use-sandboxing

## 概述
WHEN/WHERE/WHO: [Scheduling: Agents or architects granting LLMs access to terminal commands, file systems, or external APIs.]
HOW: [Structural: Use this SKILL to enforce boundary protections, user-approval loops, and containerized execution for dangerous tools.]
WHY: [Scheduling: Autonomous agents carry user-level privileges. Unconstrained tool execution leads to catastrophic code deletion or security breaches.]

## 用法
触发此技能以执行定义的工作流。有关具体的触发条件和输入，请参阅 `SKILL.md`。

## 结构
- [SKILL.md](./SKILL.md): 核心工作流和技能定义。
