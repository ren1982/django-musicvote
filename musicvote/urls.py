from django.urls import include, path
from rest_framework import routers

from . import views

app_name = 'musicvote'

urlpatterns = [
	path('', views.IndexView.as_view(), name='index'),
	path('<int:pk>/', views.ArtistDetailView.as_view(), name='artist-detail'),
	path('song/<int:pk>/', views.SongDetailView.as_view(), name='song-detail'),
	# path('song/<int:song_id>/rate/', views.rate_song, name='rate'),
	# path('api/artists/<int:pk>', views.ArtistDetailView.as_view(), name='artist-detail'),
	# path('api/artists', views.ArtistViewSet.as_view(), name='artists-api'),	
]