# extract-business-rules

## Overview
This skill guides the agent to extract and classify Business Rules from unstructured requirements text, as defined in *Software Requirements (3rd Edition)*. Business rules (policies, laws, regulations, and industry standards) dictate how a system must behave, but they are often incorrectly documented as software features. By extracting them, teams can manage the rules independently of the software implementation.

## Usage
Trigger this skill when given raw vision documents, stakeholder meeting notes, user stories, or PRDs that contain embedded business logic.

```markdown
Use the `extract-business-rules` skill to find the hidden rules in these new user stories.
```

## Structure
- [SKILL.md](./SKILL.md): The core workflow for extracting and categorizing rules.
- [details/business-rules-taxonomy.md](./details/business-rules-taxonomy.md): The taxonomy used to classify the extracted rules (Facts, Constraints, Action Enablers, Inferences, Computations).
