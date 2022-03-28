from django.contrib import admin
from django.urls import path
from . import views

app_name = 'leaderboard'

urlpatterns = [
    path('', views.leaderboard, name='leaderboard'),
    path('winning-page/', views.winning_page, name='winning_page'),
    path('gameover-page/', views.gameover_page, name='gameover_page'),
    path('calculate-leaderboard-spot/', views.calculate_leaderboard_spot, name='calculate_spot'),
]
