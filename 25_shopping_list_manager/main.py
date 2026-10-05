def display_list(shopping_list):
    if not shopping_list:
        print("\nShopping list is empty.")
        return
        
    print("\n=== Shopping List ===")
    for i, item in enumerate(shopping_list, 1):
        status = "[✓]" if item['purchased'] else "[ ]"
        print(f"{i}. {status} {item['name']}")

def main():
    shopping_list = []
    
    while True:
        print("\n=== Shopping List Menu ===")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. Search Item")
        print("4. View Items")
        print("5. Mark Purchased")
        print("6. Clear List")
        print("7. Exit")
        
        choice = input("\nChoose an option: ")
        
        if choice == '1':
            item_name = input("Enter item name: ").strip()
            if item_name:
                shopping_list.append({"name": item_name, "purchased": False})
                print(f"'{item_name}' added.")
            else:
                print("Item name cannot be empty.")
                
        elif choice == '2':
            display_list(shopping_list)
            if not shopping_list: continue
            
            try:
                idx = int(input("\nEnter item number to remove: ")) - 1
                if 0 <= idx < len(shopping_list):
                    removed = shopping_list.pop(idx)
                    print(f"Removed '{removed['name']}'.")
                else:
                    print("Invalid item number.")
            except ValueError:
                print("Please enter a valid number.")
                
        elif choice == '3':
            query = input("Search for: ").strip().lower()
            results = [i for i in shopping_list if query in i['name'].lower()]
            if results:
                print("\nSearch Results:")
                for item in results:
                    status = "[✓]" if item['purchased'] else "[ ]"
                    print(f"{status} {item['name']}")
            else:
                print("No items found.")
                
        elif choice == '4':
            display_list(shopping_list)
            
        elif choice == '5':
            display_list(shopping_list)
            if not shopping_list: continue
            
            try:
                idx = int(input("\nEnter item number to mark purchased: ")) - 1
                if 0 <= idx < len(shopping_list):
                    shopping_list[idx]['purchased'] = True
                    print(f"Marked '{shopping_list[idx]['name']}' as purchased.")
                else:
                    print("Invalid item number.")
            except ValueError:
                print("Please enter a valid number.")
                
        elif choice == '6':
            confirm = input("Are you sure you want to clear the list? (y/n): ")
            if confirm.lower() == 'y':
                shopping_list.clear()
                print("List cleared.")
                
        elif choice == '7':
            print("Exiting...")
            break
            
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
