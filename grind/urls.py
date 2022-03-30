from django.urls import path
from . import views

app_name = 'grind'

urlpatterns = [
    path('intro/', views.intro, name='intro'),
    path('enter/', views.enter_game, name='enter'),
    path('city/', views.city, name='city'),
    path('bar/', views.bar_page, name='bar'),
    path('cafe/', views.cafe_page, name='cafe'),
    path('downtown/', views.downtown_page, name='downtown'),
    path('house/', views.house_page, name='house'),
    path('agency/', views.agency_page, name='agency'),
    path('store/', views.store_page, name='store'),
    path('call-center/', views.call_center_page, name='call-center'),
    path('back-alley/', views.back_alley_page, name='back-alley'),
    path('charm-home/', views.UpdateCharmHome.as_view(), name='charm_home'),
    path('sleep/', views.Sleep.as_view(), name='sleep'),
    path('study-home/', views.StudyHome.as_view(), name='study-home'),
    path('bar-converse/', views.BarConverse.as_view(), name='bar-converse'),
    path('bar-drink/', views.BarDrink.as_view(), name='bar-drink'),
    path('cafe-study/', views.CafeStudy.as_view(), name='cafe-study'),
    path('agency-skill/', views.AgencySkill.as_view(), name='agency-skill'),
    path('agency-combine/', views.AgencyCombine.as_view(),
         name='agency-combine'),
    path('add-item/', views.AddItem.as_view(), name='add-item'),
    path('apply-job/', views.ApplyJob.as_view(), name='apply-job'),
    path('work/', views.Work.as_view(), name='work'),
    path('fight/', views.Fight.as_view(), name='fight'),
    path('gamble/', views.Gamble.as_view(), name='gamble'),
]
