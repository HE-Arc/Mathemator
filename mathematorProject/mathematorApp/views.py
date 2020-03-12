from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Exercise


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
    #exercises= Exercise.objects

    return render(request,"exercise.html",{'exercise':exercise})
