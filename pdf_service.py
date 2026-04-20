import fitz  # PyMuPDF

def extract_text_by_page(file):
    doc = fitz.open(stream=file.read(), filetype="pdf")

    pages = []

    for i, page in enumerate(doc):
        text = page.get_text()

        # clean text
        text = text.replace("\n", " ")
        text = " ".join(text.split())

        if len(text) < 100:
            continue

        pages.append({
            "page": i + 1,
            "text": text
        })

    return pages