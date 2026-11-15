import csv
from collections import defaultdict
from pathlib import Path

statistics = defaultdict(list)

with open("data/operations.csv", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        operation = row["operation"]
        result = float(row["result"])
        statistics[operation].append(result)

Path("results").mkdir(parents=True, exist_ok=True)

with open("results/brief.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["operation", "quantity", "average"])

    for operation, values in sorted(statistics.items()):
        quantity = len(values) 
        average = sum(values) / quantity
        writer.writerow([operation, quantity, average])

print ("Brief generated correctly")
