"""
System controller for SmartBudget.
Handles saving, loading, listing, and deleting backup data files.
"""


from smartbudget.entity.transaction import Income,Expense
from smartbudget.io import (
    save_to_json, load_from_json,
    file_exists, list_files, delete_file
)


def save_data():
    filename = input("Enter filename to save (e.g., backup.json): ").strip()

    if filename == "records.json":
        print("❌ Cannot save to system file.\n")
        return

    if file_exists(filename):
        overwrite = input("⚠ File exists. Overwrite? (y/n): ").lower()
        if overwrite != "y":
            print("❌ Save cancelled.\n")
            return

    data = load_from_json("records.json")
    save_to_json(data, filename)

    print(f"✔ Records saved to {filename}\n")


def load_data(incomes, expenses):
    filename = input("Enter filename to load: ").strip()

    if not file_exists(filename):
        print("❌ File not found.\n")
        return

    loaded_records = load_from_json(filename)

    for r in loaded_records:
        if isinstance(r, Income):
            incomes.append(r)
        elif isinstance(r, Expense):
            expenses.append(r)

    print(f"\n✔ Loaded {len(loaded_records)} records from '{filename}'\n")
    for rec in loaded_records:
        print(" -", rec.describe())
    print()


def show_files():
    print("\nFiles in 'files/' directory:")
    files = [f for f in list_files() if f != "records.json"]

    if not files:
        print(" (No user files found)")
    else:
        for f in files:
            print(" -", f)
    print()


def delete_backup_file():
    filename = input("Enter filename to delete: ").strip()

    if filename == "records.json":
        print("❌ Cannot delete system file.\n")
        return

    if delete_file(filename):
        print(f"✔ Deleted '{filename}'\n")
    else:
        print("❌ File not found.\n")
