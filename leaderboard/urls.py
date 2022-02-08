from django.contrib import admin
from django.urls import path
from . import views

app_name = 'leaderboard'

urlpatterns = [
    path('', views.leaderboard, name='leaderboard'),
]
