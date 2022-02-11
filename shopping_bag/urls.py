from django.urls import path
from . import views

app_name = 'shopping_bag'

urlpatterns = [
    path('', views.view_shopping_bag, name='shopping_bag'),
    path('add/<product_id>', views.add_to_bag, name='add_to_bag'),
]
