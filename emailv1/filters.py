import django_filters
from .models import Emailv1

class Emailv1Filter(django_filters.FilterSet):
    
    class Meta:
        model = Emailv1
        fields = [
            'email_address', 
            'domain', 
            'valid_syntax', 
            'created_at'
        ]