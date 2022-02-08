from django.contrib import admin
from django.urls import path
from . import views

app_name = 'premium'

urlpatterns = [
    path('', views.premium, name='premium'),
]
