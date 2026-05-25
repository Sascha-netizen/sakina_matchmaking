from django.urls import path
from . import views

app_name = 'matching'

urlpatterns = [
    path('matches/', views.matches, name='matches'),
]