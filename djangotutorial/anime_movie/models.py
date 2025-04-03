from django.db import models

class AnimeMovie(models.Model):
    title = models.CharField("Title", max_length=240)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
