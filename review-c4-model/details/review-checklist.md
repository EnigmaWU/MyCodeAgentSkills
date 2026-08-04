# C4 Diagram Review Checklist

Run every applicable item and mark PASS / FAIL / N/A. Record evidence for every FAIL
(quote the label, arrow, or missing element). Base each judgment on the C4 model rules
from Simon Brown's *The C4 Model: Visualizing Software Architecture*.

## 1. General
- [ ] **G1 Title**: The diagram has a title that states the diagram type and scope
  (e.g., "System Context View: Internet Banking System").
- [ ] **G2 Scope**: The title or content identifies the element in scope (one software
  system, one container, one component, or one deployment environment).
- [ ] **G3 Key**: A key/legend explains every shape, color, icon, border style, line
  style, and arrowhead used on the diagram.
- [ ] **G4 Consistency**: Notation is consistent within the diagram and across the set
  of diagrams describing the same system.
- [ ] **G5 Self-contained**: The diagram can be understood without a verbal narrative
  or accompanying explanation.

## 2. Elements
- [ ] **E1 Name**: Every element has a name.
- [ ] **E2 Type**: Every element has an explicit type (`[Person]`, `[Software system]`,
  `[Container: Java and Spring Boot]`, `[Component: Spring MVC]`, `[Deployment node:
  Docker container]`, etc.).
- [ ] **E3 Description**: Every element has a short description or responsibility
  summary (a single short sentence or a 7 +/- 2 bullet list).
- [ ] **E4 Technology**: Containers and components state their primary implementation
  technology (1-2 choices; major version numbers recommended, exact versions optional).
- [ ] **E5 Abbreviations**: Acronyms, abbreviations, and code names are explained or
  avoided. Common technical acronyms (HTTP, JSON, SQL) are acceptable for technical
  audiences.
- [ ] **E6 Generic labels**: No generic labels that hide purpose, such as "business
  logic", "transport", "error", "DB", "service", or "data".
- [ ] **E7 Color**: If color differentiates elements, the meaning is described in the
  key.
- [ ] **E8 Shapes**: If shapes differentiate elements, the meaning is described in the
  key.
- [ ] **E9 Icons**: If icons are used, every icon appears in the key with a full
  description.
- [ ] **E10 Border styles**: If border styles (solid, dashed, dotted) carry meaning,
  the meaning is described in the key.
- [ ] **E11 Size**: Element sizes are uniform unless size intentionally encodes meaning,
  in which case that meaning is in the key.
- [ ] **E12 Abstraction levels**: Elements on the diagram stay within the allowed
  abstraction level for the diagram type (see Level-specific section).

## 3. Relationships
- [ ] **R1 Labeled**: Every arrow has a label describing the intent of the
  relationship.
- [ ] **R2 Direction**: The label matches the arrow direction when read as a sentence
  (e.g., "The UI makes API requests to the backend").
- [ ] **R3 Preposition**: Labels end with a preposition ("to", "from", "using", "with")
  to make the direction unambiguous.
- [ ] **R4 Technology**: Relationships that cross a process or network boundary state
  the primary protocol or technology (e.g., `[JSON/HTTP]`, `[XML/HTTPS]`,
  `[MySQL protocol]`).
- [ ] **R5 Sync/async**: If synchronous vs asynchronous is shown, it uses consistent
  line styles (e.g., solid = synchronous, dashed = asynchronous) that appear in the key.
- [ ] **R6 Arrowheads**: Arrowheads are consistent; if more than one type is used, the
  variation is described in the key and limited to 2-3 types.
- [ ] **R7 Ambiguity**: No ambiguous bidirectional arrows unless the single relationship
  has identical intent in both directions and that intent is explained.
- [ ] **R8 Completeness**: No dangling elements; every element participates in at least
  one labeled relationship, or an explicit "not shown for brevity" note explains its
  absence.

## 4. Level-specific scope

### System Context Diagram (scope: one software system)
- [ ] **L1** Contains only people and software systems (plus relationships).
- [ ] **L2** Does not contain containers, components, code, or deployment
  infrastructure.
- [ ] **L3** External dependencies are named and described (e.g., "Core Banking
  System", "AWS Simple Email Service").

### Container Diagram (scope: one software system)
- [ ] **L4** Repeats the same people and software systems from the system context for
  continuity.
- [ ] **L5** Containers are applications and data stores that are separately
  runnable/deployable.
- [ ] **L6** Contains no deployment details: no servers, Docker containers, Kubernetes,
  load balancers, firewalls, or cloud regions.
- [ ] **L7** A software-system boundary (dashed box) surrounds the containers.

### Component Diagram (scope: one container)
- [ ] **L8** The scope is exactly one container.
- [ ] **L9** Components are groupings of related functionality behind a well-defined
  interface, running inside the container.
- [ ] **L10** A container boundary is drawn; the software-system boundary is optional.
- [ ] **L11** Does not show components from other containers; surrounding people,
  software systems, and containers are repeated only for continuity.

### Code Diagram (scope: one component)
- [ ] **L12** Shows only code-level elements (classes, interfaces, functions, modules).
- [ ] **L13** Scope is limited to one component, not the entire application.

### Dynamic Diagram (scope: one feature or use case)
- [ ] **L14** Shows a subset of static elements collaborating at runtime.
- [ ] **L15** Ordering is clear (sequence style or numbered collaboration style).
- [ ] **L16** Contains only elements used by the feature being described.

### Deployment Diagram (scope: one deployment environment)
- [ ] **L17** Shows exactly one deployment environment (e.g., development OR live, not
  both).
- [ ] **L18** Contains instances of containers/software systems, deployment nodes, and
  (where relevant) infrastructure nodes.
- [ ] **L19** Deployment nodes are nested to show the infrastructure hierarchy.

### System Landscape Diagram (scope: organization/group/department)
- [ ] **L20** Shows many software systems and people without focusing on a single
  system.
- [ ] **L21** Organizational boundaries are shown where they help (e.g., Big Bank vs.
  AWS).
