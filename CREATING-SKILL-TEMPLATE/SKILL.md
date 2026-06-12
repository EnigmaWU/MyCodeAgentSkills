---
name: CREATING-SKILL-TEMPLATE
description: >
  WHEN/WHERE/WHO: AI Agents or users generating a new skill for the repository.
  HOW: Use this SKILL to automatically scaffold a new skill directory, format the `SKILL.md` with the correct tier template (SIMPLE/COMPLICATED/COMPLEX), apply the standardized YAML frontmatter, and auto-generate bilingual READMEs.
  WHY: Creating skills manually from scratch leads to inconsistent folder structures, broken frontmatter, and missing READMEs. Automating this ensures every new skill strictly adheres to the repository's high-quality standards.
---

# Creating Skill Template

## Who
AI Agents acting as meta-engineers to expand the repository's capabilities, or users who want to quickly scaffold a new skill structure.

## What
Scaffolds a perfectly formatted, standard-compliant skill directory. This includes the `SKILL.md` based on `SKILL-TEMPLATE.md`, and the automated generation of both English and Chinese `README.md` files.

## When
Invoke this skill when the user asks to "create a skill template", "scaffold a new skill", "generate the boilerplate for skill X", or similar phrases.

## Where
Applies to the root directory of the `MyCodeAgentSkills` repository. The output will be a new directory named exactly after the requested skill.

## Why
Consistency is critical for agents. If frontmatter is missing or structured differently, the agent indexer might fail to find the skill. This meta-skill guarantees that every new capability injected into the system uses the exact same `description: >` format, proper Markdown sections, and bilingual support.

## Inputs
- **Skill Name** (required): The name of the new skill (kebab-case preferred unless explicitly stated otherwise).
- **Skill Complexity** (required): SIMPLE, COMPLICATED, or COMPLEX.
- **Skill Purpose** (required): The 5W1H details (Who, What, When, Where, Why, How).

## Output
- A new directory: `[skill-name]/`
- `[skill-name]/SKILL.md` formatted from `SKILL-TEMPLATE.md`.
- `[skill-name]/README.md` (English).
- `[skill-name]/README_ZH.md` (Chinese).

## Constraints
- **RULE 1: Directory Naming.** The directory name MUST exactly match the `name:` value in the `SKILL.md` YAML frontmatter.
- **RULE 2: Multi-line Frontmatter.** The YAML `description` must use the multi-line block scalar format (`>`) and explicitly include the `WHEN/WHERE/WHO`, `HOW`, and `WHY` prefixes.
- **RULE 3: Bilingual Support.** Every skill MUST have a `README.md` and a `README_ZH.md`.
- **RULE 4: Token Efficiency (Max 500 Lines).** The `SKILL.md` file MUST be concise (ideally under 500 lines). If the skill contains highly verbose checklists, code examples, or design rules, you MUST place them in a `details/` directory and link to them relatively from `SKILL.md`.
- **RULE 5: Trigger Accuracy.** The `description` block MUST explicitly define both exact trigger phrases AND "near-misses" (when NOT to use the skill) to prevent accidental executions by the agent.

## How

### Phase 1: Context Gathering
1. If the user hasn't provided the Skill Name, Complexity, or Purpose, stop and ask them for these details.
2. Review the `SKILL-TEMPLATE.md` at the root of the repository to select the correct sections based on the Complexity tier (e.g., COMPLEX requires "Resources" and "Validation").

### Phase 2: Scaffolding the Core File
3. Create the `[skill-name]` directory.
4. Create the `[skill-name]/SKILL.md` file.
5. Apply the standard YAML frontmatter exactly like this:
   ```yaml
   ---
   name: [skill-name]
   description: >
     WHEN/WHERE/WHO: [Who should use this, and when/where]
     HOW: Use this SKILL to [What this skill actually does]
     WHY: [Why this skill matters or the problem it prevents]
   ---
   ```
6. Fill in the remaining sections (Who, What, When, Where, Why, How) using the provided purpose. Always include the `## One More Thing` section.

### Phase 3: Generating Localized READMEs
7. Create `[skill-name]/README.md` (English) using this structure:
   ```markdown
   # [skill-name]

   ## Overview
   [The exact English text from the YAML description block]

   ## Usage
   Trigger this skill to execute the defined workflow. See `SKILL.md` for specific triggers and inputs.

   ## Structure
   - [SKILL.md](./SKILL.md): The core workflow and definition of the skill.
   ```
8. Translate the description block into Chinese.
9. Create `[skill-name]/README_ZH.md` using this structure:
   ```markdown
   # [skill-name]

   ## 概述 (Overview)
   [The exact Chinese translation of the description block]

   ## 使用方法 (Usage)
   触发此技能以执行定义的工作流。有关特定的触发器和输入，请参见 `SKILL.md`。

   ## 结构 (Structure)
   - [SKILL.md](./SKILL.md): 技能的核心工作流和定义。
   ```

### Phase 4: Finalization
10. Ensure that the total length of `SKILL.md` is under 500 lines. If it is longer, automatically refactor verbose sections into external files inside a `details/` subdirectory.
11. If the repository uses an automated summary script (e.g., `generate_skill_summary.py`), execute it to update the master `README_SkillSummary.md`.

### Phase 5: Test-Driven Evaluation (Skill Simulation)
12. Before finalizing the skill, the agent MUST simulate its triggering accuracy.
13. **Generate Mock Prompts:** Create 3 mock user prompts (e.g., one perfect match, one near-miss, one completely unrelated).
14. **Evaluate:** Read the newly created `SKILL.md` description frontmatter. Would an agent reading *only* this description correctly trigger the skill for the right prompt, and ignore the near-miss?
15. **Refine:** If the trigger accuracy is ambiguous, rewrite the `WHEN/WHERE/WHO` section of the description until it is perfectly precise.
16. Stage and commit the new directory to git with a standard WHAT/HOW/WHY message.

## Validation
1. Verify the frontmatter uses the `>` multi-line format and does not have surrounding quotes.
2. Verify both `README.md` and `README_ZH.md` exist and contain the description text.
3. Verify the directory name exactly matches the `name:` field in the frontmatter.
