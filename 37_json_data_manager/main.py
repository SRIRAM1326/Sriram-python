import json
import os

FILE_NAME = "data.json"

def load_records():
    if not os.path.exists(FILE_NAME):
        return []
    try:
        with open(FILE_NAME, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("Warning: data.json is corrupted or empty. Starting fresh.")
        return []

def save_records(records):
    try:
        with open(FILE_NAME, 'w') as f:
            json.dump(records, f, indent=4)
    except Exception as e:
        print(f"Error saving records: {e}")

def add_record(records):
    rec_id = input("ID: ").strip()
    if any(r['id'] == rec_id for r in records):
        print("Error: Record with this ID already exists.")
        return
        
    name = input("Name: ").strip()
    category = input("Category: ").strip()
    description = input("Description: ").strip()
    
    if not rec_id or not name:
        print("ID and Name are required.")
        return
        
    records.append({
        "id": rec_id,
        "name": name,
        "category": category,
        "description": description
    })
    save_records(records)
    print("Record added successfully.")

def view_records(records):
    if not records:
        print("No records available.")
        return
    print("\n--- All Records ---")
    for r in records:
        print(f"ID: {r['id']} | Name: {r['name']} | Category: {r['category']} | Desc: {r['description']}")

def search_records(records):
    query = input("Search term: ").strip().lower()
    results = [r for r in records if query in r['id'].lower() or query in r['name'].lower() or query in r['category'].lower()]
    
    if results:
        print("\n--- Search Results ---")
        for r in results:
            print(f"ID: {r['id']} | Name: {r['name']} | Category: {r['category']}")
    else:
        print("No matches found.")

def update_record(records):
    rec_id = input("Enter ID of record to update: ").strip()
    for r in records:
        if r['id'] == rec_id:
            print("Leave field empty to keep current value.")
            name = input(f"Name ({r['name']}): ").strip()
            category = input(f"Category ({r['category']}): ").strip()
            description = input(f"Description ({r['description']}): ").strip()
            
            if name: r['name'] = name
            if category: r['category'] = category
            if description: r['description'] = description
            
            save_records(records)
            print("Record updated.")
            return
    print("Record ID not found.")

def delete_record(records):
    rec_id = input("Enter ID of record to delete: ").strip()
    for i, r in enumerate(records):
        if r['id'] == rec_id:
            records.pop(i)
            save_records(records)
            print("Record deleted.")
            return
    print("Record ID not found.")

def main():
    records = load_records()
    
    while True:
        print("\n=== JSON Data Manager ===")
        print("1. Add Record")
        print("2. View Records")
        print("3. Search")
        print("4. Update")
        print("5. Delete")
        print("6. Exit")
        
        choice = input("\nChoose: ")
        
        if choice == '1':
            add_record(records)
        elif choice == '2':
            view_records(records)
        elif choice == '3':
            search_records(records)
        elif choice == '4':
            update_record(records)
        elif choice == '5':
            delete_record(records)
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
