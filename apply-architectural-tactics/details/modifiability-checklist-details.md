# Modifiability Design Checklist (Level-3 Details)
*Source: Software Architecture in Practice, Ch 7.3 (Table 7.2)*

Use this checklist during system design or architecture review to ensure Modifiability goals and tactics are properly implemented.

---

## 1. Allocation of Responsibilities
* **Anticipate changes**: Identify likely future changes by considering shifts in technical standards, laws, customer demands, and business goals.
* **Determine change impact**: For each change category:
  * Determine which responsibilities must be added, modified, or deleted.
  * Determine which other system responsibilities will be impacted by the change.
* **Group by change frequency**: Allocate responsibilities to modules such that:
  * Responsibilities that change together (or are impacted together) are grouped in the same module (high cohesion).
  * Responsibilities that change at different times or for different reasons are placed in separate modules.

## 2. Coordination Model
* **Runtime coordination changes**: Determine if coordination mechanisms (communication interfaces, protocols) will need to change at runtime, and ensure changes affect only a minimal, isolated set of modules.
* **Change boundaries**: Identify which devices, protocols, and communication paths are likely to change, and wrap them behind interface adaptors.
* **Decoupled coordination**: Use coordination models that reduce coupling (e.g., publish-subscribe), defer binding (e.g., event buses), or restrict dependencies.

## 3. Data Model
* **Data schema changes**: Identify likely future changes to data abstractions, schemas, operations, or properties.
* **Identify lifecycle changes**: Determine which changes affect the creation, initialization, persistence, manipulation, translation, or destruction of data abstractions.
* **Actor privileges & visibility**: For modifications to be made by end users or system administrators (rather than developers):
  * Ensure the modified data attributes are visible to that role.
  * Ensure appropriate access control privileges are in place to allow modifying the data properties.
* **Co-change grouping**: Design the database and data models so that items that change together are stored and managed together (e.g., isolate core schema from volatile extension fields).

## 4. Mapping among Architectural Elements
* **Runtime remapping**: Determine if functionality mapping to computation elements (processes, threads, servers) needs to change at compile, build, deployment, or runtime.
* **Accommodate changes in mapping**: Check the impact of modifications on execution dependencies, database assignments, and process/thread allocations.
* **Deferred mapping**: Use mechanisms that utilize deferred binding of mapping decisions (e.g., load balancers, reverse proxies, service registries).

## 5. Resource Management
* **Resource footprint changes**: Determine how changes to responsibilities or quality attributes will affect resource utilization (CPU, memory, disk, network bandwidth).
* **Resource capacity safety**: Verify that resource capacities after the modification are still sufficient to meet the system's overall performance requirements.
* **Encapsulate resource managers**: Wrap all resource managers (e.g., database connection poolers, memory cache managers) in modules, and ensure their internal management policies are encapsulated and bindings are deferred.

## 6. Binding Time
* **Identify latest binding time**: For each change, determine the latest time at which the change can be made (compile time, build time, deployment time, startup time, or runtime).
* **Select defer-binding mechanisms**:
  * Compile time: Conditional compilation, static parameterization.
  * Deployment time: Configuration files, env variables.
  * Startup time: Resource files, initial registry lookup.
  * Runtime: Plugins, publish-subscribe, dynamic lookup, polymorphism.
* **Cost-benefit comparison**: Assess the cost of introducing the deferred binding mechanism against the cost of making changes manually (hand-coding).
* **Avoid dependency complexity**: Do not introduce too many binding choices, which makes dependencies complex and hard to manage.

## 7. Choice of Technology
* **Assess tool flexibility**: Identify which modifications are made easier or harder by chosen technology suites.
* **Tooling for changes**: Determine if chosen technologies support making, testing, and deploying changes (e.g., supports hot reloading, hot swaps).
* **Avoid vendor lock-in**: Assess how easily you can change or replace the technology in the future if it becomes obsolete or expensive.
