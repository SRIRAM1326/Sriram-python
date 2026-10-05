import random

def roll_dice(num_dice):
    results = []
    for _ in range(num_dice):
        results.append(random.randint(1, 6))
    return results

def main():
    rolls_count = 0
    total_sum_all_rolls = 0
    
    while True:
        print("\n=== Dice Simulator ===")
        try:
            num = input("How many dice to roll? (or 'q' to exit): ")
            if num.lower() == 'q':
                print(f"\nSession Statistics:")
                print(f"Total times rolled: {rolls_count}")
                print(f"Sum of all dice rolled: {total_sum_all_rolls}")
                print("Exiting...")
                break
                
            num_dice = int(num)
            if num_dice <= 0:
                print("Please enter a positive number of dice.")
                continue
                
            results = roll_dice(num_dice)
            
            print("\nResults:")
            for i, result in enumerate(results, 1):
                print(f"Dice {i}: {result}")
                
            current_total = sum(results)
            print(f"\nTotal: {current_total}")
            
            rolls_count += 1
            total_sum_all_rolls += current_total
            
        except ValueError:
            print("Invalid input. Please enter a valid number or 'q'.")

if __name__ == "__main__":
    main()
