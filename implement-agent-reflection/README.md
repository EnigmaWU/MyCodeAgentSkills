# implement-agent-reflection

## Overview
WHEN/WHERE/WHO: [Scheduling: Agents or architects designing self-correcting loops for LLM-based tasks where high-quality output is critical.]
HOW: [Structural: Use this SKILL to set up an Evaluator-Generator loop, explicitly separating the generation logic from the critique logic.]
WHY: [Scheduling: Single-shot LLM outputs often contain subtle flaws. Reflection forces the agent to critique its own work before returning the final result, dramatically improving quality while preventing infinite token burn.]

## Usage
Trigger this skill to execute the defined workflow. See `SKILL.md` for specific triggers and inputs.

## Structure
- [SKILL.md](./SKILL.md): The core workflow and definition of the skill.
