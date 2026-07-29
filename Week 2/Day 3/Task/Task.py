from pathlib import Path
import pandas as pd

# TASK 1: Load the dataset
csv_path = Path(__file__).parent.parent / "Data" / "sales.csv"
df = pd.read_csv(csv_path)

print("=== Loaded data (first 5 rows) ===")
print(df.head(), "\n")

print("=== Missing values per column ===")
print(df.isna().sum(), "\n")

# TASK 2: Filter rows
# Example A: only London orders
london = df[df["city"] == "London"]
print("=== London orders ===")
print(london, "\n")

# Example B: Books with amount > 80
books_over_80 = df[(df["category"] == "Books") & (df["amount"] > 80)]
print("=== Books with amount > 80 ===")
print(books_over_80, "\n")

# TASK 3: Handle missing values
df2 = df.copy()
df2["amount"] = df2["amount"].fillna(df2["amount"].median())  # fill amount with median
df2["discount"] = df2["discount"].fillna(0)                   # fill discount with 0
df2["city"] = df2["city"].fillna("Unknown")                   # fill city with "Unknown"

print("=== Missing values AFTER filling ===")
print(df2.isna().sum(), "\n")

# TASK 4: Group by a column
# Total, count, and average amount per city
city_summary = df2.groupby("city")["amount"].agg(["count", "sum", "mean"]).sort_values("sum", ascending=False)
print("=== City summary (count / sum / mean of amount) ===")
print(city_summary, "\n")

# Average amount per category
cat_mean = df2.groupby("category")["amount"].mean()
print("=== Average amount per category ===")
print(cat_mean)