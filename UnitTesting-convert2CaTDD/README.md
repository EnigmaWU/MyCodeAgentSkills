# UnitTesting-convert2CaTDD

Convert existing or legacy test files into CaTDD (Comment-alive Test-Driven Development) format, making tests self-documenting design artifacts that humans and LLMs can collaborate on.

## What Is CaTDD

**CaTDD** (Comment-alive Test-Driven Development) is a software development methodology created by EnigmaWU (since October 2023) where:

- **Comments ARE Verification Design** — Structured comments (US/AC/TC) define what to verify, not just documentation.
- **LLMs Generate Code** — AI parses structured comments to produce test and production code.
- **Iterate Forward Together** — Design and code evolve as one through human+AI collaboration.

> **Slogan**: *"Comments is Verification Design. LLM Generates Code. Iterate Forward Together."*

The test file becomes the **single source of truth** — readable by humans, parseable by LLMs, and verified by tests.

## What This Skill Does

This skill takes existing test files that lack structured design comments and converts them into CaTDD format by:

1. **Analyzing** existing tests to understand what they verify.
2. **Extracting** verification design as User Stories (US), Acceptance Criteria (AC), and Test Cases (TC).
3. **Restructuring** the test file with CaTDD sections (OVERVIEW, DESIGN, IMPLEMENTATION, TODO).
4. **Classifying** tests by priority (P1 Functional → P2 Design → P3 Quality → P4 Addons).
5. **Reporting** coverage gaps and traceability.

All existing tests are preserved — the skill adds structure, not changes behavior.

## CaTDD Structure Overview

A CaTDD test file contains these sections:

```
┌──────────────────────────────────────────────────┐
│ OVERVIEW                                         │
│   [WHAT] / [WHERE] / [WHY] / SCOPE / KEY CONCEPTS│
├──────────────────────────────────────────────────┤
│ UNIT TESTING DESIGN                              │
│   ├── Test Case Design Aspects (Priority Framework)│
│   ├── User Story Design (US)                     │
│   ├── Acceptance Criteria Design (AC)            │
│   └── Test Cases Design (TC specs + status)      │
├──────────────────────────────────────────────────┤
│ UNIT TESTING IMPLEMENTATION                      │
│   └── Tests with 4-phase pattern:                │
│       SETUP → BEHAVIOR → VERIFY → CLEANUP        │
├──────────────────────────────────────────────────┤
│ TODO / IMPLEMENTATION TRACKING                   │
│   └── Status: ⚪ TODO → 🔴 RED → 🟢 GREEN        │
└──────────────────────────────────────────────────┘
```

## US/AC/TC Hierarchy

```
User Story (US) — WHY we need this feature (business value)
    ↓
Acceptance Criteria (AC) — WHAT behavior must be satisfied (GIVEN/WHEN/THEN)
    ↓
Test Case (TC) — HOW to verify the behavior (concrete steps)
```

## Priority Framework

```
P1 🥇 FUNCTIONAL = ValidFunc(Typical + Boundary) + InvalidFunc(Misuse + Fault)
P2 🥈 DESIGN     = State → Capability → Concurrency
P3 🥉 QUALITY    = Performance → Robust → Compatibility → Configuration
P4 🎯 ADDONS     = Demo/Example
```

## Usage

### Trigger the Skill

In a conversation with an AI agent, say:

```text
Convert this test file to CaTDD format: path/to/test_file.py
```

Or:

```text
Apply CaTDD to my existing tests in tests/
```

### Bundled References

| File | Purpose |
| ---- | ------- |
| `references/CaTDD_UserGuide.md` | Full user guide with examples, patterns, and getting-started checklist |
| `references/CaTDD_DesignPrompt.md` | Complete methodology specification with priority framework and quality gates |
| `references/CaTDD_ImplTemplate.cxx` | C++ implementation template showing the full CaTDD file structure |

## Origin

CaTDD was developed by [EnigmaWU](https://github.com/EnigmaWU) in the [MyIOC_inTDD_withGHC](https://github.com/EnigmaWU/MyIOC_inTDD_withGHC) project. This skill packages the methodology for reuse in any project through the MyCodeAgentSkills system.
