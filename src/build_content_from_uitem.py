import pandas as pd

# Load u.item (pipe separated, no header)
columns = [
    "movie_id", "title", "release_date", "video_release",
    "imdb_url",
    "unknown", "Action", "Adventure", "Animation",
    "Children", "Comedy", "Crime", "Documentary", "Drama",
    "Fantasy", "Film-Noir", "Horror", "Musical", "Mystery",
    "Romance", "Sci-Fi", "Thriller", "War", "Western"
]

movies = pd.read_csv(
    "data/movielens/u.item",
    sep="|",
    encoding="latin-1",
    names=columns
)

# Convert genre flags to text
genre_columns = columns[5:]

def build_genre_text(row):
    return " ".join([genre.lower() for genre in genre_columns if row[genre] == 1])

movies["description"] = movies.apply(build_genre_text, axis=1)

# Keep only required columns
content = movies[["title", "description"]]

# Save enriched content
content.to_csv("data/content_enriched.csv", index=False)

print(" content_enriched.csv created successfully")
