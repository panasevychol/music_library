from django.conf import settings
from django.db import models

from music_library.apps.releases.models import Release
from music_library.apps.tags.models import Tag


class Track(models.Model):
    NAME_PLURAL = 'tracks'

    name = models.CharField(max_length=200)
    release = models.ForeignKey(
        Release, on_delete=models.CASCADE, related_name=NAME_PLURAL
    )
    duration = models.DurationField()
    tags = models.ManyToManyField(Tag, related_name=NAME_PLURAL)
    popularity = models.PositiveIntegerField(
        choices=settings.POPULARITY_CHOICES, default=0
    )
    playlink = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return '"{}" from {}'.format(self.name, self.release)
