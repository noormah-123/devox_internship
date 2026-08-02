from pathlib import Path
import pandas as pd

# Get the current project folder
base_path = Path(__file__).parent

# File paths
input_file = base_path / "data" / "messy_sales.csv"
output_file = base_path / "data" / "cleaned_sales.csv"
report_file = base_path / "summary_report.txt"

# Load dataset
try:
    df = pd.read_csv(input_file)
except FileNotFoundError:
    print(f"Error: File not found -> {input_file}")
    exit()

print("========== ORIGINAL DATASET ==========")
print(df)

# Remove duplicate rows
duplicates_removed = df.duplicated().sum()
df = df.drop_duplicates()

# Remove extra spaces from text columns
df["customer"] = df["customer"].astype(str).str.strip()
df["city"] = df["city"].astype(str).str.strip()

# Standardize text formatting
df["customer"] = df["customer"].str.title()
df["city"] = df["city"].replace("Nan", pd.NA)
df["city"] = df["city"].str.title()

# Convert sales column to numeric
# Invalid values become NaN
df["sales"] = pd.to_numeric(df["sales"], errors="coerce")

# Count missing values BEFORE cleaning
missing_before = df.isna().sum()

# Fill missing city values
df["city"] = df["city"].fillna("Unknown")

# Fill missing sales with average
average_sales = df["sales"].mean()
df["sales"] = df["sales"].fillna(average_sales)

# Round sales values
df["sales"] = df["sales"].round(2)

# Save cleaned dataset
df.to_csv(output_file, index=False)

# Create summary report
with open(report_file, "w") as report:
    report.write("DATA CLEANING SUMMARY\n")
    report.write("=========================\n\n")

    report.write(f"Original Rows          : {len(df) + duplicates_removed}\n")
    report.write(f"Rows After Cleaning    : {len(df)}\n")
    report.write(f"Duplicate Rows Removed : {duplicates_removed}\n\n")

    report.write("Missing Values Before Cleaning:\n")
    report.write(str(missing_before))
    report.write("\n\n")

    report.write(f"Average Sales Used : {average_sales:.2f}\n\n")

    report.write("Cleaning Operations Performed:\n")
    report.write("- Removed duplicate rows\n")
    report.write("- Removed extra spaces\n")
    report.write("- Standardized customer names\n")
    report.write("- Standardized city names\n")
    report.write("- Converted invalid sales values to numeric\n")
    report.write("- Filled missing city values with 'Unknown'\n")
    report.write("- Filled missing sales values using average\n")
    report.write("- Saved cleaned dataset\n")

# Display cleaned dataset
print("\n========== CLEANED DATASET ==========")
print(df)

print("\n=====================================")
print(" Data cleaning completed successfully!")
print("=====================================")

print(f"\nCleaned CSV saved at:\n{output_file}")
print(f"\nSummary Report saved at:\n{report_file}")