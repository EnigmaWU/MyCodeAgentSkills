---
name: skill-common
description: >
  WHEN/WHERE/WHO: Any agent or user activating, creating, or refining a SKILL.md in this repository.
  HOW: Load this common contract first and apply the shared spine — canonical section order, frontmatter rules, Optimization Readiness rules, anti-pattern guidance, and the Review In Mind (ReviewInMindGenie) loop — while each specific skill supplies only domain-specific rules.
  WHY: One shared source of truth keeps every skill consistent, removes duplicated boilerplate, and makes every skill review-oriented by default.
---

# Skill Common Contract

## Who
Any agent or user who activates a skill in this repository, or who creates or refines one using `CREATING-SKILL-TEMPLATE`, `save-as-skill`, or `improve-existing-skill`.

## What
Defines the shared contract that every skill in this repository follows. A specific skill remains responsible for its own domain rules, but MUST load this contract at activation for the common spine: canonical section order, frontmatter conventions, Optimization Readiness rules, anti-pattern guidance, the One More Thing rule, and the Review In Mind loop.

## When
- At the start of executing any skill that includes a `## Common Contract (Load First)` section.
- When creating or refining a skill with `CREATING-SKILL-TEMPLATE`, `save-as-skill`, or `improve-existing-skill`.
- When validating skills with `save-as-skill/scripts/validate_skill.py`.

## Where
Applies to every `SKILL.md` in this repository. This package is the single source of truth for the common parts; specific skills reference it via relative links (`../skill-common/...` from top-level skills, `../../../skill-common/...` from subskills).

## Why
Skills in this repository share a large amount of structural DNA (frontmatter style, section order, Optimization Readiness, review gene, closing rule). Duplicating that DNA in every file causes drift: one skill gets fixed, the other 67 stay stale. A single common contract loaded at activation guarantees consistency, reduces token weight, and keeps every skill review-oriented by default.

## Common Files
- [common-spine](details/common-spine.md) — canonical section order and heading conventions.
- [frontmatter](details/frontmatter.md) — frontmatter format and trigger rules.
- [review-in-mind](details/review-in-mind.md) — the canonical Review In Mind (ReviewInMindGenie) loop.
- [optimization-readiness](details/optimization-readiness.md) — the Optimization Readiness contract.
- [anti-patterns](details/anti-patterns.md) — shared MUST-NOT patterns.
- [one-more-thing](details/one-more-thing.md) — the standard stop-and-ask closing rule.

## Inputs
- A specific skill being activated, created, or refined.
- The domain rules defined in that specific skill.

## Output (Logical Evidence)
- The common spine applied to the specific skill's execution.
- The Review In Mind loop executed before the specific skill delivers any artifact.
- No duplicated boilerplate added to specific skills beyond the activation reference and their own domain rules.

## Optimization Readiness
- **Failure Signals**: Specific skills drift from the common spine, skip the Review In Mind loop, duplicate common text instead of referencing it, or use wrong relative links.
- **Evidence To Collect**: Cases where a skill forgot to load the common contract, broken links, and review loops that were skipped or false-passed.
- **Safe Mutation Boundaries**: Wording of the shared files, section order, and review loop may be refined as long as every referencing skill keeps working.
- **Acceptance Criteria**: Every skill with a Common Contract section loads this package successfully; the Review In Mind loop runs; the validator recognizes the shared sections.
- **Rejected Revision Handling**: Record rejected wordings, link mistakes, and review-loop regressions in `details/validation-log.md` so they are not reintroduced.
- **Transfer Check**: Verify the contract works for a top-level skill and for a nested subskill (e.g., `managing-ai-projects/subskills/...`).
- **Stop Rule**: If a specific skill's domain rules conflict with the common spine, stop and resolve the conflict with the user instead of silently overriding the contract.

## Constraints (Logical Boundaries)
- Do not move domain-specific content into this package; only what is genuinely shared belongs here.
- Do not let a specific skill override the common Review In Mind loop without an explicit user decision.
- Keep all references relative so the package works inside a cloned repository.
- **Anti-Pattern Mapping**: MUST NOT turn this package into a dumping ground for one skill's checklists; MUST NOT let specific skills silently skip the common loop; MUST NOT hard-code absolute paths.

## One More Thing
If any shared rule conflicts with a specific skill's domain rules, stop and resolve the conflict with the user before proceeding.

## How (Structural Workflow)
1. **Input State**: A specific skill with a `## Common Contract (Load First)` section is activated.
2. **Load the Contract**: Read this `SKILL.md` and the relevant `details/` files referenced by the specific skill (at minimum `common-spine.md`, `frontmatter.md`, and `review-in-mind.md`).
3. **Apply the Spine**: Follow the canonical section order and conventions for any output or file the specific skill produces.
4. **Execute the Domain Rules**: Run the specific skill's own `How`, `Constraints`, and `Validation` as the authoritative domain logic.
5. **Run Review In Mind**: Before the specific skill delivers, run the loop in `details/review-in-mind.md`, using the specific skill's own review lens.
6. **Output State**: The specific skill delivers its artifact with a review note.

## Review In Mind (ReviewInMindGenie)

Execute the common review loop in [review-in-mind](details/review-in-mind.md) before delivering.

Review lens for this skill:
- Is every shared rule stated once here and referenced (not duplicated) by specific skills?
- Would a specific skill fail loudly if it skipped loading this contract?
- Are the relative links correct for both top-level skills and nested subskills?

## Validation (Verifiable Rewards)
1. Every referencing skill contains a `## Common Contract (Load First)` section with a working relative link to this package.
2. Every referencing skill's Review In Mind section points to `details/review-in-mind.md` and keeps its own review lens.
3. The common files contain only shared rules; domain-specific content remains in the specific skills.
