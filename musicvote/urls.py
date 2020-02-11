from django.urls import include, path
from rest_framework import routers

from . import views

app_name = 'musicvote'

urlpatterns = [
	# path('', views.home, name='home'),
	path('', views.IndexView.as_view(), name='home'),
	path('artists/', views.IndexView.as_view(), name='index'),
	path('artist/<slug:slug>-<int:pk>/', views.ArtistDetailView.as_view(), name='artist-detail'),
	path('song/<slug:slug>-<int:pk>/', views.SongDetailView.as_view(), name='song-detail'),
	path('song/<slug:slug>-<int:song_id>/rate/<int:rating>', views.rate_song, name='rate'),
]