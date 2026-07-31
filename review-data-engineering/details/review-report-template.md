# Review Report Template

Use findings first. Keep summaries short and put evidence near each claim.

```markdown
# Data Engineering Review

## Findings

| Severity | Lifecycle Stage | Undercurrent | Evidence | Risk | Advice |
| --- | --- | --- | --- | --- | --- |
| Critical/High/Medium/Low/Observation | Generation/Storage/Ingestion/Transformation/Serving/Global | Security/DataOps/etc. | File, command, doc, or Missing Evidence | What can fail or mislead | What to do next |

## Executive Summary

- Overall lifecycle maturity:
- Highest-risk lifecycle stage:
- Highest-risk undercurrent:
- Best immediate improvement:
- Main missing evidence:

## Lifecycle Map

| Stage | Status | Evidence | Key Risks | Review Advice |
| --- | --- | --- | --- | --- |
| Generation / Source Systems | Observed/Partial/Missing Evidence/Not Applicable |  |  |  |
| Storage | Observed/Partial/Missing Evidence/Not Applicable |  |  |  |
| Ingestion | Observed/Partial/Missing Evidence/Not Applicable |  |  |  |
| Transformation | Observed/Partial/Missing Evidence/Not Applicable |  |  |  |
| Serving | Observed/Partial/Missing Evidence/Not Applicable |  |  |  |

## Undercurrents

| Undercurrent | Status | Evidence | Risk | Advice |
| --- | --- | --- | --- | --- |
| Security and privacy |  |  |  |  |
| Data management |  |  |  |  |
| DataOps |  |  |  |  |
| Data architecture |  |  |  |  |
| Orchestration |  |  |  |  |
| Software engineering |  |  |  |  |
| Cost / FinOps |  |  |  |  |

## Missing Evidence

- Evidence that could not be verified:
- Why it matters:
- How to verify it next:

## Recommended Next Actions

1. Quick wins:
2. Architecture decisions:
3. Operational hardening:
4. Follow-up questions:
```

## Severity Guidance

- **Critical**: Likely data loss, privacy exposure, severe production breakage, or materially wrong downstream decisions.
- **High**: Significant reliability, correctness, security, or operability risk with plausible near-term impact.
- **Medium**: Meaningful maintainability, scalability, quality, or ownership gap.
- **Low**: Local issue or improvement with limited immediate risk.
- **Observation**: Context, tradeoff, or missing evidence worth tracking but not yet a defect.
