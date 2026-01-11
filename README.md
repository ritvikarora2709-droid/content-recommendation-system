🎬 AI-Powered Content Recommendation System

An AI-driven movie recommendation system that understands natural language user intent and provides semantic recommendations across Hollywood (TMDB) and Bollywood (IMDB) movies using pretrained NLP embeddings.

📌 Problem Statement

Traditional content recommendation systems rely heavily on user history, ratings, or predefined genres. These systems struggle in scenarios such as:

New users (cold start problem)

Users expressing vague or abstract preferences

Intent-based discovery (e.g., “epic fantasy adventure with emotional depth”)

This project aims to build a semantic content recommendation system that understands what the user wants to watch using natural language, without requiring prior user history.

🎯 Project Objective

Enable free-text, intent-based movie recommendations

Use pretrained AI models instead of training from scratch

Support both Hollywood and Bollywood movies

Build an interactive web interface for real-time recommendations

Focus on practical AI application, not model re-invention

✨ Key Features

🧠 Natural language movie search

🔍 Semantic similarity using NLP embeddings

🌍 Dual dataset support (TMDB + Bollywood IMDB)

📊 Relevance scoring using cosine similarity

💡 Human-readable recommendation explanations

🖥️ Interactive Streamlit web application

🛠️ Tech Stack

Programming Language

Python

AI / ML / NLP

Sentence-Transformers (all-MiniLM-L6-v2)

NLP Embeddings

Cosine Similarity (Vector Similarity Search)

Libraries

Pandas

NumPy

Scikit-learn

Streamlit

Datasets

TMDB Movies Dataset (Hollywood)

IMDB Bollywood Movies Dataset

🧩 System Architecture

The recommendation pipeline follows these steps:

Dataset Integration
Multiple public datasets (TMDB & Bollywood IMDB) are cleaned, standardized, and merged into a global dataset.

Text Feature Construction
Movie title, description, genres, and metadata are combined into a single text field.

Embedding Generation
Pretrained transformer model converts movie text into dense numerical embeddings.

Query Understanding
User input is embedded using the same model.

Similarity Computation
Cosine similarity is used to rank movies by semantic closeness to the user query.

Recommendation & Explanation
Top-ranked movies are returned with relevance scores and human-readable explanations.

📁 Repository Structure
Content_Recommendation_System/
│
├── data/
│   └── content_global.csv          # Unified TMDB + Bollywood dataset
│
├── src/
│   ├── ai_recommender.py            # Core AI recommendation logic
│   └── build_global_content.py      # Dataset preprocessing & merging
│
├── app.py                           # Streamlit UI application
├── notebook.ipynb                  # Primary evaluation notebook
├── requirements.txt                # Project dependencies
└── README.md                       # Project documentation

🚀 How to Run the Project
1️⃣ Install dependencies
pip install -r requirements.txt

2️⃣ Run the Streamlit app
streamlit run app.py

📊 Sample Output

User Query:

“Hobbits, dwarves, elves, epic fantasy adventure”

Recommendations:

The Hobbit: An Unexpected Journey

The Lord of the Rings: The Fellowship of the Ring

Onward

Each recommendation includes:

Description

Source (Hollywood / Bollywood)

Relevance score

Explanation of why it was recommended

📈 Evaluation Metrics

Cosine Similarity Score
Measures semantic relevance between user query and movie content.

Qualitative Evaluation
Manual inspection of recommendation relevance and diversity.

⚠️ Limitations

No user personalization or collaborative filtering

Embeddings generated once at runtime (initial loading delay)

Explanations are rule-based, not LLM-generated

Dataset limited to publicly available metadata

🔮 Future Enhancements

User profiling and personalization

Hybrid recommendation (content + collaborative)

LLM-powered explanations

Online vector databases (FAISS / Pinecone)

Streaming platform integration

Multilingual recommendations

🤖 Ethical Considerations & Responsible AI

Uses publicly available datasets

No personal user data collected or stored

Avoids demographic profiling

Transparent and explainable recommendations

📌 Conclusion

This project demonstrates how pretrained AI models can be used effectively to build real-world recommendation systems without training complex models from scratch. By focusing on semantic understanding, the system provides flexible, intuitive, and scalable content discovery across diverse movie datasets.

👤 Author

Ritvik Arora
AI Applications – Individual Open Project
Module E