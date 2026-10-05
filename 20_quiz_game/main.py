def main():
    questions = [
        {
            "question": "Which keyword is used to define a function in Python?",
            "options": ["A. function", "B. def", "C. func", "D. define"],
            "answer": "B"
        },
        {
            "question": "Which of the following is a mutable data type?",
            "options": ["A. tuple", "B. string", "C. list", "D. int"],
            "answer": "C"
        },
        {
            "question": "What is the output of 3 ** 2?",
            "options": ["A. 6", "B. 9", "C. 5", "D. 12"],
            "answer": "B"
        },
        {
            "question": "Which method removes whitespace from the beginning and end of a string?",
            "options": ["A. strip()", "B. trim()", "C. len()", "D. replace()"],
            "answer": "A"
        },
        {
            "question": "How do you start a single-line comment in Python?",
            "options": ["A. //", "B. /*", "C. <!--", "D. #"],
            "answer": "D"
        },
        {
            "question": "What does len() do?",
            "options": ["A. Returns the type", "B. Returns length of an object", "C. Reverses a list", "D. Sorts a list"],
            "answer": "B"
        },
        {
            "question": "Which of the following is not a valid variable name?",
            "options": ["A. my_var", "B. _myvar", "C. 2myvar", "D. myVar"],
            "answer": "C"
        },
        {
            "question": "What is the result of 10 % 3?",
            "options": ["A. 3.33", "B. 3", "C. 1", "D. 0"],
            "answer": "C"
        },
        {
            "question": "How do you insert an element at a specific index in a list?",
            "options": ["A. add()", "B. append()", "C. insert()", "D. extend()"],
            "answer": "C"
        },
        {
            "question": "What is the file extension for Python files?",
            "options": ["A. .py", "B. .python", "C. .pt", "D. .pyt"],
            "answer": "A"
        }
    ]

    while True:
        print("\n=== Python Quiz ===")
        score = 0
        
        for i, q in enumerate(questions, 1):
            print(f"\nQuestion {i}:")
            print(q["question"])
            for opt in q["options"]:
                print(opt)
                
            while True:
                ans = input("\nYour answer: ").strip().upper()
                if ans in ['A', 'B', 'C', 'D']:
                    break
                print("Invalid choice. Please choose A, B, C, or D.")
                
            if ans == q["answer"]:
                print("\nCorrect!")
                score += 1
            else:
                print(f"\nWrong! The correct answer was {q['answer']}.")
                
        percentage = (score / len(questions)) * 100
        print(f"\n=== Quiz Finished ===")
        print(f"Your Score: {score}/{len(questions)}")
        print(f"Percentage: {percentage:.2f}%")
        
        play_again = input("\nPlay again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
