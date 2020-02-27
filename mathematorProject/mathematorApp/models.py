from django.db import models

# Create your models here.

class Student(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    isTeacher = models.BooleanField()

class Exercise(models.Model):
    name = models.CharField(max_length=50)
    objective = models.CharField(max_length=50)
    theme = models.CharField(max_length=50)
    branches = models.CharField(max_length=50)
    year = models.CharField(max_length=50)
