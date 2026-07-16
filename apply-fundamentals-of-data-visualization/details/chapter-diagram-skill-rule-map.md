# Chapter -> Diagram -> Skill Rule Map

This file maps core book chapters and diagram themes to concrete, reusable SKILL rules.

Source book evidence:
- Local extracted text corpus for the source book
- Local extracted visual asset set for the source book

## How to Use This Map
1. Find the target chapter/theme.
2. Reuse the mapped rule statements in new SKILL constraints and validation sections.
3. Reuse anti-pattern checks as explicit rejection criteria.

## Mapping Table

| Chapter Theme | Diagram Pattern to Inspect | Reusable SKILL Rule | Validation Check | Common Anti-Pattern |
|---|---|---|---|---|
| 2. Mapping data to aesthetics | Same data shown with different encodings | Encode key quantitative comparisons primarily through position; use color/shape/size as secondary encodings. | Verify primary comparison is decodable without legend-only dependence. | Using decorative encodings as primary signal. |
| 3. Coordinate systems and axes | Same relationship under different aspect ratios/scales | Choose coordinate system and scale from analysis question; document nonlinear scale intent. | Verify axis type and units are explicit and justified. | Unexplained log scales or distorted aspect choices. |
| 4. Color scales | Baseline vs accent-color examples | Use color with purpose: distinguish, encode value, or highlight; keep baseline marks muted when highlighting. | Verify highlighted marks remain perceptually dominant. | Saturated full-rainbow styling without semantic role. |
| 5. Directory of visualizations | Side-by-side chart family catalog | Select chart family by task type (amount, distribution, proportion, trend, association, geospatial, uncertainty). | Verify chart type matches stated question. | Reusing habitual chart types regardless of task. |
| 6. Amounts | Bars, grouped/stacked bars, dots | For magnitude comparisons on linear scales, preserve proportionality and zero-based bars where bar length encodes value. | Verify bar baselines and magnitude interpretation are consistent. | Truncated bars exaggerating differences. |
| 7-9. Distributions | Histogram/density/ECDF/box/violin/sina/ridgeline comparisons | Choose distribution view by comparison depth and count; avoid misleading density/bin choices without explanation. | Verify distribution choice supports intended comparison granularity. | Single chart type forced on all distribution problems. |
| 10-11. Proportions and nested proportions | Pie vs bars vs mosaic/treemap/parallel sets | Prefer bars for precise part-to-part comparison; use pies only for simple part-to-whole narratives. | Verify reader can compare target proportions accurately. | Complex multi-condition pies causing comparison failure. |
| 12-14. Associations, time series, trends | Scatter/trend overlays/multi-series layouts | Keep trend aids transparent and non-obscuring; separate relationship signal from overplot noise. | Verify trend representation does not hide variance or imply false certainty. | Over-smoothed trend lines replacing actual data context. |
| 15. Geospatial data | Projection/layer/choropleth/cartogram variants | Choose map projection and map type intentionally; do not imply area/importance incorrectly. | Verify map type aligns with variable semantics and geographic claim. | Choropleth or cartogram used without discussing weighting effects. |
| 16. Uncertainty | Error bars/bands/frequency framing/HOP examples | Treat uncertainty as first-class output; choose representation by audience literacy and decision risk. | Verify at least one uncertainty representation is present when estimates are shown. | Showing point estimates alone when uncertainty drives interpretation. |
| 17. Proportional ink | Good vs misleading magnitude displays | Enforce proportional-ink consistency whenever area/length encodes value. | Verify no contradictory visual cue encodes a different magnitude than labels. | Area/length cues inconsistent with reported values. |
| 18. Overlap handling | Jitter/transparency/binning/contour alternatives | Resolve overplotting deliberately before interpretation claims. | Verify overlap mitigation method is appropriate for sample density. | Dense scatterplots interpreted as if all points visible. |
| 19. Color pitfalls | Too many categories/rainbow/non-CVD-safe examples | Cap qualitative color complexity; use monotonic scales for ordered values; test CVD robustness. | Verify grayscale/CVD readability and category distinguishability. | Legend puzzles and nonmonotonic value colors. |
| 20. Redundant coding | Color + shape + order-aligned legends | Use redundant coding when color-only decoding is fragile; align legend order with perceptual order. | Verify categories remain distinguishable without color alone. | Color-only coding for tiny marks or dense overlap. |
| 21. Multipanel figures | Small multiples/compound layouts | Use small multiples for structured comparisons; keep axes and panel semantics consistent. | Verify panel-to-panel comparability and consistent scale policy. | Inconsistent panel scales hiding true differences. |
| 22. Titles, captions, tables | Caption/title variants and label clarity | Ensure figure title, axis labels, units, and caption context remove ambiguity. | Verify zero ambiguous quantitative axes or missing units. | Missing units/axes requiring reader guesswork. |
| 23. Data-context balance | Grid/background variants | Balance context and data ink; keep only guides that improve comparison. | Verify grid/reference lines are minimal yet sufficient. | Overbearing grids or context-free floating data. |
| 24. Axis label legibility | Label size comparisons | Prioritize legible axis labels and text hierarchy for intended medium. | Verify text remains readable at final render size. | Tiny labels that fail in slides/reports. |
| 25. Avoid line drawings | Filled vs unfilled mark examples | Prefer filled forms when they improve figure-ground separation and readability. | Verify mark styling preserves clear visual grouping. | Thin-line-only marks losing contrast and structure. |
| 26. Don’t go 3D | 3D distortions and perspective confusion | Avoid gratuitous 3D; use 3D only when true 3D structure is essential and interpretable. | Verify 2D alternative was considered and rejected with rationale. | Decorative 3D that distorts comparison. |
| 27. Image formats | Format and compression examples | Choose export format by fidelity and reuse needs (vector first when practical). | Verify output format supports downstream usage without quality loss. | Lossy format overuse for analytical figures. |
| 28. Tooling and reproducibility | Repeatability/reproducibility workflow examples | Prefer reproducible figure pipelines; separate content and design where tooling allows. | Verify figure can be regenerated from source and documented transformations. | One-off manual edits with no reproducible path. |
| 29. Storytelling | Simple-to-complex narrative figure sequences | Build narrative arc with one primary takeaway per figure and staged complexity. | Verify each figure has a single explicit message tied to decision context. | Overloaded all-in-one charts with no clear takeaway. |

## Drop-in Rule Snippets for New Skills

Use these as copy-ready constraints in future SKILL.md files:

- "Chart selection must be justified by the analytical question category before styling choices are considered."
- "If bars encode magnitude on a linear axis, bar baselines must start at zero unless a documented exception is approved."
- "Ordered values must not use nonmonotonic color scales; qualitative colors must remain distinguishable under CVD and grayscale checks."
- "When overlap obscures mark density, apply jitter/transparency/binning/contours before making comparative claims."
- "If estimate uncertainty affects interpretation, include explicit uncertainty encoding (intervals, bands, frequency framing, or equivalent)."
- "3D styling is prohibited unless the data itself is intrinsically 3D and a 2D alternative cannot preserve the target insight."

## Integration Targets in This Repo

Recommended follow-up upgrades using this map:
- [validate-requirements-criteria/SKILL.md](../../validate-requirements-criteria/SKILL.md): add chart-quality ambiguity checks for metrics requirements.
- [create-living-documentation/SKILL.md](../../create-living-documentation/SKILL.md): add reproducible figure pipeline constraints.
- [build-feature-tree/SKILL.md](../../build-feature-tree/SKILL.md): enforce readability and color-independent interpretation for mindmaps.
