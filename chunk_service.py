def chunk_text(pages, chunk_size=500):
    chunks = []
    
    for page in pages:
        text = page["text"]
        page_num = page["page"]
        
        for i in range(0, len(text), chunk_size):
            chunk = text[i:i+chunk_size]
            
            chunks.append({
                "page": page_num,
                "text": chunk
            })
    
    return chunks