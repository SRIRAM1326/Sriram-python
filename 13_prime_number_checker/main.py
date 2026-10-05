def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def main():
    while True:
        print("\n=== Prime Number Checker ===")
        user_input = input("Enter number (or 'exit' to quit): ")
        
        if user_input.lower() == 'exit':
            print("Exiting...")
            break
            
        try:
            number = int(user_input)
            if is_prime(number):
                print(f"\n{number} is a prime number.")
            else:
                print(f"\n{number} is not a prime number.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
