from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

usernames = ["mahdi", "ali", "mohammad", "sadegh", "pooya"]

def home(request):
    return HttpResponse("this is accounts page")

def users(request):
    return HttpResponse("this is users page")

def profile(request, username):
    if username in usernames:
        return HttpResponse(f"<h1>This is {username} profile<h1/>")
    return HttpResponse("This username did't found :( ")