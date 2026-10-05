import json
import os

FILE_NAME = "scores.json"

def load_scores():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
    return []

def save_scores(scores):
    with open(FILE_NAME, 'w') as f:
        json.dump(scores, f, indent=4)

def add_score(scores):
    name = input("\nPlayer Name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return
        
    try:
        score = int(input("Score: "))
        scores.append({"name": name, "score": score})
        save_scores(scores)
        print("\nScore saved!")
    except ValueError:
        print("Invalid score. Please enter a valid number.")

def view_scores(scores):
    if not scores:
        print("\nNo scores recorded yet.")
        return
        
    sorted_scores = sorted(scores, key=lambda x: x['score'], reverse=True)
    
    print("\n========== ALL SCORES ==========")
    for i, s in enumerate(sorted_scores, 1):
        print(f"{i}. {s['name']:<10} {s['score']}")

def view_top_5(scores):
    if not scores:
        print("\nNo scores recorded yet.")
        return
        
    sorted_scores = sorted(scores, key=lambda x: x['score'], reverse=True)[:5]
    
    print("\n========== LEADERBOARD ==========")
    for i, s in enumerate(sorted_scores, 1):
        print(f"{i}. {s['name']:<10} {s['score']}")

def main():
    scores = load_scores()
    
    while True:
        print("\n=== High Score Tracker ===")
        print("1. Add Score")
        print("2. View Scores")
        print("3. View Top 5")
        print("4. Exit")
        
        choice = input("\nChoose an option: ")
        
        if choice == '1':
            add_score(scores)
        elif choice == '2':
            view_scores(scores)
        elif choice == '3':
            view_top_5(scores)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
