# Performance and Scalability Perspective Guide (Level-3 Details)
*Source: Software Systems Architecture, Ch 26*

Use this guide during system design or architecture definition to apply the cross-cutting Performance and Scalability Perspective to all views of the system.

---

## 1. Core Concerns
Designing the system to meet response time, throughput, and scalability constraints, ensuring that performance-critical pathways are optimized and workload contention is minimized.

## 2. Performance Requirements Capture Checklist
* **Establish High-Level Targets**: Have you identified approved performance targets (latency budgets, throughput goals) with key stakeholders?
* **Identify Response and Throughput Goals**: Do your targets distinguish between response time (latency for a single operation) and throughput (number of concurrent operations per unit time)?
* **Observed vs Actual Performance**: Do your targets distinguish between observed performance (what the user experiences synchronously) and actual performance (which includes background asynchronous processing)?
* **Reasonableness Assessment**: Have you assessed your performance targets for reasonableness (e.g., comparing them to database/network physical limits)?
* **Set Stakeholder Expectations**: Have you set realistic expectations among stakeholders for what is feasible given system budget and technology constraints?
* **Load Context**: Are all performance targets defined within the context of a specific workload profile (e.g., "100ms response time at 5,000 concurrent active users")?

## 3. Performance Architecture Definition Checklist
* **Identify Performance Risks**: Have you identified the major potential performance bottlenecks (e.g., database locks, shared state contention, external API call latencies) in your proposed architecture?
* **Testing and Modeling**: Have you performed enough prototyping, benchmarking, or modeling to understand the system's likely performance characteristics?
* **Workload Prioritization**: Do you know what workload your system can process, and have you prioritized different classes of work (e.g., critical transactional processing gets priority over reporting)?
* **Scalability Limits**: Do you know how far your proposed architecture can scale (scale-out limits) before requiring major structural changes or database sharding?
* **Distribution Overhead**: Have you accounted for the locations of elements and their inter-element remote invocation costs (network latency)? Ensure remote call overheads are represented in your performance model.
