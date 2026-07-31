# Evidence Discovery

Use repository evidence before drawing conclusions. If a signal is absent, record it as missing evidence unless the project explicitly proves the responsibility does not exist.

## Common Evidence Sources

- `README`, `docs`, ADRs, architecture diagrams, runbooks, and onboarding notes
- `dbt_project.yml`, `models/`, `seeds/`, `snapshots/`, `macros/`, and dbt tests
- `dags/`, `airflow`, `dagster`, `prefect`, `jobs`, `pipelines`, `workflows`, and scheduler configs
- `sql`, `schemas`, `migrations`, `proto`, `avro`, `jsonschema`, `openapi`, and contract files
- notebooks, scripts, batch jobs, streaming consumers, ETL/ELT code, and CDC connectors
- `docker`, `k8s`, `terraform`, `helm`, `cloudformation`, `pulumi`, and environment configs
- CI/CD workflows, data quality checks, unit/integration tests, smoke tests, and backfill jobs
- monitoring, alerting, logging, lineage, catalog, SLA/SLO, ownership, and incident docs

## Search Hints

Look for terms such as source, sink, warehouse, lake, lakehouse, ingest, extract, load, transform, stream, batch, CDC, Kafka, queue, Airflow, DAG, dbt, model, schema, partition, lineage, catalog, quality, freshness, SLA, backfill, retention, PII, encryption, secret, credential, and egress.

## Evidence Table

| Evidence | Path or source | Lifecycle stage | Undercurrent | Confidence | Notes |
| --- | --- | --- | --- | --- | --- |
| What was observed | File, command, doc, or conversation | Generation/storage/ingestion/transformation/serving | Security/DataOps/etc. | High/Medium/Low | Why it matters |

## Missing Evidence Rule

Use `Missing Evidence` when a responsibility appears likely but cannot be verified. Do not write "missing" as a defect until you know the project should contain that control.
