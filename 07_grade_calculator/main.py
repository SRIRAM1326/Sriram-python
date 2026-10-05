def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"

def main():
    print("=== Grade Calculator ===\n")
    name = input("Student Name: ")
    
    subjects = []
    while True:
        try:
            num_subjects = int(input("\nHow many subjects? "))
            if num_subjects > 0:
                break
            print("Please enter a number greater than 0.")
        except ValueError:
            print("Invalid input. Enter a number.")
            
    marks = []
    print("\nEnter marks for each subject (0-100):")
    for i in range(num_subjects):
        while True:
            try:
                subject_name = input(f"Subject {i+1} Name: ")
                mark = float(input(f"{subject_name} Marks: "))
                if 0 <= mark <= 100:
                    subjects.append(subject_name)
                    marks.append(mark)
                    break
                else:
                    print("Marks must be between 0 and 100.")
            except ValueError:
                print("Invalid input. Enter numeric marks.")

    total_marks = sum(marks)
    max_possible_marks = num_subjects * 100
    percentage = (total_marks / max_possible_marks) * 100
    grade = calculate_grade(percentage)
    
    print("\n" + "="*24)
    print("=== Grade Calculator ===")
    print("="*24)
    print(f"\nStudent Name: {name}\n")
    
    for subject, mark in zip(subjects, marks):
        print(f"{subject}: {mark}")
        
    print(f"\nTotal: {total_marks}/{max_possible_marks}")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {grade}")

if __name__ == "__main__":
    main()
