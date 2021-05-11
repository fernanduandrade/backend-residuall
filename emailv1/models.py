from django.db import models


class Emailv1(models.Model):
    email_address = models.CharField(max_length=100)
    domain = models.CharField(max_length=20)
    valid_syntax = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)