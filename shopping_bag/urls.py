from django.urls import path
from . import views

app_name = 'shopping_bag'

urlpatterns = [
    path('', views.view_shopping_bag, name='shopping_bag'),
]
