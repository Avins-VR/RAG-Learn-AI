import fitz  # PyMuPDF

def extract_text_by_page(file):
    doc = fitz.open(stream=file.read(), filetype="pdf")
    
    pages = []
    
    for i, page in enumerate(doc):
        text = page.get_text()
        pages.append({
            "page": i + 1,
            "text": text
        })
    
    return pages