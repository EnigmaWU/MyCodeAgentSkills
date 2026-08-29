---
name: CREATING-SKILL-TEMPLATE
description: >
  WHEN/WHERE/WHO: AI Agents or users generating a new skill for the repository.
  HOW: Use this SKILL to automatically scaffold a new skill directory, format the `SKILL.md` with the correct tier template (SIMPLE/COMPLICATED/COMPLEX), apply the standardized YAML frontmatter, and auto-generate bilingual READMEs.
  WHY: Creating skills manually from scratch leads to inconsistent folder structures, broken frontmatter, and missing READMEs. Automating this ensures every new skill strictly adheres to the repository's high-quality standards.
---

# Creating Skill Template

## Common Contract (Load First)

When this skill is activated, first load [skill-common](../skill-common/SKILL.md) and apply the shared conventions it defines: canonical section order, frontmatter rules, anti-pattern guidance, and the Review In Mind loop in [review-in-mind](../skill-common/details/review-in-mind.md). This skill adds only domain-specific rules below.

## Who
AI Agents acting as meta-engineers to expand the repository's capabilities, or users who want to quickly scaffold a new skill structure.

## What
Scaffolds a perfectly formatted, standard-compliant skill directory. This includes the `SKILL.md` based on the Hybrid 5W1H + SSL (Scheduling-Structural-Logical) `details/SKILL-TEMPLATE.md`, the automated generation of both English and Chinese `README.md` files, and an optimization-ready quality spine so the new skill can be revised safely over time.

Every generated skill also receives a mandatory `## Review In Mind (ReviewInMindGenie)` section: a built-in review gene that forces the agent to switch from author to skeptical reviewer, critique its own output against the skill's rules, fix or escalate findings, and deliver a short review note instead of an unreviewed artifact.

## When
Invoke this skill when the user asks to "create a skill template", "scaffold a new skill", "generate the boilerplate for skill X", or similar phrases.

## Where
Applies to the root directory of the `MyCodeAgentSkills` repository. The output will be a new directory named exactly after the requested skill.

## Why
Consistency is critical for agents. If frontmatter is missing or structured differently, the agent indexer might fail to find the skill. This meta-skill guarantees that every new capability injected into the system uses the exact same `description: >` format, proper Markdown sections, bilingual support, and a lightweight optimization contract inspired by controllable skill-evolution workflows such as SkillOpt and SkillOpt-Lite.

## Inputs
- **Skill Name** (required): The name of the new skill (kebab-case preferred unless explicitly stated otherwise).
- **Skill Complexity** (required): SIMPLE, COMPLICATED, or COMPLEX.
- **Skill Purpose** (required): The 5W1H details (Who, What, When, Where, Why, How).

## Output
- A new directory: `[skill-name]/`
- `[skill-name]/SKILL.md` formatted from `details/SKILL-TEMPLATE.md`.
- `[skill-name]/README.md` (English).
- `[skill-name]/README_ZH.md` (Chinese).
- An optimization-ready section in the generated skill that defines failure signals, evidence sources, mutation boundaries, acceptance criteria, rejection handling, and stop rules.
- A mandatory `## Review In Mind (ReviewInMindGenie)` section with a skill-specific review lens.
- A mandatory `## Common Contract (Load First)` section that references `../skill-common/SKILL.md` (or `../../../skill-common/SKILL.md` for nested subskills) so the generated skill loads the shared contract at activation.

## Optimization Readiness
- **Failure Signals**: Generated skills miss trigger accuracy, omit bilingual docs, exceed the token budget, fail to include the optimization contract and validation block, or omit the Review In Mind gene.
- **Evidence To Collect**: Generated skill packages, validation results, trigger examples, and cases where the template had to be hardened after ambiguous routing.
- **Safe Mutation Boundaries**: Refine template wording, tier-selection guidance, trigger hardening, and validation prompts without changing the core template-construction workflow.
- **Acceptance Criteria**: Accept revisions only if the generated skill stays under the line budget, includes the required sections, and carries explicit routing and validation rules.
- **Rejected Revision Handling**: Record weak trigger phrases, missing bilingual files, and invalid tier selections so they are not reused.
- **Transfer Check**: Verify the workflow still works for SIMPLE, COMPLICATED, and COMPLEX skill generations.
- **Stop Rule**: If the requested skill name, complexity, or purpose is missing or unclear, stop and ask before generating the template.

