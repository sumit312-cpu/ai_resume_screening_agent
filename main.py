from src.parser import load_resumes
from src.extractor import extract_all
from src.similarity import compute_similarity
from src.scorer import skill_match_score, experience_score, final_score


# Load JD
with open("data/job_description.txt", "r", encoding="utf-8") as f:
    jd_text = f.read()

# Load resumes
resumes = load_resumes("data/resumes")

results = []

for name, content in resumes.items():
    data = extract_all(content)

    similarity = compute_similarity(jd_text, content)
    skill_score = skill_match_score(jd_text, data["skills"])
    exp_score = experience_score(data["experience"])

    total = final_score(similarity, skill_score, exp_score)

    results.append({
        "file": name,
        "name": data["name"],
        "similarity": similarity,
        "skill_score": round(skill_score, 2),
        "experience_score": exp_score,
        "final_score": total
    })


# Sort by final score
results = sorted(results, key=lambda x: x["final_score"], reverse=True)


# Print ranking
print("\n===== FINAL RANKING =====\n")

for i, r in enumerate(results, start=1):
    print(f"{i}. {r['name']} - Score: {r['final_score']}")


import pandas as pd
import json
import os

# Create outputs folder if not exists
os.makedirs("outputs", exist_ok=True)

# Save CSV
df = pd.DataFrame(results)
df.to_csv("outputs/ranked_candidates.csv", index=False)

# Save JSON
with open("outputs/ranked_candidates.json", "w") as f:
    json.dump(results, f, indent=4)

print("\nResults saved in outputs folder ✅")