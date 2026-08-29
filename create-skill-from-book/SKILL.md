---
name: create-skill-from-book
description: >
  WHEN/WHERE/WHO: [Scheduling: Architects or agents wanting to translate passive technical reference books or engineering standards into executable agent skills.]
  HOW: [Structural: Use this COMPLEX SKILL to extract actionable workflows, choose the correct tier, format them into the Hybrid 5W1H + SSL structure, and refine the generated skill through an evidence-backed validation gate.]
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
- **Optimization Notes**: A short record of the selected tier, failure signals for the new skill, what evidence was used to shape it, and any rejected drafting choices that should not be repeated blindly.

## Optimization Readiness
- **Failure Signals**: The drafted skill contains vague directives, mismatched tier depth, weak trigger boundaries, non-actionable validation, domain drift, or instructions that cannot be executed from natural language alone.
- **Evidence To Collect**: Source excerpts, repeated chapter patterns, domain constraints, candidate trigger phrases, validation checks, and any review findings discovered during drafting.
- **Safe Mutation Boundaries**: Revise frontmatter wording, section structure, checklist phrasing, validation steps, and supporting detail files without changing the source material's core intent.
- **Acceptance Criteria**: Accept the generated skill only if it matches the chosen tier's control depth, includes the required template sections, contains actionable validation, preserves domain realism, and is readable without the original book open.
- **Rejected Revision Handling**: Record discarded naming choices, rejected trigger phrases, and failed structural ideas in the validation log or supporting notes so the same low-quality draft is not recreated later.
- **Transfer Check**: Confirm that the drafted skill can guide at least one nearby use case beyond the exact chapter excerpt used for extraction.
- **Stop Rule**: If the source material is ambiguous, the domain constraints are missing, or two consecutive revisions fail the same acceptance check, stop and ask the user for clarification instead of widening the draft blindly.

## Constraints (Logical Boundaries)
- **RULE 1: Token Efficiency.** Ensure the generated `SKILL.md` remains under 500 lines. Move verbose reference material into `details/`.
- **Absolute Realism**: Do not hallucinate tools, compilers, or libraries. Every command or tool recommended in the skill must be standard and validated (e.g., `cppcheck`, `gcc-arm-none-eabi`, or specific static analyzers).
- **Embedded Rigor**: When the target domain is embedded or systems programming, the skill must explicitly cover physical limits (timing, memory, interrupts, power states) and avoid cloud/web terminology.
- **Actionable Steps**: Do not use vague language like "keep code clean" or "optimize performance." Use concrete directives like "Verify that WCET is under X ms by using oscilloscope tests or profiling hooks."
- **Tier Honesty**: Choose the output tier by workflow depth and control structure, not by how important the topic sounds or how much text was extracted.
- **Independent Acceptance Gate**: Do not treat the first complete draft as accepted only because all files exist. The generated skill must pass the validation gate defined below.

## How (Structural Workflow)

### Phase 1: Ingest & Domain Mapping
1. Read the reference textbook, PDF chapters, or standard documents provided in the workspace.
2. Map the textbook content to the target engineering domain:
   * **Embedded / Real-time**: Focus on hardware constraints, register management, interrupt safety, concurrency primitives (mutexes/semaphores), RTOS tasks, and static memory bounds.
   * **Safety-Critical / Compliance**: Focus on standards compliance (MISRA C, ISO 26262, IEC 61508, AUTOSAR), fail-safe modes, defensive coding, and boundary validation.
   * **General Systems**: Focus on modular design, interface segregation, scalability, and error handling.
3. Identify and discard passive narrative, historical anecdotes, and general explanations. Filter for **actionable design patterns, rules, checklists, and testing procedures**.
4. If the source text is too broad, split it into a bounded extraction target such as one chapter, one pattern family, or one operational theme before drafting the skill.

### Phase 2: Extract Rules & Proceduralize
1. Review the detailed guidelines in [extraction-guidelines.md](details/extraction-guidelines.md).
2. Translate the textbook's passive theory into **imperative directives** (using verbs like *Verify*, *Configure*, *Implement*, *Check*).
3. Identify the **Constraints**: What *must not* happen under this methodology? (e.g., "Do not use dynamic allocation after initialization", "Do not write nested interrupts without priority configuration").
4. Define the **Verification Procedures**: How does the agent verify that the generated code conforms to the book's guidelines? (e.g., checking compiler warning flags, static analysis steps, unit test coverage targets).
5. Identify **Common Rationalizations**: Formulate typical excuses the agent might use to bypass these constraints (e.g., "Skipped safety-critical checks because hardware was not simulated") and detail the strict counter-rebuttal.
6. Identify **Red Flags**: Define warning signs that indicate the skill's instructions are being violated (e.g., using `malloc` in real-time loops, or unhandled priority inversions).
7. Extract candidate **failure signals**, **acceptance criteria**, and **transfer checks** for the future skill so the draft is optimization-ready from the first version.

