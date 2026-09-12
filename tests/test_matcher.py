from utils.matcher import calculate_match


test_cases = [
    {
        "name": "Exact and alias matches",
        "resume": ["Python", "ML", "React"],
        "job": ["Python", "Machine Learning", "React.js"]
    },
    {
        "name": "Related but different skills",
        "resume": ["Machine Learning"],
        "job": ["Artificial Intelligence"]
    },
    {
        "name": "Semantic similarity",
        "resume": ["Python programming"],
        "job": ["Python development"]
    },
    {
        "name": "Unrelated skills",
        "resume": ["Python"],
        "job": ["Photography"]
    },
    {
        "name": "Technology relationships",
        "resume": ["SQL"],
        "job": ["MySQL"]
    },
    {
        "name": "Similar names but different skills",
        "resume": ["Java"],
        "job": ["JavaScript"]
    },
    {
        "name": "Different web technologies",
        "resume": ["HTML"],
        "job": ["CSS"]
    },
    {
        "name": "Related data skills",
        "resume": ["Data Science"],
        "job": ["Data Analysis"]
    },
    {
        "name": "Related AI skills",
        "resume": ["Deep Learning"],
        "job": ["Machine Learning"]
    }
]


for test in test_cases:

    print("\n" + "=" * 60)
    print(test["name"])
    print("=" * 60)

    result = calculate_match(
        test["resume"],
        test["job"]
    )

    print("Match Score:", result["match_score"])
    print("Matched Skills:", result["matched_skills"])
    print("Missing Skills:", result["missing_skills"])

    print("\nMatch Details:")

    for detail in result["match_details"]:
        print(
            f"{detail['job_skill']} <- "
            f"{detail['resume_skill']} | "
            f"{detail['method']} | "
            f"similarity: {detail['similarity']}"
        )