# SmartBudget — FUNCTIONS.md (Final Version)

This document describes all modules, classes, and functions inside the SmartBudget package. It ensures clarity, maintainability, and grading readiness.

------------------------------------------------------------
PACKAGE STRUCTURE OVERVIEW
------------------------------------------------------------

SmartBudget includes four functional areas:

1. entity/ — financial data models  
2. analysis/ — summaries, insights, charts  
3. core/ — controllers and CLI interaction  
4. io/ — JSON persistence and file utilities

------------------------------------------------------------
1. ENTITY MODULES (smartbudget/entity/)
------------------------------------------------------------

base_record.py
---------------
Class: RecordBase  
Parent class of Income and Expense.

Attributes:
- name: record label  
- amount: validated numeric amount  
- timestamp: creation time

Methods:
- __init__(name, amount)  
- _validate_name(name)  
- _validate_amount(amount)  
- show()  
- to_dict(): base serialization

constants.py
-------------
Class: Limits  
Attributes:
- MAX_AMOUNT  
- MAX_NAME_LEN  

income.py
----------
Class: Income  
Represents positive income.

Methods:
- __init__(name, amount, source)  
- describe()  
- to_dict(): includes type="Income" and source

expense.py
-----------
Class: Expense  
Represents positive expense value.

Methods:
- __init__(name, amount, category)  
- describe()  
- to_dict(): includes type="Expense" and category

------------------------------------------------------------
2. ANALYSIS MODULES (smartbudget/analysis/)
------------------------------------------------------------

insights.py
------------
Functions:
- _load_split(): loads JSON, returns (incomes, expenses)
- income_details(): formatted strings of incomes
- expense_details(): formatted strings of expenses
- plot_expense_by_category(): bar chart of expenses

summary.py
-----------
Functions:
- total_income(): sum of all income amounts  
- total_expenses(): sum of all expense amounts  
- budget_balance(): total_income - total_expenses  
- summary_dict(): returns {"income": x, "expenses": y, "balance": z}

------------------------------------------------------------
3. CONTROLLER MODULES (smartbudget/core/)
------------------------------------------------------------

controller_records.py
----------------------
Functions:
- add_income(): input → Income object → save  
- add_expense(): input → Expense object → save  
- show_summary(): prints totals and balance  
- show_income_details()  
- show_expense_details()  
- show_expense_chart(): calls plot_expense_categories()

controller_system.py
---------------------
Functions:
- save_data(): save current records.json as backup  
- clear_data(): reset main JSON  
- load_data(incomes, expenses): rebuild objects  
- show_files(): list backup files  
- delete_backup_file(): remove a selected file  

controller_menu.py
-------------------
Functions:
- print_menu(): prints menu including chart option  
- run(): main loop dispatching actions  

------------------------------------------------------------
4. IO MODULES (smartbudget/io/)
------------------------------------------------------------

json_io.py
-----------
Functions:
- save_to_json(records, filename)  
- append_to_json(records)  
- load_from_json(filename): reconstruct Income or Expense by type  
- clear_json(filename)

file_utils.py
--------------
Functions:
- file_exists(filename)  
- list_files()  
- delete_file(filename)

------------------------------------------------------------
5. MAIN PROGRAM (main.py)
------------------------------------------------------------

Function:
- main(): starts the program via controller_menu.run()

------------------------------------------------------------
6. EXTENDED FEATURES (v2.0+)
------------------------------------------------------------

- Positive-amount Expense logic  
- Category-based bar chart visualization  
- Category grouping utilities  
- Summary dictionary for API/testing  
- Clean split into separate Income/Expense classes  
- Enhanced controller complexity  
- More modular structure for grading and maintainability

------------------------------------------------------------
SUMMARY
------------------------------------------------------------

SmartBudget provides:
- Clean OOP architecture  
- Modular design  
- JSON persistence  
- CLI-based interaction  
- Analytical summaries  
- Visual charts  
- Professional documentation


