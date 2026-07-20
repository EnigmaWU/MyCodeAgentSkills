# save-as-skill

## 概述 (Overview)

使用场景: 经过长时间对话解决了一个难题，调试会话产生了一个可重用的工作流，或者用户要求“保存为技能”时。有助于: 提取可重用的 `SKILL.md`，保留对话中的推理和工件，并按模板选择正确层级。适用于: 当前对话，生成的技能包以及 AI 助手的技能交接。

该工作流本身是一个 **COMPLEX** 元技能：它会先判断对话是否值得保存，再选择输出技能的层级，补齐 `Optimization Readiness`，并通过验证与评审循环决定是否接受结果。

## 使用方法 (Usage)

触发此技能以执行定义的工作流。有关特定的触发条件和输入，请参阅 `SKILL.md`。

常见触发语句包括：

- “save as skill”
- “capture this as a skill”
- “turn this into a skill”

## 结构 (Structure)

- [SKILL.md](./SKILL.md): 技能的核心工作流和定义。

## 为什么 frontmatter 很重要

- 自动激活通常首先依赖 frontmatter `description` 作为发现面。
- 因此，精确触发语句和 near-miss 边界必须写进 frontmatter，而不是只写在 `## When`。
- 当前版本已经按这个原则强化了路由描述，以提高被模型正确选中的概率。
