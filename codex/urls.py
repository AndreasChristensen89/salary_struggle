from django.urls import path
from . import views

app_name = 'codex'

urlpatterns = [
    path('items/', views.items_index, name='items'),
    path('items/<item_id>', views.item_details, name='item_details'),
    path('interviewers/', views.character_index, name='interviewers'),
    path('interviewers/<interviewer_id>', views.interviewer_details, name='interviewer_details'),
]
