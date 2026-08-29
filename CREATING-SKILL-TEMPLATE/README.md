# CREATING-SKILL-TEMPLATE

## Overview

WHEN/WHERE/WHO: AI Agents or users generating a new skill for the repository.
HOW: Use this SKILL to automatically scaffold a new skill directory, format the `SKILL.md` with the correct tier template, apply the standardized YAML frontmatter, auto-generate bilingual READMEs, inject a lightweight optimization-ready section for future revisions, inject the mandatory `## Review In Mind (ReviewInMindGenie)` review gene, and add the `## Common Contract (Load First)` reference to `skill-common` so the shared contract loads at activation. It enforces token efficiency (<500 lines) and uses validation-driven evaluation to ensure the skill triggers accurately and has a defined acceptance gate.
WHY: Creating skills manually from scratch leads to inconsistent folder structures, broken frontmatter, and missing READMEs. Automating this ensures every new skill strictly adheres to the repository's high-quality standards, remains executable from natural language alone, and preserves a paper-inspired clue from controllable skill-evolution workflows without making diagrams or TMP artifacts operational dependencies.

## Usage

Trigger this skill to execute the defined workflow. See `SKILL.md` for specific triggers and inputs.

## Structure

- [SKILL.md](./SKILL.md): The core workflow and definition of the skill.
- [details/SKILL-TEMPLATE.md](./details/SKILL-TEMPLATE.md): The tiered authoring template, including optimization-ready section shapes, the ReviewInMindGenie review gene, and the Common Contract reference for SIMPLE, COMPLICATED, and COMPLEX skills.
