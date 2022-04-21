from django.shortcuts import render,get_list_or_404,get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Artist
from .serializer import ArtistListSerializer, ArtistSerializer
from music import serializer

# Create your views here.


@api_view(['GET','POST'])
def artist_list(request) :
    if request.method == 'GET' : 
        artists = get_list_or_404(Artist)
        serializer = ArtistListSerializer(artists,many=True)
        return Response(serializer.data)

    elif request.method == 'POST' :
        serializer = ArtistSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True) :
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)

@api_view(['GET'])
def artist_detail(request,artist_pk) :
    artist = get_object_or_404(Artist,pk=artist_pk)
    if request.method == 'GET' :
        serializer = ArtistListSerializer(artist)
        return Response(serializer.data)