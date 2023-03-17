# SA_BSP > main > urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls'), name='main'),
    path('calculate/', include('calculate.urls')),
    path('upload/', include('upload.urls')),
    path('result/', include('result.urls')),
]
