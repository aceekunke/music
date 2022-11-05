from django.contrib import admin
from django.urls import path
from api.views import songs, songCreate, songsUpdate

urlpatterns = [
    path('songs/', songs),
    path('create/', songCreate),
    path('<int:pk>', songsUpdate)
]