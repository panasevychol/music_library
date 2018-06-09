from django.conf import settings
from django.db import models

from music_library.apps.artists.models import Artist
from music_library.apps.tags.models import Tag


class Release(models.Model):
    NAME_PLURAL = 'releases'

    name = models.CharField(max_length=200)
    artist = models.ForeignKey(
        Artist, on_delete=models.CASCADE, related_name=NAME_PLURAL
    )
    description = models.TextField(blank=True)
    released_at = models.DateField()
    cover = models.ImageField(upload_to=settings.UPLOADS_DIR)
    tags = models.ManyToManyField(Tag, related_name=NAME_PLURAL)

    def __str__(self):
        return '"{}" by {}'.format(self.name, self.artist)
