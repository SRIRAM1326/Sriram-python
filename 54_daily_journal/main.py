import json
import os
from datetime import datetime

FILE_NAME = "journal.json"

def load_journal():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return {}
    return {}

def save_journal(journal):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(journal, f, indent=4, ensure_ascii=False)

def write_entry(journal):
    today = datetime.now().strftime("%Y-%m-%d")
    now_time = datetime.now().strftime("%H:%M")
    print(f"\n--- Daily Journal: Entry for {today} ---")

    if today in journal:
        print("Note: An entry for today already exists.")
        action = input("Do you want to (a)ppend or (o)verwrite? (a/o, default: a): ").strip().lower()
        if action == "o":
            existing_text = ""
        else:
            existing_text = journal[today]["content"] + "\n\n"
    else:
        existing_text = ""

    mood = input("Today's Mood (e.g. Great, Productive, Relaxed): ").strip() or "Good"
    tags_raw = input("Tags (comma separated, e.g. coding, study, gym): ").strip()
    tags = [t.strip() for t in tags_raw.split(",") if t.strip()]

    print("\nWrite your entry below. Type 'EOF' or 'SAVE' on a new line when finished:")
    lines = []
    while True:
        try:
            line = input()
            if line.strip().upper() in ("EOF", "SAVE", ":W", ":Q"):
                break
            lines.append(line)
        except EOFError:
            break

    new_content = "\n".join(lines).strip()
    if not new_content and not existing_text:
        print("Empty entry. Nothing saved.")
        return

    full_content = (existing_text + new_content).strip()
    word_count = len(full_content.split())

    journal[today] = {
        "date": today,
        "updated_at": f"{today} {now_time}",
        "mood": mood,
        "tags": tags,
        "content": full_content,
        "word_count": word_count
    }

    save_journal(journal)
    print(f"\n✓ Entry saved successfully ({word_count} words).")

def view_today(journal):
    today = datetime.now().strftime("%Y-%m-%d")
    view_entry(journal, today)

def view_entry(journal, date_key):
    if date_key not in journal:
        print(f"\nNo journal entry found for {date_key}.")
        return

    entry = journal[date_key]
    print("\n" + "=" * 60)
    print(f"📅 DATE: {entry['date']} | Mood: {entry.get('mood', 'N/A')}")
    if entry.get("tags"):
        print(f"🏷️  Tags: {', '.join(entry['tags'])}")
    print(f"📝 Words: {entry.get('word_count', len(entry['content'].split()))}")
    print("=" * 60)
    print(entry["content"])
    print("=" * 60)

def browse_dates(journal):
    if not journal:
        print("\nJournal is currently empty.")
        return

    dates = sorted(list(journal.keys()), reverse=True)
    print("\n" + "=" * 55)
    print(f"{'#':<4} | {'Date':<12} | {'Mood':<15} | {'Words'}")
    print("=" * 55)
    for i, d in enumerate(dates, 1):
        item = journal[d]
        print(f"{i:<4} | {d:<12} | {item.get('mood', 'N/A'):<15} | {item.get('word_count', 0)}")
    print("=" * 55)

    ch = input("\nEnter number to view full entry (or press Enter to return): ").strip()
    if ch.isdigit():
        idx = int(ch) - 1
        if 0 <= idx < len(dates):
            view_entry(journal, dates[idx])

def search_entries(journal):
    if not journal:
        print("\nJournal is currently empty.")
        return

    keyword = input("\nEnter search keyword or tag: ").strip().lower()
    if not keyword:
        return

    matches = []
    for d, item in journal.items():
        in_content = keyword in item["content"].lower()
        in_tags = any(keyword in t.lower() for t in item.get("tags", []))
        in_mood = keyword in item.get("mood", "").lower()
        if in_content or in_tags or in_mood:
            matches.append((d, item))

    if not matches:
        print(f"No entries found matching '{keyword}'.")
        return

    print(f"\nFound {len(matches)} matching entry/entries:")
    for d, item in sorted(matches, key=lambda x: x[0], reverse=True):
        snippet = item["content"][:100].replace("\n", " ") + "..."
        print(f"\n• [{d}] Mood: {item.get('mood')} | {snippet}")

def export_entry(journal):
    dates = sorted(list(journal.keys()), reverse=True)
    if not dates:
        print("No entries to export.")
        return

    date_str = input(f"Enter date to export (YYYY-MM-DD, default: {dates[0]}): ").strip() or dates[0]
    if date_str not in journal:
        print("Date not found.")
        return

    entry = journal[date_str]
    filename = f"journal_{date_str}.md"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"# Journal Entry - {date_str}\n\n")
        f.write(f"- **Mood**: {entry.get('mood')}\n")
        f.write(f"- **Tags**: {', '.join(entry.get('tags', []))}\n\n")
        f.write(f"## Content\n\n{entry['content']}\n")

    print(f"✓ Exported to: {os.path.abspath(filename)}")

def main():
    journal = load_journal()
    while True:
        print("\n=== Daily Journal ===")
        print("1. Write Today's Entry")
        print("2. Read Today's Entry")
        print("3. Browse Past Entries by Date")
        print("4. Search Journal Entries")
        print("5. Export Entry to Markdown (.md)")
        print("6. Exit")

        choice = input("\nChoose an option (1-6): ").strip()

        if choice == "1":
            write_entry(journal)
        elif choice == "2":
            view_today(journal)
        elif choice == "3":
            browse_dates(journal)
        elif choice == "4":
            search_entries(journal)
        elif choice == "5":
            export_entry(journal)
        elif choice == "6":
            print("Keep reflecting and writing! Goodbye.")
            break
        else:
            print("Invalid option. Please choose 1-6.")

if __name__ == "__main__":
    main()
