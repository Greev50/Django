from django.urls import path
from .views import index, test33

urlpatterns = [ 
    path('', index),
    path('test33/', test33)
]
#когда путь будет пустой, выполнится индекс