# Quality Attribute Tactics and Checklists Reference
*Source: Software Architecture in Practice (Bass, Clements, Kazman)*

This reference guide contains the standard Quality Attribute General Scenarios, Architectural Tactics Catalogs, and Design Checklists for the seven core quality attributes in *Software Architecture in Practice (SAiP)*.

---

## 1. Availability

### General Scenario
- **Source**: Internal or external (e.g., hardware, software, network, operator).
- **Stimulus**: Fault (omission, crash, timing, response).
- **Artifact**: System processors, communication channels, storage, processes.
- **Environment**: Normal operation, degraded mode, startup, shutdown.
- **Response**: Log the fault, notify actors, degrade gracefully, failover, continue operation.
- **Response Measure**: Downtime, MTBF (Mean Time Between Failures), MTTR (Mean Time To Repair), percentage of availability (e.g., 99.99%).

### Tactics Catalog
* **Detect Faults**:
  * *Ping/Echo*: Asymmetric query-response check.
  * *Heartbeat*: Periodic status message sent by monitored component.
  * *Exception Detection*: Checking assertions, stack limits, or system failures.
* **Recover from Faults (Preparation and Repair)**:
  * *Active Redundancy (Hot Standby)*: Dual components processing inputs simultaneously; secondary drops results until primary fails.
  * *Passive Redundancy (Warm Standby)*: Secondary node periodically synchronized; takes over on primary failure.
  * *Spare (Cold Standby)*: Backup is instantiated and booted on failure; must load saved state.
  * *Shadowing*: Backup processes inputs but state is verified against primary before output.
  * *State Resynchronization*: Copying state from active to recovering node.
  * *Rollback*: Restoring database or state to a previous known good checkpoint.
* **Prevent Faults**:
  * *Removal from Service*: Temporarily putting a node offline to prevent predicted failures.
  * *Transactions*: Encapsulating operations to enforce ACID properties and roll back if aborted.
  * *Predictive Model*: Monitoring metrics (memory, temperature) to preemptively swap elements.

### Design Checklist
1. **Allocation of Responsibilities**: Identify components responsible for fault detection, logging, recovery, and failover notifications.
2. **Coordination Model**: Define heartbeat protocols, failure detector timeout limits, and voting schemes.
3. **Data Model**: Plan state synchronization intervals, write-ahead logs, and database replication schemes (synchronous vs asynchronous).
4. **Resource Management**: Configure backup resource pools, network interface bonding, and load balancer failure criteria.
5. **Mapping among Architectural Elements**: Distribute redundant components across different physical racks, virtual machines, or availability zones to prevent co-failures.
6. **Binding Time**: Define whether failover configurations are bound at compile time, initialization (startup), or runtime.

---

## 2. Performance

### General Scenario
- **Source**: Internal or external users, background services, other systems.
- **Stimulus**: Arrival of events (periodic, stochastic, sporadic requests).
- **Artifact**: System processor, network, database, memory.
- **Environment**: Normal, high load, emergency, recovery.
- **Response**: Process events, update state, write data, return result.
- **Response Measure**: Latency (response time), throughput (transactions per second), resource utilization (CPU, memory, network), variance.

### Tactics Catalog
* **Control Resource Demand**:
  * *Manage Event Rate*: Throttle, debounce, or filter requests at the gateway.
  * *Limit Event Response*: Return cached or paginated results instead of computing fresh data.
  * *Prioritize Events*: Establish priority queues to process critical requests first.
* **Manage Resources**:
  * *Increase Resources*: Scale up (more CPU/RAM) or scale out (more instances).
  * *Introduce Concurrency*: Process tasks in parallel using thread pools.
  * *Maintain Multiple Copies (Caching)*: Store computed data close to the client.
  * *Reduce Overhead*: Optimize algorithms, database indices, and serialization/deserialization.
  * *Resource Scheduling*: Implement CPU/disk scheduling policies (FIFO, Round Robin).

### Design Checklist
1. **Allocation of Responsibilities**: Identify components on the critical execution path, resource managers, and queue handlers.
2. **Coordination Model**: Determine communication models (asynchronous messaging, event loops, or blocking RPCs) to minimize latency overhead.
3. **Data Model**: Design cache expiration policies, DB index mappings, partition keys, and Denormalization strategies.
4. **Resource Management**: Define thread pool limits, database connection pool limits, task scheduling algorithms, and network bandwidth limits.
5. **Mapping among Architectural Elements**: Place high-frequency interacting components close to each other (e.g., same server, local IPC).
6. **Binding Time**: Bind compiler optimizations, static resource assets, and database schemas early.

