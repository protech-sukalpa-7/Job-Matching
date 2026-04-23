from predict import match_jobs

resume = """
Data analyst with experience in Python, SQL, Excel, and Power BI.
Skilled in dashboards, reporting, statistical analysis, and business insights.
Worked with large datasets and data visualization.
"""

results = match_jobs(resume)

print("\nTop Matching Jobs:\n")

for i, job in enumerate(results, start=1):
    print(f"{i}. {job['job_description']}")
    print(f"   Score: {job['score']}")
    print("-" * 80)