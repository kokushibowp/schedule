from django.db import models

import datetime

from django.core.validators import MaxValueValidator, MinValueValidator

class Room(models.Model):
    id = models.IntegerField(primary_key=True)
    roomNumber = models.IntegerField(default=0)
    NFC = models.CharField(max_length=50, default="none", unique=True)
    numpostfix = models.CharField(max_length=5, default="", blank=True)

class Lesson(models.Model):
    id = models.AutoField(primary_key=True)
    foreign_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    subject = models.CharField(max_length=240, default="none")
    lecturer = models.CharField(max_length=120, default="none")
    #numclassroom = models.IntegerField(default=0)
    startTime = models.TimeField(default=datetime.time(0, 0, 0))
    endTime = models.TimeField(default=datetime.time(0, 23, 59)) 
    numofday = models.IntegerField(default = 0, validators=[MaxValueValidator(14), MinValueValidator(1)])
    #weekIsFirst = models.BooleanField(default=True)

    def __str__(self):
        return self.subject