"""
Test file for SmartBudget package.
This script demonstrates how to use major features of the package.
Run it independently to validate functionality.
"""

from smartbudget.entity.transaction import Income, Expense
from smartbudget.analysis.summary import total_income, total_expenses, budget_balance
from smartbudget.analysis.insights import (
    expense_details,
    income_details,
    largest_expenses,
    largest_incomes,
)
from smartbudget.io import save_to_json, load_from_json, list_files, delete_file


print("=== TEST: Creating Records ===")

incomes = [
    Income("Salary", 5000, "Company A"),
    Income("Bonus", 1200, "Company A"),
]

expenses = [
    Expense("Rent", 1500, "Housing"),
    Expense("Groceries", 400, "Food"),
    Expense("Internet", 90, "Utilities"),
]

for i in incomes:
    print("Income:", i.describe())

for e in expenses:
    print("Expense:", e.describe())


print("\n=== TEST: Summary Calculations ===")
print("Total Income:", total_income(incomes))
print("Total Expenses:", total_expenses(expenses))
print("Balance:", budget_balance(incomes, expenses))


print("\n=== TEST: Details & Ranking ===")
print("Expense Details:")
for d in expense_details(expenses):
    print(" -", d)

print("Income Details:")
for d in income_details(incomes):
    print(" -", d)

print("Top 2 Expenses:")
for item in largest_expenses(expenses, n=2):
    print(" -", item.describe())

print("Top 2 Incomes:")
for item in largest_incomes(incomes, n=2):
    print(" -", item.describe())


print("\n=== TEST: JSON Save & Load ===")
test_filename = "test_data.json"

# Save
save_to_json(incomes + expenses, test_filename)
print(f"Saved to {test_filename}")

print("Files in directory:", list_files())

# Load
loaded = load_from_json(test_filename)
print("Loaded records:")
for r in loaded:
    print(" -", r.describe())

# Clean up
print("Deleting test file...", delete_file(test_filename))
print("Files now:", list_files())

print("\n=== ALL TESTS COMPLETED SUCCESSFULLY ===")