from django.db import models

import datetime

class DayWeek(models.Model):
    numofday = models.IntegerField(primary_key=True)

class Room(models.Model):
    id = models.IntegerField(primary_key=True)
    numclassroom = models.IntegerField(default=0)
    NFC = models.CharField(max_length=50, default="none")
    numpostfix = models.CharField(max_length=5, default="-")

class Lesson(models.Model):
    id = models.AutoField(primary_key=True)
    foreign_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    discipline = models.CharField(max_length=240, default="none")
    teachername = models.CharField(max_length=120, default="none")
    #numclassroom = models.IntegerField(default=0)
    time1 = models.TimeField(default=datetime.time(0, 0, 30))
    time2 = models.TimeField(default=datetime.time(0, 0, 30)) 
    numofday = models.ForeignKey(DayWeek, on_delete=models.CASCADE)
    #weekIsFirst = models.BooleanField(default=True)

    def __str__(self):
        return self.discipline