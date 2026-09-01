# Frontmatter Conventions

Every `SKILL.md` MUST start with YAML frontmatter following these rules:

```yaml
---
name: <skill-name>
description: >
  WHEN/WHERE/WHO: [Scheduling: who should use this, explicit trigger/boundary contexts]
  HOW: [Structural: what workflow this skill executes]
  WHY: [Scheduling: why this skill matters or which failure it prevents]
---
```

- `name` MUST exactly match the skill folder name.
- The description MUST use the multi-line `>` block scalar.
- Include the strongest exact trigger phrases AND near-miss boundaries in the description, not only in `## When`.
- Quote the description value when it contains colons.
- Keep `## When` aligned with the description; they must reinforce, not contradict, each other.
- Prefer concrete user-language triggers (e.g., "review this diagram", "save as skill") over abstract summaries.
- `WHY` MUST be skill-specific: name the concrete failure this skill prevents or the value it delivers. The generic sentence "Provides structured workflow execution to prevent errors and ensure standards." is banned boilerplate; the validator rejects any skill that uses it.
