# evolve-skill-with-wiki

## 概述 (Overview)

使用场景: 需要在多次执行中持续改进某个代理技能、让技能从历史运行中积累经验，或按 WikiSkill 框架搭建技能进化循环时。有助于: 运行 raw/wiki/skills 三层工作区、失败与成功轨迹的模式沉淀、wiki 驱动的单点技能提案、以及验证门控回滚。适用于: 需要把代理执行经验编译为持久知识并反哺技能的场景。

该工作流本身是一个 **COMPLEX** 元技能：它跨多个迭代运行完整的进化循环，而不是做一次性修补。方法源自 WikiSkill 论文 (arXiv:2608.27454)。

## 使用方法 (Usage)

常见触发语句包括：

- “evolve this skill”
- “set up skill evolution”
- “apply WikiSkill”
- “让这个技能从过去的执行记录中学习改进”

运行前需要（或让代理搭建）：带评分的任务集、验证集划分，以及迭代预算。详细分阶段流程见 `SKILL.md`。

## 结构 (Structure)

- [SKILL.md](./SKILL.md): 技能的核心工作流和定义。
- [README.md](./README.md): 英文概述与使用说明。
- [README_ZH.md](./README_ZH.md): 中文概述与使用说明。
- [references/wikiskill-paper-digest.md](./references/wikiskill-paper-digest.md): 源论文方法与关键结论的精炼摘要。

进化产出的工作区形如：

```text
evolution-runs/<task-domain>/
  ├── raw/            # 不可变的执行轨迹
  ├── wiki/           # 持续累积、永不复位的知识库
  │   ├── patterns/   # 失败模式与成功策略
  │   ├── logs.md     # 按时间顺序的进化日志
  │   └── skill-impact.md  # 每次提案的 diff、验证分数与接受/拒绝记录
  └── skills/         # 可回滚的活动技能集
```

## 与其他技能的分工

| 场景 | 使用的技能 |
| ---- | ---- |
| 跨多次 rollout 进化技能并沉淀知识库 | `evolve-skill-with-wiki`（本技能） |
| 依据单次对话证据改进技能 | `improve-existing-skill` |
| 从对话沉淀全新技能 | `save-as-skill` |
| 设计面向用户的代理记忆 | `build-agent-memory-systems` |

## 核心规则

- 技能可在验证下降时回滚，但 wiki 永不重置。
- 推理代理在执行 rollout 时不得读取 wiki（论文消融显示这会降低最终技能质量）。
- 每次迭代只提出一个原子级技能修改，并须通过严格验证门控。
- 每次提案都写入 `skill-impact.md`（diff、分数、结果），避免重复提出被拒绝的方案。
