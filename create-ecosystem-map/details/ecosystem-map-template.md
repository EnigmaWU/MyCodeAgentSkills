# Ecosystem Map Template

Use this Mermaid.js format to visualize the Ecosystem Map.

## Guidelines
- Use a distinct shape or color for the System Under Design (SUD).
- Use `([ ])` for human actors.
- Use `[( )]` for databases/external systems.
- Always label the arrows with the data being passed.

## Example: Customer Portal Ecosystem

```mermaid
graph TD
    %% Human Actors
    Customer([Customer])
    Support([Support Agent])
    
    %% System Under Design
    SUD{Customer Portal}
    
    %% External Systems
    Auth[(Identity Provider)]
    CRM[(Salesforce CRM)]
    Billing[(Stripe Billing)]
    
    %% Connections
    Customer -->|Logs in| SUD
    Customer -->|Views Invoices| SUD
    
    Support -->|Impersonates User| SUD
    
    SUD -->|Validates Token| Auth
    SUD -->|Fetches Profile Data| CRM
    SUD -->|Requests Invoice PDF| Billing
```

## Gap Analysis Example
After drawing the map, analyze the arrows:
- *"The SUD fetches profile data from the CRM, but does it ever push updates back to the CRM when the user edits their profile?"*
- *"We show the Customer logging in, but what system handles password resets?"*
