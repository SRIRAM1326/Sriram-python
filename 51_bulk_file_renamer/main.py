import os
from pathlib import Path

def get_target_files(dir_path, filter_ext=""):
    folder = Path(dir_path)
    if not folder.exists() or not folder.is_dir():
        print("Invalid directory path.")
        return []

    files = [f for f in folder.iterdir() if f.is_file()]
    if filter_ext:
        if not filter_ext.startswith("."):
            filter_ext = "." + filter_ext
        files = [f for f in files if f.suffix.lower() == filter_ext.lower()]

    return sorted(files, key=lambda f: f.name.lower())

def execute_renaming(plan):
    if not plan:
        print("No files to rename.")
        return

    print("\n" + "=" * 65)
    print(f"{'#':<4} | {'Current Name':<28} -> {'New Name'}")
    print("=" * 65)
    for i, (old_path, new_name) in enumerate(plan, 1):
        print(f"{i:<4} | {old_path.name:<28} -> {new_name}")
    print("=" * 65)
    print(f"Total: {len(plan)} file(s) queued for renaming.")

    confirm = input("\nProceed with renaming? This action modifies files! (y/n): ").strip().lower()
    if confirm != "y":
        print("Renaming cancelled. No files were changed.")
        return

    success_count = 0
    for old_path, new_name in plan:
        target_path = old_path.parent / new_name
        if target_path.exists() and target_path != old_path:
            print(f"Skipping '{old_path.name}': Target '{new_name}' already exists.")
            continue
        try:
            old_path.rename(target_path)
            success_count += 1
        except Exception as e:
            print(f"Error renaming '{old_path.name}': {e}")

    print(f"\n✓ Completed! Successfully renamed {success_count} file(s).")

def rename_prefix(files):
    prefix = input("Enter prefix to prepend (e.g., '2026_'): ")
    plan = [(f, f"{prefix}{f.name}") for f in files]
    execute_renaming(plan)

def rename_suffix(files):
    suffix = input("Enter suffix to append before extension (e.g., '_backup'): ")
    plan = [(f, f"{f.stem}{suffix}{f.suffix}") for f in files]
    execute_renaming(plan)

def rename_replace(files):
    target = input("Text to find: ")
    if not target:
        print("Search string cannot be empty.")
        return
    replacement = input("Text to replace with: ")
    plan = [(f, f.name.replace(target, replacement)) for f in files if target in f.name]
    if not plan:
        print(f"No files contained '{target}'.")
        return
    execute_renaming(plan)

def rename_numbering(files):
    base_name = input("Enter base name (e.g. 'Photo_'): ").strip()
    digits = int(input("Enter number of digits for padding (e.g. 2 for 01, 3 for 001): ") or "2")
    plan = []
    for i, f in enumerate(files, 1):
        num_str = str(i).zfill(digits)
        new_name = f"{base_name}{num_str}{f.suffix}"
        plan.append((f, new_name))
    execute_renaming(plan)

def rename_case(files):
    print("1. All lowercase (e.g., PHOTO.JPG -> photo.jpg)")
    print("2. ALL UPPERCASE (e.g., photo.jpg -> PHOTO.JPG)")
    ch = input("Choose (1-2): ").strip()
    if ch == "1":
        plan = [(f, f.name.lower()) for f in files]
    elif ch == "2":
        plan = [(f, f.name.upper()) for f in files]
    else:
        print("Invalid choice.")
        return
    execute_renaming(plan)

def main():
    while True:
        print("\n=== Bulk File Renamer ===")
        dir_path = input("\nEnter directory path to organize (or 'q' to quit): ").strip().strip('"')
        if dir_path.lower() == "q":
            print("Exiting Bulk File Renamer. Goodbye!")
            break

        ext_filter = input("Filter by extension (e.g. .jpg or press Enter for all files): ").strip()
        files = get_target_files(dir_path, ext_filter)

        if not files:
            print("No matching files found in this directory.")
            continue

        print(f"\nFound {len(files)} file(s). Select renaming strategy:")
        print("1. Add Prefix")
        print("2. Add Suffix")
        print("3. Find and Replace Text")
        print("4. Sequential Numbering Sequence")
        print("5. Lowercase / Uppercase Normalization")
        print("6. Cancel & Choose Another Folder")

        mode = input("\nChoose an option (1-6): ").strip()

        if mode == "1":
            rename_prefix(files)
        elif mode == "2":
            rename_suffix(files)
        elif mode == "3":
            rename_replace(files)
        elif mode == "4":
            rename_numbering(files)
        elif mode == "5":
            rename_case(files)
        elif mode == "6":
            continue
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
