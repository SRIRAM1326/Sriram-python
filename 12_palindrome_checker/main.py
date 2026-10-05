import string

def is_palindrome(text):
    cleaned_text = ""
    for char in text.lower():
        if char not in string.punctuation and char != " ":
            cleaned_text += char
            
    return cleaned_text == cleaned_text[::-1]

def main():
    while True:
        print("\n=== Palindrome Checker ===")
        text = input("Enter text (or type 'exit' to quit): ")
        
        if text.lower() == 'exit':
            print("Exiting...")
            break
            
        if not text.strip():
            print("Please enter a valid string.")
            continue
            
        if is_palindrome(text):
            print("\nResult: This is a palindrome.")
        else:
            print("\nResult: This is not a palindrome.")

if __name__ == "__main__":
    main()
