# Visualization Decision Checklist

Use this checklist before finalizing any chart or figure.

## 1. Question and Audience
- Verify the figure answers one primary analytical question.
- Verify the intended audience and medium are explicit.
- Verify explanatory vs exploratory purpose is clear.

## 2. Variable and Scale Mapping
- Verify each variable type is identified (quantitative/categorical/time).
- Verify critical values are encoded by position when possible.
- Verify axis units are present for quantitative variables.
- Verify scale choice (linear/log/etc.) is justified.

## 3. Chart Family Fit
- Verify chart family matches the task:
  - amounts, distributions, proportions, associations, trends, geospatial, uncertainty
- Verify simpler alternatives were considered before complex layouts.

## 4. Perception and Accuracy
- Verify magnitude encodings obey proportional-ink rules.
- Verify bars on linear scales start at zero.
- Verify overlap treatment (jitter/transparency/binning/contours) is appropriate.
- Verify trend aids or smoothing are not hiding critical variance.

## 5. Color and Accessibility
- Verify color has a clear semantic role (grouping, value scale, highlighting).
- Verify ordered data does not use nonmonotonic/rainbow scales.
- Verify category count does not overload qualitative color usage.
- Verify readability in grayscale and CVD simulation.
- Verify redundant coding exists where color-only decoding would fail.

## 6. Labels, Captions, and Context
- Verify title states the key claim or question.
- Verify axis labels and legend labels are explicit and concise.
- Verify caption provides context and data source when needed.
- Verify reference lines/grids support comparison without clutter.

## 7. Story and Flow
- Verify the figure has one memorable takeaway.
- Verify complex visuals are introduced with simpler lead visuals when possible.
- Verify decorative elements that do not aid interpretation are removed.

## 8. Output and Reproducibility
- Verify output format (vector/bitmap) fits delivery context.
- Verify generation steps are reproducible (scripted or clearly documented).
- Verify visual style can be reused consistently across related figures.
