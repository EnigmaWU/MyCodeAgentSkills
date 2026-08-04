---
name: review-c4-model
description: >
  WHEN/WHERE/WHO: Software architects, engineers, or agents who need to critique or
  review software architecture diagrams (images, PDF pages, diagram-as-code, or pasted
  descriptions) against the C4 model rules from Simon Brown's "The C4 Model" book.
  HOW: Classify the diagram type, run the general, element, relationship, and
  level-specific checklists from the book, and produce a verdict with concrete fixes.
  WHY: Most architecture diagrams are ambiguous "boxes and arrows"; a checklist-based
  review removes assumptions and makes diagrams readable by their intended audience.
---

# Review C4 Model Diagrams

## Who
Software architects, tech leads, engineers, and agents who must verify that a software
architecture diagram follows the C4 model's abstractions, scope rules, and notation
guidance, or who must give structured feedback on diagrams created by others.

## What
Review one or more software architecture diagrams against the C4 model rules and
produce a structured verdict: PASS, PASS WITH CONDITIONS, or FAIL, with every finding
mapped to a concrete rule and a suggested fix. The review covers:

- Diagram identity: title, type, scope, and key/legend.
- Element quality: names, types, technologies, descriptions, abbreviations.
- Relationship quality: labels, direction, technology, line styles.
- Level-specific scope: what may appear on each C4 diagram type.
- Notation consistency and accessibility (colors, shapes, icons, sizes).

## When
Trigger when the user asks to:

- "review / critique / check this architecture diagram"
- "is this a valid or correct C4 diagram"
- "find problems in this diagram"
- "does this diagram follow the C4 model"
- "apply the C4 review checklist to ..."

Do NOT use for: creating new C4 diagrams from scratch (use a diagram-creation skill),
explaining the C4 model theory without a concrete diagram to review, or reviewing code
quality or design outside the diagram's content.

## Where
Applies to any artifact that can be inspected:

- Raster or vector images (PNG, JPEG, SVG, PDF pages)
- Diagram-as-code (Structurizr DSL, Mermaid, PlantUML, Graphviz)
- Markdown or text descriptions of a diagram
- Whiteboard photos or pasted diagram content

The source may be a local file, pasted text, or content extracted from a document.

## Why
Most diagrams fail because authors assume a verbal narrative will explain them.
Ambiguity leads readers to wrong assumptions about elements, relationships, and
abstraction levels. A repeatable, checklist-driven review makes the diagram
self-explanatory, catches cross-diagram inconsistency, and gives the author concrete,
fixable defects instead of vague impressions.

## Inputs
- **Diagram(s) to review** (required): image path, diagram-as-code file, pasted content,
  or a page range in a PDF.
- **Diagram type** (optional): system context, container, component, code, dynamic,
  deployment, or system landscape. If absent, infer from content; if ambiguous, ask.
- **Intended audience** (optional): technical/non-technical, engineering team, ops,
  stakeholders. Used to judge whether the detail level matches the audience.

## Output (Logical Evidence)
- A review report containing:
  1. Classified diagram type and scope.
  2. Checklist results: every item marked PASS / FAIL / N/A.
  3. Findings grouped by severity (BLOCKER / MAJOR / MINOR), each with: the defect, the
     rule violated (traceable to the C4 model), and a concrete fix.
  4. Overall verdict: PASS, PASS WITH CONDITIONS, or FAIL.
- State changes: the skill only reads inputs. It writes the report as chat output, or
  to a markdown file only if the user explicitly asks for a file.

## Optimization Readiness
- **Failure Signals**: Reviews miss obvious violations (unlabeled arrows, missing key),
  reports are too vague to act on, the skill is used for diagram creation, or the verdict
  does not match the checklist results.
- **Evidence To Collect**: Example diagrams with known defects and their expected
  findings; user feedback on whether findings were actionable; cases where the skill
  misclassified a diagram type.
- **Safe Mutation Boundaries**: Checklist wording, severity thresholds, report
  formatting, and trigger phrases may change. The C4 rules themselves (abstractions,
  scope, notation requirements) must stay faithful to the book.
- **Acceptance Criteria**: A revision must pass the validation gate in the Validation
  section and correctly catch the known defects in at least one saved example diagram.
- **Rejected Revision Handling**: Record rejected checklist items, trigger phrases, and
  report formats in `details/validation-log.md` so they are not reintroduced.
- **Transfer Check**: The skill must work on at least one nearby case beyond the examples
  it was built from, e.g., reviewing a component diagram for a system different from the
  book's Internet Banking System.
- **Stop Rule**: If the diagram cannot be inspected (unsupported format, missing file,
  too ambiguous to classify), stop and ask the user instead of guessing the findings.

## Constraints (Logical Boundaries)
- Review only what is visible in the diagram. Do not invent missing elements,
  relationships, or technology choices.
- Do not rewrite or create the diagram unless the user explicitly asks for the fix to
  be applied.
- Do not flag subjective aesthetics (e.g., "too many colors") without tying the finding
  to a rule (e.g., color meaning is not in the key).
- Do not reference hallucinated tools or libraries. If you cannot parse the provided
  diagram-as-code format, ask for another format or extract its text first.
- **Anti-Pattern Mapping**:
  - MUST NOT fill in missing labels "because it is obvious".
  - MUST NOT accept "we will explain it in the presentation" as a reason to skip
    findings.
  - MUST NOT mix review findings with new design suggestions.
  - MUST NOT flag a diagram for missing component-level detail on a system context
    diagram; scope rules depend on the diagram type.

## How (Structural Workflow)

