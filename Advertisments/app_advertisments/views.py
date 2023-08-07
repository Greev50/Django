from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Успешный успех")

def test33(request):
    return HttpResponse("Тест 33")