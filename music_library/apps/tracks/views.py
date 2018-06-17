from django.shortcuts import render

from rest_framework.generics import ListAPIView
from rest_framework.filters import OrderingFilter, SearchFilter

from music_library.apps.utils.paginators import BrowsePagePagination

from .models import Track
from .serializers import TrackSerializer


class BrowseTracksView(ListAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer

    pagination_class = BrowsePagePagination
    filter_backends = (OrderingFilter, SearchFilter)
    search_fields = ('name', )
    ordering = ('-id',)
