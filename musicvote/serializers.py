from rest_framework import serializers

from .models import Artist, Song, Rating

class ArtistNameSerializer(serializers.ModelSerializer):
	class Meta:
		model = Artist
		fields = ('artist_name',)

	def to_representation(self, value):
		return value.artist_name

class SongTitleSerializer(serializers.ModelSerializer):
	songs = serializers.PrimaryKeyRelatedField(read_only=True, many=True)

	def to_representation(self, value):
		return value.song_title

	class Meta:
		model = Song
		fields = ('songs',)

class ArtistSerializer(serializers.HyperlinkedModelSerializer):
	songs = SongTitleSerializer(read_only=True, many=True)

	class Meta:
		model = Artist
		fields = ('artist_name', 'birthdate', 'songs')

class SongSerializer(serializers.HyperlinkedModelSerializer):
	artists = ArtistNameSerializer(read_only=True, many=True)
	number_of_ratings = serializers.IntegerField()
	average_rating = serializers.DecimalField(max_digits=None, decimal_places=2)

	class Meta:
		model = Song
		fields = ('song_title', 'artists', 'youtube_link', 'spotify_link', 'number_of_ratings', 'average_rating',)

