def main():
    while True:
        print("\n=== Even/Odd Analyzer ===")
        user_input = input("Enter numbers separated by spaces (or 'exit'): ")
        
        if user_input.lower() == 'exit':
            print("Exiting...")
            break
            
        try:
            numbers = [int(x) for x in user_input.split()]
        except ValueError:
            print("Invalid input. Please enter only integers separated by spaces.")
            continue
            
        if not numbers:
            print("No numbers provided.")
            continue
            
        even_nums = [n for n in numbers if n % 2 == 0]
        odd_nums = [n for n in numbers if n % 2 != 0]
        
        print("\nEven Numbers:")
        print(" ".join(map(str, even_nums)) if even_nums else "None")
        
        print("\nOdd Numbers:")
        print(" ".join(map(str, odd_nums)) if odd_nums else "None")
        
        print(f"\nEven Count: {len(even_nums)}")
        print(f"Odd Count: {len(odd_nums)}")
        print(f"Total: {len(numbers)}")

if __name__ == "__main__":
    main()
