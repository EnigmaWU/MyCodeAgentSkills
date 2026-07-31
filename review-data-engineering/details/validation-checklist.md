# Validation Checklist

Run this checklist before finalizing a data engineering review.

## Findings Quality

- Findings are listed before summary material.
- Each finding has severity, lifecycle stage, undercurrent, evidence, risk, and advice.
- Findings distinguish verified issues from missing-evidence risks.
- Recommendations do not jump to technology choices before explaining lifecycle risk.
- Advice is actionable enough for an owner to decide the next step.

## Lifecycle Coverage

- Generation/source systems are assessed or explicitly marked not applicable/missing evidence.
- Storage is assessed or explicitly marked not applicable/missing evidence.
- Ingestion is assessed or explicitly marked not applicable/missing evidence.
- Transformation is assessed or explicitly marked not applicable/missing evidence.
- Serving and downstream consumers are assessed or explicitly marked not applicable/missing evidence.

## Undercurrent Coverage

- Security and privacy are considered.
- Data management is considered.
- DataOps is considered.
- Data architecture is considered.
- Orchestration is considered.
- Software engineering is considered.
- Cost and FinOps are considered when cloud, compute, storage, egress, or third-party services appear.

## Evidence Discipline

- Every conclusion cites a file, command, doc, observed pattern, or missing-evidence label.
- Lack of evidence is not treated as proof that a control does not exist.
- The report states what evidence would reduce uncertainty.
- The review remains read-only unless the user explicitly requested fixes.

## Report Shape

- Executive summary names the highest-risk lifecycle stage and undercurrent.
- Missing evidence is separated from verified defects.
- Next actions are grouped into quick wins, architecture decisions, operational hardening, and follow-up questions.
- Residual risk is clear enough for a project owner to prioritize.
