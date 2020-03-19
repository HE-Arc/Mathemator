from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views import generic, View

from .models import Exercise, Student

@login_required
def index(request):
    return render(request, "index.html", {})


class ExerciseView(generic.TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['exercises'] = Exercise.objects.all()
        return context

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
