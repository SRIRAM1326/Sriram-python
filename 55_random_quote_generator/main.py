import json
import os
import random

FILE_NAME = "quotes.json"

DEFAULT_QUOTES = [
    {
        "quote": "The only way to do great work is to love what you do.",
        "author": "Steve Jobs",
        "category": "Motivation"
    },
    {
        "quote": "Talk is cheap. Show me the code.",
        "author": "Linus Torvalds",
        "category": "Programming"
    },
    {
        "quote": "Programs must be written for people to read, and only incidentally for machines to execute.",
        "author": "Harold Abelson",
        "category": "Programming"
    },
    {
        "quote": "Simplicity is prerequisite for reliability.",
        "author": "Edsger W. Dijkstra",
        "category": "Programming"
    },
    {
        "quote": "In the middle of difficulty lies opportunity.",
        "author": "Albert Einstein",
        "category": "Wisdom"
    },
    {
        "quote": "It does not matter how slowly you go as long as you do not stop.",
        "author": "Confucius",
        "category": "Perseverance"
    },
    {
        "quote": "First, solve the problem. Then, write the code.",
        "author": "John Johnson",
        "category": "Programming"
    },
    {
        "quote": "Knowledge is power.",
        "author": "Francis Bacon",
        "category": "Wisdom"
    },
    {
        "quote": "Code is like humor. When you have to explain it, it’s bad.",
        "author": "Cory House",
        "category": "Programming"
    },
    {
        "quote": "Whether you think you can or you think you can't, you're right.",
        "author": "Henry Ford",
        "category": "Motivation"
    },
    {
        "quote": "Make it work, make it right, make it fast.",
        "author": "Kent Beck",
        "category": "Programming"
    },
    {
        "quote": "The journey of a thousand miles begins with one step.",
        "author": "Lao Tzu",
        "category": "Wisdom"
    }
]

def load_quotes():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return DEFAULT_QUOTES.copy()
    else:
        save_quotes(DEFAULT_QUOTES)
        return DEFAULT_QUOTES.copy()

def save_quotes(quotes):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(quotes, f, indent=4, ensure_ascii=False)

def print_quote_card(item):
    text = item["quote"]
    author = item["author"]
    category = item.get("category", "General")

    width = max(len(text) + 6, len(author) + 12, 50)
    width = min(width, 70)

    print("\n" + "┌" + "─" * (width - 2) + "┐")
    print(f"│  🏷️  Category: {category:<{width - 17}}│")
    print("├" + "─" * (width - 2) + "┤")

    # Word wrap text
    words = text.split()
    current_line = "│  “"
    for w in words:
        if len(current_line) + len(w) + 1 >= width - 3:
            current_line += " " * (width - len(current_line) - 1) + "│"
            print(current_line)
            current_line = "│   " + w
        else:
            if current_line == "│  “":
                current_line += w
            else:
                current_line += " " + w
    current_line += "”"
    current_line += " " * (width - len(current_line) - 1) + "│"
    print(current_line)

    print("│" + " " * (width - 2) + "│")
    author_line = f"│  — {author}"
    author_line += " " * (width - len(author_line) - 1) + "│"
    print(author_line)
    print("└" + "─" * (width - 2) + "┘")

def get_random_quote(quotes):
    if not quotes:
        print("\nNo quotes available.")
        return
    q = random.choice(quotes)
    print_quote_card(q)

def get_by_category(quotes):
    categories = sorted(list({q.get("category", "General") for q in quotes}))
    print("\nAvailable Categories:")
    for i, c in enumerate(categories, 1):
        print(f"{i}. {c}")

    try:
        idx = int(input("\nChoose category number: ")) - 1
        if not (0 <= idx < len(categories)):
            print("Invalid selection.")
            return
        chosen = categories[idx]
        filtered = [q for q in quotes if q.get("category") == chosen]
        if filtered:
            print_quote_card(random.choice(filtered))
    except ValueError:
        print("Invalid number.")

def add_quote(quotes):
    print("\n--- Add Custom Quote ---")
    text = input("Quote Text: ").strip()
    if not text:
        print("Quote cannot be empty.")
        return
    author = input("Author: ").strip() or "Unknown"
    category = input("Category (e.g., Motivation, Programming): ").strip() or "General"

    new_q = {"quote": text, "author": author, "category": category}
    quotes.append(new_q)
    save_quotes(quotes)
    print("✓ Quote added successfully to library!")

def search_quotes(quotes):
    term = input("\nEnter search keyword or author: ").strip().lower()
    if not term:
        return

    results = [q for q in quotes if term in q["quote"].lower() or term in q["author"].lower()]
    if not results:
        print(f"No quotes matched '{term}'.")
        return

    print(f"\nFound {len(results)} quote(s):")
    for q in results:
        print(f"• “{q['quote']}” — {q['author']} [{q.get('category')}]")

def main():
    quotes = load_quotes()
    while True:
        print("\n=== Random Quote Generator ===")
        print("1. Get Random Quote")
        print("2. Get Random Quote by Category")
        print("3. Search Quotes by Author or Keyword")
        print("4. Add New Quote to Collection")
        print("5. Exit")

        choice = input("\nChoose an option (1-5): ").strip()

        if choice == "1":
            get_random_quote(quotes)
        elif choice == "2":
            get_by_category(quotes)
        elif choice == "3":
            search_quotes(quotes)
        elif choice == "4":
            add_quote(quotes)
        elif choice == "5":
            print("Stay inspired! Goodbye.")
            break
        else:
            print("Invalid option. Please choose 1-5.")

if __name__ == "__main__":
    main()
