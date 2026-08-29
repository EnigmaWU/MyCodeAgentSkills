---
name: select-ai-model-approach
description: >
  WHEN/WHERE/WHO: AI project managers and agents who must choose an AI model
  family and approach for a use case, balancing task type, data, cost,
  explainability, and team skills.
  HOW: Classify the required AI capability and task, map it to candidate model
  families (ML, DL, NLP, GenAI), decide build vs. leverage and baseline vs. best,
  estimate cost/compute, and document trade-offs with metrics.
  WHY: The book shows model choice drives feasibility, cost, explainability, and
  project risk; the right discussion up front prevents sunk-cost mistakes.
---

# Select AI Model Approach

## Who
AI project managers, tech leads, and agents facilitating model selection with
data scientists and AI engineers.

## What
Produce a model recommendation with rationale:

- required AI capability (forecast, classify, detect, complete, generate,
  automate, optimize);
- candidate model family (ML, DL, NLP/LLM, GenAI) and specific model types;
- build vs. leverage decision (custom training, open source, managed APIs);
- baseline (naive) vs. best model plan;
- cost/compute estimate and explainability trade-offs;
- evaluation metrics to confirm the choice.

## When
Trigger when the user asks to: "which AI model should we use", "choose the AI
approach", "ML or LLM for this", "should we build or buy the model", "compare
model options", or "what algorithm fits this task".

## Where
Works from the use case and data context provided by the user. Output is a
recommendation document.

## Why
The book's technical chapters emphasize that model choice affects data
requirements, compute, roadmap, and explainability — and that simpler, mature
models often beat hype. This workflow makes the trade-off discussion structured.

## Inputs
- **Use case** (required): what the system must do.
- **Data context** (required): availability, volume, labels, quality.
- **Constraints** (optional): budget, latency, explainability, regulatory,
  team skills, infrastructure.

## Output (Logical Evidence)
- Recommendation containing: capability/task classification, candidate model
  families with pros/cons, build vs. leverage decision, baseline vs. best plan,
  cost/compute estimate, chosen metrics, and risks.

## Optimization Readiness
- **Failure Signals**: Recommendation ignores data availability; always picks
  the trendiest model; no metrics proposed; cost not estimated; recommendation
  contradicts team skills.
- **Evidence To Collect**: User feedback; cases where chosen models underperformed
  and why.
- **Safe Mutation Boundaries**: Decision criteria, model lists, and cost
  estimation wording may change. The capability/task classification and
  build-vs-leverage question must remain.
- **Acceptance Criteria**: A revision must produce a defensible recommendation
  for a new use case with metrics and trade-offs.
- **Rejected Revision Handling**: Record rejected model mappings in the
  umbrella's validation log.
- **Transfer Check**: Must handle ML, DL, NLP, GenAI, RAG, and agent use cases.
- **Stop Rule**: If the use case or data context is missing, stop and ask.

## Constraints (Logical Boundaries)
- Recommend only standard, real technologies (e.g., Scikit-learn, TensorFlow,
  PyTorch, transformers, cloud AI services) — never hallucinated tools.
- Match model complexity to data: no deep learning without sufficient labeled
  data and compute.
- Include explainability implications, especially in regulated domains.
- Frame costs as ranges based on usage scenarios.
- **Anti-Pattern Mapping**:
  - MUST NOT choose GenAI "because it's trending".
  - MUST NOT recommend fine-tuning when RAG would suffice.
  - MUST NOT ignore compute/data prerequisites.

## One More Thing
If the use case or data context is missing, stop and ask the user before
recommending a model.

## How (Structural Workflow)

### Phase 1: Classify the task
1. Identify the required AI capability: forecasting, classification,
   pattern/anomaly detection, completion, generation, automation, or
   optimization.
2. Identify the task type: regression, binary/multiclass classification,
   clustering, sequence/text, image, or conversational.
3. Identify the learning context: supervised (labels available), unsupervised,
   reinforcement, or self-supervised.

### Phase 2: Map to model families
1. If data is structured/tabular and small-to-medium: prefer ML models
   (regression, decision forests, XGBoost, SVM, clustering).
2. If data is large and patterns are complex (images, sequences): consider DL
   (CNN, RNN/LSTM, autoencoders, deep RL).
3. If text/language: consider NLP/GenAI (TF-IDF/BoW for small tasks; BERT/
   transformers/LLMs for deep understanding; RAG for grounded knowledge).
4. If the task is recommendation/time series/optimization: consider those
   dedicated families (collaborative filtering, ARIMA/Prophet/LSTM, OR).

### Phase 3: Decide build vs. leverage
1. Check whether pretrained/managed models satisfy the use case.
2. If yes: choose open source or managed cloud models; estimate token/API or
   reserved-capacity costs.
3. If custom training is required: confirm data volume, labeling, GPU/TPU
   compute, and team expertise.

### Phase 4: Baseline vs. best
1. Define a simple baseline (naive) model to get quick results.
2. Define the "best" candidate and the expected improvement.
3. Set the evaluation metrics that will compare them (see
   `evaluate-ai-model-readiness` for metric tables).

### Phase 5: Document and validate
1. Write the recommendation with trade-offs (performance, interpretability,
   cost, latency).
2. Confirm each recommendation has a metric and a "good enough" threshold.
3. Deliver the recommendation.

## Validation (Verifiable Rewards)
1. The recommendation states the capability and task type.
2. Candidate families are matched to data reality (labels, volume, compute).
3. Build vs. leverage decision includes cost reasoning.
4. Baseline and best model are defined with metrics.
5. No hallucinated tools or libraries appear.
