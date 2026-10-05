import random

def scramble_word(word):
    word_list = list(word)
    if len(word) > 1:
        while True:
            random.shuffle(word_list)
            scrambled = "".join(word_list)
            if scrambled != word:
                return scrambled
    return "".join(word_list)

def main():
    words = ["PYTHON", "PROGRAMMING", "DEVELOPER", "COMPUTER", "DATABASE", "NETWORK", "ALGORITHM"]
    score = 0
    
    print("=== Word Scrambler ===")
    
    while True:
        original = random.choice(words)
        scrambled = scramble_word(original)
        
        print(f"\nScrambled word: {scrambled}")
        guess = input("Your guess (or 'exit'): ").strip().upper()
        
        if guess == 'EXIT':
            print(f"\nFinal Score: {score}")
            print("Exiting...")
            break
            
        if guess == original:
            print("\nCorrect!")
            score += 1
            print(f"Score: {score}")
        else:
            print(f"\nIncorrect! The original word was: {original}")
            print(f"Score: {score}")

if __name__ == "__main__":
    main()
