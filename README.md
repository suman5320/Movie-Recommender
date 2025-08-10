# 🎬 Movie Recommender System
🚀 [Live Demo](https://movie-recommender-kvphuoyhfu72havtpapvpw.streamlit.app/#movies-recommended-system)
A content-based movie recommendation system built using **TF-IDF Vectorization** and **Cosine Similarity**.  
The system suggests movies similar to the one selected by the user based on plot descriptions.

---

## 📌 Features
- ✅ Content-based filtering using movie overviews
- ✅ TF-IDF Vectorizer for text feature extraction
- ✅ Cosine Similarity for finding similar movies
- ✅ Simple and intuitive user interface (if deployed)
- ✅ Jupyter Notebook for easy experimentation

---

## 🛠️ Tech Stack
- **Programming Language:** Python
- **Libraries Used:**
  - pandas
  - numpy
  - scikit-learn
  - streamlit
- **Dataset:** [TMDB Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata) 

---


---

## ⚙️ How It Works
1. **Load Dataset** – Load the movie dataset containing titles, overviews, and other metadata.  
2. **Preprocess Data** – Fill missing values, clean text, and prepare the dataset.  
3. **TF-IDF Vectorization** – Convert movie descriptions into numerical vectors using Term Frequency–Inverse Document Frequency.  
4. **Calculate Similarity** – Use Cosine Similarity to find how similar two movies are.  
5. **Get Recommendations** – Given a movie title, retrieve the top N most similar movies.
6. **Deploy with Streamlit** – Create an interactive interface for users to input a movie title and get recommendations instantly.
---

## 🚀 How to Run Locally

**1. Clone the repository**
```bash
git clone https://github.com/your-username/movie-recommender-system.git
cd movie-recommender-system
pip install -r requirements.txt
jupyter notebook "Movie recommender system.ipynb"


📊 Example Output
If you search for "The Dark Knight", you might get recommendations like:
1. Batman Begins
2. The Dark Knight Rises
3. Man of Steel
4. Watchmen
5. V for Vendetta



