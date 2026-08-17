# ==============================
# SCORER MODULE
# ==============================

# ✅ Skill Match Score
def skill_match_score(jd_text, resume_skills):
    jd_text = jd_text.lower()

    match_count = 0

    for skill in resume_skills:
        if skill.lower() in jd_text:
            match_count += 1

    if len(resume_skills) == 0:
        return 0

    return (match_count / len(resume_skills)) * 100


# ✅ Experience Score (Robust: handles int + string)
def experience_score(experience):
    import re

    # If already numeric
    if isinstance(experience, (int, float)):
        years = experience
    else:
        match = re.search(r"(\d+\.?\d*)", str(experience))
        years = float(match.group(1)) if match else 0

    # Scoring logic
    if years >= 3:
        return 100
    elif years >= 2:
        return 80
    elif years >= 1:
        return 60
    else:
        return 40


# ✅ Final Score (Weighted)
def final_score(similarity, skill_score, exp_score):
    return round(
        (0.5 * similarity) +   # NLP similarity weight
        (0.3 * skill_score) +  # skill match weight
        (0.2 * exp_score),     # experience weight
        2
    )
