import string

def main():
    original_text = ""
    cleaned_text = ""
    
    while True:
        print("\n=== Text Cleaner ===")
        print("1. Enter Text")
        print("2. Remove Extra Spaces")
        print("3. Remove Punctuation")
        print("4. Convert Lowercase")
        print("5. Convert Uppercase")
        print("6. Clean Everything")
        print("7. Exit")
        
        choice = input("\nChoose: ")
        
        if choice == '1':
            original_text = input("\nEnter text:\n")
            cleaned_text = original_text
            print("\nText captured.")
            
        elif choice == '2':
            if not cleaned_text:
                print("Please enter text first (Option 1).")
                continue
            cleaned_text = " ".join(cleaned_text.split())
            print("\nCleaned:\n" + cleaned_text)
            
        elif choice == '3':
            if not cleaned_text:
                print("Please enter text first (Option 1).")
                continue
            translator = str.maketrans('', '', string.punctuation)
            cleaned_text = cleaned_text.translate(translator)
            print("\nCleaned:\n" + cleaned_text)
            
        elif choice == '4':
            if not cleaned_text:
                print("Please enter text first (Option 1).")
                continue
            cleaned_text = cleaned_text.lower()
            print("\nCleaned:\n" + cleaned_text)
            
        elif choice == '5':
            if not cleaned_text:
                print("Please enter text first (Option 1).")
                continue
            cleaned_text = cleaned_text.upper()
            print("\nCleaned:\n" + cleaned_text)
            
        elif choice == '6':
            if not cleaned_text:
                print("Please enter text first (Option 1).")
                continue
            
            translator = str.maketrans('', '', string.punctuation)
            cleaned_text = cleaned_text.translate(translator)
            cleaned_text = cleaned_text.lower()
            cleaned_text = " ".join(cleaned_text.split())
            
            print("\nOriginal:\n" + original_text)
            print("\nCleaned:\n" + cleaned_text)
            
        elif choice == '7':
            print("Exiting...")
            break
            
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
