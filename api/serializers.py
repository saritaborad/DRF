from .models import Singer, Song
from rest_framework import serializers 

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'title', 'singer', 'duration']

class SingerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Singer
        fields = ['id', 'name', 'gender']