from django.conf import settings
from django.db import models

from music_library.apps.tags.models import Tag


class Artist(models.Model):
    NAME_PLURAL = 'artists'

    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    picture = models.ImageField(blank=True, upload_to=settings.UPLOADS_DIR)
    tags = models.ManyToManyField(Tag, related_name=NAME_PLURAL)

    def __str__(self):
        return self.name
