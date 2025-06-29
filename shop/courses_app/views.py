from django.shortcuts import render
from .models import course

# Create your views here.

def courses_list(request):
    courses = course.objects.all()
    return render(request, "courses_app/courses.html", context = {'courses_list' : courses})