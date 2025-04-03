from django.urls import path

from .views import AnimeMovieCreate, AnimeMovieList, AnimeMovieDetail, AnimeMovieUpdate, AnimeMovieDelete

urlpatterns = [
    path('create/', AnimeMovieCreate.as_view(), name='create-anime_movie'),
    path('list/', AnimeMovieList.as_view(), name='anime_movie_list'),
    path('<int:pk>/', AnimeMovieDetail.as_view(), name='retrieve-anime_movie'),
    path('update/<int:pk>/', AnimeMovieUpdate.as_view(), name='update-anime_movie'),
    path('delete/<int:pk>/', AnimeMovieDelete.as_view(), name='delete-anime_movie'),
]
