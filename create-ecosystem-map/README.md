# create-ecosystem-map

## Overview
This skill guides the agent to map out the boundaries of a system using an **Ecosystem Map** (from the *Visual Models for Software Requirements* methodology). Systems do not exist in a vacuum; they interact with users, legacy databases, third-party APIs, and downstream services. An Ecosystem Map visualizes these dependencies to prevent "out of scope" surprises.

## Usage
Trigger this skill when starting a new architectural design or analyzing the integration requirements of a new feature.

```markdown
Use the `create-ecosystem-map` skill to show me all the systems this new Payment Gateway will touch.
```

## Structure
- [SKILL.md](./SKILL.md): The core workflow for identifying the System Under Design and its external actors/systems.
- [details/ecosystem-map-template.md](./details/ecosystem-map-template.md): Examples of how to format the Ecosystem Map using Mermaid.js syntax.
