# Feature Tree Examples

Use this Mermaid.js Mindmap format to visualize the Feature Tree.

## Example: E-Commerce System

```mermaid
mindmap
  root((E-Commerce System))
    L1_Account(Account Management)
      L2_Profile(User Profile)
        L3_Edit(Edit Info)
        L3_Password(Change Password)
      L2_History(Order History)
        L3_View(View Past Orders)
        L3_Track(Track Shipment)
    L1_Shopping(Shopping)
      L2_Catalog(Product Catalog)
        L3_Search(Search)
        L3_Filter(Filter)
      L2_Cart(Shopping Cart)
        L3_Add(Add Item)
        L3_Remove(Remove Item)
    L1_Checkout(Checkout)
      L2_Payment(Payment Processing)
        L3_Card(Credit Card)
        L3_PayPal(PayPal)
```

## Gap Analysis Example
Looking at the tree above, an agent might ask:
- *"Under `L1_Account -> L2_Profile`, we have `Edit Info` and `Change Password`. Do we need a `Delete Account` feature?"*
- *"Under `L1_Shopping -> L2_Cart`, we have `Add` and `Remove`. Do we need an `Update Quantity` feature?"*
