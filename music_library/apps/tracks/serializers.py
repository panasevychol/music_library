from rest_framework import serializers

from .models import Track


class TrackSerializer(serializers.ModelSerializer):
    artist_name = serializers.SerializerMethodField()

    class Meta:
        model = Track
        fields = (
            'name', 'duration', 'playlink', 'artist_name'
        )

    def get_artist_name(self, obj):
        return obj.release.artist.name
