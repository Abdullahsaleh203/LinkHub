from django.urls import path    
from . import api

urlpatterns = [
    path('search/', api.search,name='search'),
]

