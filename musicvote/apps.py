from django.apps import AppConfig
from rest_framework import viewsets, generics

from .models import Artist, Song, Rating
from .serializers import QuestionSerializer

class MusicvoteConfig(AppConfig):
    name = 'musicvote'
