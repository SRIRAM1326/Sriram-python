def count_frequencies(text, ignore_spaces):
    freq_dict = {}
    for char in text:
        if ignore_spaces and char == ' ':
            continue
        freq_dict[char] = freq_dict.get(char, 0) + 1
    return freq_dict

def main():
    while True:
        print("\n=== Character Frequency ===")
        text = input("Enter text (or 'exit' to quit): ")
        
        if text.lower() == 'exit':
            print("Exiting...")
            break
            
        if not text:
            continue
            
        ignore = input("Ignore spaces? (y/n): ").lower()
        ignore_spaces = ignore == 'y'
        
        frequencies = count_frequencies(text, ignore_spaces)
        
        print()
        for char, count in frequencies.items():
            display_char = repr(char) if char == ' ' else char
            print(f"{display_char} : {count}")

if __name__ == "__main__":
    main()
