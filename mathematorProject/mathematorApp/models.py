'''
Mathemator
Roxane Carraux - Edwin Claude - Loïc Jurasz
Avril 2020
He-Arc
'''

#Importations
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import RegexValidator

'''
Student Table
'''
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    group = models.CharField(max_length=50)
    isTeacher = models.BooleanField(default=False)
    relationExerciseDone = models.ManyToManyField('Exercise', through='ExerciseDone', symmetrical=False, related_name='related_to_exercisedone')

'''
Methods for the relation between User and Student Table
'''
@receiver(post_save, sender=User)
def create_user_student(sender, instance, created, **kwargs):
    if created:
        Student.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_student(sender, instance, **kwargs):
    instance.student.save()

'''
Exercise Table
Generic table for all the type of exercises (ExerciseOperation and ExerciseFix)
'''
class Exercise(models.Model):
    name = models.CharField(max_length=50)
    objective = models.CharField(max_length=50)
    theme = models.CharField(max_length=50)
    branches = models.CharField(max_length=50)
    year = models.CharField(max_length=50)
    relationExerciseRequirement = models.ManyToManyField('self', through='ExerciseRequirement', symmetrical=False, related_name='related_to_exerciserequirement')
    relationExerciseDone =  models.ManyToManyField('Student', through='ExerciseDone', symmetrical=False, related_name='related_to_exercisedone')
    question = models.CharField(max_length=50, default ="")

'''
Exercise Requirement Table
Table for N-N relation between an exercise and it required exercises
'''
class ExerciseRequirement(models.Model):
    idExercise = models.ForeignKey(Exercise, related_name='fromExercise', on_delete=models.CASCADE)
    idExerciseRequirement = models.ForeignKey(Exercise, related_name='toExercise', on_delete=models.CASCADE)

'''
Exercise Done Table
Table for N-N relation between a student and an exercise
'''
class ExerciseDone(models.Model):
    idStudent = models.ForeignKey(Student, on_delete=models.CASCADE)
    idExercise =  models.ForeignKey(Exercise,  on_delete=models.CASCADE)
    nbWrong = models.IntegerField()
    nbRight = models.IntegerField()

'''
Exercise Operation Table
Specific table for exercise with operators and random numbers
'''
class ExerciseOperation(Exercise):
        rangeMin = models.DecimalField(max_digits=5, decimal_places=2)
        rangeMax = models.DecimalField(max_digits=5, decimal_places=2)
        rangeStep = models.DecimalField(max_digits=5, decimal_places=2)
        nbOperators = models.IntegerField()
        regexValidator = RegexValidator("^[\+\*\/\-]*$")
        operators = models.CharField(
            max_length = 10,
            default = '+',
            validators = [regexValidator]
        )

'''
Exercise Operation Table
Specific table for exercise with just one question and one answer
'''
class ExerciseFix(Exercise):
        result = models.FloatField()
