import os

try:
    import qrcode
    QRCODE_AVAILABLE = True
except ImportError:
    QRCODE_AVAILABLE = False

def print_ascii_qr(qr):
    """Prints QR code using Unicode block characters for instant camera scanning."""
    matrix = qr.get_matrix()
    print("\nScan with your phone camera:")
    for row in matrix:
        line = "".join("  " if col else "██" for col in row)
        print(line)
    print()

def generate_qr():
    if not QRCODE_AVAILABLE:
        print("\nError: The 'qrcode' package is required. Install via: pip install qrcode[pil]")
        return

    data = input("\nEnter the text or URL to encode: ").strip()
    if not data:
        print("Input data cannot be empty.")
        return

    filename = input("Enter output PNG filename (default: qrcode.png): ").strip()
    if not filename:
        filename = "qrcode.png"
    elif not filename.lower().endswith(".png"):
        filename += ".png"

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Print ASCII directly to console
    print_ascii_qr(qr)

    # Save PNG image file
    try:
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(filename)
        abs_path = os.path.abspath(filename)
        print(f"✓ QR Code saved successfully as: {filename}")
        print(f"  Full path: {abs_path}")
    except Exception as e:
        print(f"Error saving image: {e}")

def main():
    while True:
        print("\n=== QR Code Generator ===")
        print("1. Generate QR Code (Terminal + PNG)")
        print("2. Exit")

        choice = input("\nChoose an option (1-2): ").strip()

        if choice == "1":
            generate_qr()
        elif choice == "2":
            print("Exiting QR Code Generator. Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1 or 2.")

if __name__ == "__main__":
    main()
