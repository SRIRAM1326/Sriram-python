def validate_pin(pin):
    if len(pin) not in [4, 6]:
        return False, "Invalid length. PIN must be 4 or 6 digits."
    if not pin.isdigit():
        return False, "Invalid characters. PIN must contain only numbers."
    return True, "Valid PIN."

def main():
    while True:
        print("\n=== PIN Validator ===")
        print("Type 'exit' to quit.")
        
        pin = input("Enter PIN: ")
        
        if pin.lower() == 'exit':
            print("Exiting...")
            break
            
        is_valid, message = validate_pin(pin)
        print(f"\n{message}")

if __name__ == "__main__":
    main()
