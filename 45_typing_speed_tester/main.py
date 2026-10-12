import time
import random

PROMPTS = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is an interpreted, high-level, and general-purpose programming language.",
    "Practice makes progress, and consistency is the key to mastering code.",
    "Simplicity is the soul of efficiency, especially when designing robust software.",
    "Artificial intelligence and automation are transforming the modern technological landscape.",
    "Data structures and algorithms form the bedrock of problem solving in computer science."
]

def calculate_accuracy(original, typed):
    orig_chars = list(original)
    typed_chars = list(typed)

    correct = 0
    total = len(original)

    for i in range(min(len(orig_chars), len(typed_chars))):
        if orig_chars[i] == typed_chars[i]:
            correct += 1

    accuracy = (correct / total) * 100 if total > 0 else 0
    return round(accuracy, 2), correct, total

def get_performance_grade(net_wpm):
    if net_wpm >= 80:
        return "Professional / Master typist 🚀"
    elif net_wpm >= 60:
        return "Fast / Advanced typist ⚡"
    elif net_wpm >= 40:
        return "Fluent / Intermediate typist 👍"
    elif net_wpm >= 25:
        return "Average / Developing typist ✍️"
    else:
        return "Beginner / Needs Practice 🌱"

def run_test():
    prompt = random.choice(PROMPTS)
    print("\n--- Typing Speed Test ---")
    print("Prepare yourself. The test begins after the countdown!\n")

    for i in range(3, 0, -1):
        print(f"Starting in {i}...", end="\r", flush=True)
        time.sleep(1)
    print("GO! Type the text below exactly as shown:\n")

    print("-" * 65)
    print(prompt)
    print("-" * 65)

    start_time = time.perf_counter()
    typed = input("\n> ")
    end_time = time.perf_counter()

    elapsed_seconds = end_time - start_time
    elapsed_minutes = elapsed_seconds / 60.0

    # Standard WPM formula: (all typed chars / 5) / minutes
    total_chars = len(typed)
    gross_wpm = (total_chars / 5) / elapsed_minutes if elapsed_minutes > 0 else 0

    accuracy, correct_chars, expected_chars = calculate_accuracy(prompt, typed)
    errors = max(0, expected_chars - correct_chars)

    # Net WPM penalizes uncorrected errors
    net_wpm = max(0, gross_wpm * (accuracy / 100.0))

    print("\n" + "=" * 45)
    print("              TEST RESULTS")
    print("=" * 45)
    print(f"Time Taken:      {elapsed_seconds:.2f} seconds")
    print(f"Characters:      {total_chars} typed ({correct_chars}/{expected_chars} correct)")
    print(f"Accuracy:        {accuracy}%")
    print(f"Gross Speed:     {gross_wpm:.1f} WPM")
    print(f"Net Speed:       {net_wpm:.1f} WPM")
    print(f"Rating:          {get_performance_grade(net_wpm)}")
    print("=" * 45)

def main():
    while True:
        print("\n=== Typing Speed Tester ===")
        print("1. Start Typing Test")
        print("2. Exit")

        choice = input("\nChoose an option (1-2): ").strip()

        if choice == "1":
            run_test()
        elif choice == "2":
            print("Thanks for practicing your typing! Keep it up.")
            break
        else:
            print("Invalid option. Please choose 1 or 2.")

if __name__ == "__main__":
    main()
