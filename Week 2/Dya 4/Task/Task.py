import pandas as pd

# Dataset 1: customers (lookup table)
customers = {
    "customer_id": [1, 2, 3, 4],
    "customer": ["Alice", "Bob", "Chris", "Dina"],
    "city": ["London", "Paris", "London", "Berlin"],
    "segment": ["Retail", "Retail", "Corporate", "Retail"],
}
df_customers = pd.DataFrame(customers)

# Dataset 2: orders (transactions)
orders = {
    "order_id": [1001, 1002, 1003, 1004, 1005],
    "customer_id": [1, 2, 2, 3, 99],        # 99 does not exist in customers (to show missing after merge)
    "category": ["Books", "Games", "Books", "Electronics", "Books"],
    "amount": [120, 60, 80, 200, 50],
    "discount": [0.00, 0.10, 0.05, 0.20, 0.00],
}
df_orders = pd.DataFrame(orders)

# Merge: attach customer info to each order
merged = df_orders.merge(df_customers, on="customer_id", how="left")

# Handle missing customer info (from customer_id not found)
merged["customer"] = merged["customer"].fillna("Unknown")
merged["city"] = merged["city"].fillna("Unknown")
merged["segment"] = merged["segment"].fillna("Unknown")

# Add revenue after discount
merged["revenue"] = merged["amount"] * (1 - merged["discount"])

print("=== Merged data ===")
print(merged, "\n")

# Summary 1: revenue + order count by city
city_summary = (
    merged.groupby("city")
          .agg(
              orders=("order_id", "count"),
              total_amount=("amount", "sum"),
              total_revenue=("revenue", "sum"),
              avg_discount=("discount", "mean"),
          )
          .sort_values("total_revenue", ascending=False)
)
print("=== City summary ===")
print(city_summary, "\n")

# Summary 2: top customers by revenue
customer_summary = (
    merged.groupby(["customer_id", "customer"])
          .agg(
              orders=("order_id", "count"),
              total_revenue=("revenue", "sum"),
          )
          .sort_values("total_revenue", ascending=False)
)
print("=== Customer summary ===")
print(customer_summary)