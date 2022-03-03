from django.urls import path
from . import views

app_name = 'interview'

urlpatterns = [
    path('interview-success', views.success_interview, name='interview_success'),
    path('hr-interview', views.hr_interview, name='hr_interview'),
    path('coding-interview', views.coding_interview, name='coding_interview'),
    path('difficult-coding-interview', views.coding_difficult_interview, name='coding_difficult_interview')
]
