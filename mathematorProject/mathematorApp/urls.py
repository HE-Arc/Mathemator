from django.urls import path
from django.conf.urls import include
from . import views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('profile', views.profile, name='profile'),
    path('', views.index, name='index'),
    path('operation/<int:exercise_id>/', views.exerciseOperation, name='operation'),
    path('fix/<int:exercise_id>/', views.exerciseFix, name='fix'),
    path('checkResult/', views.checkResult, name='checkResult'),
]
