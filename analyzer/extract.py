import pdfplumber

def extract_text_from_pdf(file_stream):
    pages_text = []

    with pdfplumber.open(file_stream) as pdf:
        for page in pdf.pages:
            extracted_text = page.extract_text()
            if extracted_text:   
                pages_text.append(extracted_text)

    return "\n".join(pages_text)
