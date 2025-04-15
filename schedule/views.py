from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import LessonSerializer, RoomSerializer
from django.http import HttpResponse
import datetime

from .models import Lesson, Room

from django.utils.timezone import localtime

start_first_semster = datetime.date(datetime.datetime.now().year, 9, 1)
first_semester_starting_point = datetime.date(datetime.datetime.now().year, 9, 1 - start_first_semster.weekday())
start_double_semster = datetime.date(datetime.datetime.now().year, 2, 7)
double_semester_starting_point = datetime.date(datetime.datetime.now().year, 2, 7 - start_double_semster.weekday())

def find_lessons(room_id):
    time = localtime().time()
    if (datetime.datetime.now().month >= 2) and (datetime.datetime.now().day >=7):
        numofday = ((datetime.datetime.now().date() - double_semester_starting_point).days + 1) % 14
    lessons_list = LessonSerializer(Lesson.objects.filter(foreign_id = room_id, startTime__lt = time, endTime__gt = time, numofday = numofday), many=True)
    return lessons_list.data

def create_room_list(all_id):
    room_list = []
    for i in range(len(all_id)):
        room_list.append(find_lessons(all_id[i]))
    return room_list

def room_detail(request):
    #objectsfromNFC = Room.objects.filter(NFC = entering_NFC)
    enteringNFC = request.GET.get('tagUid')
    print(enteringNFC)
    objectfromNFC = Room.objects.filter(NFC = enteringNFC).first()
    #lesson = Lesson.objects.filter(foreign_id = objectsfromNFC.id)
    all_id = list(Room.objects.all().values_list('id', flat=True)) 
    serializer = RoomSerializer(objectfromNFC, many=False)
    roomData = serializer.data
    
    time = localtime().time()
    if (datetime.datetime.now().month >= 2) and (datetime.datetime.now().day >=7):
        numofday = ((datetime.datetime.now().date() - double_semester_starting_point).days + 1) % 14
    try:
        lesson = Lesson.objects.filter(foreign_id=objectfromNFC, startTime__lt = time, endTime__gt = time, numofday = numofday).first()
    except:
        return HttpResponse(f"404")


    lessonSerializer = LessonSerializer(lesson, many=False)
    lessonData = lessonSerializer.data

    roomData['subject'] = lessonData['subject']
    roomData['lecturer'] = lessonData['lecturer']
    roomData['startTime'] = lessonData['startTime']
    roomData['endTime'] = lessonData['endTime']

    #return HttpResponse(f"Data: {((datetime.datetime.now().date() - double_semester_starting_point).days + 1) % 14}")
    #return HttpResponse(f"Data: {create_room_list(all_id)}")
    return HttpResponse(f"{roomData}")
    #return HttpResponse(f"Data: {LessonSerializer(lesson, many=True).data}")

class RoomView(APIView):
    def get(self, request):
        #my_header = request.headers.get('NFC')
        time = localtime().time()
        return HttpResponse(time)
#class LessonView(APIView):
#    def get(self, request):
#        my_header = request.headers.get('id')
#        lesson = Lesson.objects.filter(id = my_header)
#        serializer = LessonSerializer(lesson, many=True)  
#        return Response({"lesson": serializer.data})
#        return Response({"lessons": lessons})