---

## 3. Modifiability

### General Scenario
- **Source**: Developer, administrator, system integrator.
- **Stimulus**: Add, delete, or modify features, platforms, UI, or interfaces.
- **Artifact**: Source code, databases, configuration files, APIs, build scripts.
- **Environment**: Design time, compile time, build time, deployment time, runtime.
- **Response**: Implement, build, test, and deploy the modification without introducing side effects.
- **Response Measure**: Time to implement, cost (lines of code modified, developer hours), number of affected components, deployment time.

### Tactics Catalog
* **Reduce Coupling**:
  * *Encapsulate*: Hide internal implementation details behind private scopes.
  * *Use an Intermediary*: Introduce load balancers, brokers, or API gateways to prevent direct dependencies.
  * *Restrict Communication Paths*: Limit which components can call which (e.g., Layered pattern).
  * *Abstract Common Services*: Factor out shared functions (logging, authentication) into common libraries.
* **Cohesion**:
  * *Split/Merge Responsibilities*: Group elements that change together; split elements that serve unrelated concerns.

### Design Checklist
1. **Allocation of Responsibilities**: Separate business logic from UI, configuration, database access, and transport layers.
2. **Coordination Model**: Use decoupled messaging (e.g., publish-subscribe) or standardized interfaces (REST, gRPC) to hide structural changes.
3. **Data Model**: Decouple data representation using data access layers (DAL) or abstraction layers (ORMs).
4. **Resource Management**: Avoid hard-coding configuration values; use environment variables or centralized configuration services.
5. **Mapping among Architectural Elements**: Keep logical modules mapped clearly to directories/packages.
6. **Binding Time**: Rely on late binding techniques (dynamic configuration, plug-in loading, feature flags) for modifications at deployment or runtime.

---

## 4. Security

### General Scenario
- **Source**: Human (authorized or unauthorized), non-human agents (malware, botnets).
- **Stimulus**: Attack (denial of service, unauthorized access, data alteration, eavesdropping).
- **Artifact**: Data stores, system interfaces, physical hardware, processes.
- **Environment**: Normal operation, network partition, recovery mode.
- **Response**: Detect attack, block attacker, encrypt data, audit transaction, recover state.
- **Response Measure**: Authentication time, percentage of blocked attacks, recovery time after breach, audit integrity.

### Tactics Catalog
* **Detect Attacks**:
  * *Detect Intrusion*: Match traffic against signature databases or detect anomalies.
  * *Detect Service Denial*: Track request frequency and rate-limit violations.
  * *Verify Message Integrity*: Check digital signatures and checksums.
* **Resist Attacks**:
  * *Authenticate Actors*: Validate identity using tokens, certificates, or passwords.
  * *Authorize Actors*: Enforce permissions using RBAC (Role-Based Access Control) or ABAC.
  * *Limit Access*: Hide internal ports, isolate networks (VPCs), and use firewalls.
  * *Encrypt Data*: Secure data in transit (TLS) and at rest (AES-256).
  * *Sanitize Inputs*: Prevent SQL Injection and XSS via validation.
* **React to Attacks**:
  * *Revoke Access*: Block compromised tokens, users, or IP addresses.
  * *Lock out Users*: Lock accounts after multiple failed login attempts.
* **Recover from Attacks**:
  * *Audit Trail*: Write immutable logs to verify the chain of events.

### Design Checklist
1. **Allocation of Responsibilities**: Define components managing authentication (IAM), authorization (gateways), audit logs, and encryption keys.
2. **Coordination Model**: Secure communication channels using mutually authenticated TLS (mTLS).
3. **Data Model**: Identify sensitive data (PII) to encrypt and mask. Ensure password storage uses modern hashes (e.g., Argon2, bcrypt).
4. **Resource Management**: Enforce API rate-limiting, request size limits, and socket limits to prevent DOS.
5. **Mapping among Architectural Elements**: Deploy public-facing gateways in Demilitarized Zones (DMZs), and databases in isolated private subnets.
6. **Binding Time**: Enforce early binding of permissions (static roles) and late binding of runtime secrets (injected via Vault or AWS Secrets Manager).

---

## 5. Testability

