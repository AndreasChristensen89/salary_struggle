from django.urls import path
from . import views

app_name = 'profiles'

urlpatterns = [
    path('', views.profile, name='profile'),
    path('update/', views.UpdateProfile.as_view(), name="update_profile"),
    path('password/', views.PasswordChangeView.as_view(), name='password'),
    path('order_history/<order_number>/', views.order_history, name='order_history'),
    path('confirm_new_character/', views.confirm_new_char, name='confirm_new_char'),
    path('new_character/', views.create_new_character, name='new_character'),
]
