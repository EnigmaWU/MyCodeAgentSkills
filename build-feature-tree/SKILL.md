---
name: build-feature-tree
description: >
  WHEN/WHERE/WHO: Analysts or agents reviewing flat product backlogs or lengthy PRDs.
  HOW: Use this SKILL to group unstructured requirements into a hierarchical Feature Tree (L1, L2, L3) rendered as a mindmap.
  WHY: Flat lists hide missing features. A visual hierarchy exposes gaps (e.g., "We have 'Edit Profile', but where is 'Delete Profile'?").
---

# Build Feature Tree

## Who
Business Analysts, Product Managers, and AI Agents. The agent uses this skill to restructure and visualize scope.

## What
This skill implements the Feature Tree from the Requirements Modeling Language (RML). It takes a flat list of features or user stories and categorizes them into a strict hierarchy:
- **L1 (Level 1):** Major functional areas (e.g., "Account Management").
- **L2 (Level 2):** Feature groups (e.g., "User Profile").
- **L3 (Level 3):** Specific features (e.g., "Update Avatar").

It outputs this structure as a Mermaid.js Mindmap.

## When
Invoke this skill during scope definition or when analyzing a lengthy PRD. Trigger phrases include: "build a feature tree," "organize this backlog," "create a mindmap of features," or "check for missing features."

## Where
Applies to Product Requirements Documents (PRDs), JIRA backlogs, and feature lists.

## Why
A backlog with 150 items is impossible to review for completeness. By organizing features hierarchically on a single page, the human brain can instantly spot missing siblings (e.g., if L2 "Reporting" only has L3 "Export to CSV", someone will ask "What about Export to PDF?").

## Inputs
- A flat list of features, requirements, or user stories.
- The overarching Product Concept (the root node).

## Output
- A hierarchical list of features.
- A Mermaid.js Mindmap rendering the tree.
- A list of "Potential Missing Features" discovered by analyzing the visual gaps.

## Constraints
- Features should be brief noun phrases (e.g., "Shopping Cart," not "The system shall allow the user to add items to a cart").
- Limit the depth to 3 or 4 levels to maintain readability.

## One More Thing
If the input text is not a list of features but rather a list of technical tasks (e.g., "Setup database," "Configure DNS"), stop and inform the user that a Feature Tree models *business functionality*, not technical implementation.

## How

### Phase 1: Extraction and Normalization
1. Read the input and extract all functional requirements.
2. Convert long sentences into concise 1-3 word noun phrases.

### Phase 2: Hierarchical Grouping
3. Identify the **L1 Features** (Major functional areas, usually 3-7 max).
4. Group the remaining features under the appropriate L1 buckets to form **L2 Features**.
5. Break down complex L2 features into **L3 Features** if necessary.

### Phase 3: Visualization and Analysis
6. Output the structure using Mermaid.js Mindmap syntax.
7. Review the tree for symmetry and completeness. If an L2 category feels sparse compared to its siblings, suggest missing L3 features.

## Resources
- [Feature Tree Examples](./details/feature-tree-examples.md)

## Validation
1. Verify that the Mermaid syntax is valid (`mindmap` format).
2. Ensure no feature from the original list was dropped; every item must have a home in the tree.
