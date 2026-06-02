# Security Perspective Guide (Level-3 Details)
*Source: Software Systems Architecture, Ch 25*

Use this guide during system design or architecture definition to apply the cross-cutting Security Perspective to all views of the system.

---

## 1. Core Concerns
Ensuring the system is resilient against attacks, maintains the confidentiality and integrity of its data, and is available to authorized users while managing security risks against implementation complexity and cost.

## 2. Security Requirements Capture Checklist
* **Sensitive Resource Identification**: Have you identified all sensitive data entities and functional interfaces within the system?
* **Principals Identification**: Have you identified the sets of principals (users, services, administrators, batch jobs) who need access to those resources?
* **Integrity Guarantees**: Have you identified where the system needs information integrity guarantees (e.g., preventing modification of financial ledgers or logs)?
* **Availability Needs**: Have you documented the availability targets for security services (e.g., authentication server)?
* **Security Policy**: Have you established a security policy defining which principals are allowed to perform which operations on which resources? Is this policy kept as simple as possible?
* **Threat Modeling**: Have you worked through a formal threat model (e.g., STRIDE analysis) to identify the security risks your system faces?
* **Threat Scope**: Have you considered both insider threats (malicious developers, compromised credentials) and outsider threats?
* **Deployment Environment Threats**: Have you considered how the system's deployment environment (e.g., public cloud, on-premise, edge nodes) alters the threats to the system?
* **Scenario Walkthroughs**: Have you walked through example security scenarios with stakeholders so they understand the policy and risks?
* **Expert Review**: Have you reviewed your security requirements with external experts?

## 3. Security Architecture Definition Checklist
* **Threat Mitigation**: Have you addressed each threat identified in the threat model to the extent required?
* **Use Proven Tools**: Have you used standard, proven third-party security technology (e.g., OAuth2, OpenID Connect, KMS, TLS) instead of writing custom cryptographic or session-management code?
* **Integrated Overall Design**: Is there an integrated overall design for the security solution across all layers (web, application, database, network)?
* **Standard Principles**: Have you applied standard security principles (e.g., Least Privilege, Secure Defaults, Defense in Depth, Fail Securely) when designing your security infrastructure?
* **Breach Recovery**: Have you defined how security breaches will be identified, logged, and how the system will recover from them (e.g., revoking tokens, reloading clean backups)?
* **View Integration**: Have you updated all affected views (e.g., adding encryption keys in the Information view, network firewalls in the Deployment view)?
* **Design Audit**: Have external experts reviewed your security design?
