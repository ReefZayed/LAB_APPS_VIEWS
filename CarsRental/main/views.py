from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.

def index_views(request:HttpRequest):
    return render(request,'main/home.html')

def next_views(request:HttpRequest):
    return render(request,'main/prodect.html')
