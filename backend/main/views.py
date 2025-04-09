from django.db.models import Q
from rest_framework import generics, status
from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import AnimeMovie, CustomUser
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
    queryset = AnimeMovie.objects.all()
    serializer_class = AnimeMovieSerializer

class AnimeMovieDelete(generics.RetrieveDestroyAPIView):
    queryset = AnimeMovie.objects.all()
    serializer_class = AnimeMovieSerializer

class AnimeMovieUpdate(generics.RetrieveUpdateAPIView):
    queryset = AnimeMovie.objects.all()
    serializer_class = AnimeMovieSerializer

class AnimeMovieDetail(generics.RetrieveAPIView):
    queryset = AnimeMovie.objects.all()
    serializer_class = AnimeMovieSerializer

class AnimeMovieList(generics.ListAPIView):
    serializer_class = AnimeMovieSerializer

    def get_queryset(self):
        queryset = AnimeMovie.objects.all().order_by('id')
        # filter by genre
        genres = self.request.query_params.getlist('genres')
        if genres:
            genre_filters = Q()
            for genre in genres:
                genre_filters |= Q(genres__contains=[genre])
            queryset = queryset.filter(genre_filters)
        # search by title and description
        search = self.request.query_params.get('search', '').strip()
        if search:
            queryset = queryset.filter(
                Q(title__icontains=search) |
                Q(description__icontains=search)
            )
        return queryset

class CustomUserCreate(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class CustomUserDelete(generics.RetrieveDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class CustomUserUpdate(generics.RetrieveUpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class CustomUserDetail(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        pk = self.kwargs.get('pk')
        if self.request.user.id != pk:
            raise PermissionDenied("Доступ запрещён.")
        return get_object_or_404(CustomUser, pk=pk)

class CustomUserList(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class AddAnimeToWatchedList(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk, anime_id):
        if request.user.id != pk:
            return Response({'error': 'Unauthorized'}, status=status.HTTP_403_FORBIDDEN)

        try:
            anime = AnimeMovie.objects.get(id=anime_id)
        except AnimeMovie.DoesNotExist:
            return Response({'error': f'Anime with ID {anime_id} not found'}, status=status.HTTP_404_NOT_FOUND)

        request.user.movie_watched.add(anime)
        return Response({'message': 'Anime added to watched list'}, status=status.HTTP_200_OK)


class RemoveAnimeFromWatchedList(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk, anime_id):
        if request.user.id != pk:
            return Response({'error': 'Unauthorized'}, status=status.HTTP_403_FORBIDDEN)

        try:
            anime = AnimeMovie.objects.get(id=anime_id)
        except AnimeMovie.DoesNotExist:
            return Response({'error': f'Anime with ID {anime_id} not found'}, status=status.HTTP_404_NOT_FOUND)

        request.user.movie_watched.remove(anime)
        return Response({'message': 'Anime removed from watched list'}, status=status.HTTP_200_OK)


class GetWatchedList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = AnimeMovieSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if self.request.user.id != pk:
            raise PermissionDenied("Вы не можете просматривать список другого пользователя.")
        return self.request.user.movie_watched.all()
