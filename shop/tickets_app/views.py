from django.shortcuts import render, redirect
from .models import Ticket

# Create your views here.


def home(request):
    
    return render(request, "tickets_app/tickets.html")

def add_ticket(request):
    title = request.GET.get("title")
    bdy = request.GET.get("body")
    
    if title and bdy:
        Ticket.objects.create(title = title, body = bdy)
        print("ticket added successfully :)")
        
    return render(request, "tickets_app/add_ticket.html")