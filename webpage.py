import requests
import streamlit as st
import pickle
import pandas as pd

#loading datasets and ML model
movies = pd.DataFrame(pickle.load(open('Movies_dict.pkl','rb')))
similarity = pickle.load(open("similarity.pkl",'rb'))

# Defining Methods

#Method for recommending movies
def recommend(movie):
    recommended_movies_names =[]
    recommended_movie_posters = []
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    for i in distances[1:11]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies_names.append(movies.iloc[i[0]].title)
        recommended_movie_posters.append(fetch_poster(movie_id))
    return recommended_movies_names,recommended_movie_posters

# Method for Fetching posters

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=14428c9a2e620bd648757a897e26bd53&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

#Webpage

st.title("Movie Rcommendation System")
movie_name = st.selectbox("Select movie",movies["title"].values)
if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(movie_name)
    col1, col2, col3, col4, col5  = st.columns(5,gap="medium")
    col6, col7, col8, col9, col10 = st.columns(5, gap="medium")
    with col1:
        st.image(recommended_movie_posters[0])
        st.text(recommended_movie_names[0])
    with col2:
        st.image(recommended_movie_posters[1])
        st.text(recommended_movie_names[1])
    with col3:
        st.image(recommended_movie_posters[2])
        st.text(recommended_movie_names[2])
    with col4:
        st.image(recommended_movie_posters[3])
        st.text(recommended_movie_names[3])
    with col5:
        st.image(recommended_movie_posters[4])
        st.text(recommended_movie_names[4])
    with col6:
        st.image(recommended_movie_posters[5])
        st.text(recommended_movie_names[5])
    with col7:
        st.image(recommended_movie_posters[6])
        st.text(recommended_movie_names[6])
    with col8:
        st.image(recommended_movie_posters[7])
        st.text(recommended_movie_names[7])
    with col9:
        st.image(recommended_movie_posters[8])
        st.text(recommended_movie_names[8])
    with col10:
        st.image(recommended_movie_posters[9])
        st.text(recommended_movie_names[9])
