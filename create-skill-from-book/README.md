# Create Skill from Book

An agent skill for systematically ingesting engineering textbooks and reference materials and converting them into reusable, executable agent skills with explicit tier selection, optimization readiness, and validation gates.

## What Is This

Technical books contain invaluable wisdom, but reading entire chapters is too slow and expensive for an AI agent during a live coding session. This skill defines a workflow to extract **procedural guidelines** from books and compile them into a structured `SKILL.md` (and detailed checklists in `details/`).

It is designed with the rigor needed for **senior embedded software architects and developers**, emphasizing physical constraints, real-time safety, deterministic behavior, and strict validation over general software abstractions.

The workflow is intentionally **COMPLEX**: it classifies source material, chooses the correct output tier (`SIMPLE`, `COMPLICATED`, or `COMPLEX`), injects the template's `Optimization Readiness` section, and accepts a draft only after it passes an evidence-backed validation gate.

## Directory Structure

```text
create-skill-from-book/
  ├── SKILL.md                                 # Level-1: Main skill workflow (COMPLEX tier)
  ├── README.md                                # Overview and usage instructions
  ├── README_ZH.md                             # Chinese overview and usage instructions
  └── details/                                 
      └── extraction-guidelines.md             # Level-3: Detailed guide for extracting embedded & systems skills
```

## Why This Method Matters

When building complex real-time or safety-critical software, generic programming practices are not enough. We must follow rigorous domain-specific guidelines (e.g., MISRA C, ISO 26262, OSEK/VDX, or concurrency models). This skill enables:

1. **Proceduralization**: Turning passive theory ("the book says to do X") into active prompts/checklists that coding agents can step-by-step execute.
2. **Context Window Management**: Reducing a 500-page textbook into a highly focused ~200-line `SKILL.md` and related Level-3 details.
3. **Rigorous Validation**: Ensuring the generated skill is concrete, actionable, explicitly addresses domain constraints (e.g., memory limits, timing constraints, hardware hazards), and is not accepted only because the files were created.
4. **Optimization Readiness**: Ensuring each generated skill already includes failure signals, evidence sources, safe mutation boundaries, acceptance criteria, rejected-revision handling, and a stop rule for future refinement.

## What The Skill Produces

- A new skill package with `SKILL.md`, `README.md`, and `README_ZH.md`.
- Supporting `details/` files when the extracted material would otherwise bloat the main skill.
- A validation log or equivalent notes capturing the chosen tier, the acceptance-gate result, and any rejected drafting choices.

## Usage

When you want to codify a technical book or reference guide into a reusable skill package, invoke this skill using triggers like:

- *"create a skill from [Book Name]"*
- *"extract a skill for [Topic] from [Reference Document]"*
- *"codify the guidelines in [Book/Chapter] into a skill"*

The agent will read the extraction guidelines, choose the correct output tier by workflow depth, build a complete skill package in the workspace, and refine the draft through a bounded validation gate.

The generated skill should remain executable from natural language alone. Diagrams or source-book visuals may inform extraction, but they are not required for normal use of the resulting skill.
