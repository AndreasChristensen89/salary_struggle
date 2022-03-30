from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('contact-user/', views.contact_logged_in, name='contact_login'),
    path('newsletter/', views.news_letter, name='newsletter'),
]
