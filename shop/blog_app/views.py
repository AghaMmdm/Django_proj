from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, "blog_app/blog_app.html")

def contactus(request):
    return HttpResponse("this is contact us page :)")