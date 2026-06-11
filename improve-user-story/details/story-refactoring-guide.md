# Story Refactoring Guide

When a new requirement, business rule, or edge case is discovered, existing User Stories must be updated. Refactoring a User Story is like refactoring code: you want to integrate the new behavior without breaking the existing specifications.

Follow these guidelines when using the `improve-user-story` skill.

## 1. Do Not Destroy Unaffected Scenarios
If a new edge case is discovered (e.g., "What if the user's credit card is expired?"), do not delete the existing "Happy Path" scenario. Instead, add a new scenario specifically to handle the edge case.

**Existing:**
```gherkin
Scenario: Successful payment
  Given the user has a valid credit card
  When they submit the payment
  Then the payment is processed
```

**New Addition:**
```gherkin
Scenario: Expired credit card
  Given the user has an expired credit card
  When they submit the payment
  Then the payment is rejected
  And they are asked to provide a new card
```

## 2. Refactor into Scenario Outlines
If the conversation introduces multiple new data variations for an existing rule, refactor the existing `Scenario` into a `Scenario Outline` with a Data Table, rather than copy-pasting the scenario multiple times.

**Before:**
```gherkin
Scenario: Free shipping for books
  Given the user buys a book
  When they checkout
  Then shipping is free
```

**After (Refactored for new categories):**
```gherkin
Scenario Outline: Free shipping categories
  Given the user buys an item in the <Category> category
  When they checkout
  Then shipping is <Shipping Cost>

  Examples:
    | Category    | Shipping Cost |
    | Book        | free          |
    | Electronics | $5.00         |
    | Clothing    | $5.00         |
```

## 3. Update the Story Statement if the Goal Changes
Sometimes a new requirement shifts the fundamental business value of the story. 

If the original story was:
`As a user, I want to reset my password, So that I can log in if I forget it.`

And the new requirement adds 2FA for security, the value might shift. Consider proposing the "In order to" format to highlight the new goal:
`In order to securely recover accounts without risking identity theft, As a user, I want to reset my password using 2FA.`

## 4. Document Ambiguity
If the conversation introduces a new concept but does not fully define it, add it to the `### Notes` or `### Open Questions` section of the User Story rather than guessing the Acceptance Criteria.
