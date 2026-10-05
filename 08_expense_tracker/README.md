# Expense Tracker

## Description
A command-line expense tracker that permanently stores your expenses using SQLite. It allows you to categorize expenses and view totals.

## Features
- Add expense
- View expenses
- Delete expense
- Calculate total expenses
- Show expenses by category
- Store data permanently in SQLite database (`expenses.db`)
- Include amount, category, description, and date
- Validate amount

## Technologies
- Python 3
- `sqlite3` module
- `datetime` module

## How to Run
```bash
python main.py
```

## Example Usage
```text
=== Expense Tracker ===

1. Add Expense
2. View Expenses
3. Delete Expense
4. Total Expenses
5. Expenses By Category
6. Exit

Choose an option: 1

Amount: 250
Category: Food
Description: Lunch
```

## What I Learned
- Using the `sqlite3` module to interact with a SQLite database.
- Writing SQL queries (CREATE, INSERT, SELECT, DELETE, GROUP BY).
- Formatting dates with Python's `datetime` module.
