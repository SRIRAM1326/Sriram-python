def analyze_text(text):
    words = text.split()
    total_words = len(words)
    total_chars = len(text)
    total_chars_no_spaces = len(text.replace(" ", ""))
    sentences = text.count(".") + text.count("!") + text.count("?")
    
    if sentences == 0 and text.strip():
        sentences = 1
        
    return total_words, total_chars, total_chars_no_spaces, sentences

def main():
    while True:
        print("\n=== Word Counter ===")
        text = input("Enter text (or 'exit' to quit):\n")
        
        if text.strip().lower() == 'exit':
            print("Exiting...")
            break
            
        if not text.strip():
            print("Please enter some valid text.")
            continue
            
        words, chars, chars_no_spaces, sentences = analyze_text(text)
        
        print(f"\nWords: {words}")
        print(f"Characters: {chars}")
        print(f"Characters without spaces: {chars_no_spaces}")
        print(f"Sentences: {sentences}")

if __name__ == "__main__":
    main()
