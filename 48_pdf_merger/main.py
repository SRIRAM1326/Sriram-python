import os
from pathlib import Path

PDF_LIB = None
try:
    import pypdf
    PDF_LIB = "pypdf"
except ImportError:
    try:
        import PyPDF2 as pypdf
        PDF_LIB = "PyPDF2"
    except ImportError:
        pass

def merge_pdfs(file_paths, output_path):
    if not PDF_LIB:
        print("\nError: A PDF library is required. Install via: pip install pypdf")
        return False

    merger = pypdf.PdfMerger()
    total_pages = 0

    print("\nProcessing PDF files...")
    for path in file_paths:
        p = Path(path)
        if not p.exists() or not p.is_file():
            print(f"Skipping: '{p}' (file not found)")
            continue
        try:
            reader = pypdf.PdfReader(str(p))
            num_pages = len(reader.pages)
            merger.append(str(p))
            total_pages += num_pages
            print(f"  + Added '{p.name}' ({num_pages} page(s))")
        except Exception as e:
            print(f"  ✗ Error reading '{p.name}': {e}")

    if total_pages == 0:
        print("Error: No valid PDF pages were found to merge.")
        merger.close()
        return False

    try:
        out_p = Path(output_path)
        if not out_p.suffix.lower() == ".pdf":
            out_p = out_p.with_suffix(".pdf")

        merger.write(str(out_p))
        merger.close()
        print(f"\n✓ Successfully merged {len(file_paths)} files ({total_pages} total pages) into:")
        print(f"  {out_p.resolve()}")
        return True
    except Exception as e:
        print(f"Error saving merged PDF: {e}")
        merger.close()
        return False

def merge_by_list():
    print("\nEnter paths of PDF files to merge (one per line). Enter a blank line when done:")
    pdf_list = []
    idx = 1
    while True:
        line = input(f"File {idx}: ").strip().strip('"')
        if not line:
            break
        pdf_list.append(line)
        idx += 1

    if len(pdf_list) < 2:
        print("Please enter at least 2 PDF files to merge.")
        return

    out_file = input("Enter output PDF filename (default: merged_document.pdf): ").strip().strip('"')
    if not out_file:
        out_file = "merged_document.pdf"

    merge_pdfs(pdf_list, out_file)

def merge_by_folder():
    folder_str = input("\nEnter directory path containing PDF files: ").strip().strip('"')
    folder = Path(folder_str)

    if not folder.exists() or not folder.is_dir():
        print("Invalid directory.")
        return

    pdf_files = sorted(list(folder.glob("*.pdf")), key=lambda f: f.name.lower())
    if not pdf_files:
        print("No .pdf files found in this directory.")
        return

    print(f"\nFound {len(pdf_files)} PDF files in directory:")
    for i, f in enumerate(pdf_files, 1):
        print(f"  {i}. {f.name}")

    confirm = input("\nMerge these files in this order? (y/n, default: y): ").strip().lower() != "n"
    if not confirm:
        print("Cancelled.")
        return

    out_file = input("Enter output PDF name (default: merged_all.pdf): ").strip().strip('"')
    if not out_file:
        out_file = "merged_all.pdf"

    out_path = folder / out_file
    merge_pdfs([str(p) for p in pdf_files], str(out_path))

def main():
    while True:
        print("\n=== PDF Merger ===")
        print("1. Merge Selected PDF Files")
        print("2. Merge All PDFs from a Directory")
        print("3. Exit")

        choice = input("\nChoose an option (1-3): ").strip()

        if choice == "1":
            merge_by_list()
        elif choice == "2":
            merge_by_folder()
        elif choice == "3":
            print("Exiting PDF Merger. Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()
