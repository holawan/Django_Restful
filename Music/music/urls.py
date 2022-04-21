from django.urls import path
from . import views

urlpatterns = [
    path('artists/',views.artist_list),
    path('artists/<int:artist_pk>/',views.artist_detail),
    path('music/',views.music_list),
    path('artist/<int:artist_pk>/music/',views.music_detail),
]