'''
Mathemator
Roxane Carraux - Edwin Claude - Loïc Jurasz
Avril 2020
He-Arc
'''

from django.urls import path
from django.conf.urls import include
from . import views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('profile', views.profile, name='profile'),
    path('', views.index, name='index'),
    path('operation/<int:exercise_id>/', views.exerciseOperation, name='operations'),
    path('fix/<int:exercise_id>/', views.exerciseFix, name='fix'),
    path('checkResult/', views.checkResult, name='checkResult'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
