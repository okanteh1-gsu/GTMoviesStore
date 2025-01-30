from django.shortcuts import render
from .models import Movies

def home(request):
    query = request.GET.get('search', '')
    if query:
        movies = Movies.objects.filter(title__icontains=query)
    else:
        movies = Movies.objects.all()

    return render(request, 'movies/home.html', {"movies": movies, 'query': query})
