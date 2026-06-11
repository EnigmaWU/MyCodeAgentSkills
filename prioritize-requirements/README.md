# prioritize-requirements

## Overview
This skill guides the agent to systematically prioritize a backlog of requirements, user stories, or features. As noted in *Software Requirements Essentials*, simply tagging items as "High/Medium/Low" is subjective and often fails. This skill implements an analytical matrix to rank requirements based on weighted business value, user value, cost, and risk.

## Usage
Trigger this skill when provided with a list of unprioritized tasks, features, or user stories, and you need to determine build order.

```markdown
Use the `prioritize-requirements` skill to groom this backlog and tell me which 3 features we should build first.
```

## Structure
- [SKILL.md](./SKILL.md): The core workflow for scoring and ranking requirements.
- [details/analytical-matrix-guide.md](./details/analytical-matrix-guide.md): The scoring framework and formula used to rank items.
