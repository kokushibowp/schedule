from rest_framework import serializers
from .models import Lesson, Room

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'numclassroom', 'NFC', 'numpostfix']

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'#['id', 'discipline', 'teachername', 'numclassroom', 'time']