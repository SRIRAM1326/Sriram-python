import random

def main():
    names = []
    
    while True:
        print("\n=== Random Name Picker ===")
        print("1. Add Names")
        print("2. Pick a Random Name")
        print("3. View Names")
        print("4. Remove a Selected Name")
        print("5. Clear List")
        print("6. Exit")
        
        choice = input("\nChoose an option: ")
        
        if choice == '1':
            user_input = input("Enter names separated by commas: ")
            new_names = [n.strip() for n in user_input.split(",") if n.strip()]
            names.extend(new_names)
            print(f"Added {len(new_names)} names.")
            
        elif choice == '2':
            if not names:
                print("The list is empty. Add names first.")
            else:
                selected = random.choice(names)
                print(f"\nSelected:\n>>> {selected}")
                
        elif choice == '3':
            if not names:
                print("The list is empty.")
            else:
                print("\nNames:")
                for i, name in enumerate(names, 1):
                    print(f"{i}. {name}")
                    
        elif choice == '4':
            if not names:
                print("The list is empty.")
            else:
                try:
                    for i, name in enumerate(names, 1):
                        print(f"{i}. {name}")
                    idx = int(input("Enter number to remove: ")) - 1
                    if 0 <= idx < len(names):
                        removed = names.pop(idx)
                        print(f"Removed '{removed}'.")
                    else:
                        print("Invalid number.")
                except ValueError:
                    print("Invalid input.")
                    
        elif choice == '5':
            names.clear()
            print("List cleared.")
            
        elif choice == '6':
            print("Exiting...")
            break
            
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
