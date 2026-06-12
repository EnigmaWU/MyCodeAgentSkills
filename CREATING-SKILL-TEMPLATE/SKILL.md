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
Scaffolds a perfectly formatted, standard-compliant skill directory. This includes the `SKILL.md` based on the Hybrid 5W1H + SSL (Scheduling-Structural-Logical) `SKILL-TEMPLATE.md`, and the automated generation of both English and Chinese `README.md` files.

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

## How (The 4-Phase Refinement Protocol)

### Phase 1: Structural Alignment & Routing Optimization
1. **Context Gathering**: Ask the user for the Skill Name, Complexity, and Purpose if not provided.
2. **Frontmatter Hardening**: Ensure the `description` block acts as a clean routing trigger. Explicitly state when an agent should load the skill (trigger phrases) and when it shouldn't (near-misses). Apply the standard Hybrid SSL YAML frontmatter:
   ```yaml
   ---
   name: [skill-name]
   description: >
     WHEN/WHERE/WHO: [Scheduling: Who should use this, and explicit trigger/boundary contexts]
     HOW: [Structural: Use this SKILL to explicitly execute phases and workflows]
     WHY: [Scheduling: Why this skill matters or the problem it prevents]
   ---
   ```
3. **Information Decoupling**: If the skill contains heavy static reference data or massive code blocks, do not bloat the `SKILL.md`. Strip them out and place them in a `details/` directory, using dynamic file-retrieval hooks (relative links) in the core file.

### Phase 2: Execution Logic & State Machine Conversion
4. **Determinism Linting**: Scaffold the core sections (Who, What, When, Where, Why) using `SKILL-TEMPLATE.md`. Eliminate all ambiguous prose (e.g., "try to", "use judgment", "if possible") from the instructions.
5. **Branching Control**: Rewrite the `## How` execution steps into an imperative state machine using strict If-Then-Else conditional branching logic. Every phase must have an explicit input expectation and an expected state output.

### Phase 3: Negative Constraint Boundary Injection
6. **Anti-Pattern Mapping**: Explicitly define the negative space under `## Constraints (Logical Boundaries)`. State exactly what the agent *must not do* under any circumstances to prevent common reasoning drift or loop regressions during autonomous execution.

### Phase 4: Verification & Harness Layer Engineering
7. **Verifiable Rewards Design**: Build a dedicated, non-negotiable validation block (`## Validation`) at the end of the skill. This must force the agent to execute a strict checklist (such as validating output against a JSON schema or running a specific harness command) to confirm execution success before closing the task loop.

### Phase 5: Bilingual Support & Finalization
8. Create `[skill-name]/README.md` (English) and `[skill-name]/README_ZH.md` (Chinese) containing localized usage instructions based on the description block.
9. **Test-Driven Evaluation**: Simulate the skill's routing accuracy against mock prompts. If trigger accuracy is ambiguous, harden the frontmatter again.
10. Stage and commit the new directory to git.

## Validation
1. Verify the frontmatter uses the `>` multi-line format and does not have surrounding quotes.
2. Verify both `README.md` and `README_ZH.md` exist and contain the description text.
3. Verify the directory name exactly matches the `name:` field in the frontmatter.
