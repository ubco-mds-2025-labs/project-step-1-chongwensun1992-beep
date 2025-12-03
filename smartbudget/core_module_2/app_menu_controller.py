"""
SmartBudget CLI Application Interface
-------------------------------------

This module implements the USER INTERFACE layer of the SmartBudget system.

Responsibilities:
    • Render the text-based main menu
    • Provide the main application loop (`run`)
    • Route user commands to the appropriate controller modules

Architecture Role
-----------------
This module serves as the *application front controller*:

    UI Layer (this module)
        → delegates to →
            - BudgetRecordController (record operations: income/expense)
            - FileIoDataStorageController (backup, load, delete, reset)
        → which depend on →
            - entity models (Income, Expense)
            - analysis modules (summary, insights, charts)
            - file I/O utilities (JSON persistence)

This module contains:
    • ZERO business logic
    • ZERO data storage logic
    • ONLY menu printing + routing user choices

Functions
---------
print_menu() : Displays the SmartBudget main menu.
run()        : Starts the CLI loop and listens for user input.
"""

# ------------------ Imports ------------------ #

from smartbudget.core_module_2 import budget_record_controller as rec
from smartbudget.core_module_2 import file_io_data_controller as sys


# ------------------ UI Menu ------------------ #

def print_menu():
    """Displays the SmartBudget main menu."""
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
    print("8. Delete Backup File")
    print("9. Reset Records")
    print("10. Show Expense Chart")
    print("0. Exit")
    print("====================================")


# ------------------ Main Application Loop ------------------ #

def run():
    """
    Main loop for the SmartBudget CLI application.

    Continuously prints the menu, reads user input,
    and delegates actions to the appropriate controller.
    """
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
        elif choice == "9":
            sys.clear_data()
        elif choice == "10":
            rec.show_expense_plot()
        elif choice == "0":
            print("\nExiting SmartBudget. Goodbye!\n")
            break
        else:
            print("\n❌ Invalid choice. Try again.\n")


