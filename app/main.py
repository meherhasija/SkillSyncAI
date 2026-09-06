import streamlit as st

from utils.pdf_reader import extract_text_from_pdf
from utils.skill_extractor import extract_skills
from utils.matcher import calculate_match


st.title("SkillSyncAI")

st.write("AI-Powered Resume - Job Matching and Skill Gap Analysis")


st.header("1. Upload your resume")

resume = st.file_uploader(
    "Choose your resume",
    type=["pdf"]
)


st.header("2. Enter job description")

job_description = st.text_area(
    "Paste the job description here",
    height=250
)


if resume is not None and job_description.strip():

    try:
        resume_text = extract_text_from_pdf(resume)

        if resume_text:

            st.success("Resume uploaded and read successfully!")

            resume_skills = extract_skills(resume_text)
            job_skills = extract_skills(job_description)

            result = calculate_match(
                resume_skills,
                job_skills
            )

            st.header("Resume Skills")

            if resume_skills:
                st.write(", ".join(resume_skills))
            else:
                st.warning("No skills detected in the resume.")

            st.header("Job Skills")

            if job_skills:
                st.write(", ".join(job_skills))
            else:
                st.warning("No skills detected in the job description.")

            st.header("Match Analysis")

            st.metric(
                "Match Score",
                f"{result['match_score']}%"
            )

            st.subheader("Matched Skills")

            if result["matched_skills"]:
                st.write(", ".join(result["matched_skills"]))
            else:
                st.write("No matching skills found.")

            st.subheader("Missing Skills")

            if result["missing_skills"]:
                st.write(", ".join(result["missing_skills"]))
            else:
                st.write("No missing skills found.")

        else:
            st.warning(
                "The PDF was opened, but no text was found. "
                "This may be a scanned or image-based resume."
            )

    except ValueError as error:
        st.error(str(error))


elif resume is not None:
    st.info("Please enter a job description to analyze the match.")