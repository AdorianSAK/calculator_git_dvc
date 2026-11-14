import argparse
import csv
import random
from pathlib import Path
from calculator import sum, substract, multiply, divide

parser = argparse.ArgumentParser()
parser.add_argument("--n", type=int, required=True)
parser.add_argument("--seed", type=int, default=42)
args = parser.parse_args()

random.seed(args.seed)
Path("data").mkdir(exist_ok=True)

operations = {
    "sum": sum,
    "substract": substract,
    "multiply": multiply,
    "divide": divide
}

with open("data/operations.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["id", "operation", "a", "b", "result"])

    for i in range(args.n):
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        name = random.choice(list(operations))
        result = operations[name](a, b)
        writer.writerow([i + 1, name, a, b, result])

print(f"Dataset generado: {args.n} registros")
