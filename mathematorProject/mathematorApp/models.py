from django.db import models

# Create your models here.

class student(models.Model):
    firstName=models.CharField(max_length=50)