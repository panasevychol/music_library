from django.conf import settings
from django.db import models

from music_library.apps.artists.models import Artist


class Release(models.Model):
    name = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    released_at = models.DateField()
    cover = models.ImageField(upload_to=settings.UPLOADS_DIR)

    def __str__(self):
        return self.name
