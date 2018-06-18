from django.shortcuts import get_object_or_404

from rest_framework.generics import ListAPIView
from rest_framework.filters import OrderingFilter, SearchFilter

from music_library.apps.utils.paginators import BrowsePagePagination
from music_library.apps.artists.models import Artist

from .models import Release
from .serializers import ReleaseSerializer


class BrowseReleasesView(ListAPIView):
    queryset = Release.objects.all()
    serializer_class = ReleaseSerializer

    pagination_class = BrowsePagePagination
    filter_backends = (OrderingFilter, SearchFilter)
    search_fields = ('name', )
    ordering_fields = (
        'popularity',
    )
    ordering = ('-popularity',)

    def get_queryset(self):
        artist_slug = self.request.GET.get('artist')
        if artist_slug:
            artist = get_object_or_404(Artist, slug=artist_slug)
            queryset = artist.releases
        else:
            queryset = Release.objects.all()
        return queryset
