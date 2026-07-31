# Undercurrents Review

Undercurrents cut across the whole data engineering lifecycle. Review them globally and at each lifecycle stage where evidence exists.

## Security and Privacy

- Least privilege for data, infrastructure, credentials, and workflows
- Secrets management and credential rotation
- Encryption in transit and at rest
- Network exposure and access boundaries
- Backup and restore expectations
- PII, retention, deletion, anonymization, and compliance controls
- Logging, monitoring, and alerting for suspicious access or failure modes

## Data Management

- Data quality checks and ownership
- Metadata, catalog, lineage, and discoverability
- Schema evolution and compatibility rules
- Data contracts between producers and consumers
- Governance, retention, archival, and deletion policies
- Master/reference data and business definitions

## DataOps

- CI/CD for pipelines, models, schemas, and infrastructure
- Automated tests for transformations, quality, contracts, and deployment safety
- Observability for freshness, volume, distribution, failures, and SLAs
- Backfill, replay, rollback, and incident procedures
- Clear ownership, runbooks, and escalation paths

## Data Architecture

- Alignment with business use cases and consumers
- Loose coupling between sources, pipelines, storage, and serving
- Failure-aware design and reversible decisions
- Scalability, interoperability, and modularity
- Architecture choices documented as tradeoffs, not vendor defaults

## Orchestration

- Explicit dependencies, schedules, triggers, retries, and timeouts
- Backfill and replay support
- Idempotent task design
- Failure isolation and downstream impact control
- SLA/SLO awareness and alert routing

## Software Engineering

- Maintainable code structure and reviewable business logic
- Version control for code, schemas, configs, and infrastructure
- Testing strategy across unit, integration, contract, and data quality tests
- Reproducible environments and dependency management
- Documentation that lets a new maintainer operate the system

## Cost and FinOps

- Storage, compute, orchestration, observability, egress, and third-party service cost visibility
- Workload scheduling and right-sizing
- Expensive queries, scans, backfills, and cross-region movement
- Cost-to-business-value reasoning
- Alerts or budgets for runaway workloads
