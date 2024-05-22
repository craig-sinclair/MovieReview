from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from film.tmdb import search_movie, get_popular_movies, get_movie_detail, get_cast, get_person_by_id, get_person_movies, TMDB_IMAGE_BASE_URL

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

def details(request, movie_id):
    context_dict = {}
    movie = get_movie_detail(movie_id=movie_id)
    context_dict['movie'] = movie

    if(movie.get('poster_path')):
        context_dict['poster_url'] = f"{TMDB_IMAGE_BASE_URL}w500{movie['poster_path']}"

    cast = get_cast(movie.id)
    context_dict['cast'] = cast

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
        return render(request, 'film/index.html')
    
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