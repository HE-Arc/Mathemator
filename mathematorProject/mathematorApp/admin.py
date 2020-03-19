from django.contrib import admin

# Register your models here.
from .models import Student
from .models import Exercise
from .models import ExerciseRequirement
from .models import ExerciseDone
from .models import ExerciseOperation
from .models import ExerciseFix

admin.site.register(Student)
admin.site.register(Exercise)
admin.site.register(ExerciseRequirement)
admin.site.register(ExerciseDone)
admin.site.register(ExerciseOperation)
admin.site.register(ExerciseFix)
