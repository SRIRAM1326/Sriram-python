import sqlite3
from datetime import date

DB_FILE = "expenses.db"

def initialize_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            description TEXT,
            date TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def add_expense():
    try:
        amount = float(input("\nAmount: "))
        if amount <= 0:
            print("Amount must be positive.")
            return
            
        category = input("Category: ")
        description = input("Description: ")
        today = date.today().strftime("%Y-%m-%d")
        
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO expenses (amount, category, description, date)
            VALUES (?, ?, ?, ?)
        ''', (amount, category, description, today))
        conn.commit()
        conn.close()
        print("Expense added successfully.")
        
    except ValueError:
        print("Invalid amount. Please enter a valid number.")

def view_expenses():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('SELECT id, amount, category, description, date FROM expenses')
    records = cursor.fetchall()
    conn.close()
    
    if not records:
        print("\nNo expenses recorded yet.")
        return
        
    print("\n--- All Expenses ---")
    for r in records:
        print(f"ID: {r[0]} | Amount: {r[1]:.2f} | Category: {r[2]} | Date: {r[4]}")
        if r[3]:
            print(f"   Description: {r[3]}")

def delete_expense():
    view_expenses()
    try:
        exp_id = int(input("\nEnter ID of expense to delete: "))
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute('DELETE FROM expenses WHERE id = ?', (exp_id,))
        if cursor.rowcount > 0:
            print("Expense deleted.")
        else:
            print("Expense ID not found.")
        conn.commit()
        conn.close()
    except ValueError:
        print("Invalid ID.")

def calculate_total():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('SELECT SUM(amount) FROM expenses')
    total = cursor.fetchone()[0]
    conn.close()
    
    if total is None:
        total = 0.0
    print(f"\nTotal Expenses: {total:.2f}")

def view_by_category():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('SELECT category, SUM(amount) FROM expenses GROUP BY category')
    records = cursor.fetchall()
    conn.close()
    
    if not records:
        print("\nNo expenses recorded yet.")
        return
        
    print("\n--- Expenses By Category ---")
    for cat, total in records:
        print(f"{cat}: {total:.2f}")

def main():
    initialize_db()
    
    while True:
        print("\n=== Expense Tracker ===")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Total Expenses")
        print("5. Expenses By Category")
        print("6. Exit")
        
        choice = input("\nChoose an option: ")
        
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            delete_expense()
        elif choice == '4':
            calculate_total()
        elif choice == '5':
            view_by_category()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
