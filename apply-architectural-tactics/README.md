# Apply Architectural Tactics

An agent skill for applying systematic software architecture methodologies from *Software Architecture in Practice* (SAiP) by Len Bass, Paul Clements, and Rick Kazman.

## What Is This

This skill teaches coding agents how to perform structured architectural design and analysis driven by **Quality Attributes** (non-functional requirements) rather than ad-hoc technology selections. It prevents agents from jumping straight to specific tools or libraries without analyzing the system's availability, modifiability, performance, security, and testability goals.

## Directory Structure

```text
apply-architectural-tactics/
  ├── SKILL.md                                 # Level-1: Main skill workflow (COMPLEX tier)
  ├── references/
  │   └── Software Architecture in Practice.pdf # Original textbook PDF (user-provided)
  └── details/                                 # New folder for structured references
      ├── quality-attribute-tactics-and-checklists.md  # Level-2: Summary outline
      ├── availability-checklist-details.md    # Level-3: Detailed Ch 5 availability checklist
      ├── performance-checklist-details.md     # Level-3: Detailed Ch 8 performance checklist
      ├── security-checklist-details.md        # Level-3: Detailed Ch 9 security checklist
      └── modifiability-checklist-details.md   # Level-3: Detailed Ch 7 modifiability checklist
```

## Why This Method Matters

LLM agents often over-specialize or hallucinate configurations when designing software architectures. This skill forces the agent to follow the **Attribute-Driven Design (ADD)** method:
1. **Utility Tree & QAS**: Quantifying vague goals ("fast response time") into 6-part measurable scenarios.
2. **Tactics Catalog**: Selecting proven design strategies (e.g., active redundancy, caching, encapsulation) from the book before selecting technologies.
3. **ATAM (Architecture Tradeoff Analysis Method)**: Performing tradeoff analysis to highlight sensitivity points (e.g., database replication level) and risks.
4. **CBAM (Cost Benefit Analysis Method)**: Factoring in implementation costs and quality benefits to compute Return on Investment (ROI) for design choices.

## Usage

When designing or reviewing a system, invoke this skill using trigger phrases such as:
* *"apply tactics to this system design"*
* *"design a system for [requirements] using SAiP tactics"*
* *"evaluate the quality attribute scenarios of this architecture"*

The agent will load the summaries and detailed checklists from the `details/` directory to generate structured, validated design documents.
