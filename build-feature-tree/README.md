# build-feature-tree

## Overview
This skill guides the agent to organize a flat list of product features into a hierarchical **Feature Tree** (L1, L2, L3 features), as defined in *Visual Models for Software Requirements*. A Feature Tree allows stakeholders to view the entire scope of a system on a single page, making it easy to identify missing functional areas or redundant requirements.

## Usage
Trigger this skill when given a PRD, backlog, or list of user stories that is too long or flat to comprehend easily.

```markdown
Use the `build-feature-tree` skill to organize these 50 user stories into a hierarchical Mermaid mindmap.
```

## Structure
- [SKILL.md](./SKILL.md): The core workflow for identifying L1, L2, and L3 features and rendering the tree.
- [details/feature-tree-examples.md](./details/feature-tree-examples.md): Examples of how to format the Feature Tree using Mermaid.js syntax.
