from django.shortcuts import render
from django.http import HttpResponse
from film.models import Movie
from film.forms import MovieForm
from django.shortcuts import redirect

def index(request):
    all_films = Movie.objects.all()
    context_dict = {'movies': all_films}
    return render(request, 'film/index.html', context=context_dict)

def add(request):
    form = MovieForm()
    
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if(form.is_valid()):
            form.save()
            return redirect('/film/')
        else:
            print(form.errors)
    
    context_dict = {'form': form}
    return render(request, 'film/add.html', context=context_dict)
