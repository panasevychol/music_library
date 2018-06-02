from django.conf import settings

from rest_framework import pagination


class BrowsePagePagination(pagination.PageNumberPagination):
    page_size_query_param = 'page_size'
    page_size = settings.ITEMS_PER_PAGE
