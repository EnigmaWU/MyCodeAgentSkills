---
name: prioritize-requirements
description: >
  WHEN/WHERE/WHO: [Scheduling: Product owners or agents grooming a backlog of features or user stories.]
  HOW: [Structural: Use this SKILL to score items across Value, Cost, and Risk using an analytical matrix, yielding a strict rank order.]
  WHY: [Scheduling: Subjective "High/Medium/Low" labels lead to everything being marked "High." Mathematical scoring forces objective trade-offs.]
---

# Prioritize Requirements

## Common Contract (Load First)

When this skill is activated, first load [skill-common](../skill-common/SKILL.md) and apply the shared conventions it defines: canonical section order, frontmatter rules, anti-pattern guidance, and the Review In Mind loop in [review-in-mind](../skill-common/details/review-in-mind.md). This skill adds only domain-specific rules below.

## Who
Product Managers, Business Analysts, and AI Agents. The agent uses this skill to objectively rank work items.

## What
This skill implements an Analytical Prioritization Matrix. It evaluates a list of requirements, scoring each on relative Business Value, User Value, Cost (effort), and Risk. It calculates a final Priority Score and outputs a sorted backlog.

## When
Invoke this skill during sprint planning, backlog grooming, or when deciding MVP scope. Trigger phrases include: "prioritize this list," "what should we build first," "rank these user stories," or "run a prioritization matrix."

## Where
Applies to feature lists, user story backlogs, and bug trackers.

## Why
Without a strict framework, stakeholders tend to label every requirement as "Critical." By separating the *value* of a feature from the *cost/risk* to build it, we can identify "quick wins" (high value, low cost) and avoid "money pits" (low value, high cost).

## Inputs
- A list of requirements, features, or user stories.
- (Optional) Stakeholder input on relative weights (e.g., "Cost is more important than Risk right now").

## Output (Logical Evidence)
- A markdown table displaying the scores for each requirement.
- A sorted list of requirements from highest priority to lowest.

## Optimization Readiness
- **Failure Signals**: Scores are inconsistent, the matrix falls back to vague High/Medium/Low labels, unknown effort is guessed instead of flagged, or the ranking does not separate quick wins from high-risk investments.
- **Evidence To Collect**: Scoring tables, weighting choices, stakeholder adjustments, and examples where the ranking was challenged or revised after review.
- **Safe Mutation Boundaries**: Refine scoring instructions, weighting guidance, output formatting, and review prompts without changing the core numeric prioritization workflow.
- **Acceptance Criteria**: Accept revisions only if the skill yields a clear numeric ranking, documents weights when used, and calls out unknown estimates instead of masking uncertainty.
- **Rejected Revision Handling**: Record misleading scoring heuristics, non-numeric fallback patterns, and weak explanations of tradeoffs so they are not reused blindly.
- **Transfer Check**: Verify the workflow still works for features, requirements, and user stories with and without stakeholder weighting.
- **Stop Rule**: If there are too few items or too little estimation data to produce a meaningful matrix, stop and tell the user to simplify or gather estimates first.

## Constraints (Logical Boundaries)
- Do not use High/Medium/Low. You must use numerical scores (e.g., 1 to 9).
- Do not guess wildly; if a cost is completely unknown, flag it for estimation rather than giving it a random score.

## One More Thing
If the provided list has fewer than 3 items, inform the user that a matrix is unnecessary and they should just use simple pairwise comparison.

## How (Structural Workflow)
### Phase 1: Establish the Scale and Weights
1. Define the scale (usually 1 to 9, where 9 is highest value, highest cost, or highest risk).
2. Assign weights to the categories if the user provided them (e.g., Business Value = 2x, Cost = 1x). Default to 1x for all.

### Phase 2: Scoring
3. For each requirement, estimate:
   - **Business Value:** How much does this help the company (revenue, compliance)?
   - **User Value:** How much does this improve the user experience?
   - **Cost/Effort:** How hard is this to build?
   - **Risk/Complexity:** How likely is this to break or face technical hurdles?

### Phase 3: Calculation and Ranking
4. Calculate the Total Value = (Business Value) + (User Value).
5. Calculate the Total Penalty = (Cost) + (Risk).
6. Calculate the Priority Score = (Total Value) / (Total Penalty).
7. Sort the requirements descending by Priority Score.

## Resources
- [Analytical Matrix Guide](./details/analytical-matrix-guide.md)

## Review In Mind (ReviewInMindGenie)

Execute the common review loop in [review-in-mind](../skill-common/details/review-in-mind.md) before delivering.

Review lens for this skill:
- Is every requirement scored on business value, user value, cost, and risk with a calculated priority?
- Are scores traceable to stated criteria rather than hidden judgment?
- Would the sorted backlog be defensible to stakeholders?

## Validation
1. Verify that all items in the list were scored.
2. Check the math: ensure the final sorted order matches the calculated Priority Scores.
