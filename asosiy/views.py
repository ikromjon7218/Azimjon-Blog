# from .forms import *
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
def home(request):
    # data = {}
    return render(request, "home.html")

def about(request):
    # data = {}
    return render(request, "about.html")

def blog(request):
    data = {'maqolalar': Maqola.objects.all()}
    return render(request, "blog.html", data)

def bitta_maqola(request, son):
    data = {'bitta_maqola': Maqola.objects.get(id=son)}
    return render(request, "bitta_maqola.html", data)