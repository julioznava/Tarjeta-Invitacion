from django.urls import path
from .views import *

urlpatterns = [
    path('', ingresonombre, name='ingresonombre'),
    path('index/', index, name='index'),
    path('eliminardatos/<id>/', eliminardatos, name='eliminardatos'),
    path('confirmacion/', confirmacion, name='confirmacion'),
]