---
name: apply-screenplay-pattern
description: >
  WHEN/WHERE/WHO: [Scheduling: SDETs, developers, or agents writing or refactoring automated acceptance tests.]
  HOW: [Structural: Use this SKILL to structure test code around Actors, Tasks, Interactions, Abilities, and Questions rather than Page Objects.]
  WHY: [Scheduling: Page Objects bloat into massive "God classes". Screenplay applies SOLID principles to test code.]
---

# Apply Screenplay Pattern

## Common Contract (Load First)

When this skill is activated, first load [skill-common](../skill-common/SKILL.md) and apply the shared conventions it defines: canonical section order, frontmatter rules, anti-pattern guidance, and the Review In Mind loop in [review-in-mind](../skill-common/details/review-in-mind.md). This skill adds only domain-specific rules below.

## Who
Software Development Engineers in Test (SDETs), Developers, and AI Agents. The agent uses this skill to architect clean, scalable test automation code.

## What
This skill implements the Screenplay Pattern, popularized by Serenity BDD and Serenity/JS. It replaces traditional Page Objects with an actor-centric model. Instead of calling methods on a `LoginPage` class, you instruct an `Actor` (who has `Abilities` like browsing the web) to perform a `Task` (which is composed of lower-level `Interactions` and `Questions`).

## When
Invoke this skill when automating BDD scenarios, refactoring messy test scripts, or building an automation framework from scratch. Trigger phrases include: "use the screenplay pattern," "refactor these page objects," "create an actor and tasks," or "implement this using Serenity/JS."

## Where
Applies to test automation codebases (Java/Cucumber, TypeScript/Playwright, etc.).

## Why
When UI tests rely heavily on Page Objects, tests become tightly coupled to the UI structure. If the UI changes, tests break. Furthermore, Page Objects do not easily support non-UI interactions (like calling a REST API). The Screenplay Pattern abstracts the "what" (the business task) from the "how" (the UI or API interaction), allowing tests to survive UI overhauls.

## Inputs
- An automated test script, a set of Page Objects, or a Gherkin scenario.

## Output (Logical Evidence)
- Refactored test code separated into Actors, Tasks, Interactions, and Questions.

## Optimization Readiness
- **Failure Signals**: Tasks contain low-level API code, questions become assertions inside tasks, abilities are over-shared, or the design falls back to page-object style coupling.
- **Evidence To Collect**: Actor/ability maps, task definitions, interaction chains, questions, and examples of refactors that reduced UI coupling.
- **Safe Mutation Boundaries**: Refine actor naming, task decomposition, interaction guidance, and question design without changing the core Screenplay separation of intent and mechanism.
- **Acceptance Criteria**: Accept revisions only if tasks stay business-focused, interactions own framework-specific code, and questions are the assertion boundary.
- **Rejected Revision Handling**: Record page-object spillover, direct WebDriver calls in tasks, and assertion placement mistakes so they are not repeated.
- **Transfer Check**: Verify the workflow still works for UI-heavy tests, API-driven tests, and mixed interaction suites.
- **Stop Rule**: If the input is a pure unit test with no external interfaces, stop and redirect to a simpler testing approach.

## Constraints (Logical Boundaries)
- **Tasks** should describe business intent (e.g., `LoginWithCredentials`) and should NOT contain WebDriver or API specific code.
- **Interactions** handle the low-level execution (e.g., `Click.on`, `Enter.theValue`) and are the *only* place where framework-specific code lives.
- **Questions** extract state from the application to be used in assertions. Do NOT put assertions directly inside Tasks or Page Objects.

## One More Thing
If the input is just a simple unit test for a pure logic function (no external interfaces), stop and inform the user that the Screenplay Pattern is designed for integration and end-to-end testing, not simple unit tests.

## How (Structural Workflow)
### Phase 1: Identify the Actor and Abilities
1. Identify the **Actor** representing the user in the scenario.
2. Determine what **Abilities** the actor needs (e.g., `BrowseTheWeb`, `CallAnApi`).

### Phase 2: Define Tasks
3. Read the scenario steps. For each major business action (e.g., "logs in", "searches for a flight"), define a **Task**.
4. Name the task using domain language (e.g., `SearchForFlights.from(origin).to(destination)`).

### Phase 3: Define Interactions and Questions
5. Inside each Task, compose the sequence of **Interactions** required to complete it (e.g., `Click`, `Enter`, `Navigate`).
6. Identify the assertions in the scenario (the `Then` steps). Create **Questions** that query the state of the system, so the Actor can ensure the expected state is met.

## Resources
- [Screenplay Components](./details/screenplay-components.md)

## Review In Mind (ReviewInMindGenie)

Execute the common review loop in [review-in-mind](../skill-common/details/review-in-mind.md) before delivering.

Review lens for this skill:
- Are Actors, Tasks, Interactions, Abilities, and Questions cleanly separated (no Page-Object god classes)?
- Does each Task expose a single user-facing intent composed of small interactions?
- Would the suite remain readable and maintainable as the UI evolves?

## Validation
1. Verify that no Task contains direct calls to WebDriver (or other low-level API clients).
2. Verify that no Page Object or Interaction contains assertions.
