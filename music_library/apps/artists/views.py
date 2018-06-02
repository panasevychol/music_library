from django.http import HttpResponse

from rest_framework.generics import ListAPIView
from rest_framework.filters import (
    OrderingFilter,
    SearchFilter,
)

from music_library.apps.utils.paginators import BrowsePagePagination

from .models import Artist
from .serializers import ArtistSerializer

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the artists index.")


class BrowseArtistsView(ListAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

    pagination_class = BrowsePagePagination
    filter_backends = (OrderingFilter, SearchFilter)
    search_fields = ('name', )
    ordering_fields = (
        'name',
    )
    ordering = ('name',)
