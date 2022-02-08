from django.contrib import admin
from django.urls import path
from . import views

app_name = 'interview'

urlpatterns = [
    path('', views.interview, name='interview'),
]