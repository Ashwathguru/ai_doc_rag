import PyPDF2
import docx

def process_document(filename):
    # Process PDFs
    if filename.endswith('.pdf'):
        return process_pdf(filename)
    # Process DOCX files
    elif filename.endswith('.docx'):
        return process_docx(filename)

def process_pdf(filename):
    with open(filename, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        text = ''
        for page in reader.pages:
            text += page.extract_text()
    return text

def process_docx(filename):
    doc = docx.Document(filename)
    text = ''
    for para in doc.paragraphs:
        text += para.text + '\n'
    return text
