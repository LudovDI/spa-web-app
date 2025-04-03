from django.urls import path

from .views import AnimeViewerCreate, AnimeViewerList, AnimeViewerDetail, AnimeViewerUpdate, \
    AnimeViewerDelete, AddAnimeToWatchedList

urlpatterns = [
    path('create/', AnimeViewerCreate.as_view(), name='create-anime_viewer'),
    #path('', AnimeViewerList.as_view()),
    path('<int:pk>/', AnimeViewerDetail.as_view(), name='retrieve-anime_viewer'),
    path('update/<int:pk>/', AnimeViewerUpdate.as_view(), name='update-anime_viewer'),
    path('delete/<int:pk>/', AnimeViewerDelete.as_view(), name='delete-anime_viewer'),
    path('<int:pk>/add_anime/<int:anime_id>/', AddAnimeToWatchedList.as_view(), name='add-anime'),
]
