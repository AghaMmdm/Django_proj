from django.shortcuts import render
from django.http import HttpResponse, Http404

# Create your views here.

userss = [
    {
        'username' : 'mmd90',
        'name' : 'mohammad',
        'lastname' : 'rahimi',
        'phone' : '09335336402',
        'city' : 'esf'
    },
    {
        'username' : 'ali90',
        'name' : 'ali',
        'lastname' : 'movahedi',
        'phone' : '09335336402',
        'city' : 'ysj'
    },
    {
        'username' : 'mahdi90',
        'name' : 'mahdi',
        'lastname' : 'torki',
        'phone' : '09335336402',
        'city' : 'teh'
    }
]

def users(request):
    return render(request, 'accounts_app/users.html', context = {'users_list' : userss})

def home(request):
    return HttpResponse('this is accounts page')


def profile(request, username):
    for tmp in userss:
        if username == tmp['username']:
            return render(request, 'accounts_app/profile.html', context= {'user' : tmp})
    raise Http404('Invalid username')