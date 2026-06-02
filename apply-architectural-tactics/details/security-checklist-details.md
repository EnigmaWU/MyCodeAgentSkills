# Security Design Checklist (Level-3 Details)
*Source: Software Architecture in Practice, Ch 9.3 (Table 9.2)*

Use this checklist during system design or architecture review to ensure Security goals and tactics are properly implemented.

---

## 1. Allocation of Responsibilities
* **Identify secure responsibilities**: Determine which system responsibilities need to be secure.
* **Security operations allocation**: For each secure responsibility, allocate additional responsibilities to:
  * **Identify the actor** (user or calling system).
  * **Authenticate the actor** (validate credentials/tokens).
  * **Authorize the actor** (verify access rights).
  * **Grant or deny access** to specific data or services.
  * **Record attempts** to access or modify data or services (audit logging).
  * **Encrypt data** in transit and at rest.
  * **Recognize reduced availability** of resources/services, inform personnel, and restrict access (DOS mitigation).
  * **Recover from an attack** (rollback state, restore backups).
  * **Verify checksums and hash values** to check data integrity.

## 2. Coordination Model
* **Secure communication channel**: Ensure coordination mechanisms authenticate and authorize actors and encrypt data for transmission (e.g., HTTPS, mutual TLS, secure web sockets).
* **Connection throttling**: Implement mechanisms to monitor and recognize unexpectedly high demands for services and restrict or terminate connection routes (rate limiting).
* **Isolation of channels**: Separate public API communication channels from internal inter-service communication channels.

## 3. Data Model
* **Data sensitivity classification**: Determine the sensitivity of different data fields (e.g., PII, financial, internal).
* **Data separation**: Ensure data of different sensitivity levels is physically or logically separated.
* **Access control checking**: Ensure different sensitivity levels have different access rights, and that rights are checked prior to *every* access (no cached permissions bypass).
* **Audit trail**: Ensure access to sensitive data is logged and that the log files themselves are write-protected and isolated from developers/system modifications.
* **Key management**: Ensure data is encrypted with modern algorithms and that the decryption keys are stored separately from the encrypted data.
* **Data restore capability**: Ensure data can be restored from offline backups if it is inappropriately modified or deleted.

## 4. Mapping among Architectural Elements
* **Privilege changes in mapping**: Determine how alternative mappings of components to physical nodes or networks change who can read, write, or modify data or access system services.
* **Audit and load monitoring**: Check how component deployment mappings affect recording of access attempts and the recognition of DOS attacks.
* **Secure zone mapping**: For each mapping, ensure components are allocated to appropriate security zones (e.g., VPC public subnets vs private subnets, DMZs).

## 5. Resource Management
* **Identify resource monitoring tools**: Identify the resources required to authenticate actors, grant/deny access, notify systems, record attempts, encrypt data, recognize high resource demand, and restrict access.
* **Resource exhaustion prevention**: Ensure an external entity cannot access or exhaust a critical resource (e.g., database connection pool exhaustion via slowloris attack).
* **Containment of contamination**: Ensure that a contaminated or breached element can be isolated to prevent it from contaminating other components (blast radius containment).
* **Shared resources cleanup**: Ensure shared memory or temporary storage areas are not used to pass sensitive data between different security clearance levels without cleanup.

## 6. Binding Time
* **Untrusted late-bound components**: In cases where late-bound components (plugins, dynamic assemblies, runtime configurations) are untrusted:
  * Ensure they can be qualified (validate ownership certificates).
  * Enforce mechanisms to block or manage access by late-bound components to sensitive system resources.
  * Record all access, modifications, or attempts by late-bound components.
  * Enforce encryption where keys are withheld from late-bound components.

## 7. Choice of Technology
* **Tool evaluation**: Determine what technologies (e.g., OAuth2 providers, JWT libraries, KMS engines, Firewalls, Web Application Firewalls) are available to help authenticate, control access, protect resources, and encrypt data.
* **Tactic support**: Ensure that chosen technologies directly implement and support the specific security tactics relevant to your system design.
