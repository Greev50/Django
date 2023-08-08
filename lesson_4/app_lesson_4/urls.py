from django.urls import path
from .views import index, task

urlpatterns = [ 
    path('', index),
    path('lesson_4/', task)
]