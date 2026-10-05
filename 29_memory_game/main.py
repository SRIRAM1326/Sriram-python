import random
import time

def create_board():
    items = list('AABBCCDDEEFFGGHH')
    random.shuffle(items)
    return items

def display_board(board, revealed):
    print("\n  0 1 2 3")
    for row in range(4):
        print(f"{row} ", end="")
        for col in range(4):
            idx = row * 4 + col
            if revealed[idx]:
                print(f"{board[idx]} ", end="")
            else:
                print("* ", end="")
        print()

def main():
    print("=== Memory Game ===")
    board = create_board()
    revealed = [False] * 16
    attempts = 0
    matched_pairs = 0
    
    while matched_pairs < 8:
        display_board(board, revealed)
        
        try:
            first = int(input("\nChoose first position (0-15): "))
            if first < 0 or first > 15 or revealed[first]:
                print("Invalid or already revealed position.")
                continue
                
            revealed[first] = True
            display_board(board, revealed)
            
            second = int(input("\nChoose second position (0-15): "))
            if second < 0 or second > 15 or revealed[second] or second == first:
                print("Invalid or already revealed position.")
                revealed[first] = False
                continue
                
            revealed[second] = True
            display_board(board, revealed)
            
            attempts += 1
            
            print(f"\nPosition {first}: {board[first]}")
            print(f"Position {second}: {board[second]}")
            
            if board[first] == board[second]:
                print("\nMatch!")
                matched_pairs += 1
            else:
                print("\nNo match!")
                time.sleep(2)
                revealed[first] = False
                revealed[second] = False
                
        except ValueError:
            print("Invalid input. Enter numbers 0-15.")
            
    print(f"\nCongratulations! You matched all pairs in {attempts} attempts.")

if __name__ == "__main__":
    main()
