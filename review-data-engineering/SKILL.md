---
name: review-data-engineering
description: >
  WHEN/WHERE/WHO: Use when a user asks to review an existing repository, project, platform, pipeline, or architecture as a data engineering project; trigger phrases include "review data engineering", "review-data-engineering", "review-data-enginneering", "data engineering lifecycle assessment", "audit this data pipeline", "review our data stack", or "assess this project as a data platform". Near-miss: do not use for creating a new platform from scratch, standalone data visualization review, data dictionary extraction, generic code review, or prompt-only work unless the request explicitly needs data lifecycle review advice.
  HOW: Use this COMPLEX SKILL to discover project evidence, map the data engineering lifecycle from generation to serving, review cross-cutting undercurrents, classify findings by evidence and risk, and produce actionable lifecycle-assessment advice.
  WHY: Existing projects often hide data engineering responsibilities inside application code, notebooks, workflows, infrastructure, and documentation. Reviewing through the lifecycle makes source, storage, ingestion, transformation, serving, security, DataOps, architecture, orchestration, and cost risks visible.
---

# Review Data Engineering

## Who
Architects, staff engineers, data engineers, platform engineers, technical leads, reviewers, and AI agents reviewing an existing repository or project that creates, moves, stores, transforms, serves, or governs data.

## What
Reviews an existing project as a data engineering project. The skill maps observable project evidence to the data engineering lifecycle, assesses lifecycle-stage risks and cross-cutting undercurrents, then produces findings-first review advice with severity, evidence, impact, and recommended next actions.

## When
- Use for requests such as "review this data engineering project", "assess this pipeline", "audit our data stack", "do a data engineering lifecycle assessment", "review-data-engineering", or the user's misspelled shorthand "review-data-enginneering".
- Use when a software project contains data pipelines, ETL/ELT, streaming, CDC, warehouses, lakes, lakehouses, dbt models, Airflow/Dagster/Prefect jobs, data APIs, analytics datasets, ML feature data, reverse ETL, reports, or data governance concerns.
- Near-miss: use [build-data-dictionary](../build-data-dictionary/SKILL.md) for field-definition extraction only, and use [apply-fundamentals-of-data-visualization](../apply-fundamentals-of-data-visualization/SKILL.md) for chart/dashboard design only.

## Where
Applies to repositories, monorepos, data platforms, analytics projects, pipeline codebases, orchestration workflows, infrastructure-as-code, schema/model folders, notebooks, operational runbooks, and documentation that reveal how data flows through a system.

## Why
The key reusable value from *Fundamentals of Data Engineering* is lifecycle assessment: review data work from source generation through serving, while checking undercurrents that cut across every stage. This prevents tool-first reviews and surfaces hidden risks such as schema drift, unreliable ingestion, opaque transformations, weak serving contracts, missing lineage, fragile orchestration, privacy exposure, and unowned operations.

## Inputs
- **Target Project**: Repository, folder, service, pipeline, platform, or documentation set to review.
- **Review Goal**: General health review, architecture review, migration readiness, production readiness, security/privacy review, cost review, or incident-driven review.
- **Available Evidence**: Source files, docs, schemas, DAGs, dbt models, notebooks, configs, tests, IaC, CI/CD workflows, observability dashboards, runbooks, issue reports, or runtime commands.
- **Review Constraints**: Time budget, read-only requirements, excluded folders, production access boundaries, compliance needs, and stakeholder priorities.

## Output (Logical Evidence)
- A findings-first data engineering review report.
- A lifecycle map covering generation, storage, ingestion, transformation, and serving.
- An undercurrents assessment covering security/privacy, data management, DataOps, data architecture, orchestration, software engineering, and cost.
- Missing-evidence notes that distinguish unknowns from verified defects.
- Actionable review advice grouped into quick wins, design decisions, operational hardening, and follow-up questions.

## Optimization Readiness
- **Failure Signals**: The review becomes a generic code review, skips lifecycle stages, invents data flows without evidence, treats absent files as proof of absence, ignores undercurrents, produces advice without severity, or gives tool recommendations before naming user/data risks.
- **Evidence To Collect**: Repository maps, lifecycle evidence tables, sampled pipeline files, schema/model examples, orchestration configs, tests, monitoring hooks, security/privacy controls, findings, and user feedback on missed risks.
- **Safe Mutation Boundaries**: Refine trigger wording, reconnaissance patterns, lifecycle checklist items, severity labels, report templates, and validation checks without removing the lifecycle spine or evidence-first review rule.
- **Acceptance Criteria**: Accept revisions only if reviews still map data flow end to end, tie every finding to evidence or missing evidence, cover undercurrents, rank risks, and provide concrete lifecycle-assessment advice.
- **Rejected Revision Handling**: Record failed patterns such as tool-first audits, unsupported architecture assumptions, checklist-only reports, and broad unfocused scans so future revisions do not repeat them.
- **Transfer Check**: Verify the workflow works for at least two project shapes, such as a dbt warehouse repo and an application repo with embedded ETL or event streams.
- **Stop Rule**: If the target project, review goal, or permitted evidence sources are unclear, stop and ask before reviewing.

