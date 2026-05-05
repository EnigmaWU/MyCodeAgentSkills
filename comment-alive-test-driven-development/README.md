# comment-alive-test-driven-development

Write new test files from scratch using CaTDD (Comment-alive Test-Driven Development), where structured comments define verification design before any code is written. Applicable to UnitTesting, SysTesting, and UserTesting in any language.

## What Is CaTDD

**CaTDD** (Comment-alive Test-Driven Development) is a software development methodology created by EnigmaWU (since October 2023) where:

- **Comments ARE Verification Design** — Structured comments (US/AC/TC) define what to verify, not just documentation.
- **LLMs Generate Code** — AI parses structured comments to produce test and production code.
- **Iterate Forward Together** — Design and code evolve as one through human+AI collaboration.

> **Slogan**: *"Comments is Verification Design. LLM Generates Code. Iterate Forward Together."*

The test file becomes the **single source of truth** — readable by humans, parseable by LLMs, and verified by tests.

## What This Skill Does

This skill guides the creation of a brand-new test file using CaTDD methodology by:

1. **Defining scope** — Writing the OVERVIEW (WHAT/WHERE/WHY) and coverage strategy.
2. **Designing verification** — Writing User Stories (US), Acceptance Criteria (AC), and Test Case specifications (TC) as structured comments.
3. **Implementing** — Following the TDD Red→Green cycle for each TC in priority order.
4. **Validating** — Checking traceability, coverage completeness, and test quality.

## CaTDD File Structure

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

## Applicable Testing Levels

| Level | Description | Example file names |
| ----- | ----------- | ------------------ |
| UnitTesting | Single module or function | `UT_FeatureName.cxx`, `test_module.py` |
| SysTesting | Component interactions | `ST_ServiceName.go`, `sys_test_*.java` |
| UserTesting | End-to-end user flows | `UAT_Feature.ts`, `user_acceptance_*.py` |

## Usage

### Trigger the Skill

In a conversation with an AI agent, say:

```text
Use CaTDD to write new tests for the UserAuth module in Python.
```

Or:

```text
Create a new CaTDD test file for the EventQueue service, system testing level.
```

Or:

```text
Apply comment-alive test-driven development to design tests for this API: <header file>
```

### Bundled References

| File | Purpose |
| ---- | ------- |
| `references/CaTDD_UserGuide.md` | Full user guide with examples, quick-start guide, and getting-started checklist |
| `references/CaTDD_DesignPrompt.md` | Complete methodology specification with priority framework, category definitions, and quality gates |
| `references/CaTDD_ImplTemplate.cxx` | C++ implementation template showing the full CaTDD file structure (adapt for any language) |
| `references/CaTDD-UserGuide-PPT.md` | Presentation-style overview of all CaTDD concepts with slides, diagrams, and real examples |

## Related Skills

- **`UnitTesting-convert2CaTDD`** — Use this when you want to convert *existing* test files to CaTDD format. This skill (`comment-alive-test-driven-development`) is for writing *new* test files from scratch.
- **`test-driven-development`** — Classic TDD Red→Green→Refactor workflow without the CaTDD comment structure.

## Origin

CaTDD was developed by [EnigmaWU](https://github.com/EnigmaWU) in the [MyIOC_inTDD_withGHC](https://github.com/EnigmaWU/MyIOC_inTDD_withGHC) project. This skill packages the full methodology for reuse in any project through the MyCodeAgentSkills system.
