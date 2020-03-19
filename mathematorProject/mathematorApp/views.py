from django.shortcuts import redirect,render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Exercise
from .models import ExerciseOperation
from .models import ExerciseFix
from .models import Student

import random

from django.views.generic import TemplateView

@login_required
def index(request):
    return render(request, "index.html", {})

@login_required
def profile(request):
    current_user = request.user
    student = get_object_or_404(Student, pk=current_user.id)

    #exerciseDone=student.relationExerciseDone.all()
    return render(request, "profile.html", {'student':student})

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
    exerciseRequirement = set(exercise.relationExerciseRequirement.all())

    current_user = request.user
    student = get_object_or_404(Student, pk=current_user.id)
    exerciseDone=set(student.relationExerciseDone.all())

    if exerciseDone.issubset(exerciseRequirement):
        listRandom=[]
        for i in range(-1,exercise.nbOperators):
            if i >= 0:
                listRandom.append(random.choice(exercise.operators))
            listRandom.append(random.randint(exercise.rangeMin,exercise.rangeMax))

        return render(request, "exercises/exerciseOperations.html", {'exercise' : exercise, 'listRandom' : listRandom, "exerciseRequirement" : exerciseRequirement, "exerciseDone" : exerciseDone})
    else:
        # TODO : message pour information que l'on n'a pas acces à l'exercice
        return redirect('/')

def exerciseFix(request, exercise_id):
    exercise = get_object_or_404(ExerciseFix, pk=exercise_id)
    exerciseRequirement = set(exercise.relationExerciseRequirement.all())

    current_user = request.user
    student = get_object_or_404(Student, pk=current_user.id)
    exerciseDone = set(student.relationExerciseDone.all())

    if exerciseDone.issubset(exerciseRequirement):
        return render(request, "exercises/exerciseFix.html", {'exercise' : exercise})
    else:
        # TODO : message pour information que l'on n'a pas acces à l'exercice
        return redirect('/')
