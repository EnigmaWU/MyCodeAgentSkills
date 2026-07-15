# Specification by Example Enhancements for User Stories

Use this companion checklist after drafting a story.

## 1. Scope from Goal
- Verify the story traces to a business outcome, not only a technical action.
- Verify scope boundaries are explicit (what is in, what is out).

## 2. Collaboration Readiness
- Verify assumptions are listed for product/BA review.
- Verify unresolved decisions are captured as questions, not hidden in vague text.

## 3. Example Quality
- Verify each scenario uses realistic domain data.
- Verify expected outcomes are explicit and observable.
- Verify examples avoid combinatorial explosion.

## 4. Specification Quality
- Verify scenarios describe business behavior, not UI scripts.
- Verify one behavior per scenario.
- Verify language remains domain-centric and understandable by non-developers.

## 5. Executability Readiness
- Verify each scenario can be translated to automated acceptance tests without rewriting intent.
- Verify no implementation-only terms are required to understand the scenario.

## 6. Red Flags
- Story starts from click flow instead of user outcome.
- Acceptance criteria include undefined adjectives (fast, reliable, intuitive).
- Happy path exists, but no error or exception behavior is specified.
- Then clauses mention internals (DB table, endpoint, framework class) rather than behavior.
