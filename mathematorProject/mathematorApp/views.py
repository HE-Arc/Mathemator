from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Exercise
from .models import ExerciseSimpleOperation
from .models import ExerciseFixDonneeResultat

import random


@login_required
def index(request):
    return render(request, "index.html", {})

def profile(request):
    return render(request, "profile.html", {})

def login(request):
    print("hello")
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


def exercise(request, exercise_id):
    exercise = get_object_or_404(Exercise, pk=exercise_id)
    return render(request,"exercises/exercise.html",{'exercise':exercise})

def exerciseSimpleOperation(request, exercise_id):
    exercise = get_object_or_404(ExerciseSimpleOperation, pk=exercise_id)
    listRandomOperator=[]
    for i in range(-1,exercise.nbOperation):
        if i >= 0:
            listRandomOperator.append(random.choice(exercise.operators))
        listRandomOperator.append(random.randint(exercise.rangeMin,exercise.rangeMax))
    return render(request,"exercises/exerciseSimpleOperation.html",{'exercise':exercise,'listRandomOperator':listRandomOperator})

def exerciseFixDonneeResultat(request, exercise_id):
    exercise = get_object_or_404(ExerciseFixDonneeResultat, pk=exercise_id)
    return render(request,"exercises/exerciseFixDonneeResultat.html",{'exercise':exercise})
