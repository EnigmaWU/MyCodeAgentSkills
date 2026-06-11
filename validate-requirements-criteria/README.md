# validate-requirements-criteria

## Overview
This skill guides the agent to review and test requirements *before* any code is written, a core practice emphasized in *Software Requirements Essentials*. It hunts for ambiguous adjectives (e.g., "fast," "user-friendly," "robust"), identifies missing edge cases, and outputs strict, testable Acceptance Criteria using Behavior-Driven Development (BDD) syntax.

## Usage
Trigger this skill when given a drafted requirement, PRD section, or User Story that needs to be finalized before handing it to a developer.

```markdown
Use the `validate-requirements-criteria` skill to test this user story for ambiguity and write the acceptance criteria.
```

## Structure
- [SKILL.md](./SKILL.md): The core workflow for hunting ambiguity and drafting BDD acceptance criteria.
- [details/ambiguity-checklist.md](./details/ambiguity-checklist.md): A list of dangerous, ambiguous words to flag in requirements text.
