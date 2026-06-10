# Test Planning Checklist

Use this checklist during sprint planning or feature design to ensure you have considered all Agile Testing Quadrants.

## Q1: Technology & Support (The Foundation)
- [ ] Are we writing automated unit tests for the core logic?
- [ ] Is test coverage sufficient for the complex algorithms in this feature?
- [ ] Are component/integration tests needed to verify internal interactions?

## Q2: Business & Support (The Requirements)
- [ ] Are the acceptance criteria clearly defined and testable?
- [ ] Can we automate the acceptance tests using a BDD framework or UI test tool?
- [ ] Do we have a shared understanding of the "happy path" and primary alternate flows?

## Q3: Business & Critique (The Experience)
- [ ] Have we allocated time for exploratory testing?
- [ ] Who is responsible for reviewing the UX/UI for usability issues?
- [ ] Is there a need for customer feedback or UAT before full release?
- [ ] Have we brainstormed edge cases or malicious user behavior?

## Q4: Technology & Critique (The 'Ilities')
- [ ] Will this feature impact system performance or database load? If so, do we need to run load tests?
- [ ] Are there security implications (e.g., handling PII, authentication changes)?
- [ ] Does this change require updates to infrastructure or deployment pipelines?
- [ ] Have we run static analysis or dependency vulnerability checks?
