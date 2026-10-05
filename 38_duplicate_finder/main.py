import os
import hashlib
from pathlib import Path

def get_file_hash(filepath, chunk_size=8192):
    hasher = hashlib.md5()
    try:
        with open(filepath, 'rb') as f:
            while chunk := f.read(chunk_size):
                hasher.update(chunk)
        return hasher.hexdigest()
    except Exception:
        return None

def find_duplicates(folder_path):
    target_dir = Path(folder_path)
    
    if not target_dir.exists() or not target_dir.is_dir():
        print("Error: Invalid folder path.")
        return
        
    print(f"\nScanning folder: {target_dir.absolute()} ...\n")
    
    hashes = {}
    
    for item in target_dir.rglob('*'):
        if item.is_file():
            file_hash = get_file_hash(item)
            if file_hash:
                if file_hash in hashes:
                    hashes[file_hash].append(str(item))
                else:
                    hashes[file_hash] = [str(item)]
                    
    duplicates = {h: paths for h, paths in hashes.items() if len(paths) > 1}
    
    if not duplicates:
        print("No duplicate files found.")
        return
        
    print("Duplicate Files Found:\n")
    group_num = 1
    for h, paths in duplicates.items():
        print(f"Group {group_num}:")
        for p in paths:
            print(f"  {p}")
        print()
        group_num += 1
        
    print(f"Total duplicate groups: {len(duplicates)}")
    print("\nNote: Files were only reported, not deleted.")

def main():
    while True:
        print("\n=== Duplicate Finder ===")
        folder = input("Enter folder path to scan (or 'exit'): ")
        
        if folder.lower() == 'exit':
            print("Exiting...")
            break
            
        find_duplicates(folder)

if __name__ == "__main__":
    main()
