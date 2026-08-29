# Validation Log: managing-ai-projects

## Chosen tier
**COMPLEX** — the umbrella is a routing/meta-skill with multi-phase control logic
(classify -> load sub-skill -> execute -> validate), multiple sub-artifacts, and
branching across eight workflows. Each sub-skill is tiered individually (see
their own SKILL.md files and this log).

## Source material
*Managing AI Projects* by Adrián González Sánchez and Malini Jain Runtasewee
(O'Reilly, EPUB in `TMP/Managing AI Projects.epub`):
- Chapters 1-3: role, skills, stakeholders, AI literacy.
- Chapter 4: EMED methodology, prioritization, data quality, sprint zero,
  hybrid Agile/Waterfall.
- Chapter 5: technical AI lifecycle, metrics, GenAI training lifecycle.
- Chapter 6: tool trifecta, technology stack, vendor analysis.
- Chapter 7: lessons, mission projects, AI impostors, roadmapping fear.

## Acceptance gate results
- [x] Parent `SKILL.md` exists with multi-line `description: >` frontmatter.
- [x] README.md and README_ZH.md exist.
- [x] All eight sub-skill directories exist, each with a valid `SKILL.md`.
- [x] Parent routing table maps every sub-skill to real trigger phrases.
- [x] All internal markdown links resolve.
- [x] No hallucinated tools or libraries referenced.
- [x] Sub-skill workflows are executable from natural language alone.

## Rejected drafting choices
- **Rejected `ai-pm-suite` and `ai-project-management`** — user-specified name
  `managing-ai-projects` wins.
- **Rejected eight standalone top-level skills** — user asked for one umbrella
  skill containing the sub-skills; sub-skills remain copyable as standalone
  skills later.
- **Rejected single monolithic workflow** — one file would exceed token limits
  and bury routing; progressive disclosure via sub-skill SKILL.md files is
  cleaner.
- **Rejected duplicating parent instructions in sub-skills** — sub-skills are
  self-contained, the parent only routes.

## Transfer check
The routing table uses request intent (plan/review/estimate/model/evaluate/
stakeholders/team/tools) rather than book examples, so it transfers to any AI
project domain (retail, health care, finance, etc.).
