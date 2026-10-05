import random

def determine_winner(player, computer):
    if player == computer:
        return "Draw"
    elif (player == 'Rock' and computer == 'Scissors') or \
         (player == 'Paper' and computer == 'Rock') or \
         (player == 'Scissors' and computer == 'Paper'):
        return "Player"
    else:
        return "Computer"

def main():
    options = {
        '1': 'Rock',
        '2': 'Paper',
        '3': 'Scissors'
    }
    
    player_wins = 0
    comp_wins = 0
    draws = 0
    
    while True:
        print("\n=== Rock Paper Scissors ===")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        print("4. Exit")
        
        choice = input("\nYour choice: ")
        
        if choice == '4':
            print("\nFinal Score:")
            print(f"Player: {player_wins} | Computer: {comp_wins} | Draws: {draws}")
            print("Exiting...")
            break
            
        if choice in options:
            player_choice = options[choice]
            comp_choice = random.choice(['Rock', 'Paper', 'Scissors'])
            
            print(f"\nYou: {player_choice}")
            print(f"Computer: {comp_choice}")
            
            winner = determine_winner(player_choice, comp_choice)
            
            if winner == "Player":
                print("\nYou win!")
                player_wins += 1
            elif winner == "Computer":
                print("\nComputer wins!")
                comp_wins += 1
            else:
                print("\nIt's a draw!")
                draws += 1
        else:
            print("\nInvalid choice. Please choose 1-4.")

if __name__ == "__main__":
    main()
