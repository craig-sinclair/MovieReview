from django.shortcuts import render
from django.http import HttpResponse
from film.models import Movie
from film.forms import MovieForm
from django.shortcuts import redirect
from film.tmdb import search_movie, get_popular_movies, TMDB_IMAGE_BASE_URL

def index(request):
    context_dict = {}

    popular_movies = get_popular_movies()
    for movie in popular_movies:
        if(movie.get('poster_path')):
            movie['poster_url'] = f"{TMDB_IMAGE_BASE_URL}w500{movie['poster_path']}"
    context_dict["movies"] = popular_movies
    return render(request, 'film/index.html', context=context_dict)


def about(request):
    return render(request, 'film/about.html')