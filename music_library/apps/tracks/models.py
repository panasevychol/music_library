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

    def __str__(self):
        return '"{}" from {}'.format(self.name, self.release)
