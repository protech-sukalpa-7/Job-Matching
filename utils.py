import pandas as pd

def load_jobs():
    df = pd.read_csv("data.csv")

    df.columns = df.columns.str.strip().str.lower()

    if "job title" in df.columns:
        title = "job title"
    elif "title" in df.columns:
        title = "title"
    else:
        raise Exception("Job title column not found")

    if "description" in df.columns:
        desc = "description"
    else:
        raise Exception("Description column not found")

    df["job_description"] = df[title].astype(str) + " " + df[desc].astype(str)

    df = df.drop_duplicates(subset=["job_description"])

    df = df.dropna(subset=["job_description"])

    return df[["job_description"]]
