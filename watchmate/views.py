from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
# Create your views here.

from watchmate.models import Movie

def movie_list(request):
    movies = Movie.objects.all()
    print(movies.values())
    data = {
        'movies':list(movies.values())
        }
    return JsonResponse(data)

def movie_detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    print(movie.name)
    data = {
        'name':movie.name,
        'description':movie.description,
        'active':movie.active
    }
    return JsonResponse(data)
    