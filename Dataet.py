import csv
import os

# Step 1: Read CSV file

filename = "sales.csv"

with open(filename, "r", newline="") as file:
    reader = csv.DictReader(file)
    data = list(reader)

print("Original Dataset:")

for row in data:
    print(row)

# Step 2: Handle missing values

for row in data:

    for key in row:
        if row[key] is None or row[key].strip() == "":
            row[key] = "0" if key == "Revenue" else "Unknown"

# Step 3: Remove duplicate records

cleaned_data = []

for row in data:
    if row not in cleaned_data:
        cleaned_data.append(row)

# Step 4: Filter rows

filtered_data = []

for row in cleaned_data:
    if float(row["Revenue"]) > 40000:
        filtered_data.append(row)

# Step 5: Create new columns

for row in filtered_data:

    revenue = float(row["Revenue"])

    row["Bonus"] = revenue * 0.10

    if revenue >= 50000:
        row["Status"] = "High"
    else:
        row["Status"] = "Normal"

# Step 6: Display cleaned dataset

print("\nCleaned Dataset:")

for row in filtered_data:
    print(row)

# Step 7: Save cleaned dataset

fields = list(filtered_data[0].keys()) if filtered_data else [
    "Order Date", "Category", "Department",
    "Revenue", "Bonus", "Status"
]

with open("cleaned_data.csv", "w", newline="") as file:

    writer = csv.DictWriter(file, fieldnames=fields)

    writer.writeheader()
    writer.writerows(filtered_data)

print("\nCleaned dataset saved successfully!")