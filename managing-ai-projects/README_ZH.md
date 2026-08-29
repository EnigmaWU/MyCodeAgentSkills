# managing-ai-projects

AI 项目管理总技能，来源于 Adrián González Sánchez 与 Malini Jain Runtasewee
合著的《Managing AI Projects》(O'Reilly)，使用 `create-skill-from-book` 流程构建。

## 内容

`subskills/` 下包含八个聚焦子技能：

| 子技能 | 层级 | 任务 |
| --- | --- | --- |
| `plan-ai-project-emed` | COMPLEX | 使用 EMED 构建端到端 AI 项目计划 |
| `review-ai-project-plan` | COMPLICATED | 审查现有 AI 项目计划 |
| `estimate-ai-roadmap` | COMPLICATED | 估算工作量并构建 AI 路线图 |
| `select-ai-model-approach` | COMPLICATED | 选择正确的模型族/方法 |
| `evaluate-ai-model-readiness` | COMPLICATED | 执行评估/验证关卡 |
| `manage-ai-stakeholders` | COMPLICATED | 规划干系人参与 |
| `audit-ai-team-capabilities` | SIMPLE | 分析团队差距与技能提升 |
| `select-ai-pm-toolkit` | COMPLICATED | 选择 AI PM 工具与供应商 |

## 触发词

- "plan an AI project" / "create an AI project plan"
- "review my AI project plan"
- "estimate / roadmap this AI project"
- "which AI model should we use"
- "is the model ready for launch"
- "manage AI stakeholders"
- "audit our AI team capabilities"
- "which AI PM tools should we use"

## 目录结构

```text
managing-ai-projects/
  ├── SKILL.md
  ├── README.md / README_ZH.md
  ├── agents/openai.yaml
  ├── details/validation-log.md
  └── subskills/
      ├── plan-ai-project-emed/SKILL.md
      ├── review-ai-project-plan/SKILL.md
      ├── estimate-ai-roadmap/SKILL.md
      ├── select-ai-model-approach/SKILL.md
      ├── evaluate-ai-model-readiness/SKILL.md
      ├── manage-ai-stakeholders/SKILL.md
      ├── audit-ai-team-capabilities/SKILL.md
      └── select-ai-pm-toolkit/SKILL.md
```

每个子技能自包含；之后也可将任一子技能复制到工作区根目录（或
`~/.codex/skills`）作为独立技能使用。
