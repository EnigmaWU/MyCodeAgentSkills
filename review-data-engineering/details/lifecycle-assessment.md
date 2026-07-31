# Lifecycle Assessment

The review spine is the data engineering lifecycle: generation, storage, ingestion, transformation, and serving. Review advice should state where each risk sits in this lifecycle.

## Generation and Source Systems

Ask:

- Where does the data originate?
- Who owns the source system?
- What data shape, schema, rate, volume, velocity, and variety are expected?
- Can source changes break downstream pipelines?
- Are duplicates, late data, nulls, malformed values, and deletions expected?
- Does reading from the source affect its operational performance?

Review advice should call out ownership gaps, schema-change risk, undocumented source behavior, source performance risk, and missing communication channels with source owners.

## Storage

Ask:

- Where is data stored at raw, intermediate, curated, and served stages?
- Are storage choices aligned with access patterns, volume, latency, consistency, retention, privacy, and cost?
- Are metadata, cataloging, partitioning, clustering, lifecycle policies, and retention visible?
- Is compute separated from storage where useful?
- Are backup, restore, archival, and deletion expectations explicit?

Review advice should connect storage risks to retrieval, compliance, performance, durability, and cost impact.

## Ingestion

Ask:

- Is ingestion batch, micro-batch, streaming, CDC, API, file, queue, webhook, or manual?
- Is the pattern push, pull, or poll?
- Are replay, idempotency, durability, dead-letter handling, retries, and backpressure handled?
- Are payload formats, schemas, throughput, and freshness expectations explicit?
- Are late-arriving data and schema evolution handled?

Review advice should highlight reliability gaps, replay gaps, unsafe retry behavior, schema drift, and freshness risks.

## Transformation

Ask:

- How is raw data cleaned, joined, enriched, modeled, aggregated, and validated?
- Are transformations versioned, tested, documented, and observable?
- Are conceptual, logical, and physical models understandable?
- Are batch and streaming transformations handled differently where needed?
- Are quality checks tied to consumer expectations?

Review advice should identify hidden business logic, untested transformations, unclear model ownership, performance bottlenecks, and weak lineage.

## Serving

Ask:

- Who consumes the data and what decisions or actions depend on it?
- Is the serving mode analytics, ML, operational analytics, embedded analytics, API, file exchange, semantic layer, metrics layer, sharing, or reverse ETL?
- Are definitions, freshness, SLA/SLO, access controls, and trust expectations explicit?
- Can consumers discover, understand, and safely use the data?

Review advice should focus on consumer trust, definition drift, missing contracts, broken self-service assumptions, and unclear ownership.
