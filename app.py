import streamlit as st

from utils import (
    extract_text,
    extract_skills,
    get_match_score,
    get_missing_skills,
    generate_suggestions
)

st.set_page_config(
    page_title="AI Resume Matcher",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Resume Matcher Using NLP & LLM")

st.markdown(
    """
Upload your Resume PDF and paste the Job Description.

The system will:
- Calculate Resume Match Score
- Extract Skills
- Find Missing Skills
- Suggest Improvements
"""
)

uploaded_file = st.file_uploader(
    "Upload Resume PDF",
    type=["pdf"]
)

job_description = st.text_area(
    "Paste Job Description",
    height=250
)

if st.button("Analyze Resume"):

    if uploaded_file is None:

        st.error(
            "Please upload a resume."
        )

    elif job_description.strip() == "":

        st.error(
            "Please enter job description."
        )

    else:

        resume_text = extract_text(
            uploaded_file
        )

        resume_skills = extract_skills(
            resume_text
        )

        job_skills = extract_skills(
            job_description
        )

        match_score = get_match_score(
            resume_text,
            job_description
        )

        missing_skills = get_missing_skills(
            resume_skills,
            job_skills
        )

        suggestions = generate_suggestions(
            missing_skills
        )

        st.success(
            f"Resume Match Score: {match_score}%"
        )

        col1, col2 = st.columns(2)

        with col1:

            st.subheader(
                "Skills Found In Resume"
            )

            st.write(
                resume_skills
            )

        with col2:

            st.subheader(
                "Skills Required In Job"
            )

            st.write(
                job_skills
            )

        st.subheader(
            "Missing Skills"
        )

        if len(missing_skills) == 0:

            st.success(
                "No missing skills found."
            )

        else:

            st.write(
                missing_skills
            )

        st.subheader(
            "Improvement Suggestions"
        )

        for suggestion in suggestions:

            st.write(
                "•",
                suggestion
            )