from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer as JwtTokenObtainPairSerializer

from .models import AnimeMovie


class TokenObtainPairSerializer(JwtTokenObtainPairSerializer):
    username_field = get_user_model().USERNAME_FIELD


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        validated_data['is_staff'] = True
        validated_data['is_superuser'] = True
        user = get_user_model().objects.create_user(**validated_data)
        return user

class AnimeMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimeMovie
        fields = ['pk', 'title', 'description']