### Phase 3: Choose Tier & Draft SKILL.md
1. Choose the template tier from [SKILL-TEMPLATE.md](../CREATING-SKILL-TEMPLATE/details/SKILL-TEMPLATE.md):
   * **SIMPLE**: A single straight-line checklist (e.g., a MISRA C helper for pointers).
   * **COMPLICATED**: Multi-step workflows requiring inputs, outputs, and clear constraints (e.g., configuring an RTOS task pool).
  * **COMPLEX**: Branching workflows, review loops, multi-phase control logic, or multiple supporting artifacts (e.g., design viewpoints, architectural tactics, or book-derived meta-skills).
2. Create the target skill directory under the workspace.
3. Write the `SKILL.md` using the explicit **Hybrid 5W1H + SSL** structure defined in the chosen template tier (Scheduling, Structural, Logical).
4. Include the frontmatter at the top of `SKILL.md`, using the multi-line block scalar format for `description` (`WHEN/WHERE/WHO`, `HOW`, `WHY`).
5. Add the template's **Optimization Readiness** section and fill it with concrete failure signals, evidence, safe mutation boundaries, acceptance criteria, rejection handling, and a stop rule derived from the source material.
6. Always include the **"One More Thing"** section instructing future agents to stop and ask the user if instructions are unclear or conflicting.

### Phase 4: Create Supporting README and Details
1. Write a `README.md` inside the new skill directory to explain to future users (and agents) what the skill is, its folder structure, and trigger phrases.
2. Write a `README_ZH.md` that mirrors the skill's scope and trigger guidance in Chinese.
3. If the textbook contains highly detailed, chapter-specific checklists or rules, do not clutter `SKILL.md`. Move them to separate markdown files in a `details/` directory and link to them using standard relative markdown links (e.g., a link pointing to `details/checklist-name.md`).
4. Place any extraction traces, rejected naming options, or extended rule inventories in supporting files rather than bloating the main skill.

### Phase 5: Self-Verify & Refine
1. Run the validation gate on the draft: check that all internal markdown links are valid and clickable, the tier matches the workflow depth, the optimization-readiness section is present, and the validation steps are actionable.
2. Read the drafted `SKILL.md` and check for **web-stack drift** (e.g., references to JavaScript, Node.js, Web APIs, or cloud platforms in an embedded RTOS skill). Correct them immediately.
3. Compare the draft against the extracted source evidence. If a rule cannot be traced back to the source material or domain constraints, remove or rewrite it.
4. If validation fails, revise only the sections that caused the failure and rerun the same validation gate.
5. Stop after two failed revision cycles on the same issue and ask the user for missing context rather than continuing uncontrolled rewrites.

---

## Resources
- [extraction-guidelines.md](details/extraction-guidelines.md) - Deep-dive guidelines on extracting procedural checklists for embedded/systems architectures.
- [SKILL-TEMPLATE.md](../CREATING-SKILL-TEMPLATE/details/SKILL-TEMPLATE.md) - The workspace templates for SIMPLE, COMPLICATED, and COMPLEX skills.

---

## Review In Mind (ReviewInMindGenie)

Before delivering, activate the ReviewInMindGenie: stop authoring, switch to a skeptical reviewer, and critique the artifact as if someone else had produced it.

1. **Review Against Own Rules**: Re-read the output against this skill's `What`, `Constraints (Logical Boundaries)`, and `Validation` criteria. Check each rule explicitly; do not assume it passed because it was easy to write.
2. **Classify Findings**: Label each defect as BLOCKER (output unusable), MAJOR (violates a core rule), or MINOR (polish/consistency).
3. **Fix or Escalate**: Fix BLOCKER and MAJOR findings immediately when the fix is unambiguous. After each fix, re-check the affected criteria. If a finding cannot be fixed without new input (missing evidence, conflicting requirements, or a user decision), do not guess — report it as an open question or known gap.
4. **Deliver with a Review Note**: Present the output with a short note: what was checked, what was fixed, and what remains as a known gap. Never present an unreviewed artifact as final.

Review lens for this skill:
- Are guidelines faithful to the book and traceable to specific sections, not paraphrased inventions?
- Does the generated skill include the full required structure (frontmatter, 5W1H, Optimization Readiness, Constraints, How, Validation, Review In Mind)?
- Are safety-critical or normative rules marked as MUST and separated from recommendations?

## Validation
1. Verify that the skill directory contains `SKILL.md`, `README.md`, and `README_ZH.md`.
2. Verify that the frontmatter is present and uses the multi-line `description: >` format required by the template.
3. Verify that the `SKILL.md` has the required sections matching the selected template tier, including `## Optimization Readiness`.
4. Verify that there are zero references to hallucinated libraries or tools.
5. Verify that all markdown links within the skill package are valid.
6. Verify that the generated skill can be executed from natural language alone and does not depend on diagrams or direct access to the original book during normal use.
7. Verify that the validation log records the chosen tier, the acceptance gate results, and any rejected drafting choices.

---

## One More Thing
If the reference material is missing, or if the safety-critical integrity levels (ASIL, SIL) are unspecified, stop and ask the user for clarification before drafting the skill.
