#SA_BSP> result > urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.SearchFormView.as_view(), name='searchform'),
    #path('download_pdf/', views.SearchFormView.download_pdf, name='download_pdf'), 
]


