
from django.shortcuts import render, get_object_or_404
from .models import Movie
from django.core.paginator import Paginator
from django.db.models import Q

def home(request):
    query = request.GET.get('q', '')
    movies = Movie.objects.filter(
        Q(title__icontains=query) | Q(genre__icontains=query)
    )
    paginator = Paginator(movies, 10)  

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'movies/home.html', {'page_obj': page_obj, 'query': query})

def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, 'movies/movie_detail.html', {'movie': movie})
