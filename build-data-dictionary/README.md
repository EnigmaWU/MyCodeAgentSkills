# build-data-dictionary

## Overview
This skill guides the agent to extract and define data elements from functional requirements, generating a **Data Dictionary** as described in *Software Requirements (3rd Edition)*. A Data Dictionary provides a common vocabulary for the project, ensuring that when developers and stakeholders say "Customer ID," they mean the exact same data type and format.

## Usage
Trigger this skill when requirements mention specific data entities, forms, or reports, but lack technical data definitions.

```markdown
Use the `build-data-dictionary` skill to define the data structures mentioned in this checkout flow.
```

## Structure
- [SKILL.md](./SKILL.md): The core workflow for extracting nouns and defining data structures.
- [details/data-dictionary-format.md](./details/data-dictionary-format.md): The standard tabular format for defining primitive data elements and structures.
