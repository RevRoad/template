from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='<app_name>_home'),
]