import os
from pathlib import Path

try:
    from PIL import Image
    PIL_AVAILABLE = True
except ImportError:
    PIL_AVAILABLE = False

def resize_custom(img, orig_w, orig_h):
    preserve = input("Maintain original aspect ratio? (y/n, default: y): ").strip().lower() != "n"
    try:
        if preserve:
            target_w = int(input(f"Enter target width (original: {orig_w}px): "))
            aspect_ratio = orig_h / orig_w
            target_h = int(target_w * aspect_ratio)
            print(f"Calculated proportional height: {target_h}px")
        else:
            target_w = int(input(f"Enter target width  (original: {orig_w}px): "))
            target_h = int(input(f"Enter target height (original: {orig_h}px): "))
        return (target_w, target_h)
    except ValueError:
        print("Invalid dimensions. Enter integer pixel values.")
        return None

def resize_percentage(img, orig_w, orig_h):
    try:
        pct = float(input("Enter scaling percentage (e.g., 50 for half size, 200 for double): "))
        if pct <= 0:
            print("Percentage must be greater than 0.")
            return None
        target_w = int(orig_w * (pct / 100.0))
        target_h = int(orig_h * (pct / 100.0))
        return (max(1, target_w), max(1, target_h))
    except ValueError:
        print("Invalid number entered.")
        return None

def resize_preset():
    presets = {
        "1": ("Thumbnail", (150, 150)),
        "2": ("Avatar / Profile", (400, 400)),
        "3": ("Instagram Post", (1080, 1080)),
        "4": ("HD 720p", (1280, 720)),
        "5": ("Full HD 1080p", (1920, 1080))
    }
    print("\nAvailable Presets:")
    for k, (name, dims) in presets.items():
        print(f"{k}. {name} ({dims[0]}x{dims[1]})")

    ch = input("Choose preset (1-5): ").strip()
    if ch in presets:
        return presets[ch][1]
    print("Invalid preset choice.")
    return None

def process_image():
    if not PIL_AVAILABLE:
        print("\nError: Pillow is required. Install via: pip install pillow")
        return

    path_str = input("\nEnter path to image file: ").strip().strip('"')
    img_path = Path(path_str)

    if not img_path.exists() or not img_path.is_file():
        print(f"Error: File '{path_str}' does not exist.")
        return

    try:
        with Image.open(img_path) as img:
            orig_w, orig_h = img.size
            img_format = img.format or "PNG"
            print(f"\nImage loaded: {img_path.name}")
            print(f"Current dimensions: {orig_w}px wide × {orig_h}px high (Format: {img_format})")

            print("\nSelect Resizing Mode:")
            print("1. Custom Width/Height")
            print("2. Scale by Percentage")
            print("3. Predefined Standard Presets")

            mode = input("Choose mode (1-3): ").strip()

            new_size = None
            if mode == "1":
                new_size = resize_custom(img, orig_w, orig_h)
            elif mode == "2":
                new_size = resize_percentage(img, orig_w, orig_h)
            elif mode == "3":
                new_size = resize_preset()
            else:
                print("Invalid mode selection.")
                return

            if not new_size:
                return

            # Apply high quality Lanczos interpolation
            resample_filter = getattr(Image.Resampling, "LANCZOS", Image.LANCZOS)
            resized_img = img.resize(new_size, resample=resample_filter)

            default_output = f"{img_path.stem}_resized{img_path.suffix}"
            out_name = input(f"Enter output file name (default: {default_output}): ").strip().strip('"')
            if not out_name:
                out_name = default_output

            out_path = img_path.parent / out_name
            resized_img.save(out_path)

            print(f"\n✓ Image successfully resized and saved!")
            print(f"New Dimensions: {new_size[0]}px × {new_size[1]}px")
            print(f"Saved Path:     {out_path.resolve()}")

    except Exception as e:
        print(f"Error processing image: {e}")

def main():
    while True:
        print("\n=== Image Resizer ===")
        print("1. Resize an Image")
        print("2. Exit")

        choice = input("\nChoose an option (1-2): ").strip()

        if choice == "1":
            process_image()
        elif choice == "2":
            print("Exiting Image Resizer. Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1 or 2.")

if __name__ == "__main__":
    main()
