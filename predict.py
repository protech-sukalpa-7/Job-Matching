import pandas as pd
import joblib
from utils import load_jobs

vectorizer = joblib.load("model/vectorizer.pkl")
model = joblib.load("model/classifier.pkl")

df = load_jobs()

def match_jobs(resume_text):
    results = []

    for _, row in df.iterrows():
        job_desc = row["job_description"]

        combined = resume_text + " " + job_desc
        vec = vectorizer.transform([combined])

        score = model.predict_proba(vec)[0][1] * 100

        results.append({
            "job_description": job_desc,
            "score": round(score, 3)
        })

    unique_results = []
    seen = set()

    for r in results:
        if r["job_description"] not in seen:
            unique_results.append(r)
            seen.add(r["job_description"])

    results = sorted(unique_results, key=lambda x: x["score"], reverse=True)

    return results[:10]
