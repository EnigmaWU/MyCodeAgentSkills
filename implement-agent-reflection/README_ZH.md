# implement-agent-reflection

## 概述
WHEN/WHERE/WHO: [Scheduling: Agents or architects designing self-correcting loops for LLM-based tasks where high-quality output is critical.]
HOW: [Structural: Use this SKILL to set up an Evaluator-Generator loop, explicitly separating the generation logic from the critique logic.]
WHY: [Scheduling: Single-shot LLM outputs often contain subtle flaws. Reflection forces the agent to critique its own work before returning the final result, dramatically improving quality while preventing infinite token burn.]

## 用法
触发此技能以执行定义的工作流。有关具体的触发条件和输入，请参阅 `SKILL.md`。

## 结构
- [SKILL.md](./SKILL.md): 核心工作流和技能定义。
