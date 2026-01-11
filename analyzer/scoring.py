
def score_resume(
    matched_skills_resume,
    matched_skills_jd,
    resume_tokens,
    jd_tokens,
    resume_cleaned,
    taxonomy
):
    

    jd_required_skills = set()
    resume_skills = set()

    for category in taxonomy.keys():
        jd_required_skills.update(matched_skills_jd.get(category, []))
        resume_skills.update(matched_skills_resume.get(category, []))

    matched_required = jd_required_skills.intersection(resume_skills)

    if len(jd_required_skills) == 0:
        skill_score = 0.0
    else:
        skill_score = len(matched_required) / len(jd_required_skills)

    

    resume_token_set = set(resume_tokens)
    jd_token_set = set(jd_tokens)

    if len(jd_token_set) == 0:
        keyword_score = 0.0
    else:
        overlap = resume_token_set.intersection(jd_token_set)
        keyword_score = len(overlap) / len(jd_token_set)


    HEADINGS = ["experience", "projects", "education", "skills"]

    found = 0
    for heading in HEADINGS:
        if heading in resume_cleaned:
            found += 1

    sections_score = found / len(HEADINGS)

   

    final_score = (
        0.5 * skill_score +
        0.3 * keyword_score +
        0.2 * sections_score
    ) * 100


    return {
        "final_score": round(final_score, 2),
        "skill_score": round(skill_score * 100, 2),
        "keyword_score": round(keyword_score * 100, 2),
        "sections_score": round(sections_score * 100, 2)
    }
