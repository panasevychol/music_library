from rest_framework import serializers

from .models import Release


class ReleaseSerializer(serializers.ModelSerializer):
    cover = serializers.StringRelatedField()
    artist = serializers.SlugRelatedField(slug_field='slug', read_only=True)

    class Meta:
        model = Release
        fields = (
            'name', 'description', 'cover', 'released_at', 'artist', 'tracks',
            'tags', 'id'
        )
