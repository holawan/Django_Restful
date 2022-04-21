from django.contrib import admin

# Register your models here.
from .models import Music,Artist

class ArtistAdmin(admin.ModelAdmin) :
    list_display = ('name',)
admin.site.register(Artist,ArtistAdmin)

class MusicAdmin(admin.ModelAdmin) :
    list_display = ('artist', 'title')
admin.site.register(Music,MusicAdmin)