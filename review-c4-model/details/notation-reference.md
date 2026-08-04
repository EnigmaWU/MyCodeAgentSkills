# C4 Notation Reference

Condensed notation guidance from Chapter 10 of *The C4 Model* by Simon Brown. Use
this to explain WHY a finding matters and to propose concrete fixes.

## Core principle
The C4 model is notation-independent. Any shapes, colors, icons, or line styles are
acceptable as long as they are explained in a diagram key. The value of the model is
the shared abstractions and diagram types, not a fixed visual style.

## Titles
- Include a title on every diagram.
- Make the title state the diagram type and scope, e.g., "System Context View:
  Internet Banking System" or "Deployment View: Internet Banking System-Live".

## Acronyms, abbreviations, and code names
- Avoid unexplained acronyms, abbreviations, and code names.
- Common technical terms (HTTP, JSON, SQL) are fine for technical audiences.
- For internal code names (e.g., "Plutus"), add the functional name or a description:
  "Payment Service (also known as Plutus)" or "Plutus (payment service)".
- When in doubt, prefer the accessible option.

## Layout
- No correct orientation; users at the top and databases at the bottom is common.
- Keep element placement consistent between levels (same people at the top in context
  and container diagrams).

## Element content
- Start with simple rectangles and one color; add notation after the content is right.
- Include inside each element:
  - **Name**
  - **Type** (often in square brackets, e.g., `[Container]`)
  - **Technology** (for containers and components; 1-2 primary choices)
  - **Description / responsibilities** (short sentence or 7 +/- 2 bullets)
- Version numbers: optional; major versions only (e.g., "Spring 5") are a good
  balance between precision and maintenance cost.

## Color
- Use color to differentiate or emphasize (existing vs new, owned vs external,
  technical debt, etc.).
- Explain every color's meaning in the key.
- Check readability for color vision deficiency and black-and-white printing.

## Shapes
- Common shapes: rectangles/rounded boxes, person shapes for users, cylinders/buckets
  for data stores, folders for file systems, pipes for queues/topics.
- Explain every shape's meaning in the key.

## Size
- Keep element sizes approximately equal unless size intentionally means something
  (larger = more significant/complex), in which case explain it in the key.

## Icons
- Icons (e.g., cloud provider icons) are optional decoration.
- Include every icon in the key with a full description.

## Relationships
- Prefer unidirectional arrows; a bidirectional relationship can be collapsed into one
  arrow from the initiating element to the receiving element.
- Label every arrow specifically; avoid generic labels like "uses".
- End labels with a preposition ("to", "from", "with") so the direction reads like a
  sentence: "Makes API requests to", "Reads data from".
- Show two arrows only when the two relationships differ in intent, technology, or
  synchronicity.
- Use line styles for extra meaning (e.g., solid = synchronous, dashed = asynchronous)
  and describe them in the key.
- Avoid many different arrowheads; one type is simplest, and 2-3 at most if needed.

## Diagram key
- Always include a key/legend on or near the diagram.
- Include any notation that differentiates elements or relationships: shapes, colors,
  icons, line styles, arrowheads, border styles.
- Record questions raised during review or presentation; if you had to explain
  something verbally, it belongs in the key.
- Be careful with relative words ("internal"/"external") — define what they mean
  (internal to the team, to the organization, etc.).
