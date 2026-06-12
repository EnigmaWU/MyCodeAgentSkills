---
name: create-skill-from-book
description: >
  WHEN/WHERE/WHO: [Scheduling: Architects or agents wanting to translate passive technical reference books or engineering standards into executable agent skills.]
  HOW: [Structural: Use this SKILL to extract actionable workflows, format them into the Hybrid 5W1H + SSL structure, and tailor them to embedded/real-time constraints.]
  WHY: [Scheduling: Asking an agent to read a 500-page book every chat session is too slow and context-heavy. Codifying textbooks into structured procedural steps ensures strict standard compliance automatically.]
---

# Create Skill from Book

## Who
Architects, principal developers, or coding agents who want to translate passive technical reference books or standards into executable, repeatable, and verified agent skills (`SKILL.md` packages).

## What
Ingest chapters or sections of a technical book, identify the core engineering guidelines (especially embedded, real-time, concurrency, or safety-critical rules), and codify them into a self-contained skill directory.

## When
- Triggered by requests like: "create a skill from [Book/Chapter]", "codify [Standard] into a skill", "extract design guidelines from [Reference] into a skill", or "save these textbook rules as a skill".
- Do not use for documenting one-off debugging sessions, capturing simple git command shortcuts, or summarizing meeting notes. Use `save-as-skill` or standard project documentation instead.

## Where
- Input materials can be local PDFs, text files, markdown summaries, or online documentation.
- The output belongs in a new skill directory in the workspace (e.g., `[skill-name]/SKILL.md` and related folders).

## Why
- Textbooks contain deep engineering knowledge, but asking an agent to read a 500-page book in every chat session is too slow and context-heavy.
- By translating theory into structured, code-like procedural steps, we ensure coding agents conform to strict architectures, safety limits, and best practices automatically.

## Inputs
- **Reference Material** (required): The specific book, chapter, PDF path, or URL containing the design methodology or standard.
- **Target Domain Context** (optional): Constraints specific to the target architecture (e.g., STM32, ARM Cortex-M, FreeRTOS, Linux kernel, ISO 26262 ASIL-D, MISRA C compliance).

## Output (Logical Evidence)
- **Skill Directory**: A new workspace directory containing:
  - `SKILL.md` conforming to the selected template tier (SIMPLE, COMPLICATED, or COMPLEX) in the Hybrid 5W1H + SSL framework.
  - `README.md` and `README_ZH.md` introducing the skill, its scope, and how to trigger it.
  - `details/` containing Level-3 detailed checklists or cheat sheets to keep the main file under 500 lines.
- **Validation Log**: Evidence showing the generated skill works, has valid internal file links, and does not contain generic web-stack assumptions.

## Constraints (Logical Boundaries)
- **RULE 1: Token Efficiency.** Ensure the generated `SKILL.md` remains under 500 lines. Move verbose reference material into `details/`.
- **Absolute Realism**: Do not hallucinate tools, compilers, or libraries. Every command or tool recommended in the skill must be standard and validated (e.g., `cppcheck`, `gcc-arm-none-eabi`, or specific static analyzers).
- **Embedded Rigor**: When the target domain is embedded or systems programming, the skill must explicitly cover physical limits (timing, memory, interrupts, power states) and avoid cloud/web terminology.
- **Actionable Steps**: Do not use vague language like "keep code clean" or "optimize performance." Use concrete directives like "Verify that WCET is under X ms by using oscilloscope tests or profiling hooks."

## One More Thing
If the reference material is missing, or if the safety-critical integrity levels (ASIL, SIL) are unspecified, stop and ask the user for clarification before drafting the skill.

---

## How (Structural Workflow)

### Phase 1: Ingest & Domain Mapping
1. Read the reference textbook, PDF chapters, or standard documents provided in the workspace.
2. Map the textbook content to the target engineering domain:
   * **Embedded / Real-time**: Focus on hardware constraints, register management, interrupt safety, concurrency primitives (mutexes/semaphores), RTOS tasks, and static memory bounds.
   * **Safety-Critical / Compliance**: Focus on standards compliance (MISRA C, ISO 26262, IEC 61508, AUTOSAR), fail-safe modes, defensive coding, and boundary validation.
   * **General Systems**: Focus on modular design, interface segregation, scalability, and error handling.
