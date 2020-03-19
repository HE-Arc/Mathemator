from django.urls import path
from django.conf.urls import include

from . import views
urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.index, name='index'),
    path('profile', views.profile, name='profile'),
    path('operation/<int:exercise_id>/',views.exerciseOperations,name='operations'),
    path('fix/<int:exercise_id>/',views.exerciseFix,name='fix'),
]
