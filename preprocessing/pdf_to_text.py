from pypdf import PdfReader  # pyright: ignore[reportMissingImports]
import os

def pdf_to_text(pdf_path, output_path):
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"

    # ensure directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)

    print(f"[✅] Extracted text saved to {output_path}")


if __name__ == "__main__":
    pdf_file = r"data/biology_book.pdf"   # put your PDF here
    output_file = r"data/biology_text.txt"
    pdf_to_text(pdf_file, output_file)
