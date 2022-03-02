from django.urls import path
from . import views

app_name = 'interview'

urlpatterns = [
    path('hr-interview', views.hr_interview, name='hr_interview'),
    path('hr-success', views.succeed_hr_interview, name='hr_success'),
]
