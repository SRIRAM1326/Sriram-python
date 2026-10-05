import json
import os

FILE_NAME = "contacts.json"

def load_contacts():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
    return []

def save_contacts(contacts):
    with open(FILE_NAME, 'w') as f:
        json.dump(contacts, f, indent=4)

def add_contact(contacts):
    name = input("Name: ").strip()
    phone = input("Phone: ").strip()
    email = input("Email: ").strip()
    
    if not name or not phone or not email:
        print("All fields are required.")
        return
        
    if not phone.isdigit():
        print("Phone must contain only numbers.")
        return
        
    if "@" not in email or "." not in email:
        print("Invalid email format.")
        return
        
    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts(contacts)
    print("\nContact saved!")

def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return
    print("\n--- Contacts ---")
    for i, c in enumerate(contacts, 1):
        print(f"{i}. {c['name']} | {c['phone']} | {c['email']}")

def search_contact(contacts):
    query = input("Search term (name, phone, or email): ").strip().lower()
    results = [c for c in contacts if query in c['name'].lower() or query in c['phone'] or query in c['email'].lower()]
    
    if results:
        print("\n--- Search Results ---")
        for i, c in enumerate(results, 1):
            print(f"{i}. {c['name']} | {c['phone']} | {c['email']}")
    else:
        print("No matches found.")

def update_contact(contacts):
    view_contacts(contacts)
    if not contacts:
        return
    try:
        idx = int(input("\nEnter contact number to update: ")) - 1
        if 0 <= idx < len(contacts):
            print("Leave blank to keep current value.")
            name = input(f"Name ({contacts[idx]['name']}): ").strip()
            phone = input(f"Phone ({contacts[idx]['phone']}): ").strip()
            email = input(f"Email ({contacts[idx]['email']}): ").strip()
            
            if name: contacts[idx]['name'] = name
            if phone:
                if phone.isdigit(): contacts[idx]['phone'] = phone
                else: print("Invalid phone format ignored.")
            if email:
                if "@" in email and "." in email: contacts[idx]['email'] = email
                else: print("Invalid email format ignored.")
                
            save_contacts(contacts)
            print("Contact updated.")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Invalid input.")

def delete_contact(contacts):
    view_contacts(contacts)
    if not contacts:
        return
    try:
        idx = int(input("\nEnter contact number to delete: ")) - 1
        if 0 <= idx < len(contacts):
            removed = contacts.pop(idx)
            save_contacts(contacts)
            print(f"Deleted contact: {removed['name']}")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Invalid input.")

def main():
    contacts = load_contacts()
    
    while True:
        print("\n=== Address Book ===")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("\nChoose an option: ")
        
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
