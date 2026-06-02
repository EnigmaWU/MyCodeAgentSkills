# Performance Design Checklist (Level-3 Details)
*Source: Software Architecture in Practice, Ch 8.3 (Table 8.2)*

Use this checklist during system design or architecture review to ensure Performance goals and tactics are properly implemented.

---

## 1. Allocation of Responsibilities
* **Identify heavy loading components**: Determine which system responsibilities involve heavy loading, have time-critical response requirements, or are heavily used.
* **Identify bottlenecks**: For those critical responsibilities, identify their processing requirements and determine whether they might cause CPU, memory, or I/O bottlenecks.
* **Identify coordination responsibilities**: Allocate additional responsibilities to:
  * Recognize and process requests when a thread of control crosses process or processor boundaries.
  * Manage threads of control (e.g., allocation/deallocation of threads, thread pool management).
  * Schedule shared resources or manage performance-related artifacts (queues, buffers, caches).

## 2. Coordination Model
* **Concurrence & scheduling support**: Choose communication and coordination mechanisms that support thread safety, event prioritization, or scheduling strategies.
* **Performance targets**: Ensure the coordination mechanisms can deliver the required response times and throughput.
* **Event arrival patterns**: Select mechanisms that can handle periodic, stochastic, or sporadic event arrivals.
* **Protocol properties**: Ensure communication mechanisms have appropriate properties (stateful, stateless, synchronous, asynchronous, guaranteed delivery, latency/throughput characteristics).

## 3. Data Model
* **Identify heavy loading data**: Identify portions of the data model that are heavily loaded or have time-critical requirements.
* **Data replication**: Determine whether maintaining multiple copies of key data (caching, replica databases) would benefit performance.
* **Data partitioning**: Determine whether partitioning or sharding data across databases/tables would reduce contention and benefit performance.
* **Data serialization overhead**: Check if processing requirements for data creation, initialization, persistence, manipulation, translation (serialization/deserialization), or destruction can be minimized.
* **Data scaling resources**: Check if adding hardware/database resources to reduce bottlenecks during data operations is feasible.

## 4. Mapping among Architectural Elements
* **Component co-location**: Where heavy network loading occurs, determine whether co-locating components (e.g., on the same physical host or local network) reduces latency and improves efficiency.
* **Processor assignment**: Ensure components with heavy computation requirements are assigned to processors/VMs with the highest capacity.
* **Introduce concurrency**: Determine where allocating functionality to two or more copies of a component running simultaneously (scaling out) is feasible and beneficial.
* **Process/Thread boundaries**: Check if selected threads of control and their associated responsibilities introduce context-switching or communication bottlenecks.

## 5. Resource Management
* **Identify critical resources**: Determine which resources (CPU, disk I/O, DB connections, memory, network) are critical for performance.
* **Resource management & monitoring**: Ensure critical resources are monitored and managed under normal and overloaded operation, checking:
  * Process and thread models.
  * Prioritization of resources and access controls.
  * Scheduling and locking strategies.
  * Deploying additional resources on demand (autoscaling) to meet increased loads.

## 6. Binding Time
* **Late binding overhead**: For each element bound after compile time (e.g., runtime dynamic loading, runtime service discovery, database query parsing), determine:
  * The time necessary to complete the binding.
  * The additional runtime overhead introduced by the late-binding mechanism.
* **Performance penalties**: Ensure late-binding overhead does not pose unacceptable performance penalties on the system's runtime paths.

## 7. Choice of Technology
* **Real-time constraints**: Will the choice of technology allow you to set and meet hard, real-time deadlines? Do you know its limits under load?
* **Configure performance parameters**: Check if the technology allows you to set:
  * Scheduling policies and thread priorities.
  * Policies for reducing demand (e.g., queue size limits, rate limiting).
  * Processor affinity or allocation of technology elements to processors.
* **Technology overhead**: Does the chosen technology (e.g., ORM, serialization library) introduce excessive overhead for heavily used operations?
