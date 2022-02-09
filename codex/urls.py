from django.urls import path
from . import views

app_name = 'codex'

urlpatterns = [
    path('', views.full_codex, name='full_codex'),
]
