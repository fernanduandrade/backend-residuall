from django.db import models

class Emailv3(models.Model):
    email_address = models.CharField(max_length=100)
    domain = models.CharField(max_length=20)
    valid_syntax = models.BooleanField(default=False)
    disposable = models.BooleanField(default=False)
    webmail = models.BooleanField(default=False)
    deliverable = models.BooleanField(default=False)
    catch_all = models.BooleanField(default=False)
    gibberish = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)