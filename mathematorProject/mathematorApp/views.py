from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required

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
