import hashlib
import json
import os
import string
import random
import time
import webbrowser
from datetime import datetime

DB_FILE = "urls.json"
BASE_URL = "http://short.ly/"

def load_data():
    if os.path.exists(DB_FILE):
        try:
            with open(DB_FILE, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return {}
    return {}

def save_data(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=4)

def generate_short_code(length=6):
    chars = string.ascii_letters + string.digits
    return "".join(random.choice(chars) for _ in range(length))

def shorten_url(data):
    url = input("\nEnter long URL: ").strip()
    if not url:
        print("URL cannot be empty.")
        return

    if not (url.startswith("http://") or url.startswith("https://")):
        url = "https://" + url

    # Check if URL already shortened
    for code, info in data.items():
        if info["url"] == url:
            print(f"\nAlready shortened! Short URL: {BASE_URL}{code}")
            return

    custom_alias = input("Enter custom alias (press Enter for auto-generate): ").strip()
    if custom_alias:
        if custom_alias in data:
            print("Error: That alias is already in use. Please choose another.")
            return
        code = custom_alias
    else:
        code = generate_short_code()
        while code in data:
            code = generate_short_code()

    data[code] = {
        "url": url,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "clicks": 0
    }
    save_data(data)

    print("\n✓ URL successfully shortened!")
    print(f"Short URL: {BASE_URL}{code}")
    print(f"Original:  {url}")

def expand_url(data):
    code = input("\nEnter short code or alias: ").strip()
    # Strip base URL if user pasted the full short link
    code = code.replace(BASE_URL, "")

    if code in data:
        info = data[code]
        info["clicks"] += 1
        save_data(data)
        print(f"\nTarget URL: {info['url']}")
        print(f"Clicks: {info['clicks']}")
        open_choice = input("Open in browser? (y/n): ").strip().lower()
        if open_choice == "y":
            webbrowser.open(info["url"])
            print("Opened in browser.")
    else:
        print("Error: Short code not found.")

def list_urls(data):
    if not data:
        print("\nNo shortened URLs found.")
        return

    print("\n" + "=" * 70)
    print(f"{'Code':<10} | {'Clicks':<8} | {'Created At':<20} | {'Original URL'}")
    print("=" * 70)
    for code, info in data.items():
        orig = info["url"]
        if len(orig) > 35:
            orig = orig[:32] + "..."
        print(f"{code:<10} | {info['clicks']:<8} | {info['created_at']:<20} | {orig}")
    print("=" * 70)

def delete_url(data):
    code = input("\nEnter short code to delete: ").strip().replace(BASE_URL, "")
    if code in data:
        del data[code]
        save_data(data)
        print(f"✓ Short code '{code}' deleted.")
    else:
        print("Error: Code not found.")

def main():
    data = load_data()
    while True:
        print("\n=== URL Shortener ===")
        print("1. Shorten URL")
        print("2. Expand / Visit Short URL")
        print("3. List All Shortened URLs & Analytics")
        print("4. Delete Short URL")
        print("5. Exit")

        choice = input("\nChoose an option (1-5): ").strip()

        if choice == "1":
            shorten_url(data)
        elif choice == "2":
            expand_url(data)
        elif choice == "3":
            list_urls(data)
        elif choice == "4":
            delete_url(data)
        elif choice == "5":
            print("Exiting URL Shortener. Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1-5.")

if __name__ == "__main__":
    main()
