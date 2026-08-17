import os

def read_text_file(file_path):
    """Read .txt resume file"""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return ""


def load_resumes(resume_folder):
    """Load all resumes from folder"""
    resumes = {}

    for filename in os.listdir(resume_folder):
        file_path = os.path.join(resume_folder, filename)

        if filename.endswith(".txt"):
            text = read_text_file(file_path)
            resumes[filename] = text

    return resumes