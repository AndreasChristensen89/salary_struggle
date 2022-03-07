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
    path('charm-home/', views.UpdateCharmHome.as_view(), name='charm_home'),  # Done
    path('sleep/', views.Sleep.as_view(), name='sleep'),  # Done
    path('study-home/', views.StudyHome.as_view(), name='study-home'),   # Done
    path('bar-converse/', views.BarConverse.as_view(), name='bar-converse'), # Done
    path('bar-drink/', views.BarDrink.as_view(), name='bar-drink'),    # Done
    path('library-study/', views.LibraryStudy.as_view(), name='library-study'),  # Done
    path('agency-skill/', views.AgencySkill.as_view(), name='agency-skill'),     # Done
    path('agency-combine/', views.AgencyCombine.as_view(), name='agency-combine'), # Done
    path('add-item/', views.AddItem.as_view(), name='add-item'),   # Done
    path('apply-job/', views.ApplyJob.as_view(), name='apply-job'), # Done
    path('work/', views.Work.as_view(), name='work'),   # Work
    path('fight/', views.fight, name='fight'),
    path('gamble/', views.gamble, name='gamble'),
]
