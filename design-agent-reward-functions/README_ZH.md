# design-agent-reward-functions

## 概述 (Overview)
WHEN/WHERE/WHO: [Scheduling: 在为自治AI代理的执行循环设计退出标准和验证逻辑时使用。]
HOW: [Structural: 使用此技能将经典的BDD Gherkin场景转换为作为硬约束的可验证奖励函数。]
WHY: [Scheduling: 自治代理存在推理漂移和幻觉问题。显式的Given/When/Then边界检查可防止失控执行。]

## 使用方法 (Usage)
触发此技能以执行定义的工作流。有关特定的触发器和输入，请参见 `SKILL.md`。

## 结构 (Structure)
- [SKILL.md](./SKILL.md): 技能的核心工作流和定义。
