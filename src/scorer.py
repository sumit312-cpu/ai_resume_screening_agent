def skill_match_score(jd_text, resume_skills):
    jd_text = jd_text.lower()

    match_count = 0

    for skill in resume_skills:
        if skill.lower() in jd_text:
            match_count += 1

    if len(resume_skills) == 0:
        return 0

    return (match_count / len(resume_skills)) * 100


def experience_score(experience_text):
    import re

    match = re.search(r"(\d+\.?\d*)", experience_text)

    if match:
        years = float(match.group(1))

        if years >= 3:
            return 100
        elif years >= 2:
            return 80
        elif years >= 1:
            return 60
        else:
            return 40

    return 0


def final_score(similarity, skill_score, exp_score):
    return round(
        (0.5 * similarity) +
        (0.3 * skill_score) +
        (0.2 * exp_score),
        2
    )