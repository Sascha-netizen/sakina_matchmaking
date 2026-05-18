from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_profile, name='profile_create'),
    path('', views.profile_detail, name='profile_detail'),
    path('edit/', views.profile_edit, name='profile_edit'),
    path('delete/', views.delete_account, name='delete_account'),
]