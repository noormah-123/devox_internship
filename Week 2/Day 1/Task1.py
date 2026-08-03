import csv
import json

with open("data.csv", "r") as file:
    reader = csv.DictReader(file)
    csv_data = list(reader)

with open("data.json", "r") as file:
    json_data = json.load(file)

filtered_csv = []
for row in csv_data:
    if int(row["age"]) > 30 and row["city"] == "Chicago":
        filtered_csv.append(row)

filtered_json = []
for row in json_data:
    if row["age"] > 30 and row["city"] == "Chicago":
        filtered_json.append(row)

if filtered_csv:
    with open("filtered_from_csv.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=filtered_csv[0].keys())
        writer.writeheader()
        writer.writerows(filtered_csv)

with open("filtered_from_json.json", "w") as file:
    json.dump(filtered_json, file, indent=4)

print(" Task Completed Successfully!")