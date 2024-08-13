from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse('<h1>Welcome To Your LinkHub Platform</h1>')