### Phase 1: Input State
1. Read the diagram artifact(s). If the artifact is an image, extract its text content
   (OCR or the diagram-as-code source) so every label, arrow, boundary, and title is
   available as text.
2. Confirm the diagram type and scope. If the user did not provide them, infer from
   content:
   - People + one software system + external systems -> system context or container.
   - One software system with application/data-store containers -> container.
   - One container with components -> component.
   - Classes/interfaces/functions -> code.
   - Numbered runtime interactions -> dynamic.
   - Deployment nodes/infrastructure -> deployment.
   - Many software systems without a single focus -> system landscape.
   If the type remains ambiguous, stop and ask.

### Phase 2: Classification
1. Record the intended audience from the user, or infer it from the type (context and
   landscape -> anyone; container and deployment -> architects, engineers, ops;
   component -> engineers; code -> engineers only).
2. Load the relevant checklists from `details/review-checklist.md`. Run the General,
   Elements, and Relationships sections for every diagram, plus the level-specific
   section for the classified type.

### Phase 3: Execution (Checks)
Run every applicable check. For each check, record PASS, FAIL, or N/A with evidence
(quote the label, arrow, or missing element).

1. **General checks**
   - Title present and states the diagram type and scope.
   - Key/legend present and explains shapes, colors, icons, line styles, and arrowheads
     used.
   - Notation consistent within the diagram (and across the set, if multiple diagrams
     are provided).
2. **Element checks**
   - Every element has a name.
   - Every element has an explicit type (software system, container, component, person,
     deployment node, etc.).
   - Descriptions/responsibilities present where space allows.
   - Technology choices present for containers and components.
   - Acronyms, abbreviations, and code names explained or avoided.
   - No generic labels (e.g., "business logic", "transport", "error", "DB") that hide
     the element's purpose.
   - Colors, shapes, icons, border styles, and sizes, when used to differentiate, are
     explained in the key.
3. **Relationship checks**
   - Every arrow is unidirectional, or bidirectionality is intentional and explained.
   - Every relationship has a label describing intent.
   - The label reads as a sentence matching the arrow direction (end with a preposition
     such as "to", "from", or "using").
   - Technology/protocol labeled where the relationship crosses a process/network
     boundary (containers, software systems).
   - Synchronous vs asynchronous distinctions use consistent, keyed line styles.
   - Arrowheads consistent and, if varied, appear in the key.
4. **Level-specific checks** (full detail in `details/review-checklist.md`)
   - System context: only people and software systems; no containers, components, code,
     or deployment details.
   - Container: people/software systems for continuity, containers (applications and
     data stores), software-system boundary; no deployment details (servers, Docker,
     cloud).
   - Component: scope is ONE container; components; container boundary; surrounding
     elements repeated for continuity.
   - Code: scope is ONE component; code-level elements only.
   - Dynamic: subset of elements collaborating at runtime for one feature; numbering or
     sequence clear.
   - Deployment: one deployment environment per diagram; container/software-system
     instances, deployment nodes, infrastructure nodes; no mixed environments.
   - System landscape: many software systems plus people within an organizational
     scope; no single-system focus.

### Phase 4: Reporting
1. Group findings by severity:
   - BLOCKER: element or relationship missing or wrong such that the diagram misleads
     (e.g., unlabeled arrows, wrong abstraction level, unexplained notation without a
     key, mixed environments on a deployment diagram).
   - MAJOR: significant ambiguity or missing required content (e.g., no technology
     choices on containers, vague labels, missing boundaries).
   - MINOR: polish or consistency (e.g., inconsistent spacing, size implying
     significance without meaning, acronym explained only in the narrative).
2. For each finding, state the rule violated and the concrete fix (e.g., "Label the
   arrow between UI and Backend: 'Makes API requests to [JSON/HTTP]'").
3. Produce the verdict:
   - PASS: no FAIL items.
   - PASS WITH CONDITIONS: only MINOR FAIL items, or fixable MAJOR items explicitly
     listed as conditions.
   - FAIL: any BLOCKER or unresolved MAJOR item.

### Phase 5: Validation
1. Re-read the report and confirm every finding traces to a checklist item.
2. Confirm the report does not invent content that is not present in the diagram.
3. Confirm the verdict matches the checklist results.
4. If the user asked for a file, save the report and report the path; otherwise return
   it in chat.

## Resources
- [details/review-checklist.md](details/review-checklist.md) — full PASS/FAIL checklist
  including level-specific scope rules.
- [details/notation-reference.md](details/notation-reference.md) — notation guidance
  for titles, elements, relationships, and keys.
- [details/common-anti-patterns.md](details/common-anti-patterns.md) — recurring
  failure patterns, rationalizations, and red flags.
- [details/validation-log.md](details/validation-log.md) — tier choice, acceptance gate
  results, and rejected drafting choices.

## Validation (Verifiable Rewards)
1. Run the checklist from `details/review-checklist.md` against a real diagram and
   confirm every applicable item receives PASS/FAIL/N/A.
2. Confirm all internal markdown links resolve to existing files.
3. Confirm the review report includes: classified type, checklist results,
   severity-grouped findings with fixes, and a verdict.
4. Confirm the verdict is consistent with the checklist results (BLOCKER or unresolved
   MAJOR -> FAIL; only MINOR -> PASS WITH CONDITIONS; all PASS -> PASS).
5. Confirm the review used only the diagram's visible content and no hallucinated
   elements or tools.

## One More Thing
If anything is unclear, missing, or conflicting — the file cannot be read, the diagram
type is ambiguous, or the request mixes review with creation — stop and ask the user
before proceeding.
