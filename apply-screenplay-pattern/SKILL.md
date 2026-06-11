---
name: apply-screenplay-pattern
description: >
  WHEN/WHERE/WHO: SDETs, developers, or agents writing or refactoring automated acceptance tests.
  HOW: Use this SKILL to structure test code around Actors, Tasks, Interactions, Abilities, and Questions rather than Page Objects.
  WHY: Page Objects bloat into massive "God classes" full of brittle locators and mixed concerns. Screenplay applies SOLID principles to test code, making it reusable, readable, and highly maintainable at scale.
---

# Apply Screenplay Pattern

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

## Output
- Refactored test code separated into Actors, Tasks, Interactions, and Questions.

## Constraints
- **Tasks** should describe business intent (e.g., `LoginWithCredentials`) and should NOT contain WebDriver or API specific code.
- **Interactions** handle the low-level execution (e.g., `Click.on`, `Enter.theValue`) and are the *only* place where framework-specific code lives.
- **Questions** extract state from the application to be used in assertions. Do NOT put assertions directly inside Tasks or Page Objects.

## One More Thing
If the input is just a simple unit test for a pure logic function (no external interfaces), stop and inform the user that the Screenplay Pattern is designed for integration and end-to-end testing, not simple unit tests.

## How

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

## Validation
1. Verify that no Task contains direct calls to WebDriver (or other low-level API clients).
2. Verify that no Page Object or Interaction contains assertions.
