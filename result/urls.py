#SA_BSP> result > urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.SearchFormView.as_view(), name='searchform')
      
]