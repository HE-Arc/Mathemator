from django.urls import path
from django.conf.urls import include

from . import views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.index, name='index'),
    path('profile', views.profile, name='profile'),
    path('exercise/<int:exercise_id>/', views.exercise, name='exercise'),
]
