import calendar

def display_month():
    try:
        year = int(input("\nEnter year: "))
        month = int(input("Enter month (1-12): "))
        
        if 1 <= month <= 12:
            print("\n" + calendar.month(year, month))
        else:
            print("Invalid month. Please enter a number between 1 and 12.")
    except ValueError:
        print("Invalid input. Please enter valid numbers.")

def display_year():
    try:
        year = int(input("\nEnter year: "))
        print("\n" + calendar.calendar(year))
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def main():
    while True:
        print("\n=== Calendar Generator ===")
        print("1. Display Month")
        print("2. Display Year")
        print("3. Exit")
        
        choice = input("\nChoose: ")
        
        if choice == '1':
            display_month()
        elif choice == '2':
            display_year()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select 1-3.")

if __name__ == "__main__":
    main()
