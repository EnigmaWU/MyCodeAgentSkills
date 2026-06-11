# Data Dictionary Format

Use this format to define data elements.

## Data Structures
Define complex objects by showing their composition.

* **Address** = StreetAddress1 + [StreetAddress2] + City + State + ZipCode
* **Order** = OrderID + CustomerID + OrderDate + 1:N{OrderLineItem} + OrderTotal

*(Note: Brackets `[ ]` indicate optional items. `1:N{ }` indicates a repeating group or array).*

## Primitive Data Elements
Use a markdown table to define the primitive fields.

| Element Name | Description | Data Type | Length | Allowed Values |
| :--- | :--- | :--- | :--- | :--- |
| `ZipCode` | Postal routing code. | String | 10 | 5 digits, or 5 digits + hyphen + 4 digits. |
| `OrderState` | Current status of the order. | Enum | N/A | Pending, Processing, Shipped, Delivered, Canceled |
| `Quantity` | Number of items purchased. | Integer | N/A | > 0 and <= 999 |
| `DiscountCode` | Promo code applied at checkout. | String | 15 | Alphanumeric, uppercase only |
| `IsGift` | Flag indicating gift wrap requested. | Boolean | 1 | True / False |

## Guidance for AI Agents
* Always look for constraints (e.g., "must be greater than 0") and place them in the **Allowed Values** column.
* If a length is not specified in the text but is logically constrained (e.g., standard US State abbreviations), use your domain knowledge to fill in `2`.
