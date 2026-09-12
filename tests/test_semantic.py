from utils.semantic_matcher import calculate_similarity


test_pairs = [
    # Related skill pairs
    ("AI", "Artificial Intelligence"),
    ("ML", "Machine Learning"),
    ("NLP", "Natural Language Processing"),
    ("JS", "JavaScript"),
    ("React", "React.js"),
    ("Python programming", "Python development"),
    ("data analysis", "analyzing data"),
    ("web development", "frontend development"),
    ("database management", "SQL database management"),

    # Unrelated pairs
    ("AI", "Accounting"),
    ("Machine Learning", "Graphic Design"),
    ("JavaScript", "Nursing"),
    ("Python", "Marketing"),
    ("SQL", "Photography"),
]


for text1, text2 in test_pairs:
    score = calculate_similarity(text1, text2)

    print(f"{text1}  <->  {text2}")
    print(f"Similarity: {score:.4f}")
    print("-" * 50)