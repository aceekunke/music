from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from api.models import SongModel
from api.serializers import SongSerializer

# Create your views here.
@api_view(['GET'])
def songs(request):
    songs = SongModel.objects.all()
    serializer = SongSerializer(songs, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def songCreate(request):
    serializer = SongSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)

@api_view(['GET', 'PUT', 'DELETE'])
def songsUpdate(request, pk):
    try:
        songs = SongModel.objects.get(pk=pk)
    except:
        return Response({
            'Sorry': 'Song does not exist'
        }, status=status.HTTP_404_NOT_FOUND)
        
    if request.method == 'GET':
        serializer = SongSerializer(songs)
    return Response(serializer.data)

    if request.method == "PUT":
        serializer = SongSerializer(songs, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        songs.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)