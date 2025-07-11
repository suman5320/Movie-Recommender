# 🎬 Movie Recommender System

🚀 [Live Demo](https://movie-recommender-kvphuoyhfu72havtpapvpw.streamlit.app/#movies-recommended-system)

A content-based movie recommendation system built using Streamlit.  
Select a movie and get 5 similar movies recommended along with their posters — powered by TMDB API and cosine similarity.

---

## 🔍 Features

- Select a movie from a dropdown list
- Get top 5 similar movie recommendations
- Movie posters fetched dynamically from TMDB
- Fast performance using precomputed `.npz` and `.pkl` files

---

## 🛠️ Run Locally

```bash
# Clone the repo
git clone https://github.com/your-username/movie-recommender.git
cd movie-recommender

# (Optional) Create and activate virtual environment
python -m venv venv
# Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
