from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "index.html", {})

def profile(request):
    return render(request, "profile.html", {})

def logout(request):
    return HttpResponse("Logout");
