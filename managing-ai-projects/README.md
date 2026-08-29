# managing-ai-projects

Umbrella skill for AI project management, derived from *Managing AI Projects* by
Adrián González Sánchez and Malini Jain Runtasewee (O'Reilly), built with the
`create-skill-from-book` workflow.

## What it contains

Eight focused sub-skills under `subskills/`:

| Sub-skill | Tier | Task |
| --- | --- | --- |
| `plan-ai-project-emed` | COMPLEX | Build an end-to-end AI project plan using EMED |
| `review-ai-project-plan` | COMPLICATED | Review an existing AI project plan |
| `estimate-ai-roadmap` | COMPLICATED | Estimate effort and build an AI roadmap |
| `select-ai-model-approach` | COMPLICATED | Choose the right model family/approach |
| `evaluate-ai-model-readiness` | COMPLICATED | Run evaluation/validation gates |
| `manage-ai-stakeholders` | COMPLICATED | Plan stakeholder engagement |
| `audit-ai-team-capabilities` | SIMPLE | Analyze team gaps and upskilling |
| `select-ai-pm-toolkit` | COMPLICATED | Choose AI PM tools and vendors |

## Trigger phrases

- "plan an AI project" / "create an AI project plan"
- "review my AI project plan"
- "estimate / roadmap this AI project"
- "which AI model should we use"
- "is the model ready for launch"
- "manage AI stakeholders"
- "audit our AI team capabilities"
- "which AI PM tools should we use"

## Structure

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

Each sub-skill is self-contained; any of them can also be copied to the workspace
root (or `~/.codex/skills`) later and used as a standalone skill.
