# Job-Description-Classification-and-Skill-Recommendation-Using-NLP-and-LLM

https://www.kaggle.com/code/chinmayd1/nlp-project  - THE KEGGLE lINK

# Resume Screening & Job Recommendation System using NLP, ML, LLM, Streamlit & Kaggle

## Project Overview

This project is an AI-powered Resume Screening and Job Recommendation System that combines Natural Language Processing (NLP), Machine Learning (ML), and Large Language Model (LLM) techniques to analyze resumes, match them against job descriptions, identify skill gaps, and recommend suitable job roles.

The project was developed in two versions:

### 1. Streamlit Web Application

An interactive web application where users can:

* Upload a resume
* Enter a job description
* Receive a resume-job match score
* View matching and missing skills
* Get job recommendations

### 2. Kaggle Notebook Implementation

A notebook-based implementation demonstrating:

* NLP preprocessing
* Machine Learning classification
* LLM-based semantic similarity
* Resume screening workflow
* Interactive PDF upload and job matching

---

# Problem Statement

Recruiters often spend significant time manually reviewing resumes against job requirements.

This project automates the process by:

* Analyzing resumes
* Comparing them with job descriptions
* Calculating similarity scores
* Identifying skill gaps
* Recommending suitable job categories

---

# Objectives

* Automate resume screening
* Reduce recruiter effort
* Improve candidate-job matching
* Demonstrate NLP and LLM integration
* Provide explainable AI-based recommendations

---

# Technologies Used

## Programming Language

* Python

## NLP Techniques

* Text Cleaning
* Tokenization
* TF-IDF Vectorization

## Machine Learning

* Logistic Regression

## LLM / Semantic Search

* Sentence Transformers
* all-MiniLM-L6-v2 Model
* Cosine Similarity

## Visualization

* Matplotlib
* Seaborn

## User Interface

### Streamlit Version

* Streamlit

### Kaggle Version

* ipywidgets

---

# Dataset

A custom IT Job Posting Dataset was created containing:

* Job Title
* Job Description
* Job Category

Example categories:

* Software Engineer
* Data Scientist
* Machine Learning Engineer
* DevOps Engineer
* NLP Engineer
* AI Specialist
* Cloud Engineer
* Backend Developer

Dataset Fields:

| Column          | Description              |
| --------------- | ------------------------ |
| id              | Unique Job ID            |
| job_title       | Job Role                 |
| job_description | Detailed Job Description |
| category        | Job Category             |

---

# System Architecture

```text
Resume PDF
     │
     ▼
PDF Text Extraction
     │
     ▼
Text Cleaning
     │
     ▼
TF-IDF Vectorization
     │
     ▼
Similarity Calculation
     │
     ▼
Skill Extraction
     │
     ▼
Match Score Generation
     │
     ▼
Skill Gap Analysis
     │
     ▼
Final Recommendation
```

---

# NLP Pipeline

### Step 1: Data Cleaning

Operations performed:

* Convert text to lowercase
* Remove HTML tags
* Remove special characters
* Remove unnecessary spaces

Example:

Input:

```text
Python Developer!!! <html>
```

Output:

```text
python developer
```

---

### Step 2: TF-IDF Vectorization

Text is converted into numerical vectors using:

```python
TfidfVectorizer()
```

Purpose:

* Convert textual information into machine-readable features
* Capture important keywords

---

### Step 3: Classification Model

Model Used:

```text
Logistic Regression
```

Purpose:

* Predict job category
* Classify job descriptions

---

# LLM Integration

Model Used:

```text
all-MiniLM-L6-v2
```

Library:

```python
SentenceTransformer
```

Purpose:

* Generate semantic embeddings
* Understand contextual meaning
* Improve recommendation quality

Example:

```text
Python ML Engineer
```

and

```text
Machine Learning Developer
```

are recognized as semantically similar.

---

# Resume Screening Module

## Input

### Resume

* PDF Upload (Kaggle)
* File Upload (Streamlit)

### Job Description

Text entered by user

---

## Processing

### Resume Text Extraction

Using:

```python
PyPDF2
```

---

### Similarity Calculation

Using:

```python
Cosine Similarity
```

Formula:

```text
Similarity = Cosine(Vector1, Vector2)
```

---

### Skill Extraction

The system identifies skills such as:

* Python
* Java
* SQL
* Docker
* AWS
* NLP
* TensorFlow
* PyTorch
* Git
* Linux
* Machine Learning
* Deep Learning

---

# Output

The system generates:

### Match Score

Example:

```text
82.45%
```

### Matching Skills

```text
Python
SQL
Docker
AWS
```

### Missing Skills

```text
Deep Learning
Kubernetes
```

### Recommendation

```text
Improve Deep Learning and Kubernetes
to increase your job match score.
```

---

# Kaggle Notebook Features

### Data Analysis

* Dataset exploration
* Data cleaning

### Machine Learning

* TF-IDF
* Logistic Regression

### LLM Features

* Sentence Embeddings
* Semantic Search

### Visualizations

* Job Category Distribution
* Confusion Matrix
* Feature Importance Graphs

### Interactive Components

* Resume PDF Upload
* Job Description Input
* Real-time Analysis

---

# Streamlit Application Features

### Interactive Dashboard

Users can:

* Upload resume
* Paste job description
* Generate match score
* View recommendations

### User-Friendly Interface

* Simple design
* Fast processing
* Real-time results

---

# Results

### Classification Accuracy

Achieved approximately:

```text
65%
```

on the custom IT job dataset.

### Semantic Search

Successfully recommends relevant job roles based on:

* Skills
* Context
* Job descriptions

---

# Future Enhancements

* Support DOCX resumes
* Advanced skill extraction using Named Entity Recognition (NER)
* Integration with OpenAI GPT models
* Resume ranking among multiple candidates
* Job recommendation engine
* Resume improvement suggestions
* PDF report generation
* Recruiter dashboard

---

# Learning Outcomes

Through this project, the following concepts were explored:

* Natural Language Processing
* Text Vectorization
* Machine Learning Classification
* Semantic Search
* Sentence Embeddings
* Resume Screening Systems
* Interactive AI Applications
* Streamlit Development
* Kaggle Notebook Development

---

# Conclusion

This project demonstrates how NLP, Machine Learning, and LLM techniques can be integrated to build an intelligent Resume Screening and Job Recommendation System. The solution automates candidate evaluation, provides explainable recommendations, identifies skill gaps, and showcases practical applications of AI in recruitment and talent acquisition.
