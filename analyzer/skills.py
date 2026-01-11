import json
from pathlib import Path


def load_taxonomy():
    # Get project root directory
    base_dir = Path(__file__).resolve().parent.parent
    taxonomy_path = base_dir / "data" / "skills_taxonomy.json"

    with open(taxonomy_path, "r", encoding="utf-8") as f:
        return json.load(f)


def detect_skills(cleaned_text, tokens, taxonomy):
    """
    Detect skills from cleaned text and tokens using the taxonomy.
    - Single-word skills: exact match in tokens
    - Multi-word skills: phrase match in cleaned_text
    """

    detected = {}

    for category, skills_list in taxonomy.items():
        detected[category] = []

        for skill in skills_list:
            # Single-word skill
            if " " not in skill:
                if skill in tokens:
                    detected[category].append(skill)

            # Multi-word skill (phrase)
            else:
                if skill in cleaned_text:
                    detected[category].append(skill)

    return detected
