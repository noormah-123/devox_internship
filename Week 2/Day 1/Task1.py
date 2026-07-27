import csv
import json

# -------- READ CSV --------
with open("data.csv", "r") as file:
    reader = csv.DictReader(file)
    csv_data = list(reader)

# -------- READ JSON --------
with open("data.json", "r") as file:
    json_data = json.load(file)

# -------- FILTER DATA --------
filtered_csv = []
for row in csv_data:
    if int(row["age"]) > 30 and row["city"] == "Chicago":
        filtered_csv.append(row)

filtered_json = []
for row in json_data:
    if row["age"] > 30 and row["city"] == "Chicago":
        filtered_json.append(row)

# -------- WRITE FILTERED CSV --------
if filtered_csv:
    with open("filtered_from_csv.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=filtered_csv[0].keys())
        writer.writeheader()
        writer.writerows(filtered_csv)

# -------- WRITE FILTERED JSON --------
with open("filtered_from_json.json", "w") as file:
    json.dump(filtered_json, file, indent=4)

print("✅ Task Completed Successfully!")