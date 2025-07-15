from django.shortcuts import render
from projects_app.models import project
from contactUs_app.models import footer, message

def home(request):
    projects = project.objects.all()
    Footer = footer.objects.all().last()

    if request.method == "POST":
        fname = request.POST.get('fname')
        email = request.POST.get('email')
        sub = request.POST.get('sub')
        bdy = request.POST.get('body')
        message.objects.create(fname=fname, email=email, sub=sub, bdy=bdy)

    return render(request, 'index.html', context={'projects':projects, "Footer":Footer})