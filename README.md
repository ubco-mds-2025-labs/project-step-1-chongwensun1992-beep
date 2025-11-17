# SmartBudget Package Documentation

SmartBudget is a modular Python package designed to manage household budgets. It provides functionality to record incomes and expenses, analyze financial data, and save/load records using JSON files. The package also includes utility functions for managing saved data files.

---

## 📁 Project Structure

```
smartbudget_project/
│
├── main.py                 # Main program (menu-driven interface)
├── files/                  # JSON storage directory
│
├── smartbudget/
│   ├── __init__.py         # Package initializer
│   │
│   ├── core/               # Core financial record classes
│   │   ├── __init__.py
│   │   ├── base_record.py
│   │   └── transaction.py
│   │
│   ├── analysis/           # Summary and insights analysis
│   │   ├── __init__.py
│   │   ├── summary.py
│   │   └── insights.py
│   │
│   └── io/                 # Input/Output modules
│       ├── __init__.py
│       ├── json_io.py
│       └── file_utils.py
│
└── tests/                  # (Optional) Test scripts
```

---

## ✨ Features Overview

### **Income & Expense Management**

* Add income with name, amount, and source
* Add expenses with name, amount, and category
* Store these as structured objects using class inheritance

### **Financial Analysis**

From `analysis/summary.py`:

* `total_income(incomes)` – compute total income
* `total_expenses(expenses)` – compute total expenses
* `budget_balance(incomes, expenses)` – calculate net balance

From `analysis/insights.py`:

* `expense_details(expenses)` – list all expense descriptions
* `income_details(incomes)` – list all income descriptions
* `largest_expenses(expenses, n)` – return top N spending items
* `largest_incomes(incomes, n)` – return top N income items

### **Data Saving & Loading (JSON)**

`json_io.py` provides:

* `save_to_json(records, filename)`
* `load_from_json(filename)` – fully restores Income/Expense objects

### **File Utilities**

`file_utils.py` includes:

* `file_exists(filename)`
* `delete_file(filename)`
* `list_files()` (only lists files inside `files/` directory)

---

## 🧠 How the Core Classes Work

### **RecordBase (abstract parent class)**

Defines shared attributes:

```text
name
amount
```

And base methods:

```text
def show()
def is_positive()
def to_dict()
```

### **Income & Expense Classes**

Both inherit from `RecordBase`.

#### Income:

```text
Income(name, amount, source)
```

Stores positive amount.

#### Expense:

```text
Expense(name, amount, category)
```

Stores amount as negative internally for easier calculations.

Both provide:

```text
def describe()
def to_dict()  # Saves category/source and type
```

---

## 🖥 Running the Application

Execute:

```bash
python main.py
```

You will see an interactive menu:

```
1. Add Income
2. Add Expense
3. Show Summary
4. Show Expense Details
5. Show Income Details
6. Show Top 3 Expenses
7. Show Top 3 Incomes
8. Save Records to JSON
9. Load Records from JSON
10. List Files
11. Delete File
0. Exit
```

---

## 📦 JSON Storage

All JSON files are automatically stored inside the `files/` directory.

### Example JSON structure:

```json
[
    {
        "name": "Salary",
        "amount": 5000,
        "source": "CompanyA",
        "type": "Income"
    },
    {
        "name": "Rent",
        "amount": -1200,
        "category": "Housing",
        "type": "Expense"
    }
]
```

---

## 🧪 Testing

Recommended tests (not included but suggested):

* Test adding incomes/expenses
* Test saving/loading JSON
* Test file utilities
* Test analysis functions

---

## 📘 Summary

SmartBudget is a well-structured, multi-module Python package demonstrating:

* OOP with inheritance
* Package & subpackage organization
* JSON serialization/deserialization
* File system utilities
* Financial data analysis
* A full interactive console application

Perfect for course projects and real-world budgeting tools.

---

