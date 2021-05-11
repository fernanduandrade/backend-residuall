import django_filters
from .models import Emailv3

class Emailv3Filter(django_filters.FilterSet):
    
    class Meta:
        model = Emailv3
        fields = [
            'email_address', 
            'domain', 
            'valid_syntax', 
            'disposable',
            'webmail',
            'deliverable',
            'catch_all',
            'gibberish',
            'created_at'
        ]