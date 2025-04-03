from rest_framework import serializers

from .models import AnimeMovie


class AnimeMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model= AnimeMovie
        fields = ['id', 'title', 'description']
