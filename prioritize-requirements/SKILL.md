---
name: prioritize-requirements
description: >
  WHEN/WHERE/WHO: [Scheduling: Product owners or agents grooming a backlog of features or user stories.]
  HOW: [Structural: Use this SKILL to score items across Value, Cost, and Risk using an analytical matrix, yielding a strict rank order.]
  WHY: [Scheduling: Subjective "High/Medium/Low" labels lead to everything being marked "High." Mathematical scoring forces objective trade-offs.]
---

# Prioritize Requirements

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

## Validation
1. Verify that all items in the list were scored.
2. Check the math: ensure the final sorted order matches the calculated Priority Scores.
