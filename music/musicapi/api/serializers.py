from rest_framework import serializers
from api.models import ArtisteModel, SongModel, models

class SongSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    artiste = serializers.ForeignKey(ArtisteModel, on_delete=models.CASCADE, read_only=True)
    title = serializers.CharField(max_length = 200)
    date_released = serializers.DateField()
    likes = serializers.IntegerField()

    def create(self, data):
        return SongModel.objects.create(**data)

    def update(self, instance, data):
        instance.title = data.get('title', instance.title)
        instance.date_released = data.get('date_released', instance.date_released)
        instance.likes = data.get('likes', instance.likes)

        instance.save()
        return instance

class ArtisteSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(max_length = 200)
    last_name = serializers.CharField(max_length = 200)
    age = serializers.TextField()

    def create(self, data):
        return ArtisteModel.objects.create(**data)

    def update(self, instance, data):
        instance.first_name = data.get('first_name', instance.first_name)
        instance.last_name = data.get('last_name', instance.last_name)
        instance.lage = data.get('age', instance.age)

        instance.save()
        return instance