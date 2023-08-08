from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Послушай трек Josodo - Весы и Shimoro - Луна")

def task(request):
        return HttpResponse("Домашка по 4 занятию")