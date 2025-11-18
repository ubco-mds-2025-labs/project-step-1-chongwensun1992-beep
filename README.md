# 📦 SmartBudget — Python Household Budgeting Package

SmartBudget is a modular Python package designed to record incomes and expenses, perform budget analysis, and save/load financial records from JSON files.  
It demonstrates clean software architecture using **functional modules**, **class inheritance**, and **package organization** suitable for course projects or real-world use.

---

# 📁 Project Structure

```
project/
│
├── files/
│   └── records.json
│
├── smartbudget/
│   ├── __init__.py
│   │
│   ├── analysis/
│   │   ├── __init__.py
│   │   ├── insights.py
│   │   └── summary.py
│   │
│   ├── core/
│   │   ├── __init__.py
│   │   ├── controller_menu.py
│   │   ├── controller_records.py
│   │   └── controller_system.py
│   │
│   ├── entity/
│   │   ├── __init__.py
│   │   ├── base_record.py
│   │   ├── constants.py
│   │   └── transaction.py
│   │
│   ├── io/
│   │   ├── __init__.py
│   │   ├── json_io.py
│   │   └── file_utils.py
│
├── main.py
├── FUNCTIONS.md
└── README.md
```

---

# ✨ Features Overview

## ✅ 1. **Entity Models (entity/)**

### `RecordBase`
Provides:

- validation for name   
- shared data fields  
- `to_dict()` serialization  
- common behavior across records  

### `Income` / `Expense`
Both inherit from `RecordBase`:

- `Income(name, amount, source)`
- `Expense(name, amount, category)`  
  (stored as negative)

They implement:

- `describe()`
- `to_dict()` (includes category/source)

---

## 🎯 2. **Controllers (core/)**

SmartBudget uses **feature-based modular separation**:

### `controller_records.py`
Handles:

- adding income  
- adding expense  
- displaying budget summary  
- showing detailed records  

### `controller_system.py`
Handles:

- saving data to JSON  
- loading JSON  
- listing available files  
- deleting files  

### `controller_menu.py`
Contains:

- printed menu UI  
- `run()` main loop  
- routing user choices to controllers  

---

## 📊 3. Analysis Tools (analysis/)

### `summary.py`
- `total_income()`
- `total_expenses()`
- `budget_balance()`

### `insights.py`
- `_load_split()`
- `income_details()`
- `expense_details()`

---

## 💾 4. JSON IO (io/)

### `json_io.py`
- serialize Python objects to JSON  
- deserialize JSON data back into Income/Expense objects  
- `save_to_json()`
- `load_from_json()`
- `append_to_json()`
- `clear_json()`
### `file_utils.py`
- `file_exists()`  
- `list_files()`  
- `delete_file()`  

---

# 🚀 Running SmartBudget

Use:

```bash
python main.py
```

You will see:

```
1. Add Income
2. Add Expense
3. Show Summary
4. Show Expense Details
5. Show Income Details
6. Backup Records to JSON
7. List Backup Files
8. Delete File
9. Records Reset
0. Exit
```

---

# 📂 Example JSON Output

Records are saved in: `files/records.json`

```json
[
    {
        "name": "Salary",
        "amount": 5000,
        "source": "Company A",
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

# 🧪 Testing

Suggested tests include:

- object creation  
- JSON save/load  
- summary calculations  
- file utility functions  
- command-line menu behavior  

---

# 🎓 Academic Notes

SmartBudget demonstrates:

- **Modular Python package architecture**  
- **Object-oriented programming with inheritance**  
- **JSON serialization & deserialization**  
- **Separation of concerns: entity / controller / analysis / io**  
- **Expandable and maintainable project structure**

---

# 📘 Summary

SmartBudget is a well-organized Python budgeting application suitable for academic assignments and practical use.  
Its modular architecture makes it easy to extend, test, and maintain.

---

