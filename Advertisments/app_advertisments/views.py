from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')

def top(request):
    return render(request, 'top-sellers.html')

def place(request):
    return render(request, 'Advertisement-post.html')

def reg(request):
    return render(request, 'register.html')

def log(request):
    return render(request, 'login.html')

def profile(request):
    return render(request,'profile.html')