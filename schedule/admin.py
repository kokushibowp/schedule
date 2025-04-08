from django.contrib import admin

from .models import Lesson, Room, DayWeek

admin.site.register(Lesson)
admin.site.register(Room)
admin.site.register(DayWeek)
