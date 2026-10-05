import random

def main():
    while True:
        print("\n=== Number Guessing Game ===")
        print("\nI selected a number between 1 and 100.")
        
        target_number = random.randint(1, 100)
        attempts = 0
        
        while True:
            try:
                guess = int(input("\nYour guess: "))
                attempts += 1
                
                if guess < target_number:
                    print("\nToo low!")
                elif guess > target_number:
                    print("\nToo high!")
                else:
                    print("\nCorrect!")
                    print(f"\nAttempts: {attempts}")
                    break
            except ValueError:
                print("\nInvalid input. Please enter a number.")
                
        play_again = input("\nPlay again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
