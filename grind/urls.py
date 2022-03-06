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
    path('charm-home/', views.update_charm_home.as_view(), name='charm_home'),  # Done
    path('sleep/', views.sleep.as_view(), name='sleep'),  # Done
    path('study-home/', views.study_home.as_view(), name='study-home'),   # Done
    path('bar-converse/', views.bar_converse.as_view(), name='bar-converse'), # Done
    path('bar-drink/', views.bar_drink.as_view(), name='bar-drink'),    # Done
    path('library-study/', views.library_study.as_view(), name='library-study'),  # Done
    path('agency-skill/', views.agency_skill.as_view(), name='agency-skill'),     # Done
    path('agency-combine/', views.agency_combine.as_view(), name='agency-combine'), # Done
    path('add-item/<int:item_id>/', views.add_item, name='add-item'),
    path('apply-job/', views.apply_job, name='apply-job'),
    path('work/', views.work, name='work'),
    path('fight/', views.fight, name='fight'),
    path('gamble/', views.gamble, name='gamble'),
]
