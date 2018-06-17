from rest_framework.generics import ListAPIView
from rest_framework.filters import (
    OrderingFilter,
    SearchFilter,
)

from music_library.apps.utils.paginators import BrowsePagePagination

from .models import Artist
from .serializers import ArtistSerializer



class BrowseArtistsView(ListAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

    pagination_class = BrowsePagePagination
    filter_backends = (OrderingFilter, SearchFilter)
    search_fields = ('name', )
    ordering_fields = (
        'popularity',
    )
    ordering = ('-popularity',)
