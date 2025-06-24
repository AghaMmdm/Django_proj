from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.



def home(request):
    return HttpResponse("this is accounts page")

def users(request):
    return HttpResponse("this is users page")