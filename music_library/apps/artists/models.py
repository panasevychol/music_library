from django.conf import settings
from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    description = models.TextField(blank=True)
    picture = models.ImageField(blank=True, upload_to=settings.UPLOADS_DIR)

    def __str__(self):
        return self.name
