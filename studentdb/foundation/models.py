from django.db import models

class StudentDB(models.Model):
    fname = models.CharField(max_length = 50)
    lname = models.CharField(max_length = 50)
    mark = models.FloatField()
    email = models.CharField(max_length=100)
