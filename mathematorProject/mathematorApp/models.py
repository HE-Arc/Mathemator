from django.db import models

# Create your models here.

class Student(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    isTeacher = models.BooleanField()
    relationExerciseDone =  models.ManyToManyField('Exercise', through='ExerciseDone', symmetrical=False, related_name='related_to_exercisedone')


class Exercise(models.Model):
    name = models.CharField(max_length=50)
    objective = models.CharField(max_length=50)
    theme = models.CharField(max_length=50)
    branches = models.CharField(max_length=50)
    year = models.CharField(max_length=50)
    relationExerciseRequirement = models.ManyToManyField('self', through='ExerciseRequirement', symmetrical=False, related_name='related_to_exerciserequirement')
    relationExerciseDone =  models.ManyToManyField('Student', through='ExerciseDone', symmetrical=False, related_name='related_to_exercisedone')

class ExerciseRequirement(models.Model):
    idExercise = models.ForeignKey(Exercise, related_name='fromExercise', on_delete=models.CASCADE)
    idExerciseRequirement = models.ForeignKey(Exercise, related_name='toExercise', on_delete=models.CASCADE)

class ExerciseDone(models.Model):
    idStudent = models.ForeignKey(Student, on_delete=models.CASCADE)
    idExercise =  models.ForeignKey(Exercise,  on_delete=models.CASCADE)
    nbWrong = models.IntegerField()
    nbRight = models.IntegerField()
