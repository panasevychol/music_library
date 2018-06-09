from django.db import models


class Tag(models.Model):
    name = models.SlugField()

    def __str__(self):
        return self.name
