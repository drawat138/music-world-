from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),
    path('songdetails/',views.songdetails),
    path('movies/',views.movies),
    path('videos/',views.videos),
    path('download/<id>',views.download),
    path('player/<id>',views.player),
    path('moviedownload/<id>',views.moviedownload),
    path('register/',views.register),
    path('login/',views.login),
    path('instrumental/',views.instrumental),
    path('godsong/',views.godsong),
]
