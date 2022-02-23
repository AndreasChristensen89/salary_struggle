from django.urls import path
from . import views

app_name = 'grind'

urlpatterns = [
    path('enter/', views.enter_game, name='enter'),
    path('city/', views.city, name='city'),
    path('bar/', views.bar_page, name='bar'),
    path('library/', views.library_page, name='library'),
    path('downtown/', views.downtown_page, name='downtown'),
    path('house/', views.house_page, name='house'),
    path('agency/', views.agency_page, name='agency'),
    path('store/', views.store_page, name='store'),
    path('call-center/', views.call_center_page, name='call-center'),
    path('back-alley/', views.back_alley_page, name='back-alley'),
]
