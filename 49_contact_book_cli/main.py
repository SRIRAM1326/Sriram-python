import json
import os

FILE_NAME = "contacts.json"

def load_contacts():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
    return []

def save_contacts(contacts):
    with open(FILE_NAME, "w") as f:
        json.dump(contacts, f, indent=4)

def add_contact(contacts):
    print("\n--- Add New Contact ---")
    name = input("Full Name: ").strip()
    if not name:
        print("Error: Contact name cannot be empty.")
        return

    # Check for existing duplicate name
    for c in contacts:
        if c["name"].lower() == name.lower():
            print(f"Warning: A contact named '{name}' already exists.")
            overwrite = input("Do you still want to add? (y/n): ").strip().lower()
            if overwrite != "y":
                return
            break

    phone = input("Phone Number: ").strip()
    email = input("Email Address: ").strip()
    notes = input("Category / Notes (e.g. Work, Family): ").strip()

    new_contact = {
        "id": len(contacts) + 1,
        "name": name,
        "phone": phone or "N/A",
        "email": email or "N/A",
        "notes": notes or "General"
    }

    contacts.append(new_contact)
    save_contacts(contacts)
    print(f"✓ Contact '{name}' added successfully.")

def list_contacts(contacts):
    if not contacts:
        print("\nNo contacts saved yet.")
        return

    print("\n" + "=" * 75)
    print(f"{'#':<4} | {'Name':<20} | {'Phone':<16} | {'Email':<22} | {'Category'}")
    print("=" * 75)
    for idx, c in enumerate(contacts, 1):
        print(f"{idx:<4} | {c['name']:<20} | {c['phone']:<16} | {c['email']:<22} | {c.get('notes', '')}")
    print("=" * 75)
    print(f"Total: {len(contacts)} contact(s)")

def search_contacts(contacts):
    query = input("\nEnter search keyword (name, phone, or email): ").strip().lower()
    if not query:
        print("Search term cannot be empty.")
        return

    results = [
        c for c in contacts
        if query in c["name"].lower() or query in c["phone"].lower() or query in c["email"].lower()
    ]

    if not results:
        print(f"No contacts matching '{query}' found.")
        return

    print(f"\nFound {len(results)} matching contact(s):")
    print("-" * 65)
    for c in results:
        print(f"• Name:  {c['name']}")
        print(f"  Phone: {c['phone']}")
        print(f"  Email: {c['email']}")
        print(f"  Notes: {c.get('notes', '')}\n")

def edit_contact(contacts):
    list_contacts(contacts)
    if not contacts:
        return

    try:
        idx = int(input("\nEnter contact index number to edit: ")) - 1
        if 0 <= idx < len(contacts):
            target = contacts[idx]
            print(f"\nEditing: {target['name']} (Press Enter to keep current value)")

            new_name = input(f"New Name [{target['name']}]: ").strip()
            new_phone = input(f"New Phone [{target['phone']}]: ").strip()
            new_email = input(f"New Email [{target['email']}]: ").strip()
            new_notes = input(f"New Notes [{target.get('notes', '')}]: ").strip()

            if new_name:
                target["name"] = new_name
            if new_phone:
                target["phone"] = new_phone
            if new_email:
                target["email"] = new_email
            if new_notes:
                target["notes"] = new_notes

            save_contacts(contacts)
            print("✓ Contact updated successfully.")
        else:
            print("Invalid contact index.")
    except ValueError:
        print("Please enter a valid number.")

def delete_contact(contacts):
    list_contacts(contacts)
    if not contacts:
        return

    try:
        idx = int(input("\nEnter contact number to delete: ")) - 1
        if 0 <= idx < len(contacts):
            target = contacts[idx]
            confirm = input(f"Are you sure you want to delete '{target['name']}'? (y/n): ").strip().lower()
            if confirm == "y":
                deleted = contacts.pop(idx)
                save_contacts(contacts)
                print(f"✓ Contact '{deleted['name']}' deleted.")
            else:
                print("Deletion cancelled.")
        else:
            print("Invalid index.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    contacts = load_contacts()
    while True:
        print("\n=== Contact Book CLI ===")
        print("1. View All Contacts")
        print("2. Add Contact")
        print("3. Search Contact")
        print("4. Edit Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("\nChoose an option (1-6): ").strip()

        if choice == "1":
            list_contacts(contacts)
        elif choice == "2":
            add_contact(contacts)
        elif choice == "3":
            search_contacts(contacts)
        elif choice == "4":
            edit_contact(contacts)
        elif choice == "5":
            delete_contact(contacts)
        elif choice == "6":
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1-6.")

if __name__ == "__main__":
    main()
