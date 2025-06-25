from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

usernames = ["mahdi", "ali", "mohammad", "sadegh", "pooya"]

def home(request):
    return HttpResponse("this is accounts page")

def users(request):
    return HttpResponse("this is users page")

def profile(request, username):
    return render(request, "accounts_app/profile.html", context= {"name" : username})