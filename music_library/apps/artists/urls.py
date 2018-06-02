from django.urls import path

from . import views

urlpatterns = [
    path('browse/', views.BrowseArtistsView.as_view(), name='browse-artists'),
]
