"""
AI-powered recommendation system using NLP embeddings
This is the main system used in the final application
"""

genre_reason_map = {
    "sci-fi": "space or futuristic themes",
    "drama": "emotional storytelling",
    "action": "high-energy sequences",
    "thriller": "suspense and tension",
    "war": "conflict-driven narrative",
    "romance": "emotional relationships"
}

import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
from pathlib import Path
import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Resolve project root
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "content_enriched.csv"

# Load dataset
df = pd.read_csv(DATA_PATH)

# Combine text fields
df["text"] = df["title"] + " " + df["description"]

# Load pre-trained AI embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Generate embeddings for all content
content_embeddings = model.encode(
    df["text"].tolist(),
    show_progress_bar=True
)

def explain_recommendation(query, description):
    reasons = []
    for genre, reason in genre_reason_map.items():
        if genre in description:
            reasons.append(reason)

    if reasons:
        return "Recommended due to " + ", ".join(reasons)
    else:
        return "Recommended based on semantic similarity"

def recommend(user_query, top_n=3):
    # Encode user query
    query_embedding = model.encode([user_query])

    # Compute similarity
    similarities = cosine_similarity(
        query_embedding,
        content_embeddings
    )[0]

    # Sort by similarity
    top_indices = np.argsort(similarities)[::-1][:top_n]

    results = df.iloc[top_indices][["title", "description"]].copy()
    #results["explanation"] = results["description"].apply(
    #    lambda x: explain_recommendation(query, x)
    #)
    return results

if __name__ == "__main__":
    query = "space travel with emotional story"
    print("User Query:", query)
    print("\nAI Recommendations:")
    print(recommend(query))