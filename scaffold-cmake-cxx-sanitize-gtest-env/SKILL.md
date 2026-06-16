---
name: scaffold-cmake-cxx-sanitize-gtest-env
description: >
  WHEN/WHERE/WHO: [Scheduling: Use when an AI Agent needs to bootstrap a C/C++ project with robust testing and security guardrails.]
  HOW: [Structural: Use this SKILL to inject a standardized CMakeLists.txt that auto-discovers Google Tests and supports Clang/GCC Sanitizers, and to generate a build guide.]
  WHY: [Scheduling: Ensures all C/C++ projects have a uniform, secure, and easily testable baseline environment without manual configuration.]
---

# Scaffold CMake C++ Sanitize & GTest Environment

## Who
AI Agents, C/C++ Developers, and Build Engineers setting up or upgrading a project repository.

## What
Injects a battle-tested `CMakeLists.txt` template that enforces C11/CXX17 standards, provides compiler fallbacks (e.g., macOS Homebrew LLVM), configures Address/Thread/Memory/UndefinedBehavior Sanitizers, and uses a custom function to auto-discover and build Google Tests. It also generates a `README_BuildRunTest.md` guide for the project.

## When
Invoke this skill when a user asks to "set up a C++ project", "configure CMake with GTest", "add sanitizers to this C project", or "scaffold the C++ testing environment".
*Near-miss*: Do not use this if the user explicitly wants to use a different build system like Bazel or Make.

## Where
Applies to the root directory of a C or C++ codebase.

## Why
Manually configuring CMake for cross-platform compilation, sanitizer flags, and GTest linkage is highly error-prone. Standardizing this via an agentic skill ensures that every codebase is immediately ready for secure, test-driven development.

## Inputs
- **Project Name**: The name of the C/C++ project.
- **Target Directory**: The root directory of the project.

## Output (Logical Evidence)
- A configured `CMakeLists.txt` in the root directory.
- A `Test/` directory for unit tests.
- A `README_BuildRunTest.md` explaining how to build and test the project.

## Constraints (Logical Boundaries)
- **Sanitizer Flags**: The `CMakeLists.txt` MUST include branches for `DiagASAN`, `DiagTSAN`, `DiagUBSAN`, `DiagMSAN`, and `DiagLSAN`.
- **macOS Compatibility**: MUST include the `-Wno-availability` compiler option to suppress macOS system header warnings.
- **Anti-Pattern Mapping**: 
  1. DO NOT hardcode test executable names manually in CMake; use the template's auto-discovery loop for `*.cxx` files.
  2. DO NOT overwrite an existing `CMakeLists.txt` without the user's explicit confirmation or taking a backup.

## One More Thing
If the project already has a complex `CMakeLists.txt`, stop and ask the user if they want to merge the sanitizer/GTest logic into the existing file or replace it entirely.

## How (The 4-Phase Refinement Protocol)
<Use imperative state-machine logic. Every phase must explicitly define branching (If/Then/Else).>

### Phase 1: Environment Analysis
**Input State**: A target directory and project name.
1. Check for the existence of an existing `CMakeLists.txt`.
2. *Branch*: If it exists, pause and ask the user how to proceed (merge or overwrite).
**Output State**: Clearance to write CMake configuration.

### Phase 2: Scaffold CMakeLists.txt
**Input State**: Clearance to write.
1. Read the template from `details/cmake-template.md`.
2. Replace the placeholder project name (`MyCraftCodes`) with the user's **Project Name**.
3. Write the resulting configuration to `CMakeLists.txt` in the target directory.
**Output State**: A robust CMake configuration file created.

### Phase 3: Scaffold Test Directory
**Input State**: CMake configured.
1. Check if the `Test/` directory exists in the target directory.
2. *Branch*: If it does not exist, create it.
**Output State**: A `Test/` directory ready to receive `*.cxx` files.

### Phase 4: Generate Build/Run/Test Documentation
**Input State**: Scaffolding complete.
1. Read the template from `details/readme-build-run-test-template.md`.
2. Replace any placeholders with the **Project Name**.
3. Write the resulting markdown to `README_BuildRunTest.md` in the target directory.
**Output State**: Project documentation generated.

## Validation (Verifiable Rewards)
1. Verify that `CMakeLists.txt` exists and contains the string `DiagASAN`.
2. Verify that the `Test/` directory exists.
3. Verify that `README_BuildRunTest.md` exists.
4. If verification passes, report successful scaffolding to the user.
