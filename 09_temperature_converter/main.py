def c_to_f(c):
    return (c * 9/5) + 32

def c_to_k(c):
    return c + 273.15

def f_to_c(f):
    return (f - 32) * 5/9

def f_to_k(f):
    return (f - 32) * 5/9 + 273.15

def k_to_c(k):
    return k - 273.15

def k_to_f(k):
    return (k - 273.15) * 9/5 + 32

def get_temperature():
    while True:
        try:
            return float(input("\nEnter temperature value: "))
        except ValueError:
            print("Invalid input. Please enter a valid decimal number.")

def main():
    while True:
        print("\n=== Temperature Converter ===")
        print("1. Celsius -> Fahrenheit")
        print("2. Fahrenheit -> Celsius")
        print("3. Celsius -> Kelvin")
        print("4. Kelvin -> Celsius")
        print("5. Fahrenheit -> Kelvin")
        print("6. Kelvin -> Fahrenheit")
        print("7. Exit")
        
        choice = input("\nChoose: ")
        
        if choice == '7':
            print("Exiting...")
            break
            
        if choice in ('1', '2', '3', '4', '5', '6'):
            temp = get_temperature()
            
            if choice == '1':
                res = c_to_f(temp)
                print(f"{temp}°C is {res:.2f}°F")
            elif choice == '2':
                res = f_to_c(temp)
                print(f"{temp}°F is {res:.2f}°C")
            elif choice == '3':
                res = c_to_k(temp)
                print(f"{temp}°C is {res:.2f}K")
            elif choice == '4':
                res = k_to_c(temp)
                print(f"{temp}K is {res:.2f}°C")
            elif choice == '5':
                res = f_to_k(temp)
                print(f"{temp}°F is {res:.2f}K")
            elif choice == '6':
                res = k_to_f(temp)
                print(f"{temp}K is {res:.2f}°F")
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
