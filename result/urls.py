#SA_BSP> result > urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.SearchFormView.as_view(), name='searchform'),
    path('/<int:id>/', views.certi_print, name='certi_print'), 
]


## result url, views, html ; certi_print 문제