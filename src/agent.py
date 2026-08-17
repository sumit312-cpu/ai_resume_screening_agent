import os
from src.parser import parse_resume

def load_resumes(folder_path):
    resumes = []

    for file in os.listdir(folder_path):
        if file.endswith((".txt", ".pdf", ".docx")):
            full_path = os.path.join(folder_path, file)
            text = parse_resume(full_path)
            resumes.append((file, text))

    return resumes