# Create Living Documentation

An agent skill for automating software specifications, glossaries, system diagrams, and design decisions using dynamic extraction, single-source publishing, and reconciliation tests, based on Cyrille Martraire's book *Living Documentation*.

## What Is This

This skill guides coding agents and developers in creating documentation that is **reliable, low-effort, collaborative, and insightful**. Instead of maintaining manual Word documents, wikis, or PDFs that drift from the source code, this skill implements mechanisms to extract documentation directly from code annotations, types, tests, and compilation artifacts, ensuring it remains a single source of truth.

## TOP-3 Golden Rules of Living Documentation

Developers and agents using this skill must strictly follow these three critical principles:

1. **Single Source of Truth & Zero Manual Duplication**
   * *Rule*: Never maintain duplicate manual documentation for properties, specifications, structures, or configurations that can be extracted directly from source code, annotations, or compilation artifacts.
   * *WHY*: Manual documentation drifts instantly the moment code changes, becoming misleading. Extracting specifications, glossaries, or diagrams dynamically from code elements ensures that documentation is always accurate and updated automatically with the codebase.

2. **Automated Reconciliation & Consistency Checking**
   * *Rule*: Always establish automated reconciliation tests (e.g., unit tests, BDD feature verification, or metadata checks) that assert the consistency between source code, dynamic specifications, and external documentation.
   * *WHY*: If documentation extraction runs in a vacuum, silent extraction failures or API shifts can render documentation incomplete. Automated consistency checks fail the build if code representations and generated docs mismatch, enforcing alignment.

3. **Refactorable & Intent-Revealing Code Elements**
   * *Rule*: Document code structure and business intent primarily using type-driven design, expressive naming conventions, and custom annotations rather than free-form text comments.
   * *WHY*: Plain text comments cannot be refactored by IDEs and are ignored by compilers. Expressive names, custom annotations, and strong types are refactored automatically by tools, preserving the accuracy of documentation during code modifications.

## Directory Structure

```text
create-living-documentation/
  ├── SKILL.md                                 # Level-1: Main skill workflow (COMPLEX tier)
  ├── README.md                                # Overview and usage instructions
  └── details/                                 
      ├── reconciliation-checklists.md         # Level-2/3: Checklists for single-source curation & BDD
      └── code-examples.md                     # Level-3: Parser, diagram generator, & contract test scripts
```

## Why This Method Matters

Traditional documentation is expensive to produce, expensive to maintain, and rarely read. By adopting living documentation, developers guarantee:
1. **Zero Drift**: Documentation is generated from the code, meaning the code *is* the documentation.
2. **High Credibility**: Automated tests fail when documentation rules are violated, making the docs as reliable as the test suite.
3. **Reduced Overhead**: Developers write documentation using the programming languages, types, and annotations they already use daily.
4. **Actionable Insights**: Visual tools generate living architecture and class diagrams (PlantUML, Graphviz) from the current code, not outdated whiteboard drawings.

## Usage

Invoke this skill using trigger phrases such as:
* *"create a living glossary from these packages..."*
* *"automate system diagrams using PlantUML from source..."*
* *"design a reconciliation test for this specification..."*
* *"extract living specifications from BDD feature files..."*
* *"generate architecture codex from class annotations..."*

The invoking agent will parse class files, extract metadata, compile living glossaries, and generate automated diagram specs by referring to [SKILL.md](file:///Users/enigmawu/VSCode/MyCodeAgentSkills/create-living-documentation/SKILL.md).
