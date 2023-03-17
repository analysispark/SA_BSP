#SA_BSP> main > urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main_index'),
    path('index', views.index, name='main_index'),
    path('about', views.about, name='main_about'),
    path('calculate', views.calculate, name='main_view'),
    path('result', views.result, name='main_result'),
    
]
