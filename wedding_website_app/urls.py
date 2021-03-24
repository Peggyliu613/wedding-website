from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add_guest', views.add_guest),
    path('submited', views.submited)
]