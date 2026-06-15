# design-agent-perception-layers

## 概述 (Overview)
WHEN/WHERE/WHO: [Scheduling: 在为自治代理设计上下文收集工具（能力）时使用，特别是当混合使用快速API和慢速UI交互时。]
HOW: [Structural: 使用此技能将“快思考”（API查询）与“慢思考”（UI视觉工具）分离开来，强制代理使用最快的方法进行感知。]
WHY: [Scheduling: 与UI交互的代理速度慢、成本高且脆弱。混合感知层通过依赖底层API获取上下文，优化了令牌使用和执行速度。]

## 使用方法 (Usage)
触发此技能以执行定义的工作流。有关特定的触发器和输入，请参见 `SKILL.md`。

## 结构 (Structure)
- [SKILL.md](./SKILL.md): 技能的核心工作流和定义。
