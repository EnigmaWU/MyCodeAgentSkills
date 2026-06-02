# Functional Viewpoint Guide (Level-3 Details)
*Source: Software Systems Architecture, Ch 17*

Use this guide during system design or architecture definition to construct the Functional View of the system.

---

## 1. Core Concerns
The Functional Viewpoint defines the runtime component structure of the system, their responsibilities, and how they interact to achieve system-level functional requirements.

## 2. Design Process and Principles
* **Judicious Compression**: Keep the system complexity low. Focus on defining a minimal, high-cohesion set of components.
* **Visibility Rule**: A system element should only need to be aware of a small subset of other elements to perform its function. If a component must call more than 50% of the other elements in the system, refactor the design to reduce coupling.
* **Decouple via Interfaces**: Never allow components to interact directly with internal implementations; force all communication through abstract interfaces and connectors.

## 3. Required Models
* **Functional Decomposition Model**: Shows the system's components, subcomponents, and their hierarchical boundaries.
* **Behavioral Model**: Illustrates dynamic interactions (e.g., Sequence Diagrams, Activity Diagrams, or Statecharts) to show how components coordinate to fulfill specific use case scenarios.

## 4. Verification Checklist
* **Element Count**: Do you have fewer than 15 to 20 top-level elements to prevent high cognitive load?
* **Clear Specifications**: Do all elements have a unique name, clear responsibilities, and clearly defined interfaces (APIs, parameters, data formats)?
* **Interactions**: Do all element interactions take place via well-defined interfaces and connectors that link them?
* **Cohesion**: Do your elements exhibit an appropriate level of cohesion (does each module have a "unity of purpose")?
* **Coupling**: Are dependencies minimized? Can a component be modified without propagating changes to others?
* **Scenario Validation**: Have you identified the most important usage scenarios and traced them step-by-step through the functional structure to validate completeness?
