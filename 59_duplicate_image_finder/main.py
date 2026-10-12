import os
import hashlib
from pathlib import Path
from collections import defaultdict

IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".svg", ".tiff", ".ico"}

def get_file_hash(filepath, chunk_size=65536):
    """Calculates SHA-256 hash by streaming chunks to avoid excessive memory usage."""
    hasher = hashlib.sha256()
    try:
        with open(filepath, "rb") as f:
            while chunk := f.read(chunk_size):
                hasher.update(chunk)
        return hasher.hexdigest()
    except Exception as e:
        print(f"Error reading '{filepath}': {e}")
        return None

def scan_directory(dir_path, recursive=True):
    folder = Path(dir_path)
    if not folder.exists() or not folder.is_dir():
        print(f"Error: Directory '{dir_path}' does not exist.")
        return {}

    pattern = "**/*" if recursive else "*"
    all_files = [f for f in folder.glob(pattern) if f.is_file() and f.suffix.lower() in IMAGE_EXTENSIONS]

    print(f"\nScanning {len(all_files)} image file(s) for duplicates...")

    # Phase 1: Group by file size in bytes
    size_groups = defaultdict(list)
    for f in all_files:
        try:
            sz = f.stat().st_size
            size_groups[sz].append(f)
        except Exception:
            continue

    # Filter out sizes with only 1 file
    potential_candidates = [paths for paths in size_groups.values() if len(paths) > 1]

    # Phase 2: Compute SHA-256 hashes for candidates
    hash_groups = defaultdict(list)
    for group in potential_candidates:
        for f in group:
            h = get_file_hash(f)
            if h:
                hash_groups[h].append(f)

    # Filter for true duplicates (hash count > 1)
    duplicates = {h: paths for h, paths in hash_groups.items() if len(paths) > 1}
    return duplicates

def format_size(size_bytes):
    if size_bytes >= 1024 * 1024:
        return f"{size_bytes / (1024 * 1024):.2f} MB"
    elif size_bytes >= 1024:
        return f"{size_bytes / 1024:.2f} KB"
    return f"{size_bytes} Bytes"

def display_duplicates(duplicates):
    if not duplicates:
        print("\n✓ Great news! No duplicate images found in the target directory.")
        return 0, 0

    total_wasted_bytes = 0
    total_dupes_count = 0

    print("\n" + "=" * 70)
    print("                     DUPLICATE IMAGES DETECTED")
    print("=" * 70)

    for cluster_id, (h, paths) in enumerate(duplicates.items(), 1):
        file_sz = paths[0].stat().st_size
        wasted_for_group = file_sz * (len(paths) - 1)
        total_wasted_bytes += wasted_for_group
        total_dupes_count += (len(paths) - 1)

        print(f"\n[Group {cluster_id}] SHA-256: {h[:16]}... ({format_size(file_sz)} each)")
        print(f"  Keep (Original): {paths[0]}")
        for dup in paths[1:]:
            print(f"  Duplicate:       {dup}")

    print("\n" + "=" * 70)
    print(f"Summary: {total_dupes_count} duplicate file(s) found across {len(duplicates)} group(s).")
    print(f"Potential Space Reclaimable: {format_size(total_wasted_bytes)}")
    print("=" * 70)

    return total_dupes_count, total_wasted_bytes

def delete_duplicates(duplicates):
    if not duplicates:
        return

    print("\nCleanup Options:")
    print("1. Keep first file in each group and delete all extra duplicates")
    print("2. Cancel (Do not delete anything)")

    ch = input("\nChoose an option (1-2): ").strip()
    if ch != "1":
        print("No files deleted.")
        return

    confirm = input("Are you sure? This permanently deletes redundant files! (y/n): ").strip().lower()
    if confirm != "y":
        print("Deletion aborted.")
        return

    deleted_count = 0
    for h, paths in duplicates.items():
        # Keep paths[0], delete paths[1:]
        for extra in paths[1:]:
            try:
                extra.unlink()
                print(f"Deleted: {extra.name}")
                deleted_count += 1
            except Exception as e:
                print(f"Error deleting {extra.name}: {e}")

    print(f"\n✓ Successfully removed {deleted_count} redundant duplicate image(s)!")

def main():
    while True:
        print("\n=== Duplicate Image Finder ===")
        print("1. Scan Directory for Duplicate Images")
        print("2. Exit")

        choice = input("\nChoose an option (1-2): ").strip()

        if choice == "1":
            target_dir = input("\nEnter directory path to scan: ").strip().strip('"')
            rec = input("Include subdirectories recursively? (y/n, default: y): ").strip().lower() != "n"
            duplicates = scan_directory(target_dir, recursive=rec)
            count, _ = display_duplicates(duplicates)
            if count > 0:
                delete_duplicates(duplicates)
        elif choice == "2":
            print("Exiting Duplicate Image Finder. Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1 or 2.")

if __name__ == "__main__":
    main()
