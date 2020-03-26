from django.shortcuts import redirect,render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views import generic, View
from .models import Exercise
from .models import ExerciseOperation
from .models import ExerciseFix
from .models import Student
from .models import ExerciseRequirement

import random


@login_required
def index(request):
    exercisesOp = ExerciseOperation.objects.all()
    exercisesFix = ExerciseFix.objects.all()

    return render(request, "index.html", {'exercisesOp' : exercisesOp,
        'exercisesFix': exercisesFix})

@login_required
def profile(request):
    current_user = request.user
    student = get_object_or_404(Student, pk=current_user.id)

    exercises = Exercise.objects.all()
    exerciseDone= student.relationExerciseDone.all()
    exercisesOp = ExerciseOperation.objects.all()
    exerciseFix = ExerciseFix.objects.all()
    exDone = set()
    for exD in exerciseDone:
        exDone.add(exD.id)
    return render(request, "profile.html", 
        {'student':student, "exercises":exercises,
         "exerciseDone":exerciseDone, "exerciseOperation" : exercisesOp,
         "exerciseFix" : exerciseFix, "exDone":exDone})

def login(request):
    if request.user.is_authenticated:
        return render(request, "index.html", {})
    else:
        return login(request)

def login_view(request):
    if request.method == 'POST':
        print("error, no post")
    else:
        form = AuthentificationForm()
    return render(request,'mathemator/login.html',{'form':form})

def exerciseOperation(request, exercise_id):

    exercise = get_object_or_404(ExerciseOperation, pk=exercise_id)
    exercisesOp = ExerciseOperation.objects.all()
    exercisesFix = ExerciseFix.objects.all()

    exerciseRequirement = set(exercise.relationExerciseRequirement.all())

    current_user = request.user
    student = get_object_or_404(Student, pk=current_user.id)
    exerciseDone=set(student.relationExerciseDone.all())

    if exerciseDone.issuperset(exerciseRequirement):
        listRandom=[]
        for i in range(-1,exercise.nbOperators):
            if i >= 0:
                listRandom.append(random.choice(exercise.operators))
            listRandom.append(random.randint(exercise.rangeMin,exercise.rangeMax))

        return render(request, "exercises/exerciseOperations.html",
            {'exercise' : exercise, 'listRandom' : listRandom,
            "exerciseRequirement" : exerciseRequirement,
            "exerciseDone" : exerciseDone,'exercisesOp' : exercisesOp,
            'exercisesFix': exercisesFix})
    else:
        return render(request, "exercises/requirements.html",
            {'exercise' : exercise,
            "exerciseRequirement" : exerciseRequirement,
            'exercisesOp' : exercisesOp, 'exercisesFix': exercisesFix})

def exerciseFix(request, exercise_id):
    exercise = get_object_or_404(ExerciseFix, pk=exercise_id)
    exercisesOp = ExerciseOperation.objects.all()
    exercisesFix = ExerciseFix.objects.all()
    exerciseRequirement = set(exercise.relationExerciseRequirement.all())

    current_user = request.user
    student = get_object_or_404(Student, pk=current_user.id)
    exerciseDone = set(student.relationExerciseDone.all())

    if exerciseDone.issubset(exerciseRequirement):
        return render(request, "exercises/exerciseFix.html",
        {'exercise' : exercise, 'exercisesOp' : exercisesOp,
        'exercisesFix': exercisesFix})
    else:
        return render(request, "exercises/requirements.html",
            {'exercise' : exercise,
            "exerciseRequirement" : exerciseRequirement,
            'exercisesOp' : exercisesOp, 'exercisesFix': exercisesFix})
