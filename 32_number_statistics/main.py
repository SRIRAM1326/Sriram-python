import statistics

def main():
    while True:
        print("\n=== Number Statistics ===")
        user_input = input("Enter numbers separated by spaces (or 'exit'): ")
        
        if user_input.lower() == 'exit':
            print("Exiting...")
            break
            
        try:
            numbers = [float(x) for x in user_input.split()]
        except ValueError:
            print("Invalid input. Please enter only numbers separated by spaces.")
            continue
            
        if not numbers:
            print("No numbers provided.")
            continue
            
        count = len(numbers)
        minimum = min(numbers)
        maximum = max(numbers)
        total_sum = sum(numbers)
        average = statistics.mean(numbers)
        median = statistics.median(numbers)
        
        print(f"\nCount: {count}")
        print(f"Minimum: {minimum}")
        print(f"Maximum: {maximum}")
        print(f"Sum: {total_sum}")
        print(f"Average: {average}")
        print(f"Median: {median}")

if __name__ == "__main__":
    main()
