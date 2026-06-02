# Viewpoints and Perspectives Reference Guide
*Source: Software Systems Architecture (Rozanski & Woods)*

This reference guide summarizes the Viewpoints, Perspectives, and Inter-view Consistency Rules defined in *Software Systems Architecture: Working with Stakeholders using Viewpoints and Perspectives*.

---

## 1. Viewpoint Catalog

Architectural views represent specific aspects of a system. A viewpoint defines the concerns, models, and checklists used to construct a view.

### A. Context Viewpoint
* **Primary Concerns**: System scope, boundaries, external dependencies, system users, data sources, and external interfaces.
* **Key Models**:
  * *Context Diagram*: Core system box surrounded by actors, external databases, and third-party APIs with interface directions.
* **Problems/Pitfalls**: Ambiguity about boundaries, neglecting manual processes, assuming interfaces are static.
* **Key Checklist Item**: Are all third-party systems and API providers explicitly identified?

### B. Functional Viewpoint
* **Primary Concerns**: Component structure, connector types, functional responsibilities, runtime behavior, and functional interfaces.
* **Key Models**:
  * *Functional Decomposition Model*: Components and subcomponents.
  * *Behavioral Model*: Sequence diagrams, statecharts, or activity charts.
* **Problems/Pitfalls**: Too much detail (writing code in diagrams), wrong level of abstraction, poor interface definitions.
* **Key Checklist Item**: Is every component's functional responsibility uniquely defined and documented?

### C. Information Viewpoint
* **Primary Concerns**: Static data models, data flow, data lifecycle (creation, updates, archival), database ownership, integrity, and synchronization.
* **Key Models**:
  * *Static Information Model*: Entity-relationship diagrams (ERDs) or class diagrams.
  * *Information Flow Model*: Data pipeline diagrams, ETL schemas.
  * *Lifecycle Model*: State diagrams representing data modifications.
* **Problems/Pitfalls**: Underestimating data volume, poor schema definitions, ignoring archival and purge policies.
* **Key Checklist Item**: Does the system define how stale or historical data is archived or deleted?

### D. Concurrency Viewpoint
* **Primary Concerns**: Processes, threads, runtime boundaries, synchronization, concurrency bottlenecks, deadlocks, and race conditions.
* **Key Models**:
  * *Process/Thread Model*: Mapping of functional components to OS processes and threads.
  * *State Synchronization Model*: Use of locks, semaphores, queues, or mutexes.
* **Problems/Pitfalls**: Over-complex thread models, assuming thread safety without design checks, deadlock risks.
* **Key Checklist Item**: Are all shared resources guarded by thread-safe synchronization primitives?

### E. Development Viewpoint
* **Primary Concerns**: Code organization, package structure, build dependencies, compile configurations, third-party libraries, and testing layouts.
* **Key Models**:
  * *Module Structure Model*: Package/directory trees, project dependencies.
  * *Common Design Standards*: Code conventions, formatting, library usage.
* **Problems/Pitfalls**: Circular dependencies, hard-to-build codebases, poor dependency control.
* **Key Checklist Item**: Does the module structure contain circular package dependencies (e.g., A depends on B, B depends on A)?

### F. Deployment Viewpoint
* **Primary Concerns**: Physical infrastructure, virtual machines, containers, cloud zones, network topology, and hardware capacity.
* **Key Models**:
  * *Deployment Diagram*: Nodes (servers, VMs), networks (VPCs, subnets), firewalls, and ports.
* **Problems/Pitfalls**: Neglecting network partitions, assuming unlimited bandwidth, omitting firewall/port configurations.
* **Key Checklist Item**: Are all firewall, load balancer, and security group boundaries mapped?

### G. Operational Viewpoint
* **Primary Concerns**: System administration, software installation, configuration updates, health monitoring, backup/restore, and failover procedures.
* **Key Models**:
  * *Operational Model*: Logging structure, alerting rules, and administrative tools.
* **Problems/Pitfalls**: Leaving operations to the end, missing health check endpoints, untested backups.
* **Key Checklist Item**: Is there a documented and tested backup recovery process for critical data?

---

## 2. Perspective Catalog

Perspectives represent cross-cutting quality requirements applied across all views.

### A. Security Perspective
* **Applicability**: Critical to Context (external threats), Functional (user validation), Information (data encrypt), Deployment (networks).
* **Key Concerns**: Integrity, confidentiality, availability, accountability, auditability.
* **Core Activities**:
  1. Identify sensitive assets (data, components).
  2. Perform threat modeling (STRIDE analysis).
  3. Define security policies (authentication, encryption, RBAC).
* **Key Checklist Item**: Are credentials and secrets externalized from code and encrypted?

### B. Performance and Scalability Perspective
* **Applicability**: Critical to Functional (algorithms), Information (queries), Concurrency (scheduling), Deployment (hardware capacity).
* **Key Concerns**: Response time, throughput, capacity under load, scaling vectors (scale out vs scale up).
* **Core Activities**:
  1. Establish performance budgets (latency per call).
  2. Model worst-case load spikes.
  3. Identify performance bottlenecks (database locks, serialized calls).
* **Key Checklist Item**: How does the system handle a 10x spike in standard transaction volume?

### C. Availability and Resilience Perspective
* **Applicability**: Critical to Functional (error handling), Deployment (redundancy), Operational (recovery).
* **Key Concerns**: Disaster recovery, business continuity, fault tolerance, MTTR/MTBF targets.
* **Core Activities**:
  1. Identify Single Points of Failure (SPOFs).
  2. Define failover and recovery actions.
  3. Plan for partial network partitions.
* **Key Checklist Item**: What happens to the system if a critical external service is unavailable for 1 hour?

### D. Evolution Perspective
* **Applicability**: Critical to Development (coupling), Functional (interfaces), Information (schema migration).
* **Key Concerns**: Ease of change, extensible design, forward/backward compatibility, module isolation.
* **Core Activities**:
  1. Identify future change scenarios (e.g., swapping database provider).
  2. Isolate external dependencies using wrappers/adaptors.
  3. Design database schema migration strategies.
* **Key Checklist Item**: Can the database engine be replaced without modifying core business logic components?

---

## 3. Inter-View Consistency Checking Rules

Architectural descriptions must be internally consistent. Perform these pairwise validation checks:

| View A | View B | Consistency Check Rule |
| --- | --- | --- |
| **Context** | **Functional** | Every actor and external system in the Context view must map to a component interface in the Functional view. |
| **Functional** | **Development** | Every component in the Functional view must correspond to a package, module, or assembly in the Development view. |
| **Functional** | **Concurrency** | Logical component call graphs must align with the process and thread execution boundaries. Ensure no cross-process blocking calls. |
| **Concurrency** | **Deployment** | Every process or container defined in the Concurrency view must be mapped to a physical or virtual node in the Deployment view. |
| **Deployment** | **Operational** | The operational monitoring and failover procedures must cover all nodes, load balancers, and network connections in the Deployment view. |
| **Information** | **Deployment** | Verify database server node replication models in the Deployment view align with the consistency and write properties in the Information view. |
