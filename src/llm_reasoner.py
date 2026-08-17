def generate_reason(skills, score):
    if score > 65:
        return f"Strong match with required skills: {', '.join(skills[:3])} and relevant experience"
    elif score > 50:
        return f"Moderate match with skills: {', '.join(skills[:3])}"
    else:
        return f"Weak match, missing key required skills"