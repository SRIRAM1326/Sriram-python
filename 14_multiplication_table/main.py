def generate_table(number, limit):
    print()
    for i in range(1, limit + 1):
        print(f"{number} x {i} = {number * i}")

def main():
    while True:
        print("\n=== Multiplication Table ===")
        print("Type 'exit' in any prompt to quit.\n")
        
        user_num = input("Enter number: ")
        if user_num.lower() == 'exit':
            print("Exiting...")
            break
            
        user_limit = input("Enter limit: ")
        if user_limit.lower() == 'exit':
            print("Exiting...")
            break
            
        try:
            number = int(user_num)
            limit = int(user_limit)
            
            if limit < 1:
                print("Limit must be at least 1.")
                continue
                
            generate_table(number, limit)
            
        except ValueError:
            print("Invalid input. Please enter valid integers.")

if __name__ == "__main__":
    main()
