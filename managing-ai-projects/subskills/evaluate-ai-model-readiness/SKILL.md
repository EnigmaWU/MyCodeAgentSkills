---
name: evaluate-ai-model-readiness
description: >
  WHEN/WHERE/WHO: AI project managers and agents who must decide whether an AI
  model is ready to advance or deploy, using the evaluation and validation
  guidance from "Managing AI Projects".
  HOW: Select the right metrics for the model type, compare against thresholds
  and baseline, run safety and bias checks, collect human evaluation, document
  results, and issue a go/no-go decision.
  WHY: Models are never perfect; readiness gates prevent both endless tuning and
  premature launches.
---

# Evaluate AI Model Readiness

## Who
AI project managers, data scientists, and agents running evaluation gates and
go/no-go reviews.

## What
Produce a readiness decision for an AI model:

- metric selection per model type (classification, regression, NLP, GenAI);
- comparison to baseline and agreed thresholds;
- safety testing and bias audit;
- human evaluation where needed;
- documentation (model card) and go/no-go recommendation.

## When
Trigger when the user asks to: "is the model ready", "evaluate the model",
"validate the model", "should we deploy", "run the go/no-go review", "check
model performance", or "is this good enough to launch".

## Where
Works from experiment results, metrics, and thresholds provided by the user or
the project plan.

## Why
The book stresses that evaluation must be pre-agreed, not discovered at the end:
locked metrics, locked datasets, "good enough" thresholds, and readiness gates
prevent both proof-of-concept purgatory and unsafe launches.

## Inputs
- **Model/experiment results** (required): metrics, confusion matrix or
  samples, comparisons.
- **Agreed thresholds** (required or to be set): target and minimum acceptable
  performance.
- **Context** (optional): baseline results, use-case risk level, regulatory
  requirements.

## Output (Logical Evidence)
- Readiness report with: chosen metrics and values, baseline comparison,
  safety/bias findings, human evaluation results, documentation status, and a
  verdict: GO / GO WITH CONDITIONS / NO-GO.

## Optimization Readiness
- **Failure Signals**: Metrics chosen after the fact; no "good enough"
  threshold; safety/bias checks skipped; verdict not tied to evidence;
  hallucinated metric values.
- **Evidence To Collect**: Real evaluation runs; feedback on whether gates
  caught problems; misuse of metrics.
- **Safe Mutation Boundaries**: Metric lists, report format, and severity rules
  may change. The go/no-go gate and locked-evaluation principle must remain.
- **Acceptance Criteria**: A revision must produce a verdict with evidence for a
  new evaluation run.
- **Rejected Revision Handling**: Record rejected metrics/verdict patterns in
  the umbrella's validation log.
- **Transfer Check**: Must handle ML, DL, NLP, and GenAI evaluations.
- **Stop Rule**: If results or thresholds are missing, stop and ask.

## Constraints (Logical Boundaries)
- Lock evaluation datasets and metrics before comparing models.
- Use the right metric family:
  - Classification: precision, recall, F1/F2, AUC-ROC.
  - Regression: MAE, MSE, R².
  - NLP: BLEU, ROUGE, perplexity.
  - GenAI: groundedness, relevance, toxicity, coherence, fluency, faithfulness.
- Include human evaluation for GenAI/LLM outputs.
- Never report metrics the user did not provide.
- **Anti-Pattern Mapping**:
  - MUST NOT approve deployment without safety/bias review in high-risk use
    cases.
  - MUST NOT move goalposts after results are known.
  - MUST NOT equate accuracy with business value.

## One More Thing
If results or thresholds are missing, stop and ask the user before issuing a
verdict.

## How (Structural Workflow)

### Phase 1: Lock evaluation criteria
1. Confirm the metric(s) for the model type (see Constraints).
2. Confirm the "good enough" threshold (minimum acceptable) and the target
   threshold, agreed with stakeholders.
3. Confirm the evaluation dataset is fixed and comparable to the baseline.

### Phase 2: Measure
1. Compare current results to baseline (naive) and previous iterations.
2. Record every metric with its source.
3. Check system performance: inference time, resource usage, latency.

### Phase 3: Safety and ethics
1. Run content-safety checks (prompt attacks, harmful output) for GenAI.
2. Run bias detection / fairness audit against protected segments.
3. Record findings and required mitigations (guardrails, retraining, human
   oversight).

### Phase 4: Human evaluation
1. For GenAI/LLM and other subjective outputs, collect human scores on the
   relevant criteria (usefulness, tone, correctness).
2. Summarize scores against thresholds.

### Phase 5: Document
1. Produce a model card: purpose, metrics, limitations, provenance.
2. Ensure traceability (data/code/model versions) for audit.

### Phase 6: Decide
1. GO: all thresholds met and no blockers.
2. GO WITH CONDITIONS: thresholds met except documented conditions with
   owners/dates.
3. NO-GO: thresholds not met or blocker exists.
4. Deliver the readiness report.

## Review In Mind (ReviewInMindGenie)

Before delivering, activate the ReviewInMindGenie: stop authoring, switch to a skeptical reviewer, and critique the artifact as if someone else had produced it.

1. **Review Against Own Rules**: Re-read the output against this skill's `What`, `Constraints (Logical Boundaries)`, and `Validation` criteria. Check each rule explicitly; do not assume it passed because it was easy to write.
2. **Classify Findings**: Label each defect as BLOCKER (output unusable), MAJOR (violates a core rule), or MINOR (polish/consistency).
3. **Fix or Escalate**: Fix BLOCKER and MAJOR findings immediately when the fix is unambiguous. After each fix, re-check the affected criteria. If a finding cannot be fixed without new input (missing evidence, conflicting requirements, or a user decision), do not guess — report it as an open question or known gap.
4. **Deliver with a Review Note**: Present the output with a short note: what was checked, what was fixed, and what remains as a known gap. Never present an unreviewed artifact as final.

Review lens for this skill:
- Are metrics matched to model type with baseline comparison and agreed thresholds?
- Do safety/bias checks and human evaluation cover the highest-risk outputs?
- Is the go/no-go recommendation traceable to evidence rather than optimism?

## Validation (Verifiable Rewards)
1. Metrics match the model type and are sourced from user input.
2. Thresholds are explicit and pre-agreed (or set with stakeholders).
3. Safety/bias checks are present for high-risk use cases.
4. Verdict is consistent with evidence.
5. Documentation (model card) is included.
