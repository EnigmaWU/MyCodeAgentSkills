# Analytical Prioritization Matrix

Use this guide to calculate priority scores for requirements.

## 1. The Scale
Score every category on a relative scale from **1 to 9**.
- **Value:** 9 = Extremely valuable; 1 = Barely noticeable value.
- **Cost/Penalty:** 9 = Extremely expensive/risky; 1 = Trivial effort/no risk.

*Tip: Anchor the scale. Pick a well-understood, medium-sized feature and assign it 5s across the board. Score everything else relative to that anchor.*

## 2. The Formula

**Value Score** = (Business Value * Weight) + (User Value * Weight)
**Penalty Score** = (Cost * Weight) + (Risk * Weight)

**Priority Score** = Value Score / Penalty Score

*The higher the Priority Score, the higher the requirement goes in the backlog.*

## 3. Example Matrix

| Requirement | Business Value (1-9) | User Value (1-9) | Cost (1-9) | Risk (1-9) | Priority Score (Value / Penalty) | Rank |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Single Sign-On | 8 | 9 | 5 | 6 | (17 / 11) = **1.54** | 1 |
| Dark Mode | 2 | 8 | 3 | 1 | (10 / 4) = **2.50** | 2 |
| Legacy DB Migration | 9 | 1 | 9 | 9 | (10 / 18) = **0.55** | 3 |

*Wait, look at the math!*
- Dark Mode: 10 / 4 = 2.50 (Highest Priority - Quick Win)
- Single Sign-On: 17 / 11 = 1.54 (Medium Priority)
- DB Migration: 10 / 18 = 0.55 (Lowest Priority - Money Pit)
