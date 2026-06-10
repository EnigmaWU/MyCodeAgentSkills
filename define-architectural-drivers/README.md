# define-architectural-drivers

## Overview
This skill guides the agent to extract and formalize **Architectural Drivers** from unstructured product requirements (PRDs, User Stories, or transcripts). It ensures that before any design happens (via ADD 3.0), the four types of drivers are clearly defined: Design Purpose, Quality Attributes, Primary Functionality, and Constraints/Concerns.

## Usage
Trigger this skill when given raw requirements and asked to prepare them for architectural design.

```markdown
Use the `define-architectural-drivers` skill to extract the drivers from this PRD before we start designing.
```

## Structure
- [SKILL.md](./SKILL.md): The core workflow for extracting and formalizing the drivers.
- [details/driver-extraction-template.md](./details/driver-extraction-template.md): A template for recording the extracted drivers formally.
