from django.shortcuts import render
from rest_framework import generics

from .models import AnimeMovie
from .serializers import AnimeMovieSerializer


class AnimeMovieCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new anime movie
    queryset = AnimeMovie.objects.all(),
    serializer_class = AnimeMovieSerializer

class AnimeMovieList(generics.ListAPIView):
    # API endpoint that allows anime movie to be viewed
    queryset = AnimeMovie.objects.all()
    serializer_class = AnimeMovieSerializer

class AnimeMovieDetail(generics.RetrieveAPIView):
    # API endpoint that returns a single anime movie by pk.
    queryset = AnimeMovie.objects.all()
    serializer_class = AnimeMovieSerializer

class AnimeMovieUpdate(generics.RetrieveUpdateAPIView):
    # API endpoint that allows an anime movie record to be updated.
    queryset = AnimeMovie.objects.all()
    serializer_class = AnimeMovieSerializer

class AnimeMovieDelete(generics.RetrieveDestroyAPIView):
    # API endpoint that allows an anime movie record to be deleted.
    queryset = AnimeMovie.objects.all()
    serializer_class = AnimeMovieSerializer
