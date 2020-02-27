from django.contrib import admin

# Register your models here.
from .models import Student
from .models import Exercise
from .models import ExerciseRequirement
from .models import ExerciseDone

admin.site.register(Student)
admin.site.register(Exercise)
admin.site.register(ExerciseRequirement)
admin.site.register(ExerciseDone)
