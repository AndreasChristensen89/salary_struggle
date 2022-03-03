from django.urls import path
from . import views

app_name = 'interview'

urlpatterns = [
    path('hr-interview', views.hr_interview, name='hr_interview'),
    path('hr-success', views.succeed_hr_interview, name='hr_success'),
    path('coding-interview', views.coding_interview, name='coding_interview'),
    path('coding-success', views.succeed_coding_interview, name='coding_success'),
]
