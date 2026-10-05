import os

def create_file():
    filename = input("Enter filename to create (e.g., test.txt): ").strip()
    if not filename:
        return
    try:
        with open(filename, 'w') as f:
            pass
        print(f"File '{filename}' created successfully.")
    except Exception as e:
        print(f"Error creating file: {e}")

def read_file():
    filename = input("Enter filename to read: ").strip()
    if not os.path.exists(filename):
        print("File does not exist.")
        return
    try:
        with open(filename, 'r') as f:
            content = f.read()
        print("\n--- File Content ---")
        print(content if content else "(File is empty)")
        print("--------------------")
    except Exception as e:
        print(f"Error reading file: {e}")

def append_text():
    filename = input("Enter filename to append to: ").strip()
    if not os.path.exists(filename):
        print("File does not exist.")
        return
    text = input("Enter text to append: ")
    try:
        with open(filename, 'a') as f:
            f.write(text + "\n")
        print("Text appended successfully.")
    except Exception as e:
        print(f"Error appending to file: {e}")

def overwrite_file():
    filename = input("Enter filename to overwrite: ").strip()
    if not os.path.exists(filename):
        print("File does not exist.")
        return
    text = input("Enter text to overwrite with: ")
    try:
        with open(filename, 'w') as f:
            f.write(text + "\n")
        print("File overwritten successfully.")
    except Exception as e:
        print(f"Error overwriting file: {e}")

def file_information():
    filename = input("Enter filename: ").strip()
    if not os.path.exists(filename):
        print("File does not exist.")
        return
    try:
        size = os.path.getsize(filename)
        print(f"\nFile: {filename}")
        print(f"Size: {size} bytes")
    except Exception as e:
        print(f"Error getting file info: {e}")

def main():
    while True:
        print("\n=== Text File Editor ===")
        print("1. Create File")
        print("2. Read File")
        print("3. Append Text")
        print("4. Overwrite File")
        print("5. File Information")
        print("6. Exit")
        
        choice = input("\nChoose: ")
        
        if choice == '1':
            create_file()
        elif choice == '2':
            read_file()
        elif choice == '3':
            append_text()
        elif choice == '4':
            overwrite_file()
        elif choice == '5':
            file_information()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
