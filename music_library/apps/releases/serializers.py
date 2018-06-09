from rest_framework import serializers

from .models import Release


class ReleaseSerializer(serializers.ModelSerializer):
    cover = serializers.StringRelatedField()

    class Meta:
        model = Release
        fields = (
            'name', 'description', 'cover', 'released_at', 'artist'
        )
