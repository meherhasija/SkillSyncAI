import json
import re


def load_skills():
    with open("data/skills.json", "r", encoding="utf-8") as file:
        skills_data = json.load(file)

    return skills_data


def extract_skills(text):
    skills_data = load_skills()

    found_skills = []

    for category in skills_data.values():
        for skill in category:
            pattern = r"(?<![a-zA-Z0-9])" + re.escape(skill) + r"(?![a-zA-Z0-9])"

            if re.search(pattern, text, re.IGNORECASE):
                found_skills.append(skill)

    return found_skills