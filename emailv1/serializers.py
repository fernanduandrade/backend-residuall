from rest_framework import serializers
from .models import Emailv1

class Emailv1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Emailv1
        fields = '__all__'