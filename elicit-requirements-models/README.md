# elicit-requirements-models

## Overview
This skill guides the agent to convert flat, text-based software requirements into structured visual models (using Mermaid.js). According to *Software Requirements Essentials*, creating requirements models (like state transition diagrams or data flow diagrams) is one of the most effective ways to expose missing requirements, logical dead ends, and edge cases that are invisible in raw text.

## Usage
Trigger this skill when given a complex user story, PRD, or set of business rules that need to be analyzed for completeness.

```markdown
Use the `elicit-requirements-models` skill to draw a state diagram for this checkout process and tell me what requirements are missing.
```

## Structure
- [SKILL.md](./SKILL.md): The core workflow for extracting models from text and hunting for missing requirements.
- [details/mermaid-modeling-templates.md](./details/mermaid-modeling-templates.md): Examples of Mermaid syntax for Context, State, and Flow models.
