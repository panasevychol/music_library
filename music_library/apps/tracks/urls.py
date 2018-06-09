from django.urls import path

from . import views


urlpatterns = [
    path('browse/', views.BrowseTracksView.as_view(), name='browse-tracks'),
]
