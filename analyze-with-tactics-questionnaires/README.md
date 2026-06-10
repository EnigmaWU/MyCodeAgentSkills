# analyze-with-tactics-questionnaires

## Overview
This skill guides the agent to evaluate a software architecture design by applying Tactics-Based Questionnaires (from Chapter 8 / Appendix B of *Designing Software Architectures*). Instead of generic reviews, these questionnaires force a targeted review of specific Quality Attributes like Availability, Modifiability, or Security.

## Usage
Trigger this skill when reviewing a proposed design document, an existing architecture, or a pull request with major structural changes.

```markdown
Use the `analyze-with-tactics-questionnaires` skill to evaluate our proposed cloud migration architecture for Availability.
```

## Structure
- [SKILL.md](./SKILL.md): The core workflow for executing the questionnaire review.
- [details/tactics-questionnaires.md](./details/tactics-questionnaires.md): Example questions tailored to specific Quality Attributes.
