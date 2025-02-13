from django.contrib import admin
from django.urls import path,re_path
from FD import views


urlpatterns = [
    path("", views.index, name='home')
]
