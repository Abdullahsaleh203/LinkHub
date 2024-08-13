#!/usr/bin/python3
"""to get the urls """


from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index')
]