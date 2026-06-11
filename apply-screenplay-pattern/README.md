# apply-screenplay-pattern

## Overview
This skill guides the agent to design and implement automated tests using the **Screenplay Pattern**, an advanced architectural pattern for test automation. Traditional Page Objects become brittle and bloated at scale, mixing test execution logic with page locators. The Screenplay Pattern resolves this by modeling tests from the perspective of an Actor interacting with the system to accomplish a Task.

## Usage
Trigger this skill when refactoring an existing automated test suite (like Selenium WebDriver, Cypress, or Playwright) or when defining the architecture for a new set of Cucumber step definitions.

```markdown
Use the `apply-screenplay-pattern` skill to refactor these Selenium Page Objects into Actors and Tasks.
```

## Structure
- [SKILL.md](./SKILL.md): The core workflow for identifying the Actors, Tasks, Interactions, and Questions for a test scenario.
- [details/screenplay-components.md](./details/screenplay-components.md): An overview of the 5 core elements of the Screenplay Pattern.
