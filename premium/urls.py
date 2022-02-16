from django.urls import path
from . import views
from .webhooks import webhook

app_name = 'premium'

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('checkout_success/<order_number>', views.checkout_success, name='checkout_success'),
    path('webhook/', webhook, name='webhook'),
    path('premium/', views.premium, name='premium'),
]
