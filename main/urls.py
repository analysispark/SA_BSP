#SA_BSP> main > urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main_index'),
]
