# create-skill-from-book

## 概述 (Overview)

使用场景: 将技术教科书、工程标准或参考手册整理为可重用的代理技能时。有助于: 提取程序化工作流、设计约束和检查表；按控制深度选择 `SIMPLE`、`COMPLICATED` 或 `COMPLEX` 模板；并通过验收门细化生成结果。适用于: 工作区中的技能目录、参考指南和设计检查表。

该工作流本身是一个 **COMPLEX** 元技能：它不仅生成文件，还要求输出技能具备 `Optimization Readiness` 区段、明确的验证步骤，以及受控的修订循环。

## 使用方法 (Usage)

触发此技能以执行定义的工作流。有关特定的触发条件和输入，请参阅 `SKILL.md`。

常见触发语句包括：

- “从这本书创建一个技能”
- “把这个章节整理成技能”
- “把这份标准中的规则提炼成可执行技能”

## 结构 (Structure)

- [SKILL.md](./SKILL.md): 技能的核心工作流和定义。
- [README.md](./README.md): 英文概述与使用说明。
- [README_ZH.md](./README_ZH.md): 中文概述与使用说明。
- [details/extraction-guidelines.md](./details/extraction-guidelines.md): 提取嵌入式/系统类知识时使用的详细规则。

## 产出 (Outputs)

- 一个新的技能包，包含 `SKILL.md`、`README.md`、`README_ZH.md`。
- 在需要时创建 `details/` 辅助文件，避免主技能过长。
- 一份验证记录，说明所选层级、验收门结果，以及被拒绝的低质量草案选择。

## 方法价值 (Why It Matters)

- 把被动的书本知识转成代理可以执行的步骤，而不是每次重新阅读整本书。
- 把输出技能设计成从自然语言即可执行，不依赖图示或原书常驻上下文。
- 让后续优化有依据，因为生成结果一开始就包含失败信号、证据来源、可变更边界和停止规则。
