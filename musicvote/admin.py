from django.contrib import admin
from .models import Artist, Song, Rating

class ArtistAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('artist_name',)}
	list_display = ('artist_name', 'get_songs')

class SongAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('song_title',)}
	list_display = ('song_title', 'get_artists', 'youtube_link', 'spotify_link')

class RatingAdmin(admin.ModelAdmin):
	list_display = ('song', 'user', 'rating')

# Register your models here.
admin.site.register(Artist, ArtistAdmin)
admin.site.register(Song, SongAdmin)
admin.site.register(Rating, RatingAdmin)