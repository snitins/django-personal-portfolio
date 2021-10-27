from django.shortcuts import render
from django.http import HttpResponse
from .models import Project


# Create your views here.
def about(request):
    return render(request,'personal_portfolio/about.html')

def home(request):
    projects = Project.objects.all()
    return render(request,'portfolio/home.html',{'projects':projects})
