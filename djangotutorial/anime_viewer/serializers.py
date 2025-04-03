from rest_framework import serializers

from .models import AnimeViewer
from anime_movie.serializers import AnimeMovieSerializer


class AnimeViewerSerializer(serializers.ModelSerializer):
    watched_anime_list = AnimeMovieSerializer(many=True, read_only=True)

    class Meta:
        model = AnimeViewer
        fields = ['pk', 'name', 'email', 'created', 'watched_anime_list']
