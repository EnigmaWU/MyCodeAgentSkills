# Document Legacy Codebase

An agent skill for reverse-engineering legacy (brownfield) codebases, mapping superimposed structures, and establishing boundaries (Bubble Context/Strangler patterns) without breaking legacy operations, based on Cyrille Martraire's book *Living Documentation*.

## What Is This

This skill guides coding agents and developers in extracting, preserving, and managing knowledge from fossilized legacy codebases. Instead of performing high-risk in-place modifications, it guides users in software archaeology, wrapping legacy structures with anticontamination/bubble interfaces, and superimposing metadata layers (external databases, sidecars, and decorators) to make the legacy system manageable and safe to evolve.

## TOP-3 Golden Rules of Legacy Documentation

Developers and agents using this skill must strictly follow these three critical principles:

1. **Bubble Context Boundaries**
   * *Rule*: Always define and enforce a clear semantic boundary (Bubble Context or Anticorruption Layer) around legacy code before introducing new functionality or metadata.
   * *WHY*: Attempting to document or refactor legacy code in-place causes scope creep and logic corruption. Wrapping legacy systems in a clean, adapter-based boundary isolates legacy behaviors and permits modern, clean patterns inside the new bubble.

2. **Superimposed Structures over In-Place Refactoring**
   * *Rule*: Use superimposed structures (e.g., external sidecars, custom metadata databases, decorators, or aspect-oriented wrappers) to document and classify legacy behavior without altering the historical code itself.
   * *WHY*: Editing legacy source code directly carries severe regression risks and invalidates existing, fragile test suites. Superimposing metadata structures organizes legacy understanding without changing executable code.

3. **Biodegradable Transformation & Strangler Annotations**
   * *Rule*: Mark legacy code targeted for replacement with biodegradable annotations (e.g., `@StranglerApplication`, `@DeprecatedWithDeadline`, or external registry tracking) that explicitly record deprecation timelines, ownership, and replacement paths.
   * *WHY*: Unmarked legacy code remains in production indefinitely due to fear of deletion. Biodegradable markers create visibility and positive pressure on teams to replace outdated code, preventing it from remaining fossilized.

## Directory Structure

```text
document-legacy-codebase/
  ├── SKILL.md                                 # Level-1: Main skill workflow (COMPLEX tier)
  ├── README.md                                # Overview and usage instructions
  └── details/                                 
      ├── legacy-checklists.md                 # Level-2/3: Checklists for archaeology & boundaries
      └── code-examples.md                     # Level-3: Metadata mappings, strangler decorators, & test examples
```

## Why This Method Matters

Legacy code is fossilized knowledge. Changing it is dangerous, but leaving it undocumented is equally risky. This method enables teams to:
1. **Minimize Risk**: Map legacy flows without rewriting stable, high-value historical code.
2. **Isolate Complexity**: Establish clear boundaries so modern features do not inherit legacy technical debt.
3. **Plan Migration**: Use strangler patterns and biodegradable decorators to incrementally migrate legacy systems to new architectures.
4. **Build System Transparency**: Map external databases and sidecars to document system endpoints and dependencies.

## Usage

Invoke this skill using trigger phrases such as:
* *"document this legacy codebase to map its structures..."*
* *"establish a bubble context around this module..."*
* *"apply a strangler pattern boundary for migration..."*
* *"superimpose a metadata structure on this legacy code..."*
* *"perform software archaeology on this brownfield module..."*

The invoking agent will outline legacy endpoints, define boundary interfaces, and establish external metadata mappings by referring to [SKILL.md](file:///Users/enigmawu/VSCode/MyCodeAgentSkills/document-legacy-codebase/SKILL.md).
