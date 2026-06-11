# Event Storming Legend

When conducting an Event Storming session or documenting its output, use the following vocabulary and conceptual "colors" to classify components. This structure ensures that behavior and intent are modeled correctly before writing code.

## 🟧 Domain Event (Orange)
* **What:** Something meaningful that happened in the domain.
* **Grammar:** Past tense verb.
* **Example:** `OrderPlaced`, `PaymentDeclined`, `AccountSuspended`.
* **Note:** Events are facts. They cannot be changed or deleted once they occur.

## 🟦 Command (Blue)
* **What:** A decision, intent, or request to do something. It triggers a Domain Event.
* **Grammar:** Imperative verb.
* **Example:** `Place Order`, `Retry Payment`, `Suspend Account`.
* **Note:** Commands can be rejected if business rules fail. Events cannot be rejected.

## 🟨 Actor / User (Yellow)
* **What:** A person or role who executes a Command.
* **Example:** `Customer`, `Admin`, `Fulfillment Worker`.

## 🟪 External System (Pink)
* **What:** A third-party system, legacy application, or external Bounded Context that triggers an event or receives an event.
* **Example:** `Stripe Payment Gateway`, `Legacy CRM`, `UPS Shipping API`.

## 🟨 Aggregate (Pale Yellow)
* **What:** The state machine or data entity that receives a Command, applies business rules, and emits a Domain Event.
* **Example:** `Order`, `PaymentTransaction`, `UserAccount`.
* **Note:** Aggregates are the transactional boundaries where consistency must be maintained.

## 🟪 Policy (Lilac)
* **What:** A reactive business rule that listens for a Domain Event and automatically triggers a new Command.
* **Grammar:** "Whenever [Event] happens, then [Command]".
* **Example:** "Whenever `PaymentDeclined` happens, trigger `SendFailureEmail`".

## 🟩 Read Model (Green)
* **What:** Data required by an Actor to make a decision and issue a Command.
* **Example:** `Available Inventory View`, `Account Balance Dashboard`.

---

## Standard Flow

The standard architectural flow to document in Design-Level Event Storming is:

**[Actor/Policy]** -> executes -> **[Command]** -> against -> **[Aggregate]** -> which validates and emits -> **[Domain Event]** -> which updates -> **[Read Model]** OR triggers -> **[Policy]**
