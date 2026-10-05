from datetime import datetime

def main():
    print("=== Age Calculator ===")
    
    while True:
        dob_input = input("\nEnter date of birth (DD-MM-YYYY) or 'exit': ")
        
        if dob_input.lower() == 'exit':
            print("Exiting...")
            break
            
        try:
            dob = datetime.strptime(dob_input, "%d-%m-%Y").date()
            today = datetime.today().date()
            
            if dob > today:
                print("Birth date cannot be in the future!")
                continue
                
            age_years = today.year - dob.year
            if (today.month, today.day) < (dob.month, dob.day):
                age_years -= 1
                
            print(f"\nAge: {age_years} years")
            
            next_birthday_year = today.year
            if (today.month, today.day) > (dob.month, dob.day) or \
               ((today.month, today.day) == (dob.month, dob.day) and age_years > 0):
                next_birthday_year += 1
                
            if dob.month == 2 and dob.day == 29:
                try:
                    next_birthday = datetime(next_birthday_year, dob.month, dob.day).date()
                except ValueError:
                    next_birthday = datetime(next_birthday_year, 3, 1).date() 
            else:
                next_birthday = datetime(next_birthday_year, dob.month, dob.day).date()
                
            print(f"Next birthday: {next_birthday.strftime('%d-%m-%Y')}")
            
        except ValueError:
            print("Invalid date format. Please use DD-MM-YYYY.")

if __name__ == "__main__":
    main()
