# Common Anti-Patterns, Rationalizations, and Red Flags

Patterns from Chapter 1 and Chapter 10 of *The C4 Model* that indicate a diagram
needs revision. Use this file to recognize violations quickly and to rebut excuses.

## Anti-patterns (visible defects)
- **Unlabeled relationships**: Arrows exist but say nothing about intent.
- **Ambiguous elements**: Boxes whose purpose cannot be inferred (e.g., "Security").
- **Generic labels**: "Business logic", "transport", "error", "DB", "data" — labels
  that describe almost any system.
- **Missing relationships**: Elements that should connect are disconnected.
- **Missing technology choices**: Containers/components without implementation
  technology, especially when technology is expensive to change.
- **Unexplained acronyms or code names**: "RS", "TDS", "Plutus" without explanation.
- **Mixed abstraction levels**: Containers and components on the same diagram, or
  deployment details on a container diagram.
- **Inconsistent notation across a set**: Same concept drawn differently on the
  context vs. container diagram.
- **No diagram key**: Notation varies (shapes/colors/icons) with no legend.
- **No title**: Readers cannot tell the diagram type or scope.
- **Ambiguous arrows**: Lines without arrowheads, or bidirectional arrows with a label
  that only reads correctly in one direction.
- **Deployment details on container diagrams**: Servers, Docker, Kubernetes, load
  balancers, cloud regions mixed into a container view.
- **One deployment diagram for multiple environments**: Dev and live mixed into a
  single diagram.
- **Component diagrams for every container**: Unnecessary low-level diagrams that age
  rapidly; recommended only where they add value.

## Common rationalizations and rebuttals
- **"We'll talk through the diagrams."**
  Rebuttal: Diagrams must stand alone. Any explanation that is required to understand
  the diagram should be added to the diagram or its key.
- **"The solution is simple and can be built with any technology."**
  Rebuttal: Technology choices are significant decisions. If they are absent, the
  reader assumes a version that may be wrong and expensive to change.
- **"We don't want to force a solution on developers."**
  Rebuttal: Include the developers in the design and capture the agreed choices on the
  diagram. Not showing decisions creates ambiguity, not freedom.
- **"Technology is an implementation detail."**
  Rebuttal: For containers and components, technology is one of the three themes of
  architecture (technology, elements, relationships) and is usually expensive to
  change.
- **"This doesn't make sense, but we'll explain it during the presentation."**
  Rebuttal: If the diagram cannot be understood without the author, it has limited
  value as documentation and will mislead future readers.
- **"The diagram is high-level/logical."**
  Rebuttal: High-level does not mean empty. Include the decisions that matter (types,
  responsibilities, technology) at the level of abstraction the diagram claims.
- **"We already know what these boxes are."**
  Rebuttal: Explicit types and descriptions remove assumptions for new team members,
  reviewers, and non-engineers.

## Red flags (quick scan)
- Any arrow without a label.
- Any label ending in a verb without a preposition (direction unclear).
- Any element without a type in square brackets.
- Any container/component without technology.
- Any generic word in a box: logic, data, error, transport, service, module.
- A diagram with no title.
- A diagram using colors/shapes/icons with no key.
- A system context diagram containing a database cylinder.
- A container diagram containing a Docker icon, server icon, or cloud region.
- A deployment diagram showing both "dev" and "live" in one picture.
- A component diagram showing components from more than one container.
