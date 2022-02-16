from django.urls import path
from . import views

app_name = 'premium'

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('premium/', views.premium, name='premium'),
]
