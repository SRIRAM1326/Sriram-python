def is_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

def main():
    while True:
        print("\n=== Leap Year Checker ===")
        user_input = input("Enter year (or 'exit' to quit): ")
        
        if user_input.lower() == 'exit':
            print("Exiting...")
            break
            
        try:
            year = int(user_input)
            if is_leap_year(year):
                print(f"\n{year} is a leap year.")
            else:
                print(f"\n{year} is not a leap year.")
        except ValueError:
            print("Invalid input. Please enter a valid year.")

if __name__ == "__main__":
    main()
