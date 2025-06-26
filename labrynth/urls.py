from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('keep_walking/', views.keep_walking),
]