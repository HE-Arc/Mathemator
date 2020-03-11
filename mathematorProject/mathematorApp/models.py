from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    group = models.CharField(max_length=50)
    isTeacher = models.BooleanField()
    relationExerciseDone = models.ManyToManyField('Exercise', through='ExerciseDone', symmetrical=False, related_name='related_to_exercisedone')

@receiver(post_save, sender=User)
def create_user_student(sender, instance, created, **kwargs):
    if created:
        Student.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_student(sender, instance, **kwargs):
    instance.student.save()

class Exercise(models.Model):
    name = models.CharField(max_length=50)
    objective = models.CharField(max_length=50)
    theme = models.CharField(max_length=50)
    branches = models.CharField(max_length=50)
    year = models.CharField(max_length=50)
    relationExerciseRequirement = models.ManyToManyField('self', through='ExerciseRequirement', symmetrical=False, related_name='related_to_exerciserequirement')
    relationExerciseDone =  models.ManyToManyField('Student', through='ExerciseDone', symmetrical=False, related_name='related_to_exercisedone')
    donnee = models.CharField(max_length=50,default ="")

class ExerciseSimpleOperation(Exercise):
    rangeMin = models.DecimalField(max_digits=5, decimal_places=2)
    rangeMax = models.DecimalField(max_digits=5, decimal_places=2)
    rangeStep = models.DecimalField(max_digits=5, decimal_places=2)
    nbOperation = models.IntegerField()
    ADDITION='+'
    SOUSTRACTION='-'
    DIVISION='/'
    MULTIPLICATION='*'
    OPERATORS_CHOICES = [
        (ADDITION, 'addition'),
        (SOUSTRACTION, 'soustraction'),
        (DIVISION, 'division'),
        (MULTIPLICATION, 'multiplication'),
    ]
    operators = models.CharField(
        max_length=1,
        choices=OPERATORS_CHOICES,
        default=ADDITION,
    )

class ExerciseRequirement(models.Model):
    idExercise = models.ForeignKey(Exercise, related_name='fromExercise', on_delete=models.CASCADE)
    idExerciseRequirement = models.ForeignKey(Exercise, related_name='toExercise', on_delete=models.CASCADE)

class ExerciseDone(models.Model):
    idStudent = models.ForeignKey(Student, on_delete=models.CASCADE)
    idExercise =  models.ForeignKey(Exercise,  on_delete=models.CASCADE)
    nbWrong = models.IntegerField()
    nbRight = models.IntegerField()
