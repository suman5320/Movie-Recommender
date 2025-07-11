import streamlit as st

import pandas as pd
import requests

import pickle


np.savez_compressed("model/similarity_matrix.npz", similarity=similarity)
loaded = np.load("similarity_matrix.npz")
similarity = loaded['similarity']



print("File downloaded and loaded successfully!")


movie_list = pickle.load(open('model/movie_dict.pkl','rb'))








movies  = pd.DataFrame(movie_list)

st.title('Movies Recommended System')
option = st.selectbox('which movie would you to watch',movies['title'].values)

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=113815bf61e209e244b9a3299c1bc256'.format(movie_id))
    data = response.json()
    return  "https://image.tmdb.org/t/p/w500/"+ data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)),reverse = True,key=lambda x:x[1])[1:6]
    recommended_movies = []
    movie_posters = []

    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        movie_posters.append(fetch_poster(movie_id))
    return recommended_movies,movie_posters

if st.button('Recommend'):
    name,posters = recommend(option)
    col1, col2, col3 ,col4, col5 = st.columns(5)

    with col1:
        st.text(name[0])
        st.image(posters[0])

    with col2:
        st.text(name[1])
        st.image(posters[1])

    with col3:
        st.text(name[2])
        st.image(posters[2])

    with col4:
        st.text(name[3])
        st.image(posters[3])

    with col5:
        st.text(name[4])
        st.image(posters[4])






