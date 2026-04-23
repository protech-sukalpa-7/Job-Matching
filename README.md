# Smart Job Matching and Recruitment System using Machine Learning

## 1. Project Overview

The Smart Job Matching and Recruitment System is an AI-powered web application designed to match resumes with the most relevant job opportunities using Machine Learning and Natural Language Processing (NLP).

The system analyzes resume text, compares it with job descriptions, and predicts the best matching jobs with confidence scores.

---

## 2. Features

* Resume-to-job matching based on skill similarity
* Match score prediction using Machine Learning
* Dynamic ranking of jobs
* Interactive and animated web interface
* Supports multiple job domains
* Uses synthetic labeled data generation for training

---

## 3. Tech Stack

### Backend

* Python
* Flask

### Machine Learning

* scikit-learn
* Pandas
* Joblib

### Frontend

* HTML
* CSS
* JavaScript

---

## 4. Folder Structure

| File / Folder           | Purpose                                 |
| ----------------------- | --------------------------------------- |
| `app.py`                | Runs the Flask web application          |
| `train_model.py`        | Trains the Machine Learning model       |
| `predict.py`            | Predicts matching jobs                  |
| `utils.py`              | Loads and preprocesses data             |
| `data/jobs.csv`         | Stores the job dataset                  |
| `data/labeled_data.csv` | Stores generated labeled training data  |
| `model/vectorizer.pkl`  | Saved TF-IDF Vectorizer                 |
| `model/classifier.pkl`  | Saved trained Logistic Regression model |
| `templates/index.html`  | Frontend user interface                 |

---

## 5. Dataset Details

The dataset contains job postings with the following columns:

* Job Title
* Description

The system combines both fields into one `job_description` column for processing.

---

## 6. Installation Guide

Install dependencies:

```bash
pip install -r requirements.txt
```

Run model training:

```bash
python train_model.py
```

Run the application:

```bash
python app.py
```

---

## 7. How It Works

1. User enters resume text.
2. Resume is combined with each job description.
3. TF-IDF converts text into numerical vectors.
4. Logistic Regression predicts match probability.
5. Top jobs are displayed with scores.

---

## 8. Machine Learning Workflow

### Data Preprocessing

* Cleaning column names
* Removing duplicates
* Combining job title and description

### Synthetic Label Generation

* Positive samples = matching job-resume pairs
* Negative samples = mismatched pairs

### Feature Engineering

* TF-IDF Vectorization

### Model Training

* Logistic Regression classifier

### Prediction

* Match probability scoring

---

## 9. Test Prompts

Use these sample resume inputs to test the system:

**Data Analyst**
Data analyst with experience in Python, SQL, Excel, and Power BI. Skilled in dashboards, reporting, statistical analysis, and business insights.

**Machine Learning Engineer**
Machine learning engineer with experience in Python, TensorFlow, scikit-learn, deep learning, NLP, and predictive analytics.

**Frontend Developer**
Frontend developer skilled in HTML, CSS, JavaScript, React, responsive web design, and API integration.

**Backend Developer**
Backend developer experienced in Node.js, Express, MongoDB, SQL, REST APIs, authentication, and server-side development.

**DevOps Engineer**
DevOps engineer skilled in Docker, Kubernetes, AWS, Linux, CI/CD pipelines, deployment automation, and infrastructure monitoring.

---

## 10. Project Link

GitHub Repository: [[Add Your GitHub Repository Link Here]](https://github.com/protech-sukalpa-7/Job-Matching)

Live Demo: https://job-matching-08z2.onrender.com/
---

## 11. Future Improvements

* Resume PDF parsing
* Skill extraction using NLP
* Better ranking using cosine similarity
* Advanced models like BERT
* Cloud deployment

---

## 12. Conclusion

This project demonstrates an end-to-end Machine Learning pipeline integrated with a web application to solve real-world recruitment and job-matching problems.
