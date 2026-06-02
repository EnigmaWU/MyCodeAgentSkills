# Availability Design Checklist (Level-3 Details)
*Source: Software Architecture in Practice, Ch 5.3 (Table 5.4)*

Use this checklist during system design or architecture review to ensure Availability goals and tactics are properly implemented.

---

## 1. Allocation of Responsibilities
* **Identify critical responsibilities**: Determine which system functionalities need to be highly available.
* **Fault detection allocation**: Ensure that additional responsibilities are allocated within the system to detect:
  * Omission faults (missing requests/responses).
  * Crash faults (abrupt stops).
  * Timing faults (too slow/fast).
  * Response faults (incorrect calculations/responses).
* **Fault handling allocation**: Ensure there are specific components allocated to:
  * Log the fault for auditing.
  * Notify appropriate entities (administrators, operators, or monitoring systems).
  * Disable the source of events causing the fault (throttling or blacklisting).
  * Manage temporary unavailability (displaying offline messages, queuing inputs).
  * Fix or mask the fault/failure.
  * Operate the system in a degraded mode.

## 2. Coordination Model
* **Fault detection in communication**: Ensure coordination mechanisms can detect omissions, crashes, timing, or response faults (e.g., timeouts, checksums, guaranteed delivery protocols).
* **Communication under stress**: Ensure that coordination works under conditions of degraded communication or network partitions.
* **Reaction coordination**: Verify that coordination mechanisms support:
  * Logging the fault.
  * Notifying appropriate entities.
  * Disabling event sources.
  * Masking/fixing the fault.
  * Operating in degraded mode.
* **Component replacement**: Ensure the coordination model supports the online replacement of artifacts (processors, communication channels, storage, and processes) without system shutdown.
* **Lifecycle states**: Determine if coordination works at startup, shutdown, in repair mode, or under overloaded operation.
* **Data loss tolerance**: Determine how much lost information the coordination model can withstand and with what consequences.

## 3. Data Model
* **Data fault analysis**: Within portions of the system that must be highly available, identify which data abstractions, operations, or properties could cause a fault (omission, crash, timing, response).
* **Data fault mitigation**: Ensure that affected data abstractions can be:
  * Disabled temporarily.
  * Buffered/cached (e.g., cache write requests if a server is temporarily offline and replay them on return).
  * Fixed or masked in the event of a fault.

## 4. Mapping among Architectural Elements
* **Fault boundary identification**: Determine which elements (processors, communication channels, persistent storage, processes) may produce a fault.
* **Remapping flexibility**: Ensure that the mapping (or remapping) of elements is flexible enough to permit recovery. Consider:
  * Which processes on failed processors must be reassigned at runtime.
  * Which processors, data stores, or communication channels can be activated/reasigned at runtime.
  * How data on failed processors/storage can be served by replacement units.
  * How quickly the system can be reinstalled based on the units of delivery.
  * How runtime elements are assigned to physical processors, networks, and databases.
  * Modules-to-components mapping: E.g., write one module that contains code appropriate for both active and backup nodes in a protection group.

## 5. Resource Management
* **Critical resource identification**: Determine what resources are necessary to continue operating in the presence of a fault (omission, crash, timing, response).
* **Resource overhead safety**: Ensure there are sufficient remaining resources in the event of a fault to perform logging, notifications, disabling event sources, masking faults, or degraded operations.
* **Availability schedule**: Determine the availability time for critical resources, what resources must be available during specific time intervals, and repair times.
* **Buffer/Queue sizing**: Ensure input queues are large enough to buffer anticipated messages if a server fails, preventing permanent data loss.

## 6. Binding Time
* **Late binding strategies**: If late binding (runtime registration, plugins, publish-subscribe) is used to alternate between components that can be sources of faults:
  * Ensure the availability strategy covers faults introduced by all possible bindings.
  * Check if chosen fault detection and recovery work for all possible bindings.
* **Fault definition variation**: If late binding changes the definition of what constitutes a fault (e.g., timeout durations), ensure the recovery strategy is sufficient to handle all cases (e.g., avoid mismatch where a timeout is flagged at 0.1ms but recovery takes 1.5s).
* **Binding mechanism availability**: Assess the availability characteristics of the late-binding mechanism itself (what happens if the name server or plugin loader fails?).

## 7. Choice of Technology
* **Tool support**: Determine available technologies that can help detect, recover, or reintroduce failed components.
* **Logging/response support**: Identify technologies that assist in the response to a fault (e.g., distributed event loggers).
* **Tool availability**: Determine the availability characteristics of the chosen technologies: What faults can they recover from, and what faults might they introduce?
