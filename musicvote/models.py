from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import Avg
from django.conf import settings
from django.utils.text import slugify
from django.urls import reverse

class Artist(models.Model):
	artist_name = models.CharField(max_length=200, unique=True)
	slug = models.SlugField(unique=True)
	birthdate = models.DateField(blank=True, null=True)
	# photo = models.CharField(max_length=200, blank=True, default='') # Placeholder for image name in \music\musicvote\static\musicvote
	photo = models.ImageField(upload_to='artistphotos', blank=True, null=True)

	class Meta:
		ordering = ['artist_name']

	def __str__(self):
		return self.artist_name

	def save(self, *args, **kwargs):
		self.slug = self.slug or slugify(self.artist_name)
		super().save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse('musicvote:artist-detail', kwargs={"slug": self.slug, "pk": self.pk})

	def get_songs(self):
		return ", ".join(["\"" + s.song_title +"\"" for s in self.songs.all()])
	get_songs.short_description = 'Song(s)'

class Song(models.Model):
	song_title = models.CharField(max_length=200)
	slug = models.SlugField(unique=True)
	artists = models.ManyToManyField(Artist, related_name='songs')
	youtube_link = models.URLField(max_length=200, blank=True, default='')
	spotify_link = models.URLField(max_length=200, blank=True, default='')
	cover = models.ImageField(upload_to='songcovers', blank=True, null=True)

	class Meta:
		ordering = ['song_title']

	def __str__(self):
		return self.song_title

	def save(self, *args, **kwargs):
		self.slug = self.slug or slugify(self.song_title)
		super().save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse('musicvote:song-detail', kwargs={"slug": self.slug, "pk": self.pk})

	def get_artists(self):
		return ", ".join([a.artist_name for a in self.artists.all()])
	get_artists.short_description = 'Artist(s)'

class Rating(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user')
	song = models.ForeignKey(Song, on_delete=models.CASCADE, related_name='ratings')
	rating = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])

	class Meta:
		constraints = [
			models.UniqueConstraint(fields=['user', 'song'], name='rating by user')
		]			

	def __str__(self):
		return str(self.rating)