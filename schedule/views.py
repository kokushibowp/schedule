from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import LessonSerializer

from .models import Lesson


class LessonView(APIView):
    def get(self, request):
        my_header = request.headers.get('id')
        lesson = Lesson.objects.filter(id = my_header)
        serializer = LessonSerializer(lesson, many=True)  
        return Response({"lesson": serializer.data})
#        return Response({"lessons": lessons})
