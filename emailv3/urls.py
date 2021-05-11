from django.urls import path
from . import views

urlpatterns = [
    path('mail/validation/v3', views.validation_v3, name='validation_v3')
]