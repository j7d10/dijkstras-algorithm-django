from django.urls import path
from .views import index, calculate

app_name = 'dijkstra_app'

urlpatterns = [
    path('', index, name='index'),
    path('calculate/', calculate, name='calculate'),
]