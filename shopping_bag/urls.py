from django.urls import path
from . import views

app_name = 'shopping_bag'

urlpatterns = [
    path('', views.view_shopping_bag, name='shopping_bag'),
    path('add/<item_id>/', views.add_to_bag, name='add_to_bag'),
    path('adjust/<item_id>/', views.adjust_bag, name='adjust_bag'),
    path('remove/<item_id>/', views.remove_from_bag, name='remove_from_bag'),
]
