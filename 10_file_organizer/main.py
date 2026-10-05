import os
import shutil
from pathlib import Path

EXTENSION_MAP = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg'],
    'Documents': ['.pdf', '.doc', '.docx', '.txt', '.xls', '.xlsx', '.ppt', '.pptx', '.csv'],
    'Videos': ['.mp4', '.avi', '.mkv', '.mov', '.wmv'],
    'Audio': ['.mp3', '.wav', '.flac', '.aac', '.m4a'],
    'Python': ['.py', '.ipynb'],
    'Archives': ['.zip', '.tar', '.gz', '.rar', '.7z']
}

def get_folder_name(extension):
    for folder, extensions in EXTENSION_MAP.items():
        if extension.lower() in extensions:
            return folder
    return 'Others'

def organize_files(directory_path):
    target_dir = Path(directory_path)
    
    if not target_dir.exists() or not target_dir.is_dir():
        print(f"Error: Directory '{directory_path}' does not exist or is not a valid directory.")
        return
        
    print(f"\nOrganizing files in: {target_dir.absolute()}\n")
    
    moved_count = 0
    
    for item in target_dir.iterdir():
        if item.is_dir():
            continue
            
        extension = item.suffix
        if not extension:
            folder_name = 'Others'
        else:
            folder_name = get_folder_name(extension)
            
        dest_folder = target_dir / folder_name
        dest_folder.mkdir(exist_ok=True)
        
        dest_path = dest_folder / item.name
        
        if dest_path.exists():
            print(f"Skipping '{item.name}', already exists in {folder_name}/")
            continue
            
        try:
            shutil.move(str(item), str(dest_path))
            print(f"Moved {item.name} -> {folder_name}/")
            moved_count += 1
        except Exception as e:
            print(f"Error moving {item.name}: {e}")
            
    print(f"\nSummary: Successfully moved {moved_count} file(s).")

def main():
    print("=== File Organizer ===")
    dir_path = input("Enter the directory path to organize: ")
    organize_files(dir_path)

if __name__ == "__main__":
    main()
