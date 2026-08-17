import re

# ✅ Name extraction
def extract_name(text):
    match = re.search(r"Name:\s*(.*)", text)
    if match:
        return match.group(1).strip()

    # Fallback (for PDF/DOCX)
    lines = text.split("\n")
    for line in lines[:10]:  # check first few lines
        line = line.strip()
        if (
            len(line) > 3
            and "@" not in line
            and not any(word in line.lower() for word in ["resume", "curriculum", "vitae"])
        ):
            return line

    return "Unknown"


# ✅ Skills extraction (your existing logic)
def extract_skills(text):
    skills = ["Python", "SQL", "Machine Learning", "Deep Learning",
              "NLP", "Pandas", "NumPy", "Excel", "Power BI", "Tableau"]

    found = [skill for skill in skills if skill.lower() in text.lower()]
    return found


# ✅ Experience extraction (simple version)
def extract_experience(text):
    match = re.search(r"(\d+)\s+year", text.lower())
    if match:
        return int(match.group(1))
    return 0


# ✅ MAIN FUNCTION (VERY IMPORTANT)
def extract_all(text):
    return {
        "name": extract_name(text),   # ✅ FIX HERE
        "skills": extract_skills(text),
        "experience": extract_experience(text)
    }