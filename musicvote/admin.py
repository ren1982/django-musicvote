from django.contrib import admin
from .models import Artist, Song, Rating

class ArtistAdmin(admin.ModelAdmin):
	list_display = ('artist_name', 'get_songs')

class SongAdmin(admin.ModelAdmin):
	list_display = ('song_title', 'get_artists', 'youtube_link', 'spotify_link')

# Register your models here.
admin.site.register(Artist, ArtistAdmin)
admin.site.register(Song, SongAdmin)
admin.site.register(Rating)