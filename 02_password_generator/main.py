import secrets
import string

def generate_password(length):
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special = string.punctuation

    all_characters = uppercase + lowercase + digits + special
    
    password = ''.join(secrets.choice(all_characters) for _ in range(length))
    return password

def main():
    while True:
        print("\n=== Password Generator ===")
        print("1. Generate Password")
        print("2. Exit")
        
        choice = input("\nChoose an option: ")
        
        if choice == '2':
            print("Exiting...")
            break
            
        if choice == '1':
            try:
                length = int(input("\nPassword length: "))
                if length < 4:
                    print("Please enter a length of at least 4.")
                    continue
                
                password = generate_password(length)
                print(f"\nGenerated Password:\n{password}")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
