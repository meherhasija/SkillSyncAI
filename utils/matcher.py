def calculate_match(resume_skills, job_skills):
    resume_set = set(resume_skills)
    job_set = set(job_skills)

    matched_skills = resume_set.intersection(job_set)
    missing_skills = job_set.difference(resume_set)

    if job_set:
        match_score = (len(matched_skills) / len(job_set)) * 100
    else:
        match_score = 0

    return {
        "match_score": round(match_score, 2),
        "matched_skills": sorted(matched_skills),
        "missing_skills": sorted(missing_skills)
    }