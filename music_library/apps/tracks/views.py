from django.shortcuts import get_object_or_404

from rest_framework.generics import ListAPIView
from rest_framework.filters import OrderingFilter, SearchFilter

from music_library.apps.utils.paginators import BrowsePagePagination

from music_library.apps.releases.models import Release

from .models import Track
from .serializers import TrackSerializer


class BrowseTracksView(ListAPIView):
    serializer_class = TrackSerializer

    pagination_class = BrowsePagePagination
    filter_backends = (OrderingFilter, SearchFilter)
    search_fields = ('name', )
    ordering = ('id',)

    def get_queryset(self):
        artist_slug = self.request.GET.get('artist')
        if artist_slug:
            return Track.objects.filter(release__artist__slug=artist_slug)

        release_id = self.request.GET.get('release')
        if release_id:
            release = get_object_or_404(Release, id=release_id)
            return release.tracks

        return Track.objects.all()
