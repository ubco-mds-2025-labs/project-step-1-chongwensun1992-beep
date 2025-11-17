# SmartBudget – Function Documentation

This document provides a detailed explanation of all modules and functions included in the **SmartBudget** package. Functions are grouped based on their sub-packages and modules.

---

# 📦 1. `core` Sub-Package

The `core` package contains the foundational classes used to represent financial records. It demonstrates **inheritance**, which is required by the project.

---

## ## 1.1 `base_record.py`

### **Class: RecordBase(name, amount)**

The parent class for all income and expense records.

#### **Methods:**

* **show()**
  Returns a formatted string that displays the record's name and amount.

* **is_positive()**
  Returns `True` if the amount stored in the object is positive.

* **to_dict()**
  Serializes the object into a basic dictionary. Subclasses override this method to add more fields.

---

## ## 1.2 `transaction.py`

### **Class: Income(name, amount, source)**

Represents an income record. Inherits from `RecordBase`.

#### **Methods:**

* **yearly_income()**
  Returns 12 times the monthly income amount.

* **describe()**
  Returns a formatted string describing the income.

* **to_dict()**
  Serializes the income into a dictionary including name, amount, source, and type.

---

### **Class: Expense(name, amount, category)**

Represents a spending record. Inherits from `RecordBase`.

#### **Methods:**

* **yearly_cost()**
  Returns 12 times the expense amount.

* **describe()**
  Returns a readable summary of the expense.

* **to_dict()**
  Serializes the expense into a dictionary including name, amount, category, and type.

---

# 📊 2. `analysis` Sub-Package

This sub-package provides summary statistics and financial insights to help users analyze their household budget.

---

## ## 2.1 `summary.py`

### **Functions:**

* **total_income(incomes)**
  Returns the total sum of income amounts.

* **total_expenses(expenses)**
  Returns the total sum of all expenses.

* **budget_balance(incomes, expenses)**
  Computes the net budget balance (total income + total expenses).

---

## ## 2.2 `insights.py`

### **Functions:**

* **expense_details(expenses)**
  Returns a list of formatted descriptions for all recorded expenses.

* **income_details(incomes)**
  Returns a list of formatted descriptions for all recorded incomes.

* **largest_expenses(expenses, n=3)**
  Returns the top **N** largest expenses sorted by absolute value.

* **largest_incomes(incomes, n=3)**
  Returns the top **N** largest incomes in descending order.

* **print_records(title, records)**
  Utility function that prints a block of records in a clean, readable format.

---

# 📁 3. `io` Sub-Package

This sub-package is responsible for saving and loading data, as well as file management.

---

## ## 3.1 `json_io.py`

### **Functions:**

* **save_to_json(records, filename)**
  Saves a list of `Income` and `Expense` objects into a JSON file. Automatically writes into the `files/` directory.

* **load_from_json(filename)**
  Loads a JSON file and reconstructs `Income` and `Expense` objects.

---

## ## 3.2 `file_utils.py`

### **Functions:**

* **file_exists(filename)**
  Checks whether a file exists inside the `files/` directory.

* **delete_file(filename)**
  Removes a specified file from the `files/` directory.

* **list_files()**
  Returns a list of all files stored in the `files/` directory.

---

# 🖥 4. Main Program (`main.py`)

The main program serves as the user interface and connects all package functions.

### **Key Functions:**

* **add_income()** – Adds a new income record.
* **add_expense()** – Adds a new expense record.
* **show_summary()** – Displays total income, total expenses, and balance.
* **show_expense_details()** – Prints all expense records.
* **show_income_details()** – Prints all income records.
* **show_top_expenses()** – Displays top 3 expense records.
* **show_top_incomes()** – Displays top 3 income records.
* **save_data()** – Saves data into JSON.
* **load_data()** – Loads data from JSON.
* **show_files()** – Lists JSON files.
* **remove_file()** – Deletes a file.

---

# ✔ Summary

SmartBudget provides:

* A complete class hierarchy for financial records.
* Summary and insight analysis functions.
* JSON-based persistence.
* File management utilities.
* A menu-driven main application.

This fulfills all requirements for the project and demonstrates professional package design.
