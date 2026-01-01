"""
Baseline content-based recommender
Used for initial experimentation (non-AI)
"""

from pathlib import Path
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Resolve project root
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "content.csv"

# Load dataset
df = pd.read_csv(DATA_PATH)

# Combine important text fields
df["text"] = df["title"] + " " + df["description"]

# Convert text to vectors
vectorizer = TfidfVectorizer(stop_words="english")
tfidf_matrix = vectorizer.fit_transform(df["text"])

# Compute similarity matrix
similarity = cosine_similarity(tfidf_matrix)


def recommend(title, top_n=3):
    idx = df[df["title"] == title].index[0]
    scores = list(enumerate(similarity[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)[1:top_n+1]

    recommendations = [df.iloc[i]["title"] for i, _ in scores]
    return recommendations


# Test
if __name__ == "__main__":
    print("Recommendations for Interstellar:")
    print(recommend("Interstellar"))
