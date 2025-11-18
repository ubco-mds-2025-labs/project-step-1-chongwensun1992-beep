"""
User interface: menu + main loop for SmartBudget.
This module only contains two methods: print_menu() and run().
"""

from smartbudget.core import controller_records as rec
from smartbudget.core import controller_system as sys


def print_menu():
    print("====================================")
    print("       SmartBudget Main Menu        ")
    print("====================================")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. Show Summary")
    print("4. Show Expense Details")
    print("5. Show Income Details")
    print("6. Backup Records to JSON")
    print("7. List Backup Files")
    print("8. Delete File")
    print("0. Exit")
    print("====================================")


def run():
    """Main loop: routes menu choices to controller functions."""
    while True:
        print_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            rec.add_income()
        elif choice == "2":
            rec.add_expense()
        elif choice == "3":
            rec.show_summary()
        elif choice == "4":
            rec.show_expense_details()
        elif choice == "5":
            rec.show_income_details()
        elif choice == "6":
            sys.save_data()
        elif choice == "7":
            sys.show_files()
        elif choice == "8":
            sys.delete_backup_file()
        elif choice == "0":
            print("\nExiting SmartBudget. Goodbye!\n")
            break
        else:
            print("\n❌ Invalid choice. Try again.\n")
