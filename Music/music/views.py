from django.shortcuts import render,get_list_or_404,get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Artist,Music
from .serializer import ArtistListSerializer, ArtistSerializer, MusicSerializer
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

@api_view(['GET','DELETE','PUT'])
def artist_detail(request,artist_pk) :
    artist = get_object_or_404(Artist,pk=artist_pk)
    if request.method == 'GET' :
        serializer = ArtistListSerializer(artist)
        return Response(serializer.data)
    
    elif request.method == 'DELETE' :
        artist.delete()
        data = {
            'delete' : f'데이터 {artist_pk} 삭제 완료'
        }
        return Response(data,status=status.HTTP_204_NO_CONTENT)
    elif request.method =='PUT' :
        serializer = ArtistSerializer(artist,data=request.data)
        if serializer.is_valid(raise_exception=True) :
            serializer.save()
            return Response(serializer.data)

@api_view(['GET'])
def music_list(request) :
    musics = get_list_or_404(Music)
    serializer = MusicSerializer(musics,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def music_create(request,artist_pk) :
    artist = get_object_or_404(Artist,pk=artist_pk) 
    serializer = MusicSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True) :
        serializer.save(artist=artist)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET','DELETE','PUT'])
def music_detial(request,music_pk) :
    music = get_object_or_404(Music,pk=music_pk)
    if request.method == 'GET' :
        serializer = MusicSerializer(music)
        return Response(serializer.data)
    elif request.method == 'DELETE' :
        music.delete()
        data = {
            'delete' : f'데이터 {music_pk} 삭제 완료'
        }
        return Response(data,status=status.HTTP_204_NO_CONTENT)
    elif request.method =='PUT' :
        serializer = MusicSerializer(music,data=request.data)
        if serializer.is_valid(raise_exception=True) :
            serializer.save()
            return Response(serializer.data)
