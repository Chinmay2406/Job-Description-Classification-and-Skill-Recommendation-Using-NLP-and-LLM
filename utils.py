import PyPDF2
from skills import SKILLS
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")


def extract_text(pdf_file):
    text = ""

    reader = PyPDF2.PdfReader(pdf_file)

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + " "

    return text


def extract_skills(text):

    text = text.lower()

    skills_found = []

    for skill in SKILLS:

        if skill.lower() in text:

            skills_found.append(skill)

    return list(set(skills_found))


def get_match_score(
    resume_text,
    job_description
):

    resume_embedding = model.encode(
        [resume_text]
    )

    job_embedding = model.encode(
        [job_description]
    )

    similarity = cosine_similarity(
        resume_embedding,
        job_embedding
    )[0][0]

    return round(similarity * 100, 2)


def get_missing_skills(
    resume_skills,
    job_skills
):

    missing = list(
        set(job_skills) -
        set(resume_skills)
    )

    return missing


def generate_suggestions(
    missing_skills
):

    if len(missing_skills) == 0:

        return [
            "Excellent match for the job description."
        ]

    suggestions = []

    for skill in missing_skills:

        suggestions.append(
            f"Consider learning or adding {skill} to your resume."
        )

    return suggestions