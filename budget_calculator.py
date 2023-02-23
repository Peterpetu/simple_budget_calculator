import csv
from datetime import datetime

BUDGET_FILE = "budget.csv"

# Read budget data from file
budget = {}
try:
    with open(BUDGET_FILE, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            budget[row["month"]] = {category: float(amount) for category, amount in row.items() if category != "month"}
except FileNotFoundError:
    pass

# Get current month and year
now = datetime.now()
month_year = now.strftime("%B %Y")

# Get total income
total_income = float(input("Enter your total monthly income: "))

# Get budget amounts for each category
new_budget = {}
for i in range(10):
    category = input("Add budget category (or leave blank to finish): ")
    if not category:
        break
    amount = float(input("Enter budget amount for {}: ".format(category)))
    new_budget[category] = amount

# Add new budget data to existing budget data
if month_year in budget:
    budget[month_year].update(new_budget)
else:
    budget[month_year] = new_budget

# Calculate total expenses
total_expenses = sum(budget[month_year].values())

# Calculate remaining budget
remaining_budget = total_income - total_expenses

# Print budget summary
print("Total income: ${:.2f}".format(total_income))
print("Budget:")
for category, amount in budget[month_year].items():
    print("- {}: ${:.2f}".format(category, amount))
print("Total expenses: ${:.2f}".format(total_expenses))
print("Remaining budget: ${:.2f}".format(remaining_budget))

# Write budget data to file
with open(BUDGET_FILE, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["month"] + list(new_budget.keys()) + ["total_income", "remaining_budget"])
    for month, budget_data in budget.items():
        row = [month] + [budget_data.get(category, "") for category in new_budget.keys()] + [total_income, total_income - sum(budget_data.values())]
        writer.writerow(row)