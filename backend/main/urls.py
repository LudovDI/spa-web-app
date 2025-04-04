from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import EmailTokenObtainPairView, RegisterView, AnimeMovieCreate, AnimeMovieList

app_name = "main"

urlpatterns = [
    path('register/', RegisterView.as_view(), name='token_obtain_pair'),
    path('token/', EmailTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('anime_movie/list/', AnimeMovieList.as_view(), name='anime_movie_list'),
    path('anime_movie/create/', AnimeMovieCreate.as_view(), name='anime_movie_create'),
]