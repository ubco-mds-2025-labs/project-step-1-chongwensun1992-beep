"""
Record-related controller functions for SmartBudget.
Handles income, expense, and summary display.
"""
from smartbudget.entity.income import Income
from smartbudget.entity.expense import  Expense


from smartbudget.analysis.summary import total_income, total_expenses, budget_balance
from smartbudget.analysis.insights import income_details, expense_details,plot_expense_by_category
from smartbudget.io import append_to_json



incomes = []
expenses = []


def add_income():
    print("\n--- Add Income ---")
    name = input("Enter income name: ")
    amount = float(input("Enter amount: "))
    source = input("Enter source: ")

    inc = Income(name, amount, source)
    incomes.append(inc)
    append_to_json([inc])

    print("\n✔ Income added:", inc.describe(), "\n")


def add_expense():
    print("\n--- Add Expense ---")
    name = input("Enter expense name: ")
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")

    exp = Expense(name, amount, category)
    expenses.append(exp)
    append_to_json([exp])

    print("\n✔ Expense added:", exp.describe(), "\n")


def show_summary():
    print("\n=== Budget Summary ===")
    print("Total Income:", total_income())
    print("Total Expenses:", total_expenses())
    print("Balance:", budget_balance())
    print("=======================\n")


def show_income_details():
    print("\n=== Income Details ===")
    details = income_details()
    if not details:
        print("No incomes recorded.\n")
        return

    for d in details:
        print(" -", d)
    print()


def show_expense_details():
    print("\n=== Expense Details ===")
    details = expense_details()
    if not details:
        print("No expenses recorded.\n")
        return

    for d in details:
        print(" -", d)
    print()


def show_expense_plot():
    print("\n=== Expense Visualization ===")
    print("Generating chart...")
    plot_expense_by_category()
    print("\n✔ Chart displayed!\n")

def show_expense_plot():
    print("\n=== Expense Visualization ===")
    try:
        plot_expense_by_category()
        print("\n✔ Chart displayed!\n")
    except Exception as exc:
        print(f"\n✘ Failed to generate plot: {exc}\n")
