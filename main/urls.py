#SA_BSP> main > urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main_index'),
    path('index', views.index, name='main_index'),
    path('classes', views.classes, name='main_classes'),
    path('contact', views.contact, name='main_contact'),
    path('shortcodes', views.shortcodes, name='main_shortcodes'),
    path('shows', views.shows, name='main_shows'),
    path('about', views.about, name='main_about'),
]
