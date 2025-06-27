from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('keep_walking/', views.keep_walking),
    path('asleep1/', views.asleep1),
    path('labyrinth_hole/', views.labyrinth_hole),
    path('brace_for_landing/', views.brace_for_landing),
    path('dont_brace_for_landing/', views.dont_brace_for_landing),
    path('follow_parrot/', views.follow_parrot),
    path('sketchy_parrot/', views.sketchy_parrot),
    path('say_nothing/', views.say_nothing),
    path('say_diseased/', views.say_diseased),
    path('befriend/', views.befriend),
]