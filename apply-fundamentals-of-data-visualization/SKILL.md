---
name: apply-fundamentals-of-data-visualization
description: >
  WHEN/WHERE/WHO: [Scheduling: Analysts, researchers, product teams, and agents creating or reviewing charts, dashboards, reports, or infographics.]
  HOW: [Structural: Use this SKILL to select the right chart for the analytical task, apply perception-safe visual encodings, and refine figure design for clarity, accessibility, and storytelling.]
  WHY: [Scheduling: Poor chart choices and visual styling errors hide insights and create misleading interpretation.]
---

# Apply Fundamentals of Data Visualization

## Common Contract (Load First)

When this skill is activated, first load [skill-common](../skill-common/SKILL.md) and apply the shared conventions it defines: canonical section order, frontmatter rules, anti-pattern guidance, and the Review In Mind loop in [review-in-mind](../skill-common/details/review-in-mind.md). This skill adds only domain-specific rules below.

## Who
Analysts, data scientists, researchers, product managers, and AI agents who need to produce clear, accurate, and persuasive data visualizations.

## What
This skill turns data visualization principles into a practical execution workflow:
- map data to appropriate aesthetics and scales,
- choose chart types by question,
- design readable figures with robust color and labeling,
- communicate uncertainty and narrative clearly,
- avoid misleading and low-signal visual patterns.

All operational guidance in this SKILL is written in natural language. Diagrams, if present elsewhere in the package, are optional references and must not be required to execute the workflow.

## When
Invoke this skill when the user asks to:
- design charts or dashboards,
- improve readability of existing figures,
- choose among chart alternatives,
- fix misleading visuals,
- prepare publication-grade or presentation-ready visual outputs.

Trigger phrases include:
- "improve this chart"
- "choose a better visualization"
- "make this figure clearer"
- "design a compelling but accurate chart"

## Where
Applies to:
- data visualization code and notebooks,
- static report figures,
- dashboard components,
- diagram artifacts in markdown (including Mermaid-compatible outputs).

## Why
Good visualizations reduce interpretation effort and improve decision quality. Bad visualizations can bias conclusions through encoding errors (for example, truncated bars, nonmonotonic color scales, unnecessary 3D effects, or overloaded legends).

## Inputs
- Dataset and variable dictionary (required)
- Primary analytical question (required)
- Audience type and medium (required): report, dashboard, social, slide, publication
- Constraints (optional): grayscale print, color-vision deficiency support, size limits, file format constraints

## Output (Logical Evidence)
- Visualization specification (chart type, mappings, scales, and annotations)
- Figure design decisions (color, labels, context, layout, and export format)
- Validation checklist results (accuracy, readability, accessibility, and storytelling)
- Risk notes (known tradeoffs and residual ambiguity)

## Optimization Readiness
- **Failure Signals**: Chart choice is driven by aesthetics instead of analytical intent, encodings mislead magnitude or order, accessibility is ignored, or the figure tries to communicate too many messages at once.
- **Evidence To Collect**: Visualization specs, design decisions, validation checklist results, accessibility notes, and examples where a chart choice improved or obscured the question.
- **Safe Mutation Boundaries**: Refine chart-selection guidance, encoding rules, accessibility checks, and storytelling prompts without changing the core perception-safe visualization workflow.
- **Acceptance Criteria**: Accept revisions only if the figure type answers the stated analytical question, encodings stay truthful, and readability/accessibility checks are explicit.
- **Rejected Revision Handling**: Record misleading encoding patterns, decorative chartjunk, and unreadable label choices so they are not repeated.
- **Transfer Check**: Verify the workflow still works for exploratory charts, presentation figures, and publication-ready visuals.
- **Stop Rule**: If the analysis question, audience, or medium is unclear, stop and ask before finalizing the recommendation.

