# OOPSI Framework Template

Use this format to deconstruct a workflow using the OOPSI model.

## 1. Outcome
*What is the high-level business goal?*

**Example:**
* Book a flight using Frequent Flyer points.

## 2. Outputs
*What tangible artifacts, messages, or state changes prove the outcome was achieved?*

**Example:**
* A new ticket is issued.
* A "Ticket Purchase" message is published to the message broker.
* A confirmation email is sent to the customer.
* The Frequent Flyer's point balance is updated.
* Error message: "Sorry, you don't have enough points for this flight."

## 3. Process
*What high-level steps lead to these outputs?*

**Example:**
1. Search flights.
2. Select eligible flight.
3. Confirm seat availability.
4. Confirm purchase using points.

## 4. Scenarios
*What are the variations, edge cases, and business rules?*

**Example:**
* The one where Fred can book his flight successfully.
* The one where Fred has insufficient points.
* The one where the flight has no more eligible seats.
* [RULE] Flights can be purchased at a rate of 10 Frequent Flyer points per dollar.

## 5. Inputs
*What specific data is needed to execute these scenarios?*

**Example:**

| Point Balance | Flight | Cost | Available FF Seats | Purchase Successful | Cost in Points | New Point Balance |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 5,000 | London to Paris | $450 | Yes | Yes | 4,500 | 500 |
| 5,000 | London to Athens | $650 | Yes | No | N/A | 5,000 |
| 5,000 | London to Paris | $450 | No | No | N/A | 5,000 |
