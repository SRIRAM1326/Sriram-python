import json
import os
import re
import webbrowser
from datetime import datetime

FILE_NAME = "playlists.json"

def load_data():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return {}
    return {}

def save_data(data):
    with open(FILE_NAME, "w") as f:
        json.dump(data, f, indent=4)

def normalize_youtube_url(url):
    url = url.strip()
    if not (url.startswith("http://") or url.startswith("https://")):
        url = "https://" + url

    # Extract standard video ID if short link
    if "youtu.be/" in url:
        vid_id = url.split("youtu.be/")[1].split("?")[0]
        return f"https://www.youtube.com/watch?v={vid_id}"

    return url

def list_playlists(data):
    if not data:
        print("\nNo playlists found.")
        return []

    print("\n" + "=" * 50)
    print(f"{'#':<4} | {'Playlist Name':<28} | {'Videos'}")
    print("=" * 50)
    names = list(data.keys())
    for i, name in enumerate(names, 1):
        count = len(data[name])
        print(f"{i:<4} | {name:<28} | {count}")
    print("=" * 50)
    return names

def create_playlist(data):
    name = input("\nEnter new playlist name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return
    if name in data:
        print("Error: Playlist with that name already exists.")
        return
    data[name] = []
    save_data(data)
    print(f"✓ Playlist '{name}' created successfully.")

def add_video(data):
    names = list_playlists(data)
    if not names:
        print("Create a playlist first!")
        return

    try:
        idx = int(input("\nSelect playlist number to add video: ")) - 1
        if not (0 <= idx < len(names)):
            print("Invalid playlist index.")
            return
        target_name = names[idx]
    except ValueError:
        print("Please enter a number.")
        return

    title = input("Video Title: ").strip()
    if not title:
        print("Title cannot be empty.")
        return

    url = input("YouTube Video URL: ").strip()
    clean_url = normalize_youtube_url(url)

    video_entry = {
        "title": title,
        "url": clean_url,
        "added_at": datetime.now().strftime("%Y-%m-%d %H:%M")
    }

    data[target_name].append(video_entry)
    save_data(data)
    print(f"✓ Video '{title}' added to '{target_name}'!")

def view_and_play_playlist(data):
    names = list_playlists(data)
    if not names:
        return

    try:
        idx = int(input("\nSelect playlist number to open: ")) - 1
        if not (0 <= idx < len(names)):
            print("Invalid playlist index.")
            return
        target_name = names[idx]
    except ValueError:
        print("Invalid number.")
        return

    videos = data[target_name]
    if not videos:
        print(f"\nPlaylist '{target_name}' is currently empty.")
        return

    print(f"\n--- Videos in '{target_name}' ---")
    print("=" * 65)
    for i, v in enumerate(videos, 1):
        print(f"{i}. {v['title']}")
        print(f"   URL: {v['url']} (Added: {v['added_at']})")
    print("=" * 65)

    print("\nOptions: (Enter video # to open in browser, 'all' to play all, or press Enter to return)")
    action = input("> ").strip().lower()

    if action == "all":
        print(f"Opening all {len(videos)} videos in your browser...")
        for v in videos:
            webbrowser.open(v["url"])
    elif action.isdigit():
        v_idx = int(action) - 1
        if 0 <= v_idx < len(videos):
            target_vid = videos[v_idx]
            print(f"Opening '{target_vid['title']}'...")
            webbrowser.open(target_vid["url"])
        else:
            print("Invalid video number.")

def remove_video(data):
    names = list_playlists(data)
    if not names:
        return

    try:
        idx = int(input("\nSelect playlist number: ")) - 1
        if not (0 <= idx < len(names)):
            return
        target_name = names[idx]
    except ValueError:
        return

    videos = data[target_name]
    if not videos:
        print("No videos in this playlist.")
        return

    for i, v in enumerate(videos, 1):
        print(f"{i}. {v['title']}")

    try:
        v_num = int(input("\nEnter video number to remove: ")) - 1
        if 0 <= v_num < len(videos):
            removed = videos.pop(v_num)
            save_data(data)
            print(f"✓ Removed '{removed['title']}' from '{target_name}'.")
        else:
            print("Invalid number.")
    except ValueError:
        print("Invalid number.")

def delete_playlist(data):
    names = list_playlists(data)
    if not names:
        return

    try:
        idx = int(input("\nSelect playlist number to DELETE: ")) - 1
        if not (0 <= idx < len(names)):
            return
        target_name = names[idx]
    except ValueError:
        return

    confirm = input(f"Are you sure you want to delete '{target_name}' and all its videos? (y/n): ").strip().lower()
    if confirm == "y":
        del data[target_name]
        save_data(data)
        print(f"✓ Playlist '{target_name}' deleted.")
    else:
        print("Deletion cancelled.")

def main():
    data = load_data()
    while True:
        print("\n=== YouTube Playlist Manager ===")
        print("1. View Playlists & Open Videos")
        print("2. Create New Playlist")
        print("3. Add Video to Playlist")
        print("4. Remove Video from Playlist")
        print("5. Delete Playlist")
        print("6. Exit")

        choice = input("\nChoose an option (1-6): ").strip()

        if choice == "1":
            view_and_play_playlist(data)
        elif choice == "2":
            create_playlist(data)
        elif choice == "3":
            add_video(data)
        elif choice == "4":
            remove_video(data)
        elif choice == "5":
            delete_playlist(data)
        elif choice == "6":
            print("Exiting Playlist Manager. Happy watching!")
            break
        else:
            print("Invalid option. Please choose 1-6.")

if __name__ == "__main__":
    main()
