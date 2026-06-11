# Business Rules Taxonomy

Use this taxonomy to classify extracted Business Rules.

## 1. Facts
Statements that are true about the business at a specified time. They often describe associations or relationships.
* **Example:** "Every order has a shipping charge."
* **Example:** "A standard work week is 40 hours."

## 2. Constraints
Statements that restrict the actions that the system or its users are allowed to perform. Words like *must*, *must not*, *may not*, and *only* indicate constraints.
* **Example:** "A borrower may not have more than 5 books checked out at one time."
* **Example:** "Passwords must be at least 12 characters long."

## 3. Action Enablers
Statements that trigger an activity under specific conditions. They take the form of "If <condition> is true, then <action>."
* **Example:** "If the inventory level falls below the reorder point, then generate a purchase order."
* **Example:** "If the account is 30 days past due, assess a $15 late fee."

## 4. Inferences
Statements that derive a new fact from existing facts. They take the form of "If <condition> is true, then <fact>."
* **Example:** "If a customer has placed more than 10 orders in a year, they are considered a VIP."
* **Example:** "If the shipping address is a PO Box, then express delivery is not available."

## 5. Computations
Specific formulas or mathematical algorithms used to calculate a value.
* **Example:** `Total Cost = (Item Price * Quantity) + Shipping - Discount`
* **Example:** `Sales Tax = Subtotal * 0.0825 (for Texas residents)`
