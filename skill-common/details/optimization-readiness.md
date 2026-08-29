# Optimization Readiness Contract

Every skill MUST include an `## Optimization Readiness` section with the following fields. The wording may be tailored per skill, but the contract is shared:

- **Failure Signals**: What repeated defects, routing misses, or unstable outputs show the skill needs revision.
- **Evidence To Collect**: What examples, traces, reviews, or transcripts must be gathered before revising.
- **Safe Mutation Boundaries**: Which parts may be revised and which invariants must remain stable.
- **Acceptance Criteria**: What independent check proves a revision is an improvement.
- **Rejected Revision Handling**: How failed edits and anti-patterns are recorded so they are not repeated.
- **Transfer Check**: How to confirm the skill still works on at least one nearby use case.
- **Stop Rule**: When to stop iterating and escalate for missing context or conflicting evidence.

Rules:
- The stop rule MUST be explicit; iteration must never run forever.
- Rejected revisions belong in the skill's `details/validation-log.md` (or the common `validation-log.md` if the skill has no details folder).
- A revision cannot be accepted because it "reads better"; it must pass the skill's independent acceptance criteria.
