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
		fields = ('id', 'artist_name', 'birthdate', 'songs')

class SongSerializer(serializers.HyperlinkedModelSerializer):
	artists = ArtistNameSerializer(read_only=True, many=True)
	number_of_ratings = serializers.IntegerField(read_only=True)
	average_rating = serializers.DecimalField(read_only=True, max_digits=None, decimal_places=2)

	class Meta:
		model = Song
		fields = ('id', 'song_title', 'artists', 'youtube_link', 'spotify_link', 'number_of_ratings', 'average_rating',)

	# def create(self, validated_data):
	# 	artist_data = validated_data.pop('artists')
	# 	print(artist_data)
	# 	song = Song.objects.create(**validated_data)
	# 	song.save()
	# 	for artist_item in artist_data:
	# 		print(artist_item)
	# 		a, created = Artist.objects.get_or_create(artist_name=artist_item['artist_name'])
	# 		print(a)
	# 		song.artists.add(a)
	# 	return song