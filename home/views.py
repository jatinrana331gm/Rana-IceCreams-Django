from django.shortcuts import render, HttpResponse
from django.contrib import messages
from .models import Contact

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact_view(request):
    if request.method == "POST":
        # process form
        pass
    return render(request, 'contact.html')
