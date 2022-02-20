from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.all_products, name='all_products'),
    path('int:<item_id>/', views.product_details, name='product_details'),   # Django doesn't know the difference between int and strings, so it will think that the product number is a string if no int
    path('add/', views.add_product, name='add_product'),
]
