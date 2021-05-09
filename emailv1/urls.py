from django.urls import path
from . import views

urlpatterns = [
    path('mail/validation/v1', views.validation_v1, name='validation_v1')
]