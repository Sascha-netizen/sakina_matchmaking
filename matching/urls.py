from django.urls import path
from . import views

app_name = 'matching'

urlpatterns = [
    path('matches/', views.matches, name='matches'),
    path('profile/<int:profile_id>/', views.profile_view, name='profile_view'),
    path('inbox/', views.inbox, name='inbox'),
    path('conversation/<int:user_id>/', views.conversation, name='conversation'),
]