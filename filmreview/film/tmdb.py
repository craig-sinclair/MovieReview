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
    movies = response.json().get('results', [])
    return movies[:16]

def get_trending_movies():
    url = f"https://api.themoviedb.org/3/trending/movie/week"
    params = {
        'api_key': settings.TMDB_API_KEY,
        'language': 'en-US',
        'page': 1,
    }
    response = requests.get(url, params=params)
    movies = response.json().get('results', [])
    return movies[:16]

def get_cast(movie_id):
    credits = movie.credits(movie_id)
    cast = list(credits.get('cast', []))
    for member in cast:
        if member.get('profile_path'):
            member['profile_url'] = f"https://image.tmdb.org/t/p/w500{member['profile_path']}"
        else:
            member['profile_url'] = 'https://static.vecteezy.com/system/resources/thumbnails/004/141/669/small_2x/no-photo-or-blank-image-icon-loading-images-or-missing-image-mark-image-not-available-or-image-coming-soon-sign-simple-nature-silhouette-in-frame-isolated-illustration-vector.jpg'
    return cast


def get_person_by_id(person_id):
    url = f"https://api.themoviedb.org/3/person/{person_id}" 
    params = {
        'api_key': settings.TMDB_API_KEY, 
        'language': 'en-US'
    }
    response = requests.get(url, params=params)
    if response.status_code == 200: 
        return response.json() 
    else:
        return None 
    
def get_person_movies(person_id):
    url = f"https://api.themoviedb.org/3/person/{person_id}/movie_credits"
    params = {
        'api_key': settings.TMDB_API_KEY,
        'language': 'en-US'
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:  
       data = response.json()
       casted_films = data.get('cast', [])
       sorted_casted_films = sorted(casted_films, key=lambda x: x.get('popularity', 0), reverse=True)
       return sorted_casted_films[:12]

    else:
        return None
    

def get_top_rated():
    url = f"https://api.themoviedb.org/3/movie/top_rated"
    params = {
        'api_key': settings.TMDB_API_KEY,
        'language': 'English',
        'page': 1,
    }
    response = requests.get(url, params=params)
    return response.json().get('results', [])

def get_recommendations(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/recommendations"
    params = {
        'api_key': settings.TMDB_API_KEY,
        'language': 'English',
        'page': 1,
    }
    response = requests.get(url, params=params)
    return response.json().get('results', [])