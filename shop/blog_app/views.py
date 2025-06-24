from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("hi i'm mohammad")

def contactus(request):
    return HttpResponse("this is contact us page :)")