from django.shortcuts import render
from .models import course

# Create your views here.

def courses_list(request):
    courses = course.objects.all()
    return render(request, "courses_app/courses.html", context = {'courses_list' : courses})

def course_detail(request, id):
    tmp = course.objects.get(id = id)
    tmp.views += 1
    if tmp.status == False:
        tmp.status = True
    else :
        tmp.status = False
    tmp.save()
    return render(request, "courses_app/course_detail.html", context= { 'course' : tmp })