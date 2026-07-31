# review-data-engineering

## Overview

WHEN/WHERE/WHO: Use this skill when reviewing an existing repository, project, platform, pipeline, or architecture as a data engineering project. Trigger phrases include "review data engineering", "data engineering lifecycle assessment", "audit this data pipeline", "review our data stack", and "assess this project as a data platform".

HOW: The skill discovers project evidence, maps the data engineering lifecycle, reviews cross-cutting undercurrents, classifies findings by evidence and risk, and produces actionable lifecycle-assessment advice.

WHY: Existing projects often hide data engineering responsibilities inside application code, notebooks, workflows, infrastructure, and documentation. Lifecycle review makes source, storage, ingestion, transformation, serving, security, operations, and cost risks visible.

## Usage

Use this skill for:

- Reviewing a repo as a data engineering project.
- Assessing data pipeline production readiness.
- Auditing source, storage, ingestion, transformation, and serving responsibilities.
- Reviewing DataOps, orchestration, data management, security/privacy, and cost risks.
- Producing findings-first data engineering review advice.

Do not use it for standalone chart review, data dictionary extraction, generic code review, or designing a new data platform from scratch unless the request explicitly asks for review of an existing project.

## Structure

- [SKILL.md](./SKILL.md): Core review workflow and validation gate.
- [details/evidence-discovery.md](./details/evidence-discovery.md): Evidence patterns to inspect.
- [details/lifecycle-assessment.md](./details/lifecycle-assessment.md): Lifecycle-stage review advice.
- [details/undercurrents-review.md](./details/undercurrents-review.md): Cross-cutting undercurrent checks.
- [details/review-report-template.md](./details/review-report-template.md): Findings-first report template.
- [details/validation-checklist.md](./details/validation-checklist.md): Final quality checklist.
