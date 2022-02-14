from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.all_products, name='all_products'),
    path('<item_id>', views.product_details, name='product_details'),
]
