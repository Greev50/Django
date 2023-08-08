from django.urls import path
from .views import index, top, place, reg, log, profile

urlpatterns = [ 
    path('', index,name='index'),
    path('top-sell/',top,name='top'),
    path('place/',place,name='place'),
    path('reg/',reg,name='reg'),
    path('log/',log,name='log'),
    path('profile/',profile,name='profile')
]
#когда путь будет пустой, выполнится индекс