def main():
    while True:
        print("\n=== Text Case Converter ===")
        text = input("Enter text (or 'exit' to quit):\n")
        
        if text.strip().lower() == 'exit':
            print("Exiting...")
            break
            
        if not text.strip():
            print("Please enter valid text.")
            continue
            
        print("\nUppercase:")
        print(text.upper())
        
        print("\nLowercase:")
        print(text.lower())
        
        print("\nTitle Case:")
        print(text.title())
        
        print("\nSentence case:")
        sentence_case = text.capitalize()
        print(sentence_case)

if __name__ == "__main__":
    main()
