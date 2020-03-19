from django.urls import path
from django.conf.urls import include

from . import views
urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('profile', views.profile, name='profile'),
    path('', views.ExerciseView.as_view(), name='index'),
]
