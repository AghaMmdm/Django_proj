from django.shortcuts import render, redirect
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


def add_course(request):
    title = request.GET.get('title')
    desc = request.GET.get('description')
    if title and desc:
        course.objects.create(title= title, description = desc)
        return redirect("/course/list")
    return render(request, "courses_app/add_course.html")