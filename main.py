from src.agent import load_resumes
from src.extractor import extract_all
from src.similarity import compute_similarity
from src.scorer import skill_match_score, experience_score, final_score
from src.llm_reasoner import generate_reason

import pandas as pd
import json
import os

# Load JD
with open("data/job_description.txt", "r", encoding="utf-8") as f:
    jd_text = f.read()

# Load resumes
resumes = load_resumes("data/resumes")

results = []

for file_name, content in resumes:  # ✅ fixed (list, not dict)
    data = extract_all(content)

    similarity = compute_similarity(jd_text, content)
    skill_score = skill_match_score(jd_text, data["skills"])
    exp_score = experience_score(data["experience"])

    total = final_score(similarity, skill_score, exp_score)

    reason = generate_reason(data["skills"], total)

    results.append({
        "file": file_name,
        "name": data["name"],
        "skills": data["skills"],  # ✅ added
        "similarity": round(similarity, 2),
        "skill_score": round(skill_score, 2),
        "experience_score": exp_score,
        "final_score": round(total, 2),
        "reason": reason  # ✅ added
    })

# Sort by score
results = sorted(results, key=lambda x: x["final_score"], reverse=True)

# Print results
print("\n===== FINAL RANKING =====\n")

for i, candidate in enumerate(results, 1):
    print(f"{i}. {candidate['name']} - Score: {candidate['final_score']}")
    print(f"   Reason: {candidate['reason']}\n")

# Save outputs
os.makedirs("outputs", exist_ok=True)

df = pd.DataFrame(results)
df.to_csv("outputs/ranked_candidates.csv", index=False)

with open("outputs/ranked_candidates.json", "w") as f:
    json.dump(results, f, indent=4)

print("\nResults saved in outputs folder ✅")