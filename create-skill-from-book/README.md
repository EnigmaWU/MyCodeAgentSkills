# Create Skill from Book

An agent skill for systematically ingesting engineering textbooks and reference materials (e.g., in embedded software, RTOS, safety-critical systems, or general systems engineering) and extracting their methodologies, checklists, and design rules into reusable, executable agent skills.

## What Is This

Technical books contain invaluable wisdom, but reading entire chapters is too slow and expensive for an AI agent during a live coding session. This skill defines a workflow to extract **procedural guidelines** from books and compile them into a structured `SKILL.md` (and detailed checklists in `details/`). 

It is designed with the rigor needed for **senior embedded software architects and developers**, emphasizing physical constraints, real-time safety, deterministic behavior, and strict validation over general software abstractions.

## Directory Structure

```text
create-skill-from-book/
  ├── SKILL.md                                 # Level-1: Main skill workflow (COMPLEX tier)
  ├── README.md                                # Overview and usage instructions
  └── details/                                 
      └── extraction-guidelines.md             # Level-3: Detailed guide for extracting embedded & systems skills
```

## Why This Method Matters

When building complex real-time or safety-critical software, generic programming practices are not enough. We must follow rigorous domain-specific guidelines (e.g., MISRA C, ISO 26262, OSEK/VDX, or concurrency models). This skill enables:
1. **Proceduralization**: Turning passive theory ("the book says to do X") into active prompts/checklists that coding agents can step-by-step execute.
2. **Context Window Management**: Reducing a 500-page textbook into a highly focused ~200-line `SKILL.md` and related Level-3 details.
3. **Rigorous Validation**: Ensuring the generated skill is concrete, actionable, and explicitly addresses domain constraints (e.g., memory limits, timing constraints, hardware hazards) rather than relying on LLM general assumptions.

## Usage

When you want to codify a technical book or reference guide into a reusable skill package, invoke this skill using triggers like:
* *"create a skill from [Book Name]"*
* *"extract a skill for [Topic] from [Reference Document]"*
* *"codify the guidelines in [Book/Chapter] into a skill"*

The agent will read the extraction guidelines and build a complete, compliant skill package in the workspace.
