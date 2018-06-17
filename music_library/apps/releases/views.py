from django.shortcuts import render

from rest_framework.generics import ListAPIView
from rest_framework.filters import OrderingFilter, SearchFilter

from music_library.apps.utils.paginators import BrowsePagePagination

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
