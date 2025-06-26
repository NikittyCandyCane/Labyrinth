from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('keep_walking/', views.keep_walking),
    path('asleep1/', views.asleep1),
    path('labrynth_hole/', views.labrynth_hole)
]