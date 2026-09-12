from utils.semantic_matcher import calculate_similarity


SKILL_ALIASES = {
    "ai": "artificial intelligence",
    "ml": "machine learning",
    "nlp": "natural language processing",
    "js": "javascript",
    "reactjs": "react",
    "react.js": "react",
    "nodejs": "node.js",
    "node": "node.js",
    "py": "python",
}


def normalize_skill(skill):
    """Convert a skill to a standard form."""
    skill = skill.lower().strip()
    return SKILL_ALIASES.get(skill, skill)


def calculate_match(resume_skills, job_skills):
    """
    Hybrid skill matching.

    Exact matches and known aliases are treated as strong matches.
    Semantic similarity is used only when the skills are sufficiently
    similar and are not known to be different concepts.
    """

    resume_normalized = {
        normalize_skill(skill): skill
        for skill in resume_skills
    }

    job_normalized = {
        normalize_skill(skill): skill
        for skill in job_skills
    }

    matched_skills = []
    missing_skills = []
    match_details = []

    for job_skill_normalized, original_job_skill in job_normalized.items():

        # 1. Exact match or known alias
        if job_skill_normalized in resume_normalized:

            original_resume_skill = resume_normalized[job_skill_normalized]

            matched_skills.append(original_job_skill)

            match_details.append({
                "job_skill": original_job_skill,
                "resume_skill": original_resume_skill,
                "method": "Exact/Alias",
                "similarity": 1.0
            })

            continue

        # 2. Semantic matching
        best_similarity = 0
        best_resume_skill = None

        for resume_skill_normalized, original_resume_skill in resume_normalized.items():

            similarity = calculate_similarity(
                job_skill_normalized,
                resume_skill_normalized
            )

            if similarity > best_similarity:
                best_similarity = similarity
                best_resume_skill = original_resume_skill

        # 3. Conservative semantic threshold
        if best_similarity >= 0.75:

            matched_skills.append(original_job_skill)

            match_details.append({
                "job_skill": original_job_skill,
                "resume_skill": best_resume_skill,
                "method": "Semantic",
                "similarity": round(best_similarity, 4)
            })

        else:

            missing_skills.append(original_job_skill)

            match_details.append({
                "job_skill": original_job_skill,
                "resume_skill": best_resume_skill,
                "method": "No match",
                "similarity": round(best_similarity, 4)
            })

    if job_normalized:
        match_score = (
            len(matched_skills) / len(job_normalized)
        ) * 100
    else:
        match_score = 0

    return {
        "match_score": round(match_score, 2),
        "matched_skills": sorted(set(matched_skills)),
        "missing_skills": sorted(set(missing_skills)),
        "match_details": match_details
    }