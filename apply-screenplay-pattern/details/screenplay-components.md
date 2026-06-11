# Screenplay Pattern Components

The Screenplay Pattern breaks test execution down into five distinct components.

## 1. Actors
**Who** is performing the action.
Actors represent the users (or external systems) interacting with your system. They are the core of the pattern.
* *Example:* `Actor tracy = Actor.named("Tracy");`

## 2. Abilities
**What** the actor can do.
Abilities give actors the power to interact with the system using specific tools (e.g., a web browser, a REST client).
* *Example:* `tracy.can(BrowseTheWeb.with(driver));`

## 3. Tasks
**What** the actor wants to achieve in business terms.
Tasks group lower-level interactions into reusable business actions. Tasks do *not* contain implementation details.
* *Example:* `tracy.attemptsTo(Login.usingCredentials("tracy@email.com", "password"));`

## 4. Interactions
**How** the actor interacts with the system.
Interactions are low-level actions like clicking, typing, or sending an HTTP request. This is the *only* layer that touches the underlying automation framework (like Selenium or Playwright).
* *Example:* `Click.on(LoginForm.SUBMIT_BUTTON)`

## 5. Questions
**What** the actor observes about the system state.
Questions query the system and return a value that can be asserted against. You never put assertions inside a Page Object; the Actor asks a Question and ensures the answer is correct.
* *Example:* `tracy.attemptsTo(Ensure.that(AccountBalance.value(), isEqualTo(500)));`

---

## Architectural Flow
```text
[Actor] --has--> [Abilities]
   |
   +--performs--> [Tasks]
                    |
                    +--composed of--> [Interactions] --use--> [Abilities]
                    |
                    +--answers--> [Questions] --use--> [Abilities]
```
