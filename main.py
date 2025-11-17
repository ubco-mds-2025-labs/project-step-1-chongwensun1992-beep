"""
Main program for SmartBudget.
Provides a menu interface for adding, analyzing, saving, loading, and managing files.
"""

from smartbudget.core.transaction import Expense, Income
from smartbudget.analysis.summary import total_income, total_expenses, budget_balance
from smartbudget.analysis.insights import (
    expense_details,
    largest_expenses,
    income_details,
    largest_incomes,
)
from smartbudget.io import (
    save_to_json,
    load_from_json,
    file_exists,
    delete_file,
    list_files,
)

# Global storage
incomes = []
expenses = []


def add_income():
    print("\n--- Add Income ---")
    name = input("Enter income name: ")
    amount = float(input("Enter amount: "))
    source = input("Enter source: ")

    inc = Income(name, amount, source)
    incomes.append(inc)
    print("\n✔ Income added:", inc.describe(), "\n")


def add_expense():
    print("\n--- Add Expense ---")
    name = input("Enter expense name: ")
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")

    exp = Expense(name, amount, category)
    expenses.append(exp)
    print("\n✔ Expense added:", exp.describe(), "\n")


def show_summary():
    print("\n=== Budget Summary ===")
    print("Total Income:", total_income(incomes))
    print("Total Expenses:", total_expenses(expenses))
    print("Balance:", budget_balance(incomes, expenses))
    print("=======================\n")


# ============================
# New Feature Calls
# ============================

def show_expense_details():
    print("\n=== Expense Details ===")
    details = expense_details(expenses)
    if not details:
        print("No expenses recorded.\n")
        return
    for d in details:
        print(" -", d)
    print()


def show_income_details():
    print("\n=== Income Details ===")
    details = income_details(incomes)
    if not details:
        print("No incomes recorded.\n")
        return
    for d in details:
        print(" -", d)
    print()


def show_top_expenses():
    print("\n=== Top 3 Expenses ===")
    top3 = largest_expenses(expenses, n=3)
    if not top3:
        print("No expenses recorded.\n")
        return
    for e in top3:
        print(" -", e.describe())
    print()


def show_top_incomes():
    print("\n=== Top 3 Incomes ===")
    top3 = largest_incomes(incomes, n=3)
    if not top3:
        print("No incomes recorded.\n")
        return
    for inc in top3:
        print(" -", inc.describe())
    print()


# ============================
# Save / Load / File Mgmt
# ============================

def save_data():
    filename = input("Enter filename to save (e.g., data.json): ")

    if file_exists(filename):
        overwrite = input("⚠ File exists. Overwrite? (y/n): ").lower()
        if overwrite != "y":
            print("❌ Save cancelled.\n")
            return

    save_to_json(incomes + expenses, filename)
    print(f"✔ Records saved to {filename}\n")


def load_data():
    filename = input("Enter filename to load: ")

    if not file_exists(filename):
        print("❌ File not found.\n")
        return

    loaded_records = load_from_json(filename)

    for r in loaded_records:
        if isinstance(r, Income):
            incomes.append(r)
        elif isinstance(r, Expense):
            expenses.append(r)

    print(f"\n✔ Loaded {len(loaded_records)} records from {filename}\n")
    for rec in loaded_records:
        print(" -", rec.describe())
    print()


def show_files():
    print("\nFiles in 'files/' directory:")
    files = list_files()
    if not files:
        print(" (No files found)")
    else:
        for f in files:
            print(" -", f)
    print()


def remove_file():
    filename = input("Enter filename to delete (inside files/): ")
    if delete_file(filename):
        print(f"✔ File '{filename}' deleted from files/\n")
    else:
        print("❌ File not found.\n")


def print_menu():
    print("====================================")
    print("       SmartBudget Main Menu        ")
    print("====================================")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. Show Summary")
    print("4. Show Expense Details")
    print("5. Show Income Details")
    print("6. Show Top 3 Expenses")
    print("7. Show Top 3 Incomes")
    print("8. Save Records to JSON")
    print("9. Load Records from JSON")
    print("10. List Files")
    print("11. Delete File")
    print("0. Exit")
    print("====================================")


def main():
    while True:
        print_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_income()
        elif choice == "2":
            add_expense()
        elif choice == "3":
            show_summary()
        elif choice == "4":
            show_expense_details()
        elif choice == "5":
            show_income_details()
        elif choice == "6":
            show_top_expenses()
        elif choice == "7":
            show_top_incomes()
        elif choice == "8":
            save_data()
        elif choice == "9":
            load_data()
        elif choice == "10":
            show_files()
        elif choice == "11":
            remove_file()
        elif choice == "0":
            print("\nExiting SmartBudget. Goodbye!\n")
            break
        else:
            print("\n❌ Invalid choice. Try again.\n")


if __name__ == "__main__":
    main()
