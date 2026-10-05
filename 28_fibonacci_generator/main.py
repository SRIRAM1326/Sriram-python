def generate_fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
        
    sequence = [0, 1]
    for _ in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

def main():
    while True:
        print("\n=== Fibonacci Generator ===")
        
        user_input = input("How many numbers? (or 'exit'): ")
        
        if user_input.lower() == 'exit':
            print("Exiting...")
            break
            
        try:
            count = int(user_input)
            if count <= 0:
                print("Please enter a positive integer.")
                continue
                
            fib_seq = generate_fibonacci(count)
            print("\n" + " ".join(map(str, fib_seq)))
            
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
