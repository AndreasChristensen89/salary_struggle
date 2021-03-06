from django.urls import path
from . import views

app_name = 'interview'

urlpatterns = [
    path('interview-success/', views.SuccessInterview.as_view(), name='interview_success'),
    path('hr-interview/', views.hr_interview, name='hr_interview'),
    path('coding-interview/', views.coding_interview, name='coding_interview'),
    path('difficult-coding-interview/', views.coding_difficult_interview, name='coding_difficult_interview'),
    path('final-interview/', views.final_interview, name='final_interview'),
    path('reset-energy/', views.ResetEnergy.as_view(), name='reset_energy'),
]
