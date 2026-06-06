# Software Archaeology and Legacy Codebase Checklists

This document provides checklists for developers and coding agents to analyze, isolate, and replace legacy codebase modules using principles of Software Archaeology, Bubble Contexts, and Strangler patterns.

---

## Section 1: Software Archaeology Checklists

Software archaeology is the study of historical codebases to extract mental models and understand behavior. Use these checkpoints to analyze brownfield systems:

- [ ] **Establish Code Ownership & History**:
  * Identify who originally wrote the code and who has maintained it recently (using `git log` or version history).
  * Determine if active team members have context on the module, or if the original authors have left the organization.
- [ ] **Map System Boundaries & API Endpoints**:
  * List all entry points: exposed REST endpoints, SOAP services, message broker listeners, cron job hooks, or CLI commands.
  * Map how parameters are passed and what data schemas are returned.
- [ ] **Track Database & Persistence Pipelines**:
  * Identify which database schemas, tables, and views are read or written to by the legacy code.
  * Highlight any shared tables that are also accessed by other external applications (potential integration databases).
- [ ] **Identify Core Risk Zones**:
  * Look for modules with high cyclomatic complexity, zero unit tests, or frequent historic bug reports.
  * Mark components that use hard-coded environment configuration, obsolete encryption libraries, or out-of-date runtime dependencies.

---

## Section 2: Bubble Context & Superimposed Structure Checklists

A Bubble Context (Anticorruption Layer) insulates new code from legacy contamination, while a Superimposed Structure maps metadata to legacy entities without editing their code directly.

- [ ] **Design the Bubble Context (Anticorruption Layer)**:
  * Define a clean, modern domain model for the new functionality.
  * Create interfaces that represent the required actions/data from the legacy system.
  * Implement adapter/translator classes that invoke the legacy systems and map legacy structures (e.g. database rows or dictionaries) into the new domain models.
- [ ] **Establish Import Constraints**:
  * Enforce that new greenfield modules *only* import from the Bubble Context's adapter interface.
  * Prevent greenfield modules from importing legacy files directly.
- [ ] **Establish Superimposed Structures (Sidecars & Decorators)**:
  * If legacy source code cannot be modified, create external metadata files (e.g. `metadata.json` or `mappings.yml`) that map legacy class/method names to business concepts.
  * Use Python decorators, Aspect-Oriented programming, or proxy patterns to wrap legacy methods to record telemetry or log data payloads.

---

## Section 3: Biodegradable Transformation Checklists

Biodegradable documentation is designed to disappear when the code it refers to is deleted or replaced. Use these checkpoints:

- [ ] **Apply Biodegradable Annotations**:
  * Mark deprecated or strangler-target classes with custom metadata (e.g., `@StranglerApplication`, `@DeprecatedWithDeadline`).
  * Always include:
    1. **Owner**: The team or engineer responsible for decommissioning.
    2. **Deadline**: An explicit expiration date (e.g., `2026-12-31`).
    3. **Replacement Target**: A link or path to the modern equivalent class.
- [ ] **Implement Strangler Pattern Routing**:
  * Position a routing proxy (API Gateway, HTTP proxy, or routing class) in front of the system.
  * Route requests for newly migrated features to the new Bubble Context.
  * Route all other unmigrated requests to the legacy application.
- [ ] **Automate Expiration Warnings**:
  * Write a test or compile check that scans biodegradable annotations.
  * Log warning messages if a deadline is approaching.
  * Fail the build or block commits if a deadline has expired, forcing the team to address the legacy removal.
- [ ] **Plan Clean Decommissioning**:
  * When a legacy module is fully strangled, verify that no references exist in the routing table.
  * Delete the legacy code files along with their associated sidecar files, test scripts, and documentation mappings.
