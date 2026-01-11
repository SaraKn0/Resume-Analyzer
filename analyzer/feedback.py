
def generate_feedback(missing_skills, resume_cleaned):
    """
    Generates human-readable resume feedback based on:
    - missing skills
    - resume sections
    - weak action verbs

    Returns: list of feedback strings
    """

    feedback = []

    
    #Top missing skills (max 5–10)
    
    all_missing = []

    for category, skills in missing_skills.items():
        all_missing.extend(skills)

    # remove duplicates while preserving order
    seen = set()
    unique_missing = []
    for skill in all_missing:
        if skill not in seen:
            seen.add(skill)
            unique_missing.append(skill)

    top_missing = unique_missing[:10]

    if top_missing:
        feedback.append(
            f"Top missing skills for this role: {', '.join(top_missing)}."
        )

    
    # Missing Projects section
   
    if "projects" not in resume_cleaned:
        feedback.append(
            "Add a Projects section if you have one — projects help demonstrate hands-on experience."
        )

    
    # Mention tools explicitly
    
    tool_missing = missing_skills.get("tools", [])

    if tool_missing:
        feedback.append(
            "Mention tools explicitly in your resume, such as: "
            + ", ".join(tool_missing[:5]) + "."
        )

    
    #Weak action verbs detection
    
    weak_verbs = [
        "helped",
        "worked on",
        "assisted",
        "participated",
        "involved in",
        "responsible for"
    ]

    strong_verbs = [
        "built",
        "implemented",
        "designed",
        "developed",
        "optimized",
        "automated",
        "refactored",
        "debugged",
        "tested",
        "led"
    ]

    found_weak = [verb for verb in weak_verbs if verb in resume_cleaned]

    if found_weak:
        feedback.append(
            "Use stronger action verbs instead of phrases like "
            + ", ".join(found_weak[:3])
            + ". Consider verbs such as "
            + ", ".join(strong_verbs[:5]) + "."
        )

    return feedback
