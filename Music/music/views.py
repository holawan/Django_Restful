from django.shortcuts import render,get_list_or_404,get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Artist
from .serializer import ArtistListSerializet

# Create your views here.


@api_view(['GET'])
def artist_list(request) :
    artists = get_list_or_404(Artist)
    serializer = ArtistListSerializet(artists,many=True)
    return Response(serializer.data)