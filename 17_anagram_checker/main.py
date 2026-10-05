def is_anagram(text1, text2):
    t1_clean = text1.replace(" ", "").lower()
    t2_clean = text2.replace(" ", "").lower()
    return sorted(t1_clean) == sorted(t2_clean)

def main():
    while True:
        print("\n=== Anagram Checker ===")
        print("Type 'exit' to quit.")
        
        text1 = input("First text: ")
        if text1.lower() == 'exit':
            print("Exiting...")
            break
            
        text2 = input("Second text: ")
        if text2.lower() == 'exit':
            print("Exiting...")
            break
            
        if is_anagram(text1, text2):
            print("\nResult: They are anagrams.")
        else:
            print("\nResult: They are not anagrams.")

if __name__ == "__main__":
    main()
