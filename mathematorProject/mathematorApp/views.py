from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Exercise
from .models import ExerciseSimpleOperation
from .models import ExerciseFixDonneeResultat
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

def exerciseSimpleOperation(request, exercise_id):
    exercise = get_object_or_404(ExerciseSimpleOperation, pk=exercise_id)
    exerciseRequirement = exercise.relationExerciseRequirement.all()

    # TODO: changer !!!!!!!
    idStudent=1
    student = get_object_or_404(Student, pk=idStudent)
    exerciseDone=student.relationExerciseDone.all()


    listRandomOperator=[]
    for i in range(-1,exercise.nbOperation):
        if i >= 0:
            listRandomOperator.append(random.choice(exercise.operators))
        listRandomOperator.append(random.randint(exercise.rangeMin,exercise.rangeMax))
    return render(request,"exercises/exerciseSimpleOperation.html",{'exercise':exercise,'listRandomOperator':listRandomOperator,"exerciseRequirement":exerciseRequirement,"exerciseDone":exerciseDone})

def exerciseFixDonneeResultat(request, exercise_id):
    exercise = get_object_or_404(ExerciseFixDonneeResultat, pk=exercise_id)
    return render(request,"exercises/exerciseFixDonneeResultat.html",{'exercise':exercise})
