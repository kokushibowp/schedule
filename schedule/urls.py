from django.urls import path
from . import views

from .views import RoomView


app_name = "lessons"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    #path('lessons/', LessonView.as_view()),
    #path('rooms/', RoomView.as_view()),
    path('rooms/', views.room_detail, name='room_detail'),
]