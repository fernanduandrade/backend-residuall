from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('index.urls')),
    path('', include('emailv1.urls')),
    path('admin/', admin.site.urls),
]
