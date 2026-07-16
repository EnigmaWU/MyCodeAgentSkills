# Visualization Anti-Patterns

Use this list to detect and correct common failure modes.

## 1. Truncated Magnitude Charts
- Pattern: bar charts start above zero on linear scales.
- Risk: exaggerates differences.
- Correction: start bars at zero or switch to dots/lines if non-zero baseline is essential.

## 2. Gratuitous 3D Effects
- Pattern: 2D comparisons shown with 3D bars/pies/areas.
- Risk: perspective distortion and comparison errors.
- Correction: use 2D encodings unless true 3D structure is the analytical target.

## 3. Rainbow or Nonmonotonic Value Scales
- Pattern: ordered values encoded with hue cycles that reverse perceptual order.
- Risk: false gradients and misread magnitude relationships.
- Correction: use monotonic sequential/diverging scales with tested luminance behavior.

## 4. Color-Only Identification for Many Categories
- Pattern: many categories differentiated only by color and large legends.
- Risk: legend lookup burden and ambiguity.
- Correction: reduce categories, group by higher-level classes, and add direct labels/redundant coding.

## 5. Overly Saturated Large Fill Areas
- Pattern: intense color blocks dominate the chart.
- Risk: visual fatigue and reduced precision reading.
- Correction: reduce saturation for baseline marks; reserve accent colors for focal elements.

## 6. Missing Units or Ambiguous Axes
- Pattern: quantitative axes without clear units/titles.
- Risk: interpretation uncertainty.
- Correction: add explicit labels and units; keep concise but unambiguous.

## 7. Context Imbalance
- Pattern: too many grid/background elements or none where needed.
- Risk: clutter or poor comparability.
- Correction: add minimal useful guides perpendicular to key comparison direction.

## 8. Complex Figure Without Onboarding
- Pattern: audience sees full complexity first.
- Risk: cognitive overload; key insight lost.
- Correction: sequence visuals from simple to complex and emphasize one takeaway per figure.

## 9. Irreproducible Figure Pipeline
- Pattern: manual edits are not traceable/repeatable.
- Risk: inconsistencies and update friction.
- Correction: script generation where possible; document post-processing exactly when unavoidable.
