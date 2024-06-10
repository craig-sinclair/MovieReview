from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404
from film.tmdb import search_movie, get_popular_movies, get_movie_detail, get_cast, get_person_by_id, get_person_movies, get_top_rated, get_recommendations, get_trending_movies, get_search_suggestions, TMDB_IMAGE_BASE_URL
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegistrationForm, UserLoginForm
import requests
from django.http import JsonResponse
from django.conf import settings
from .models import SavedMovie, CustomUser
from django.contrib.auth.decorators import login_required


def index(request):
    context_dict = {}

    popular_movies = get_popular_movies()
    for movie in popular_movies:
        if(movie.get('poster_path')):
            movie['poster_url'] = f"{TMDB_IMAGE_BASE_URL}w500{movie['poster_path']}"
        average_rating = round(movie['vote_average'] * 10)
        movie['average_rating'] = str(average_rating) + "%"
    context_dict["movies"] = popular_movies

    trending_films = get_trending_movies()
    for film in trending_films:
        if(film.get('poster_path')):
                film['poster_url'] = f"{TMDB_IMAGE_BASE_URL}w500{film['poster_path']}"
        average_rating = round(film['vote_average'] * 10)
        film['average_rating'] = str(average_rating) + "%"

    context_dict['trending_films'] = trending_films
    return render(request, 'film/index.html', context=context_dict)


def about(request):
    return render(request, 'film/about.html')

def details(request, movie_id):
    context_dict = {}
    movie = get_movie_detail(movie_id=movie_id)
    context_dict['movie'] = movie

    if(movie.get('poster_path')):
        context_dict['poster_url'] = f"{TMDB_IMAGE_BASE_URL}w500{movie['poster_path']}"

    context_dict['release_date'] = movie.release_date[:4]
    average_score = round(movie.vote_average * 10)
    context_dict['average_score'] = (str(average_score) + "%")
    cast = get_cast(movie.id)
    context_dict['cast'] = cast

    recommended_movies = get_recommendations(movie_id)
    for film in recommended_movies:
        if(film.get('poster_path')):
            film['poster_url'] = f"{TMDB_IMAGE_BASE_URL}w500{film['poster_path']}"
    context_dict['recommended'] = recommended_movies
    return render(request, 'film/details.html', context=context_dict)

def search(request):
    query = request.GET.get('query')
    if query and query != "":
        movies = search_movie(query)
        movies_with_poster = []

        for movie in movies:
            if(movie.get('poster_path')):
                movie['poster_url'] = f"{TMDB_IMAGE_BASE_URL}w500{movie['poster_path']}"
                movies_with_poster.append(movie)

        return render(request, 'film/search.html', {'movies': movies_with_poster})
    else:
        return redirect('film:index')
    
def person(request, person_id):
    context_dict = {}
    person = get_person_by_id(person_id=person_id)
    context_dict['person'] = person

    profile_path = ""
    if(person.get('profile_path')):
        profile_path = f"https://image.tmdb.org/t/p/w500{person['profile_path']}"
    context_dict['profile_path'] = profile_path

    person_movies = get_person_movies(person_id=person_id)
    movies_with_poster = []

    if person_movies:
        for movie in person_movies:
            if(movie.get('poster_path')):
                movie['poster_url'] = f"{TMDB_IMAGE_BASE_URL}w500{movie['poster_path']}"
                movies_with_poster.append(movie)
    
    context_dict['movies'] = movies_with_poster
    return render(request, 'film/person.html', context=context_dict)


def top(request):
    context_dict = {}
    top_movies = get_top_rated()
    for movie in top_movies:
        if(movie.get('poster_path')):
            movie['poster_url'] = f"{TMDB_IMAGE_BASE_URL}w500{movie['poster_path']}"
        average_rating = round(movie['vote_average'] * 10)
        movie['average_rating'] = str(average_rating) + "%"
    context_dict["movies"] = top_movies
    return render(request, 'film/top.html', context=context_dict)

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('film:index')
    else:
        form = UserRegistrationForm()
    return render(request, 'film/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('film:index')
    else:
        form = UserLoginForm()
    return render(request, 'film/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('film:index')

def profile(request):
    context_dict = {}
    user = request.user
    context_dict['name'] = user.username
    context_dict['saved_movies'] = user.saved_movies
    return render(request, 'film/profile.html', context=context_dict)

def search_suggestions(request):
    query = request.GET.get('query', '')
    return get_search_suggestions(query)

@login_required
def add_movie_to_saved(request, movie_id):
    movie, created = SavedMovie.objects.get_or_create(movie_id=movie_id)
    user = request.user
    if (created == False):
        user.saved_movies.add(movie_id)
    return redirect('film:profile')

@login_required
def remove_movie_from_saved(request, movie_id):
    movie = get_object_or_404(SavedMovie, movie_id=movie_id)
    user = request.user
    user.saved_movies.remove(movie_id)
    return redirect('film:profile')