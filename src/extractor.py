import re

def extract_name(text):
    match = re.search(r"Name:\s*(.*)", text)
    return match.group(1).strip() if match else ""


def extract_email(text):
    match = re.search(r"Email:\s*(.*)", text)
    return match.group(1).strip() if match else ""


def extract_skills(text):
    match = re.search(r"Skills:\s*(.*)", text)
    if match:
        skills = match.group(1)
        return [skill.strip() for skill in skills.split(",")]
    return []


def extract_experience(text):
    match = re.search(r"Experience:\s*(.*)", text)
    return match.group(1).strip() if match else ""


def extract_education(text):
    match = re.search(r"Education:\s*(.*)", text)
    return match.group(1).strip() if match else ""


def extract_all(text):
    return {
        "name": extract_name(text),
        "email": extract_email(text),
        "skills": extract_skills(text),
        "experience": extract_experience(text),
        "education": extract_education(text),
    }