## Constraints (Logical Boundaries)
- Review evidence before giving conclusions. If evidence is missing, label it as missing evidence instead of guessing.
- Findings must lead the report and be ordered by severity.
- Do not recommend a technology migration before explaining the lifecycle risk it addresses.
- Do not treat a repository as a mature data platform only because it contains data files, notebooks, or SQL.
- Do not treat missing observability, tests, lineage, or runbooks as harmless; classify the operational risk and state what evidence would reduce uncertainty.
- Do not modify project code during a review unless the user explicitly asks for fixes.
- Avoid exhaustive repository mapping when a smaller evidence set can answer the review goal. Escalate only when lifecycle ownership or risk cannot be determined locally.
- **Anti-Pattern Mapping**: Avoid generic code-review findings, cloud-vendor shopping lists, architecture diagrams without evidence, unranked checklists, and lifecycle reports that omit consumers or operations.

## One More Thing
If the project boundary, review goal, or allowed evidence sources are unclear, stop and ask the user before proceeding.

## How (Structural Workflow)

### Phase 1: Scope the Review and Evidence Plan
**Input State**: A target project or folder and a review request.
1. Identify the review goal: general lifecycle health, production readiness, architecture tradeoff, migration readiness, incident review, security/privacy review, or cost review.
2. Confirm the review is read-only unless the user explicitly requested fixes.
3. Define the minimum evidence set: docs, config, pipeline code, schemas, orchestration, tests, CI/CD, infrastructure, observability, and runbooks.
4. If the target or review goal is missing, ask for clarification. Otherwise continue.
**Output State**: A bounded review scope and evidence plan.

### Phase 2: Discover Data Surfaces
**Input State**: A bounded review scope.
1. Inspect project structure for data clues: `README`, `docs`, `dbt`, `models`, `dags`, `pipelines`, `jobs`, `notebooks`, `schemas`, `migrations`, `sql`, `infra`, `docker`, `k8s`, `terraform`, workflow files, environment files, and test folders.
2. Identify source systems, storage systems, ingestion jobs, transformation logic, serving interfaces, and data consumers.
3. Record evidence paths and unknowns. If no data surfaces are found, report that the project cannot be reviewed as a data engineering project from available evidence.
**Output State**: A data-surface inventory with evidence and gaps.

### Phase 3: Build the Lifecycle Map
**Input State**: A data-surface inventory.
1. Map evidence to lifecycle stages using [lifecycle-assessment.md](details/lifecycle-assessment.md): generation/source systems, storage, ingestion, transformation, and serving.
2. For each stage, record owner, purpose, data shape, freshness, quality expectations, reliability controls, tests, observability, and consumer impact when visible.
3. Mark each stage as **Observed**, **Partial**, **Missing Evidence**, or **Not Applicable**.
4. If any stage is business-critical but lacks evidence, create a review finding rather than silently skipping it.
**Output State**: A lifecycle map with stage status and evidence quality.

### Phase 4: Review Undercurrents
**Input State**: A lifecycle map.
1. Review cross-cutting undercurrents using [undercurrents-review.md](details/undercurrents-review.md): security/privacy, data management, DataOps, data architecture, orchestration, software engineering, and cost.
2. Tie each undercurrent risk to the affected lifecycle stage or state that it applies globally.
3. Classify missing controls as operational, correctness, privacy, reliability, maintainability, or cost risks.
**Output State**: An undercurrents assessment tied to lifecycle evidence.

### Phase 5: Classify Findings and Advice
**Input State**: Lifecycle and undercurrents assessments.
1. Convert risks into findings using severity: **Critical**, **High**, **Medium**, **Low**, or **Observation**.
2. For each finding, include lifecycle stage, undercurrent, evidence, risk, impact, and advice.
3. Separate verified issues from missing-evidence risks.
4. Group recommendations into quick wins, architecture decisions, operational hardening, and follow-up questions.
**Output State**: Prioritized review findings with actionable advice.

### Phase 6: Produce and Validate the Review Report
**Input State**: Prioritized findings.
1. Use [review-report-template.md](details/review-report-template.md) to write the report.
2. Run [validation-checklist.md](details/validation-checklist.md) against the report.
3. If validation fails and the issue is local, revise the report once and rerun the checklist.
4. If validation still fails because evidence is unavailable, state the blocker and the exact evidence needed.
**Output State**: A findings-first data engineering review report.

## Resources
- [evidence-discovery.md](details/evidence-discovery.md) - Repository evidence patterns for data engineering reviews.
- [lifecycle-assessment.md](details/lifecycle-assessment.md) - Generation, storage, ingestion, transformation, and serving review advice.
- [undercurrents-review.md](details/undercurrents-review.md) - Cross-cutting security, data management, DataOps, architecture, orchestration, software engineering, and cost review prompts.
- [review-report-template.md](details/review-report-template.md) - Findings-first report structure.
- [validation-checklist.md](details/validation-checklist.md) - Final validation gate for review quality.

## Validation (Verifiable Rewards)
1. Verify every finding has severity, lifecycle stage, undercurrent, evidence or missing-evidence label, risk, impact, and advice.
2. Verify the report covers generation, storage, ingestion, transformation, and serving, or explicitly marks stages as not applicable or missing evidence.
3. Verify the report covers security/privacy, data management, DataOps, architecture, orchestration, software engineering, and cost where applicable.
4. Verify the review distinguishes verified defects from unknowns.
5. Verify recommendations are actionable and grouped by quick wins, architecture decisions, operational hardening, and follow-up questions.
6. Verify no code changes were made unless the user explicitly requested fixes.
