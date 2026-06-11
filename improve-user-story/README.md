# improve-user-story

## Overview
This skill guides the agent to proactively detect when a conversation introduces a new improvement, edge case, or feature change, and updates the relevant existing user story to reflect it using strict BDD formatting.

## Usage
Trigger this skill when you are discussing a feature with an agent and you discover a new edge case or a change in requirements. The agent will update the corresponding story file automatically.

```markdown
We just realized that users need to confirm their email before logging in. Use `improve-user-story` to update the login story.
```

## Structure
- [SKILL.md](./SKILL.md): The core workflow for safely modifying an existing User Story.
- [details/story-refactoring-guide.md](./details/story-refactoring-guide.md): Best practices for adding new scenarios without destroying the intent of existing ones.