## Constraints
- **RULE 1: Directory Naming.** The directory name MUST exactly match the `name:` value in the `SKILL.md` YAML frontmatter.
- **RULE 2: Multi-line Frontmatter.** The YAML `description` must use the multi-line block scalar format (`>`) and explicitly include the `WHEN/WHERE/WHO`, `HOW`, and `WHY` prefixes.
- **RULE 3: Bilingual Support.** Every skill MUST have a `README.md` and a `README_ZH.md`.
- **RULE 4: Token Efficiency (Max 500 Lines).** The `SKILL.md` file MUST be concise (ideally under 500 lines). If the skill contains highly verbose checklists, code examples, or design rules, you MUST place them in a `details/` directory and link to them relatively from `SKILL.md`.
- **RULE 5: Trigger Accuracy.** The `description` block MUST explicitly define both exact trigger phrases AND "near-misses" (when NOT to use the skill) to prevent accidental executions by the agent.
- **RULE 6: Optimization Readiness.** Every generated skill MUST state how it will detect failure, what evidence can justify revision, what parts are safe to mutate, how acceptance is validated independently, how rejected revisions are recorded, and when iteration must stop.
- **RULE 7: Natural-Language Execution.** Paper-inspired optimization logic may shape the workflow, but the generated skill MUST remain fully executable from text alone. Diagrams and figures are optional references only.
- **RULE 8: Review In Mind (ReviewInMindGenie).** Every generated skill MUST include a `## Review In Mind (ReviewInMindGenie)` section before its `## Validation` block (or at the end of the file if the skill has no Validation section). The section MUST contain a deterministic-first review loop (run every automatable check — required fields, schema, syntax, links, build/test/lint commands — before using the reviewer persona; classify findings; fix or escalate; deliver with a review note) and at least two skill-specific review lens questions derived from the skill's `What`, `Constraints (Logical Boundaries)`, and `Validation` criteria.
- **RULE 9: Common Contract (Load First).** Every generated skill MUST include a `## Common Contract (Load First)` section immediately after the title. It MUST reference `../skill-common/SKILL.md` (or `../../../skill-common/SKILL.md` for nested subskills) and instruct the agent to load the shared contract on activation. The generated skill's `## Review In Mind (ReviewInMindGenie)` section MUST reference `skill-common/details/review-in-mind.md` and keep only the skill-specific review lens.

## How (The 5-Phase Refinement Protocol)

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
4. **Determinism Linting**: Scaffold the core sections (Who, What, When, Where, Why) using `details/SKILL-TEMPLATE.md`. Eliminate all ambiguous prose (e.g., "try to", "use judgment", "if possible") from the instructions.
5. **Branching Control**: Rewrite the `## How` execution steps into an imperative state machine using strict If-Then-Else conditional branching logic. Every phase must have an explicit input expectation and an expected state output.
6. **Review Gene Injection**: Add the `## Review In Mind (ReviewInMindGenie)` section using the tier shape in `details/SKILL-TEMPLATE.md`. Make the loop deterministic-first: automatable checks run before the skeptical-reviewer persona. Derive the review lens from the skill's own `What`, `Constraints (Logical Boundaries)`, and `Validation` criteria so the review is domain-specific rather than generic boilerplate.
7. **Common Contract Injection**: Add the `## Common Contract (Load First)` section immediately after the title, referencing `../skill-common/SKILL.md` (or `../../../skill-common/SKILL.md` for nested subskills). Replace any duplicated common block in the generated skill with a reference to the corresponding `skill-common/details/` file.

### Phase 3: Optimization-Ready Contract Injection
6. **Failure Signal Design**: Add an `## Optimization Readiness` section using the template tier in `details/SKILL-TEMPLATE.md`. It MUST declare concrete failure signals, the evidence to collect from repeated usage, and the safe mutation boundaries for future revisions.
7. **Independent Acceptance Gate**: Require the generated skill to define acceptance criteria that are checked independently from the drafting step. A rewrite cannot be accepted only because it reads better; it must state what evidence proves improvement.
8. **Rejected Revision Memory**: Require a simple rule for recording rejected edits or anti-patterns so future improvements do not repeat the same failed mutations.

### Phase 4: Negative Constraint Boundary Injection
9. **Anti-Pattern Mapping**: Explicitly define the negative space under `## Constraints (Logical Boundaries)`. State exactly what the agent *must not do* under any circumstances to prevent common reasoning drift or loop regressions during autonomous execution.

### Phase 5: Verification & Packaging
10. **Verifiable Rewards Design**: Build a dedicated, non-negotiable validation block (`## Validation`) at the end of the skill. This must force the agent to execute a strict checklist (such as validating output against a schema, running a specific harness command, or comparing candidate outputs) to confirm execution success before closing the task loop.
11. Create `[skill-name]/README.md` (English) and `[skill-name]/README_ZH.md` (Chinese) containing localized usage instructions based on the description block.
12. **Test-Driven Evaluation**: Simulate the skill's routing accuracy against mock prompts. If trigger accuracy is ambiguous, harden the frontmatter again.
13. If the user asked for version control actions, stage the new directory and prepare a commit. Otherwise stop after validation and report the generated artifacts.

## Review In Mind (ReviewInMindGenie)

Execute the common review loop in [review-in-mind](../skill-common/details/review-in-mind.md) before delivering.

Review lens for this skill:
- Does the generated skill include every required section (frontmatter, 5W1H, Optimization Readiness, Constraints, How, Validation, Review In Mind)?
- Is the frontmatter `description` a precise trigger with near-misses, and does the directory name match the `name:` field?
- Do both READMEs exist, and is the generated SKILL.md within the line budget?

## Validation
1. Verify the frontmatter uses the `>` multi-line format and does not have surrounding quotes.
2. Verify both `README.md` and `README_ZH.md` exist and contain the description text.
3. Verify the directory name exactly matches the `name:` field in the frontmatter.
4. Verify the generated `SKILL.md` contains an `## Optimization Readiness` section with failure signals, evidence, mutation boundaries, acceptance criteria, rejection handling, and a stop rule.
5. Verify the `## Validation` section checks execution quality or routing quality, not only file presence.
6. Verify the generated `SKILL.md` contains a `## Review In Mind (ReviewInMindGenie)` section with the deterministic-first four-step review loop and at least two skill-specific review lens questions.
7. Verify the generated `SKILL.md` contains a `## Common Contract (Load First)` section immediately after the title with a correct relative link to `skill-common/SKILL.md`.
