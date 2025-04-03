from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import AnimeViewer
from .serializers import AnimeViewerSerializer
from anime_movie.models import AnimeMovie


class AnimeViewerCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new anime viewer
    queryset = AnimeViewer.objects.all(),
    serializer_class = AnimeViewerSerializer

class AnimeViewerList(generics.ListAPIView):
    # API endpoint that allows anime viewer to be viewed
    queryset = AnimeViewer.objects.all()
    serializer_class = AnimeViewerSerializer

class AnimeViewerDetail(generics.RetrieveAPIView):
    # API endpoint that returns a single anime viewer by pk.
    queryset = AnimeViewer.objects.all()
    serializer_class = AnimeViewerSerializer

class AnimeViewerUpdate(generics.RetrieveUpdateAPIView):
    # API endpoint that allows an anime viewer record to be updated.
    queryset = AnimeViewer.objects.all()
    serializer_class = AnimeViewerSerializer

class AnimeViewerDelete(generics.RetrieveDestroyAPIView):
    # API endpoint that allows an anime viewer record to be deleted.
    queryset = AnimeViewer.objects.all()
    serializer_class = AnimeViewerSerializer

class AddAnimeToWatchedList(APIView):
    def post(self, request, pk, anime_id):
        try:
            viewer = AnimeViewer.objects.get(pk=pk)
        except AnimeViewer.DoesNotExist:
            return Response({'error': 'Viewer not found'}, status=status.HTTP_404_NOT_FOUND)

        try:
            anime = AnimeMovie.objects.get(id=anime_id)
        except AnimeMovie.DoesNotExist:
            return Response({'error': f'Anime with ID {anime_id} not found'}, status=status.HTTP_404_NOT_FOUND)

        print(f"User:{viewer} Anime:{anime}")
        viewer.watched_anime_list.add(anime)
        viewer.save()
        return Response({'message': 'Anime movie added successfully'}, status=status.HTTP_200_OK)
