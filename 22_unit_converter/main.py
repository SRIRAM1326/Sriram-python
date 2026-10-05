def main():
    while True:
        print("\n=== Unit Converter ===")
        print("1. Kilometers -> Miles")
        print("2. Miles -> Kilometers")
        print("3. Meters -> Feet")
        print("4. Feet -> Meters")
        print("5. Kilograms -> Pounds")
        print("6. Pounds -> Kilograms")
        print("7. Exit")
        
        choice = input("\nChoose an option: ")
        
        if choice == '7':
            print("Exiting...")
            break
            
        if choice in ['1', '2', '3', '4', '5', '6']:
            try:
                value = float(input("\nEnter value to convert: "))
                
                if choice == '1':
                    res = value * 0.621371
                    print(f"{value} km = {res:.4f} miles")
                elif choice == '2':
                    res = value / 0.621371
                    print(f"{value} miles = {res:.4f} km")
                elif choice == '3':
                    res = value * 3.28084
                    print(f"{value} m = {res:.4f} ft")
                elif choice == '4':
                    res = value / 3.28084
                    print(f"{value} ft = {res:.4f} m")
                elif choice == '5':
                    res = value * 2.20462
                    print(f"{value} kg = {res:.4f} lbs")
                elif choice == '6':
                    res = value / 2.20462
                    print(f"{value} lbs = {res:.4f} kg")
            except ValueError:
                print("Invalid input. Please enter a numerical value.")
        else:
            print("Invalid choice. Please select 1-7.")

if __name__ == "__main__":
    main()
