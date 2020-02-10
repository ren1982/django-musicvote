from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.db.models import Avg, Count
# from django.http import Http404
# from django.template import loader
from rest_framework import viewsets, generics

from .models import Artist, Song
from .serializers import ArtistSerializer, SongSerializer

# APP/WEBSITE VIEWS
class IndexView(generic.ListView):
	queryset = Artist.objects.all()
	# ListView: "display a list of objects"
	# default template_name is <app_name>/<model_name>_list.html
	template_name = 'musicvote/index.html'
	# automatically generated context variable is named question_list, so we override it here (because of our template)
	# context_object_name = 'latest_question_list'

	# def get_queryset(self):
	# 	"""Return the last five published questions (excluding those set to be published in the future."""
	# 	return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

	def get_queryset(self):
		return Artist.objects.annotate(number_of_songs=Count('songs'))

class ArtistDetailView(generic.DetailView):
	# DetailView: "display a detail page for a particular type of object"
	model = Artist
	# Django is able to determine an appropriate name of the context variable, which is the model name in lowercase
	# Django then uses the pk to find the object in the given model
	# default template_name is <app_name>/<model_name>_detail.html

	def get_queryset(self):
		return Artist.objects.annotate(number_of_songs=Count('songs'))

	def get_context_data(self, **kwargs):
		"""
		Add list of songs by the artist.
		"""
		context = super().get_context_data(**kwargs)
		context['song_titles'] = context['artist'].songs.all()
		return context

	def get(self, request, *args, **kwargs):
		self.object = self.get_object()

		if self.request.path != self.object.get_absolute_url():
			return redirect(self.object, permanent=True)

		return super().get(self, request, args, kwargs)

class SongDetailView(generic.DetailView):
	# DetailView: "display a detail page for a particular type of object"
	model = Song
	# Django is able to determine an appropriate name of the context variable, which is the model name in lowercase
	# Django then uses the pk to find the object in the given model
	# default template_name is <app_name>/<model_name>_detail.html

	def get_queryset(self):
		return Song.objects.annotate(number_of_ratings=Count('ratings__rating'), average_rating=Avg('ratings__rating'))

	def get_object(self, queryset=None):
		object = super().get_object(queryset)
		temp = object.youtube_link
		object.youtube_stub = temp.split('=')[-1]
		temp = object.spotify_link
		object.spotify_stub = temp.split('/')[-1].split('?')[0]
		return object

	def get_context_data(self, **kwargs):
		"""
		Add list of names of all artists involved in the song
		"""
		context = super().get_context_data(**kwargs)
		context['artist_names'] = ', '.join([artist.artist_name for artist in context['song'].artists.all()])
		return context

	def get(self, request, *args, **kwargs):
		self.object = self.get_object()

		if self.request.path != self.object.get_absolute_url():
			return redirect(self.object, permanent=True)

		return super().get(self, request, args, kwargs)

# def rate_song(request, song_id):
# 	song = get_object_or_404(Song, pk=song_id)
# 	score = request.POST['score']
# 	new_rating = Rating(song=song, rating=score)
# 		selected_choice = question.choice_set.get(pk=request.POST['choice'])
# 	except (KeyError, Choice.DoesNotExist):
# 		# Redisplay the question voting form
# 		return render(request, 'polls/detail.html', {
# 			'question': question,
# 			'error_message': "You didn't select a choice.",
# 		})
# 	else:
# 		selected_choice.votes += 1
# 		selected_choice.save()
# 		# Always return an HttpResponseRedirect after successfully dealing with POST data.
# 		# This prevents data from being posted twice ifa user hits the Back button.
# 		# reverse('polls:results', args=(question.id)) is analog to {% url 'polls:results' question.id %}
# 		return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

# API VIEWS
class ArtistViewSet(viewsets.ModelViewSet):
	queryset = Artist.objects.all()
	serializer_class = ArtistSerializer

class SongViewSet(viewsets.ModelViewSet):
	queryset = Song.objects.all()
	serializer_class = SongSerializer

	def get_queryset(self):
		return Song.objects.annotate(number_of_ratings=Count('ratings__rating'), average_rating=Avg('ratings__rating'))