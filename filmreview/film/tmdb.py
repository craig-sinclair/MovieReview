from tmdbv3api import TMDb, Movie
import requests
from django.conf import settings

tmdb = TMDb()
tmdb.api_key = settings.TMDB_API_KEY

TMDB_API_URL = "https://api.themoviedb.org/3"
TMDB_IMAGE_BASE_URL = "https://image.tmdb.org/t/p/"

movie = Movie()

def search_movie(title):
    search_results = movie.search(title)
    return search_results

def get_movie_detail(movie_id):
    details = movie.details(movie_id)
    return details

def get_popular_movies():
    url = f"https://api.themoviedb.org/3/movie/popular"
    params = {
        'api_key': settings.TMDB_API_KEY,
        'language': 'en-US',
        'page': 1,
    }
    response = requests.get(url, params=params)
    return response.json().get('results', [])
