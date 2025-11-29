"""
Analysis helpers for SmartBudget.
Provides simple income/expense details and sorting.
"""
import logging
from typing import List, Tuple
from smartbudget.entity.income import Income
from smartbudget.entity.expense import  Expense
from smartbudget.io.json_io import load_from_json
import matplotlib.pyplot as plt

logger = logging.getLogger(__name__)
# ======================================
# Internal helpers
# ======================================



def plot_expense_by_category():
    _, expenses = _load_split()


    category_totals = {}
    for e in expenses:
        value = abs(e.amount)
        category_totals[e.category] = category_totals.get(e.category, 0) + value

    if not category_totals:
        print("\n(No expenses available for plotting)")
        return

    cats = list(category_totals.keys())
    vals = list(category_totals.values())

    plt.figure(figsize=(8, 5))

    if len(cats) == 1:
        bar_width = 0.2
        x = [0]
        bars = plt.bar(x, vals, width=bar_width, color="#4a90e2")
        plt.xticks(x, cats)
    else:
        bars = plt.bar(cats, vals, color="#4a90e2")


    plt.title("Expenses by Category", fontsize=14)
    plt.xlabel("Category", fontsize=12)
    plt.ylabel("Amount ($)", fontsize=12)
    plt.xticks(rotation=30)


    for bar in bars:
        height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width()/2,
            height + height * 0.02,
            f"{height:.0f}",
            ha='center',
            va='bottom',
            fontsize=10
        )

    plt.tight_layout()
    plt.show()

def _validate_record_types(records: List[object]) -> None:
    """
    Validate that the records loaded from file belong to supported classes.
    Log warnings for invalid entries instead of failing silently.
    """
    for r in records:
        if not isinstance(r, (Income, Expense)):
            logger.warning(
                f"[analysis] Ignored unsupported record type: {type(r).__name__} — {r}"
            )


def _split_records(records: List[object]) -> Tuple[List[Income], List[Expense]]:
    """
    Split raw record list into Income and Expense lists with internal validation.
    """
    incomes: List[Income] = []
    expenses: List[Expense] = []

    for r in records:
        if isinstance(r, Income):
            incomes.append(r)
        elif isinstance(r, Expense):
            expenses.append(r)
        else:
            logger.debug(f"[analysis] Skipping unrecognized record: {r}")

    return incomes, expenses


def _load_split() -> Tuple[List[Income], List[Expense]]:
    """
    Load records from storage and split them into income/expense groups.
    Performs logging, validation, and safe handling for corrupt data.
    """
    try:
        records = load_from_json()
        logger.info(f"[analysis] Loaded {len(records)} records from JSON file.")
    except Exception as exc:
        logger.error(f"[analysis] Failed to load JSON data: {exc}")
        return [], []

    # Validation step
    _validate_record_types(records)

    # Split step
    incomes, expenses = _split_records(records)

    logger.info(
        f"[analysis] Parsed {len(incomes)} incomes and {len(expenses)} expenses."
    )

    return incomes, expenses


# ======================================
# Expense detail extraction
# ======================================

def expense_details() -> List[str]:
    """
    Return formatted descriptions for all expense entries.
    Includes robust error handling and logs invalid descriptions.
    """
    _, expenses = _load_split()
    formatted = []

    for e in expenses:
        try:
            desc = e.describe()
            formatted.append(desc)
        except Exception as exc:
            logger.error(
                f"[analysis] Failed to generate description for expense {e}: {exc}"
            )

    return formatted


# ======================================
# Income detail extraction
# ======================================

def income_details() -> List[str]:
    """
    Return formatted descriptions for all income entries.
    Performs per-item error handling to avoid breaking the whole function.
    """
    incomes, _ = _load_split()
    output = []

    for inc in incomes:
        try:
            desc = inc.describe()
            output.append(desc)
        except Exception as exc:
            logger.error(
                f"[analysis] Failed to generate description for income {inc}: {exc}"
            )

    return output

