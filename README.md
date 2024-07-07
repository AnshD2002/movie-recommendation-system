# Movie Recommendation System
[Movie_Recommendation](https://movie-recommendation-system-vx82xsm8zcnd7wr4pusesp.streamlit.app/)

[Movie_recommendation_System.webm](https://github.com/AnshD2002/movie-recommendation-system/assets/89890890/9144aa91-fa97-41f3-800f-e19d24789059)

A movie recommendation system built with Python using Streamlit, NLTK for natural language processing, and TMDB API for fetching movie posters.

## Overview

This application recommends movies based on similarity scores computed using vector similarity techniques. It allows users to select a movie from a dropdown menu and displays top recommendations along with their posters.

### Features

- **Interactive UI:** Select a movie from the dropdown menu and click a button to see recommendations.
- **Movie Posters:** Fetches movie posters using TMDB API to enhance user experience.
- **Vector Similarity:** Computes similarity scores between movies based on their descriptions.

## Files

- **Movies.pkl**: Pickled file containing movie data.
- **Movies_dict.pkl**: Pickled file containing movie dictionary for quick lookup.
- **similarity.pkl**: Pickled file containing precomputed similarity matrix using vector similarity.

## Technologies Used

- Python
- Streamlit
- NLTK (Natural Language Toolkit)
- TMDB API (The Movie Database API)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/movie-recommendation-system.git
2. Navigate to the project directory:
   ```bash
   cd movie-recommendation-system
3. Run the Streamlit app:
   ```bash
   streamlit run webpage.py

