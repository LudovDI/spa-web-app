from django.db import models

from anime_movie.models import AnimeMovie


class AnimeViewer(models.Model):
    name = models.CharField("Name",max_length=240)
    email = models.EmailField()
    created = models.DateField(auto_now_add=True)

    watched_anime_list = models.ManyToManyField(AnimeMovie, blank=True, related_name="viewers")

    def __str__(self):
        return self.name

