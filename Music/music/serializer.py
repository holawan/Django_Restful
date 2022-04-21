from nntplib import ArticleInfo
from rest_framework import serializers
from .models import Artist


class ArtistListSerializer(serializers.ModelSerializer) :

    class Meta :
        model = Artist
        fields = ('id','name',)

class ArtistSerializer(serializers.ModelSerializer) :
    
    class Meta :
        model = Artist
        fields = '__all__'