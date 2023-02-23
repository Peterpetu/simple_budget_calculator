import csv
import matplotlib.pyplot as plt

BUDGET_FILE = "budget.csv"

# Read budget data from file
budget_data = []
with open(BUDGET_FILE, "r") as f:
    reader = csv.reader(f)
    headings = next(reader)
    for i in range(5):
        try:
            row = next(reader)
        except StopIteration:
            break
        budget_data.append(row)

# Print headings and first 5 rows
print(", ".join(headings))
for row in budget_data:
    print(", ".join(row))

# Create bar chart
months = [row[0] for row in budget_data]
income = [float(row[-2]) for row in budget_data]
expenses = [sum(float(x) for x in row[1:-2]) for row in budget_data]
remaining = [float(row[-1]) for row in budget_data]

plt.bar(months, income, label="Income")
plt.bar(months, expenses, bottom=income, label="Expenses")
plt.plot(months, remaining, label="Remaining Budget")
plt.legend()
plt.xlabel("Month")
plt.ylabel("Amount ($)")
plt.title("Monthly Budget Summary")
plt.show()
