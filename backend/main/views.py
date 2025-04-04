from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import AnimeMovie
from .serializers import UserSerializer, TokenObtainPairSerializer, AnimeMovieSerializer


class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User created successfully"}, status=201)
        return Response(serializer.errors, status=400)


class EmailTokenObtainPairView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer

class AnimeMovieCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new customer
    queryset = AnimeMovie.objects.all(),
    serializer_class = AnimeMovieSerializer

class AnimeMovieList(generics.ListAPIView):
    # API endpoint that allows creation of a new customer
    queryset = AnimeMovie.objects.all(),
    serializer_class = AnimeMovieSerializer
