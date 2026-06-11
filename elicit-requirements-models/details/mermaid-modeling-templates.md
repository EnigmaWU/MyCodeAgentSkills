# Mermaid Modeling Templates

Use these Mermaid templates to visualize text requirements.

## 1. State Transition Diagram
*Use when an entity (like an Order, Ticket, or User) moves through different statuses.*

```mermaid
stateDiagram-v2
    [*] --> Draft : User creates item
    Draft --> Submitted : User clicks submit
    Submitted --> Approved : Manager approves
    Submitted --> Rejected : Manager rejects
    Rejected --> Draft : User edits item
    Approved --> [*]
    
    %% Gap Analysis Example: 
    %% Question: What happens if a User cancels the item while it is "Submitted"? Is there a transition to a "Canceled" state?
```

## 2. Activity / Flow Diagram
*Use to show a sequence of steps, decisions, and parallel tasks.*

```mermaid
graph TD
    Start([Start Checkout]) --> CheckCart{Is Cart Empty?}
    CheckCart -->|Yes| ShowError[Show Empty Cart Error]
    CheckCart -->|No| EnterShipping[Enter Shipping Info]
    EnterShipping --> ProcessPayment[Process Payment]
    
    ProcessPayment --> PaymentSuccess{Payment OK?}
    PaymentSuccess -->|Yes| CreateOrder[Create Order]
    PaymentSuccess -->|No| ShowPaymentError[Show Payment Error]
    
    CreateOrder --> End([End Checkout])
    
    %% Gap Analysis Example:
    %% Question: What happens after "ShowError" or "ShowPaymentError"? Do we route the user back to the cart, or do we end the process?
```

## 3. Context Diagram
*Use to show how the system interacts with external actors or APIs.*

```mermaid
graph LR
    User([Customer]) -->|Submits Order| System[E-Commerce System]
    System -->|Charges Card| PaymentAPI[(Payment Gateway)]
    System -->|Sends Confirmation| EmailAPI[(Email Provider)]
    Warehouse([Warehouse Worker]) -->|Fulfills Order| System
    
    %% Gap Analysis Example:
    %% Question: What happens if the PaymentAPI is unreachable? Does the E-Commerce System queue the order or reject it immediately?
```
