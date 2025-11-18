# 📘 SmartBudget — FUNCTIONS.md  
This document provides a full overview of **all functions**, **classes**, and **modules** included in the SmartBudget package.  
It serves as API documentation and supports code readability, maintainability, and grading requirements.

---

# 📁 Package Overview

SmartBudget consists of four major functional areas:

1. **entity/** – core data models (OOP classes)
2. **analysis/** – financial calculations and insight helpers
3. **core/** – controllers and menu-driven application logic
4. **io/** – data persistence and file utilities

Below is a detailed explanation of all modules and functions.

---

# 🧱 1. ENTITY MODULES (`smartbudget/entity/`)

## ## `base_record.py`
### **Class: RecordBase**
Parent class for both `Income` and `Expense`.  
Handles validation and shared behavior.

#### Methods
- **`__init__(self, name, amount)`**  
  Creates a base record and performs validation.

- **`_validate_name(self, name)`**  
  Ensures name is a string and does not exceed max length.

- **`_validate_amount(self, amount)`**  
  Ensures amount is numeric, non-negative, and below MAX_AMOUNT.

- **`show(self)`**  
  Returns formatted string representation of the record.

- **`to_dict(self)`**  
  Serializes the object into a dictionary for JSON saving.

---

## ## `constants.py`
### **Class: Limits**
Container class storing global constraints shared across entity models.

#### Attributes
- `MAX_AMOUNT` – maximum allowable monetary amount  
- `MAX_NAME_LEN` – maximum length for name strings  

---

## ## `transaction.py`
*(You will rename this file into two modules later)*  
Contains Income and Expense entity classes that inherit from `RecordBase`.

### **Class: Income**
Represents money coming in.

#### Methods
- **`__init__(name, amount, source)`** – stores validated positive amount  
- **`describe()`** – human-readable summary of the income  
- **`to_dict()`** – extends serialization with `"source"` and `"type": "Income"`

### **Class: Expense**
Represents money going out.

#### Methods
- **`__init__(name, amount, category)`** – stores amount as negative  
- **`describe()`** – readable expense description  
- **`to_dict()`** – extends serialization with `"category"` and `"type": "Expense"`

---

# 📊 2. ANALYSIS MODULES (`smartbudget/analysis/`)

## ## `summary.py`

### Functions
- **`total_income()`**  
  Returns the sum of all positive amounts.

- **`total_expenses()`**  
  Returns the sum of all negative amounts.

- **`budget_balance()`**  
  Net balance = total_income - abs(total_expenses).

---

## ## `insights.py`

### Functions
- **`_load_split()`**  
  Internal helper to load both income and expense lists.

- **`income_details()`**  
  Returns a list of formatted strings for each income.

- **`expense_details()`**  
  Returns a list of formatted strings for each expense.

---

# ⚙️ 3. CONTROLLER MODULES (`smartbudget/core/`)

These modules implement the *logic layer* of the application.

---

## ## `controller_records.py`
Handles adding and displaying financial records.

### Functions
- **`add_income()`**  
  Collects input → creates an Income object → appends to records → saves to JSON.

- **`add_expense()`**  
  Collects input → creates Expense object → appends → saves to JSON.

- **`show_summary()`**  
  Prints total income, total expenses, and balance.

- **`show_income_details()`**  
  Displays detailed descriptions of all income records.

- **`show_expense_details()`**  
  Displays detailed descriptions of all expense records.

---

## ## `controller_system.py`
Handles file saving, loading, listing, and deletion.

### Functions
- **`save_data()`**  
  Saves the current records.json data to a chosen backup file.

- **`load_data(incomes, expenses)`**  
  Reads from a JSON file and reconstructs Income/Expense objects.

- **`show_files()`**  
  Lists all user-created backup JSON files.

- **`delete_backup_file()`**  
  Deletes a backup file if it exists.

---

## ## `controller_menu.py`
Implements the command-line user interface.

### Functions
- **`print_menu()`**  
  Prints the SmartBudget main menu.

- **`run()`**  
  Main application loop.  
  Routes user input to appropriate controller functions.

---

# 💾 4. IO MODULES (`smartbudget/io/`)

## ## `json_io.py`
Responsible for saving/loading JSON files.

### Functions
- **`save_to_json(records, filename)`**  
  Writes a list of record dictionaries to the target file.

- **`append_to_json(records)`**  
  Appends new records to `records.json`.

- **`load_from_json(filename)`**  
  Loads JSON data and reconstructs Income/Expense objects.

---

## ## `file_utils.py`
General filesystem utilities.

### Functions
- **`file_exists(filename)`**  
  Checks if a file exists inside `/files`.

- **`list_files()`**  
  Returns a list of files inside `/files`.

- **`delete_file(filename)`**  
  Deletes the selected file if present.

---

# 🚀 5. MAIN PROGRAM (`main.py`)

### Function
- **`main()`**  
  Entry point. Calls `run()` from `controller_menu.py` to start the interactive program.

---

# 📘 Summary

SmartBudget provides:

- Clean and modular folder structure  
- Object-oriented record modeling  
- Feature-based controllers  
- JSON persistence  
- Command-line interaction  

This architecture is easy to extend and maintains excellent readability for course grading.

If you need UML diagrams, a setup.py file, or an auto-generated usage example, just ask!
