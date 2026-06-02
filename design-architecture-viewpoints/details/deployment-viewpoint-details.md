# Deployment Viewpoint Guide (Level-3 Details)
*Source: Software Systems Architecture, Ch 21*

Use this guide during system design or architecture definition to construct the Deployment View of the system.

---

## 1. Core Concerns
The Deployment Viewpoint defines the physical environment in which the system runs, including hardware servers, virtual machines, cloud instances, network infrastructure, and database nodes.

## 2. Design Process and Principles
* **Runtime Platform Specification**: Map all logical processes, databases, and containers to specific virtual computing environments (e.g., containers, VMs, serverless compute).
* **Headroom Allocation**: Specify headroom in CPU, memory, storage, and network capacities to cope with unexpected load growth without immediately triggering upgrade costs.
* **Disaster Recovery (DR) Integration**: Include a standby disaster recovery environment (active-active or active-passive standby) located in a different data center region to protect against regional outages.

## 3. Required Models
* **Deployment Diagram**: A physical map showing computing nodes, network links, load balancers, database clusters, firewalls, VPC boundaries, subnets, and communication ports.

## 4. Verification Checklist
* **Logical-to-Physical Mapping**: Have you mapped all of the system's functional elements (defined in the Functional View) to a type of element in your runtime platform? Have you mapped them to specific virtual/physical devices?
* **Hardware Suitability**: Is the role of each piece of your runtime platform (e.g., web server, cache, worker) fully understood? Is the specified hardware or hosted service suitable for this role?
* **Capacity and Sizing**: Have you established detailed specifications (CPU, RAM, storage, IOPS) for the system's hardware devices or hosted services? Do you know exactly how many instances are needed?
* **Disaster Recovery (DR)**: Does your Deployment view include a specification of the disaster recovery standby hardware and replication links?
* **Third-Party SLAs**: Do you have service-level agreements (SLAs) for elements of the runtime environment that are supplied by third parties? Are the guarantees in the SLAs sufficient to meet your overall availability targets?
