from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


# Load the pretrained NLP model
model = SentenceTransformer("all-MiniLM-L6-v2")


def calculate_similarity(text1, text2):
    """
    Calculate semantic similarity between two pieces of text.
    Returns a score between 0 and 1.
    """

    embeddings = model.encode([text1, text2])

    similarity = cosine_similarity(
        [embeddings[0]],
        [embeddings[1]]
    )[0][0]

    return float(similarity)