3. Identify and discard passive narrative, historical anecdotes, and general explanations. Filter for **actionable design patterns, rules, checklists, and testing procedures**.

### Phase 2: Extract Rules & Proceduralize
1. Review the detailed guidelines in [extraction-guidelines.md](details/extraction-guidelines.md).
2. Translate the textbook's passive theory into **imperative directives** (using verbs like *Verify*, *Configure*, *Implement*, *Check*).
3. Identify the **Constraints**: What *must not* happen under this methodology? (e.g., "Do not use dynamic allocation after initialization", "Do not write nested interrupts without priority configuration").
4. Define the **Verification Procedures**: How does the agent verify that the generated code conforms to the book's guidelines? (e.g., checking compiler warning flags, static analysis steps, unit test coverage targets).
5. Identify **Common Rationalizations**: Formulate typical excuses the agent might use to bypass these constraints (e.g., "Skipped safety-critical checks because hardware was not simulated") and detail the strict counter-rebuttal.
6. Identify **Red Flags**: Define warning signs that indicate the skill's instructions are being violated (e.g., using `malloc` in real-time loops, or unhandled priority inversions).

### Phase 3: Choose Tier & Draft SKILL.md
1. Choose the template tier from [SKILL-TEMPLATE.md](../SKILL-TEMPLATE.md):
   * **SIMPLE**: A single straight-line checklist (e.g., a MISRA C helper for pointers).
   * **COMPLICATED**: Multi-step workflows requiring inputs, outputs, and clear constraints (e.g., configuring an RTOS task pool).
   * **COMPLEX**: Branching workflows, review loops, or references to PDF files (e.g., design viewpoints, architectural tactics).
2. Create the target skill directory under the workspace.
3. Write the `SKILL.md` using the explicit **Hybrid 5W1H + SSL** structure defined in the chosen template tier (Scheduling, Structural, Logical).
4. Include the frontmatter at the top of `SKILL.md`, using the multi-line block scalar format for `description` (`WHEN/WHERE/WHO`, `HOW`, `WHY`).
5. Always include the **"One More Thing"** section instructing future agents to stop and ask the user if instructions are unclear or conflicting.

### Phase 4: Create Supporting README and Details
1. Write a `README.md` inside the new skill directory to explain to future users (and agents) what the skill is, its folder structure, and trigger phrases.
2. If the textbook contains highly detailed, chapter-specific checklists or rules, do not clutter `SKILL.md`. Move them to separate markdown files in a `details/` directory and link to them using standard relative markdown links (e.g., a link pointing to `details/checklist-name.md`).
3. Always include the **"One More Thing"** section instructing future agents to stop and ask the user if instructions are unclear or conflicting.

### Phase 5: Self-Verify & Refine
1. Check that all internal markdown links are valid and clickable.
2. Read the drafted `SKILL.md` and check for **web-stack drift** (e.g., references to JavaScript, Node.js, Web APIs, or cloud platforms in an embedded RTOS skill). Correct them immediately.
3. Verify that all instructions are actionable, and that every step is clear.

---

## Resources
- [extraction-guidelines.md](details/extraction-guidelines.md) - Deep-dive guidelines on extracting procedural checklists for embedded/systems architectures.
- [SKILL-TEMPLATE.md](../SKILL-TEMPLATE.md) - The workspace templates for SIMPLE, COMPLICATED, and COMPLEX skills.

---

## Validation
1. Verify that the skill directory contains `SKILL.md` and `README.md`.
2. Verify that the frontmatter is present and syntactically correct (description quoted).
3. Verify that the `SKILL.md` has the required sections matching the selected template tier.
4. Verify that there are zero references to hallucinated libraries or tools.
5. Verify that all markdown links within the skill package are valid.
