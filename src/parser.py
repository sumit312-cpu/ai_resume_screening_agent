import os
from pypdf import PdfReader
from docx import Document

def read_txt(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def read_pdf(file_path):
    text = ""
    reader = PdfReader(file_path)
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text

def read_docx(file_path):
    doc = Document(file_path)
    return "\n".join([para.text for para in doc.paragraphs])

def parse_resume(file_path):
    ext = file_path.split(".")[-1].lower()

    if ext == "txt":
        return read_txt(file_path)
    elif ext == "pdf":
        return read_pdf(file_path)
    elif ext == "docx":
        return read_docx(file_path)
    else:
        print(f"Unsupported file format: {file_path}")
        return ""