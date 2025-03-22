from django.db import models

class Lesson(models.Model):
    id = models.IntegerField(primary_key=True)
    discipline = models.CharField(max_length=240)
    teachername = models.CharField(max_length=120)
    numclassroom = models.IntegerField()
    time = models.TimeField()

    def __str__(self):
        return self.discipline