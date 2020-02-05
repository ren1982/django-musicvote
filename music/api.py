from rest_framework import routers
from musicvote import views as myapp_views

router = routers.DefaultRouter()
router.register(r'artists', myapp_views.ArtistViewSet)
router.register(r'songs', myapp_views.SongViewSet)