from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import EmailTokenObtainPairView, RegisterView, AnimeMovieCreate, AnimeMovieList, AddAnimeToWatchedList, \
    AnimeMovieDetail, AnimeMovieUpdate, AnimeMovieDelete, CustomUserCreate, CustomUserUpdate, CustomUserDelete, \
    CustomUserList, CustomUserDetail, RemoveAnimeFromWatchedList, GetWatchedList

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('token/', EmailTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('anime_movie_create/', AnimeMovieCreate.as_view(), name='anime_movie_create'),
    # path('anime_movie_update/<int:pk>/', AnimeMovieUpdate.as_view(), name='anime_movie_update'),
    # path('anime_movie_delete/<int:pk>/', AnimeMovieDelete.as_view(), name='anime_movie_delete'),
    path('anime_movie_list/', AnimeMovieList.as_view(), name='anime_movie_list'),
    path('anime_movie_detail/<int:pk>/', AnimeMovieDetail.as_view(), name='anime_movie_detail'),
    # path('user/create/', CustomUserCreate.as_view(), name='custom_user_create'),
    # path('user/update/<int:user_id>/', CustomUserUpdate.as_view(), name='custom_user_update'),
    # path('user/delete/<int:user_id>/', CustomUserDelete.as_view(), name='custom_user_delete'),
    # path('user_list/', CustomUserList.as_view(), name='custom_user_list'),
    path('user_detail/<int:pk>/', CustomUserDetail.as_view(), name='custom_user_detail'),
    path('<int:pk>/add_anime/<int:anime_id>/', AddAnimeToWatchedList.as_view(), name='add_anime'),
    path('<int:pk>/remove_anime/<int:anime_id>/', RemoveAnimeFromWatchedList.as_view(), name='remove_anime'),
    path('<int:pk>/watched_anime/', GetWatchedList.as_view(), name='watched_anime_list'),
]