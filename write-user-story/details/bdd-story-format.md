# BDD User Story Format

Use this format when generating or refining User Stories to ensure they are testable, business-focused, and unambiguous.

## Primary Story Format

By default, use the standard Agile format:

**As a** <role / persona>
**I want** <capability / feature>
**So that** <business value / outcome>

**Example:**
*As a* Frequent Flyer member
*I want* to be able to renew my membership online
*So that* I renew my membership more easily

## Advisory Story Format

If the business goal is getting lost or seems disconnected from the feature, you can suggest the "Value-First" format favored by BDD practitioners:

**In order to** <achieve a business goal>
**As a** <stakeholder>
**I want** <to be able to do something>

**Example:**
*In order to* reduce lost sales from lapsing memberships
*As a* Flying High sales manager
*I want* members to be able to renew their membership online

---

## BDD Executable Specifications (Acceptance Criteria)

Acceptance Criteria MUST be written as executable scenarios using the **Given / When / Then** format.

### 1. The Scenario Title
The title should summarize what is special about this example in a short, declarative sentence. Do not include the expected outcome in the title.
* **Good:** `Scenario: Flights within Europe earn 100 points`
* **Bad:** `Scenario: Check that flights within Europe earn points`

### 2. The Given Step (Preconditions)
Describes the initial state or context. Only include preconditions directly related to the scenario.
* **Example:** `Given Tara is a registered Frequent Flyer member`

### 3. The When Step (Action)
Describes the principal action or event you want to test.
* **Example:** `When she searches for one-way flights from London to New York in Economy`

### 4. The Then Step (Outcomes)
Compares the observed outcome or state of the system with what you expect. It must tie back to the business value.
* **Example:** `Then she should be informed that her booking was successful`

### 5. And / But
Use `And` and `But` to chain multiple steps together. Do NOT put multiple actions or assertions into a single Given, When, or Then step.

### 6. Using Tables
For scenarios with multiple variables or datasets, use Data Tables to prevent duplication and make the scenario concise.

**Example:**
```gherkin
Scenario Outline: Travelers earn points depending on the points schedule
  Given Stacy is a Standard Frequent Flyer member
  When she flies from <From> to <To> in <Cabin> class
  Then she should earn <Points Earned> points

  Examples:
    | From   | To          | Cabin    | Points Earned |
    | London | New York    | Economy  | 550           |
    | London | New York    | Business | 800           |
    | London | New York    | First    | 1650          |
```
