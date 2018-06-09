from rest_framework import serializers

from .models import Artist


class ArtistSerializer(serializers.ModelSerializer):
    picture = serializers.StringRelatedField()

    class Meta:
        model = Artist
        fields = (
            'name', 'slug', 'description', 'picture', 'releases'
        )