## Constraints (Logical Boundaries)
- Choose chart type from analytical intent, not aesthetics preference.
- Preserve proportional encoding for magnitude charts (bars on linear scales start at zero).
- Do not use gratuitous 3D effects for 2D data comparisons.
- Do not use rainbow/nonmonotonic scales for ordered values.
- Limit qualitative color categories to manageable counts; use direct labels or grouping when category count is large.
- Use redundant coding when color alone is risky (shape, line type, label, position).
- Balance context and data ink: enough reference cues to compare values, not clutter.
- Treat uncertainty as first-class information when decisions depend on it.
- Keep SKILL instructions text-first and executable via plain language checklists.
- Do not make execution depend on reading diagrams, images, or visual assets.
- Anti-Pattern Mapping:
  - Forbidden: truncated-bar exaggeration, color-for-decoration only, legend puzzles, chartjunk-heavy 3D decoration, unreadable tiny labels, unreported units for quantitative axes.

## One More Thing
If the analysis question, audience, or medium is unclear, stop and ask for clarification before finalizing the chart recommendation.

## How (Structural Workflow)
### Phase 1: Define the Message and Audience
1. Extract the main question in one sentence (comparison, distribution, trend, proportion, association, geospatial, uncertainty).
2. Identify the audience decision context and expected reading depth.
3. Determine whether the figure is exploratory, explanatory, or both.

### Phase 2: Map Data to Encodings
1. Classify each variable (quantitative continuous/discrete, categorical ordered/unordered, date/time, text).
2. Map variables to appropriate aesthetics (position first, then color/shape/size/line type as needed).
3. Select linear or nonlinear scales intentionally and document why.

### Phase 3: Select Visualization Family
1. Use chart family by task:
   - amounts: bars, dots, heatmaps
   - distributions: histogram, density, ECDF, box/violin/sina/ridgeline
   - proportions: side-by-side bars, stacked bars, pie only when simple fractions are primary
   - associations: scatter/correlogram/dimension-reduction views
   - trends/time series: lines with trend aids when needed
   - geospatial: projection-aware maps, choropleth/cartogram when justified
   - uncertainty: intervals, bands, frequency framing, or hypothetical outcomes
2. Prefer the simplest chart that answers the question without hiding structure.

### Phase 4: Design for Perception and Accessibility
1. Apply proportional-ink checks for area/length encodings.
2. Handle overlap with jitter, transparency, binning, or contours.
3. Use color purposefully:
   - distinguish categories,
   - encode ordered values with monotonic scales,
   - highlight focal items with accent colors.
4. Test color-vision-deficiency robustness; add redundant coding if needed.
5. Set labels, legends, captions, and units for immediate interpretation.
6. Avoid 3D unless representing true 3D structure and no better 2D alternative exists.

### Phase 5: Story and Context Refinement
1. Ensure each figure makes one primary point.
2. If figure complexity is high, introduce a simpler lead figure first, then expand.
3. Remove decorative elements that do not support interpretation.
4. Align title and caption with the intended claim and evidence.

### Phase 6: Export and Reproducibility
1. Choose output format by usage:
   - vector when possible for publication/editability,
   - high-resolution bitmap when needed.
2. Preserve reproducibility with scripted generation or explicit transformation notes.
3. Keep content and design separable when tooling supports themes/styles.

## Resources
- [Visualization Decision Checklist](./details/visualization-decision-checklist.md)
- [Visualization Anti-Patterns](./details/visualization-anti-patterns.md)

Diagram-related files in `details/` are for optional reference and evidence only; they are not required steps in this SKILL workflow.

## Review In Mind (ReviewInMindGenie)

Execute the common review loop in [review-in-mind](../skill-common/details/review-in-mind.md) before delivering.

Review lens for this skill:
- Does the chosen chart type answer the analytical question without misleading encodings?
- Are color, labels, scales, and uncertainty handled accessibly and consistently?
- Would the intended audience read the intended message correctly at a glance?

## Validation (Verifiable Rewards)
1. Verify chart type and encodings directly answer the stated analytical question.
2. Verify quantitative axes and units are explicit and not misleading.
3. Verify color and legend design remains readable in grayscale/CVD simulation.
4. Verify no prohibited anti-patterns are present.
5. Verify title/caption and annotations support a clear single takeaway.
