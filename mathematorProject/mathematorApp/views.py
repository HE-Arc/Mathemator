'''
Mathemator
Roxane Carraux - Edwin Claude - Loïc Jurasz
Avril 2020
He-Arc
'''

#Importations
from django.shortcuts import redirect,render, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views import generic, View
from django.contrib import messages
from .models import Exercise
from .models import ExerciseOperation
from .models import ExerciseFix
from .models import Student
from .models import ExerciseRequirement
from .models import ExerciseDone
import random

'''
Index Page
'''
@login_required
def index(request):
    exercisesOp = ExerciseOperation.objects.all()
    exercisesFix = ExerciseFix.objects.all()
    return render(request, "index.html", {'exercisesOp' : exercisesOp,
        'exercisesFix': exercisesFix})

'''
Profile Page
'''
@login_required
def profile(request):
    current_user = request.user
    student = get_object_or_404(Student, pk=current_user.id)
    exercises = Exercise.objects.all()
    exerciseDone= ExerciseDone.objects.filter(idStudent=current_user.id)
    exercisesOp = ExerciseOperation.objects.all()
    exerciseFix = ExerciseFix.objects.all()
    exDone = set()
    for exD in exerciseDone:
        if exD.nbRight > 0:
            exDone.add(exD.idExercise.id)

    return render(request, "profile.html",
        {'student':student, "exercises":exercises,
         "exerciseDone":exerciseDone, "exerciseOperation" : exercisesOp,
         "exerciseFix" : exerciseFix, "exDone":exDone})

'''
Login Page
'''
def login(request):
    if request.user.is_authenticated:
        return render(request, "index.html", {})
    else:
        return login(request)

'''
Login Request
'''
def login_view(request):
    if request.method == 'POST':
        print("error, no post")
    else:
        form = AuthentificationForm()
    return render(request,'mathemator/login.html',{'form':form})

'''
ExerciseOperation view
- Verify requirements
- Generate operator and random numbers for operations
- Generate result
'''
def exerciseOperation(request, exercise_id):
    exercise = get_object_or_404(ExerciseOperation, pk=exercise_id)
    exercisesOp = ExerciseOperation.objects.all()
    exercisesFix = ExerciseFix.objects.all()

    exerciseRequirement = set(exercise.relationExerciseRequirement.all())

    current_user = request.user
    exerciseDone=ExerciseDone.objects.filter(idStudent=current_user.id)
    exercisesRight=set()
    for exD in exerciseDone:
        if exD.nbRight > 0:
            exercisesRight.add(exD.idExercise)

    if len(exerciseRequirement) == 0 or exercisesRight.issuperset(exerciseRequirement):
        listRandom=[]
        for i in range(-1,exercise.nbOperators):
            if i >= 0:
                listRandom.append(random.choice(exercise.operators))
            listRandom.append(random.randrange(exercise.rangeMin, exercise.rangeMax,exercise.rangeStep))

        try:
            result = eval("".join([str(element) for element in listRandom]))
        except ZeroDivisionError:
            return exerciseOperation(request, exercise_id)

        return render(request, "exercises/exerciseOperations.html",
            {'exercise' : exercise, 'listRandom' : listRandom,
            "exerciseRequirement" : exerciseRequirement,
            "exerciseDone" : exerciseDone,'exercisesOp' : exercisesOp,
            'exercisesFix': exercisesFix, 'result' : result })
    else:
        return render(request, "exercises/requirements.html",
            {'exercise' : exercise,
            "exerciseRequirement" : exerciseRequirement,
            'exercisesOp' : exercisesOp, 'exercisesFix': exercisesFix})

'''
Exercise Fix view
- Verify requirements
'''
def exerciseFix(request, exercise_id):
    exercise = get_object_or_404(ExerciseFix, pk=exercise_id)
    exercisesOp = ExerciseOperation.objects.all()
    exercisesFix = ExerciseFix.objects.all()
    exerciseRequirement = set(exercise.relationExerciseRequirement.all())

    current_user = request.user
    exerciseDone=ExerciseDone.objects.filter(idStudent=current_user.id)
    exercisesRight=set()
    for exD in exerciseDone:
        if exD.nbRight > 0:
            exercisesRight.add(exD.idExercise)

    if len(exerciseRequirement) == 0 or exercisesRight.issuperset(exerciseRequirement):
        return render(request, "exercises/exerciseFix.html",
        {'exercise' : exercise, 'exercisesOp' : exercisesOp,
        'exercisesFix': exercisesFix, 'result' : exercise.result})
    else:
        return render(request, "exercises/requirements.html",
            {'exercise' : exercise,
            "exerciseRequirement" : exerciseRequirement,
            'exercisesOp' : exercisesOp, 'exercisesFix': exercisesFix})

'''
Method to check if the answer of the user is right
Update the table exerciseDone
'''
def checkResult(request):
    try:
        if float(request.POST.get('resultInput')) == float(request.POST.get('result')):
            isRight = True
            messages.add_message(request, messages.INFO, 'Bravo ta réponse est juste !')
        else:
            isRight = False
            messages.add_message(request, messages.INFO, 'Ta réponse est fausse !')
    except ValueError:
        isRight = False
        messages.add_message(request, messages.INFO, 'Ta réponse est fausse ! Fais attention, ta réponse doit être un nombre.')

    try:
        exDone = ExerciseDone.objects.get(idStudent=request.user.id, idExercise=request.POST.get('exercise_id'))
        if isRight:
            exDone.nbRight=exDone.nbRight + 1
        else:
            exDone.nbWrong=exDone.nbWrong + 1
        exDone.save()
    except ExerciseDone.DoesNotExist:
        exercise = get_object_or_404(Exercise, pk=request.POST.get('exercise_id'))
        current_user = request.user
        student = get_object_or_404(Student, pk=current_user.id)
        if isRight:
            ExerciseDone.objects.create(idStudent=student, idExercise=exercise, nbRight=1, nbWrong=0)
        else:
            ExerciseDone.objects.create(idStudent=student, idExercise=exercise, nbRight=0, nbWrong=1)

    next = request.POST.get('next', '/')
    return HttpResponseRedirect(next)
