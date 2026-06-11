# draft-srs-document

## Overview
This skill guides the agent to compile scattered requirements into a formal **Software Requirements Specification (SRS)** document, using the industry-standard template provided in *Software Requirements (3rd Edition)*. The SRS serves as the ultimate agreement between the customer and the development team.

## Usage
Trigger this skill when transitioning from discovery/elicitation into formal specification, or when asked to consolidate multiple user stories into a single source of truth.

```markdown
Use the `draft-srs-document` skill to generate an SRS from this folder of meeting notes and rough user stories.
```

## Structure
- [SKILL.md](./SKILL.md): The core workflow for mapping raw requirements to the SRS structure.
- [details/srs-template.md](./details/srs-template.md): The structural template (Introduction, Overall Description, Features, Data, Interfaces, Quality Attributes).
