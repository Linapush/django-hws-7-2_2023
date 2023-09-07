from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from django.contrib.auth import views as auth_views

router = DefaultRouter()
router.register(r'Tracks', views.TracksViewSet, basename='Tracks')
router.register(r'Genres', views.GenresViewSet, basename='Genres')
router.register(r'Artists', views.ArtistsViewSet, basename='Artists')
router.register(r'Albums', views.AlbumsViewSet, basename='Albums')

urlpatterns = [
    path('', views.custom_main, name='homepage'),
    path('profile/', views.profile_page, name='profile'),
    path('purchase/', views.purchase_page, name='purchase'),
    path('listen/', views.listen_music, name='listen'),
    path('subscription/', views.subscription, name='subscription'),
    path('audio_page/', views.audio_page, name='audio_page'),
    path('succes/', views.purchase_page, name='succes'),
    path('error/', views.purchase_page, name='error'),

    path('tracks/', views.TracksListView.as_view(), name='tracks'),
    path('tracks/rest/track_list', views.track_list, name='track_list'),
    path('artists/', views.ArtistsListView.as_view(), name='artists'),
    path('genres/', views.GenresListView.as_view(), name='genres'),
    path('albums/', views.AlbumsListView.as_view(), name='albums'),

    path('track/', views.track_view, name='track'),
    path('genre/', views.genre_view, name='genre'),
    path('artist/', views.artist_view, name='artist'),
    path('album/', views.album_view, name='album'),

    # REST
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('rest/', include(router.urls)),
    path('api_youtube/', views.tracks_api, name='youtube library'),
    path('rest/track_list/', views.track_list, name='track_list'),

    # auth
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    
]


from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)