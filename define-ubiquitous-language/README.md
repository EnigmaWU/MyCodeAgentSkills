# define-ubiquitous-language

## Overview
WHEN/WHERE/WHO: Domain experts, developers, or agents analyzing raw business requirements.
HOW: Use this SKILL to extract a strict Ubiquitous Language glossary for a specific Bounded Context. Reject synonyms, define exact semantics, and enforce these terms in all code, tests, and documentation.
WHY: Ambiguous terminology causes translation costs and bugs. If the business says "Guest" but the code says "Visitor", the mental model breaks. The Ubiquitous Language ensures developers and domain experts speak the exact same language.

## Usage
Trigger this skill to execute the defined workflow. See `SKILL.md` for specific triggers and inputs.

## Structure
- [SKILL.md](./SKILL.md): The core workflow and definition of the skill.