### General Scenario
- **Source**: Developers, testers, QA automated suites, CI/CD runners.
- **Stimulus**: System development, integration milestones, bug fix verification.
- **Artifact**: Modules, subsystems, system interfaces, integrations.
- **Environment**: Design, development, build, integration, testing environment.
- **Response**: Run automated tests, execute test suites, isolate modules, verify output.
- **Response Measure**: Code coverage percentage, test suite execution time, defect detection rate, mock/stub complexity.

### Tactics Catalog
* **Control and Observe State**:
  * *Isolate Components*: Implement dependency injection (DI) to swap real database/network clients with stubs or mocks.
  * *Separate Interface from Implementation*: Use interfaces to allow alternative test implementations.
  * *Provide Test Interfaces*: Add status endpoints, diagnostics APIs, or debug consoles.
  * *Abstract Common Resources*: Move time, filesystem, and network calls behind mockable interfaces.
* **Limit Complexity**:
  * *Limit Structural Complexity*: Keep component call graphs shallow.
  * *Limit Cyclomatic Complexity*: Minimize branch structures in methods.

### Design Checklist
1. **Allocation of Responsibilities**: Allocate logging, telemetry, and self-diagnostic features to components.
2. **Coordination Model**: Plan how components handle test mode parameters (e.g., passing a transaction ID or mock header).
3. **Data Model**: Prepare test database seed scripts, schema migration tooling, and isolated mock datasets.
4. **Resource Management**: Isolate CPU/memory limits in test containers to identify resource leaks during load tests.
5. **Mapping among Architectural Elements**: Ensure unit test assemblies run completely isolated from databases/network filesystems.
6. **Binding Time**: Use compile-time mock injection (DI frameworks) and runtime mock configurations (test-profile properties).

---

## 6. Interoperability

### General Scenario
- **Source**: External systems or application clients.
- **Stimulus**: Request to exchange data, invoke services, or share states.
- **Artifact**: System integration endpoints, APIs, message queues.
- **Environment**: Online operation, system mismatch, high load.
- **Response**: Parse incoming format, translate schemas, execute request, respond in target schema.
- **Response Measure**: Interface translation latency, percentage of parsed formats, schema conformance rate.

### Tactics Catalog
* **Locate Services**:
  * *Discover Service*: Use service discovery registries (Consul, DNS) to find dynamic endpoints.
* **Manage Interfaces**:
  * *Orchestrate*: Use central workflow engines to coordinate calls across services.
  * *Tailor Interface*: Adapt interface schemas using wrappers, adaptors, or translation layers.

### Design Checklist
1. **Allocation of Responsibilities**: Establish translation layers, schema validators, and data mapping modules.
2. **Coordination Model**: Align on protocols (HTTP REST, gRPC, AMQP) and format schemas (JSON, Protobuf, XML).
3. **Data Model**: Design canonical data formats to map incoming fields to internal models.
4. **Resource Management**: Configure API gateway routing tables, circuit breakers, and rate limiters.
5. **Mapping among Architectural Elements**: Position bridges/integrators between internal networks and external providers.
6. **Binding Time**: Enforce compile-time API client code generation (e.g., OpenAPI generator, Protobuf compilation) or runtime service discovery.

---

## 7. Usability

### General Scenario
- **Source**: End users, administrators.
- **Stimulus**: Intention to execute a task, cancel an action, or recover from an error.
- **Artifact**: UI screens, error notification layers, command APIs.
- **Environment**: Normal operation, high workload, system failure, user error.
- **Response**: Provide clear feedback, undo action, suggest correct steps, adapt view.
- **Response Measure**: Time to complete task, user error rate, satisfaction score, training time.

### Tactics Catalog
* **Support User Initiative**:
  * *Undo*: Track state changes to allow rolling back user actions.
  * *Cancel*: Terminate active network requests or operations in progress.
  * *Pause/Resume*: Temporarily suspend operations and preserve state.
* **Support System Initiative**:
  * *Maintain User Model*: Track user preferences and history.
  * *Maintain System Model*: Display system status, progress bars, and operational errors clearly.

### Design Checklist
1. **Allocation of Responsibilities**: Isolate state managers, command patterns (for undo/redo), and UI rendering components.
2. **Coordination Model**: Use asynchronous feedback models to keep the UI responsive during long backend calls.
3. **Data Model**: Store user preferences, session history, and checkpoint states.
4. **Resource Management**: Optimize load speeds of UI assets and local client storage.
5. **Mapping among Architectural Elements**: Separate frontend files completely from backend service logic (MVC/MVVM).
6. **Binding Time**: Use runtime styling, layout templates, and language translation configurations.
