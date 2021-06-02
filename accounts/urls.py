
from django.urls import path, include

from . import views

app_name='job'

urlpatterns = [
    path('siginup/', views.siginup, name='siginup'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit', views.profile_edit, name='profile_edit'),
]

