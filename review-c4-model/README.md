# review-c4-model

Review software architecture diagrams against the C4 model rules from Simon Brown's
*The C4 Model: Visualizing Software Architecture*.

## What it does

Classifies a diagram's type (system context, container, component, code, dynamic,
deployment, or system landscape), runs the book's general/element/relationship
checklists plus level-specific scope checks, and produces a verdict (PASS, PASS WITH
CONDITIONS, or FAIL) with every finding mapped to a concrete rule and fix.

## Structure

```text
review-c4-model/
  ├── SKILL.md                       # Main workflow (COMPLICATED tier)
  ├── README.md                      # This overview
  ├── README_ZH.md                   # Chinese overview
  ├── agents/openai.yaml             # UI metadata
  └── details/
      ├── review-checklist.md        # Full PASS/FAIL checklist
      ├── notation-reference.md      # Chapter 10 notation guidance
      ├── common-anti-patterns.md    # Failure patterns and rebuttals
      └── validation-log.md          # Tier choice and acceptance evidence
```

## Trigger phrases

- "review / critique / check this architecture diagram"
- "is this a valid or correct C4 diagram"
- "find problems in this diagram"
- "does this diagram follow the C4 model"

## Usage

Provide one or more diagrams (image, PDF page, diagram-as-code, or pasted content)
and optionally the diagram type or intended audience. The skill returns a structured
review report. Ask for a file if you want the report saved to disk.

Created from *The C4 Model: Visualizing Software Architecture* by Simon Brown
(O'Reilly, 2026) using the `create-skill-from-book` workflow.
