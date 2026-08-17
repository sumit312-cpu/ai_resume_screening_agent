# 🤖 AI Resume Screening Agent

## 📌 Overview
This project is an AI-powered Resume Screening Agent that ranks candidates based on their relevance to a given Job Description.

The system parses resumes, extracts key information, computes similarity using NLP, and generates a ranked shortlist of candidates.

---

## 🚀 Features
- Parse multiple resumes (TXT format)
- Extract structured data (Name, Email, Skills, Experience, Education)
- Compute NLP similarity (TF-IDF + Cosine Similarity)
- Calculate weighted final score
- Rank candidates automatically
- Export results to CSV and JSON
- (Optional) LLM-based reasoning using Groq

---

## 🛠️ Tech Stack
- Python
- Scikit-learn
- Pandas
- NumPy
- Groq (LLM for reasoning)

---

## 📂 Project Structure
tcan you write again for readme

Got it 👍 — here is a clean, professional, copy-paste READY README.md for your project.

📄 README.md (Final Version)
# 🤖 AI Resume Screening Agent


## 📌 Overview
This project is an AI-powered Resume Screening Agent that ranks candidates based on their relevance to a given Job Description.


The system parses resumes, extracts key information, computes similarity using NLP, and generates a ranked shortlist of candidates.


---


## 🚀 Features
- Parse multiple resumes (TXT format)
- Extract structured data (Name, Email, Skills, Experience, Education)
- Compute NLP similarity (TF-IDF + Cosine Similarity)
- Calculate weighted final score
- Rank candidates automatically
- Export results to CSV and JSON
- (Optional) LLM-based reasoning using Groq


---


## 🛠️ Tech Stack
- Python
- Scikit-learn
- Pandas
- NumPy
- Groq (LLM for reasoning)


---


## 📂 Project Structure

resume_screening_agent/
│
├── data/
│ ├── job_description.txt
│ └── resumes/
│ ├── resume_01.txt
│ ├── resume_02.txt
│ └── ...
│
├── outputs/
│ ├── ranked_candidates.csv
│ └── ranked_candidates.json
│
├── src/
│ ├── parser.py
│ ├── extractor.py
│ ├── similarity.py
│ ├── scorer.py
│ ├── llm_reasoner.py
│ └── agent.py
│
├── main.py
├── requirements.txt
├── .env
├── .env.example
├── README.md

---

## ⚙️ How It Works

1. Load Job Description
2. Load all resumes from folder
3. Extract structured information (skills, experience, education)
4. Compute similarity using TF-IDF + cosine similarity
5. Calculate skill match score
6. Evaluate experience score
7. Compute final weighted score
8. Rank all candidates
9. Save results to CSV and JSON

---

## 🧮 Scoring Logic

Final Score is calculated as:
Final Score =
50% NLP Similarity
30% Skill Match
20% Experience Score



---


## ▶️ How to Run


```bash
conda activate resume_agent
pip install -r requirements.txt
python main.py

📊 Example Output
===== FINAL RANKING =====


1. Sneha Gupta - Score: 71.36
2. Rahul Sharma - Score: 64.13
3. Amit Verma - Score: 61.42
4. Ankit Patel - Score: 60.26
...
10. Arjun Mehta - Score: 26.63
📁 Output Files

The system generates:

outputs/ranked_candidates.csv
outputs/ranked_candidates.json
🔐 Environment Variables

Create a .env file and add:
GROQ_API_KEY="your_api_key_here"

⚠️ Tradeoffs
Used TF-IDF instead of embeddings for simplicity and speed
Rule-based extraction instead of advanced NLP parsing
Currently supports TXT format (can be extended to PDF/DOCX)


🔮 Future Improvements
Add PDF/DOCX resume parsing
Use embeddings (Sentence Transformers / BERT)
Build a Streamlit UI
Improve skill extraction using NLP
Add recruiter dashboard
💡 Use Case

This project can be used by recruiters to:

Automatically shortlist candidates
Reduce manual screening effort
Improve hiring efficiency
👨‍💻 Author

Sumit Tiwari
B.Tech CSE | Data Science & AI Enthusiast
