from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Movie

# Create your views here.

def index(request):
    return render(request, 'home.html',)


@login_required
def movies(request):
    movies = Movie.objects.all()
    return render(request, 'movies.html', {'movies': movies})

@login_required
def details(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'detail.html', {'movie':movie})