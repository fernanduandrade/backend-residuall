from rest_framework import serializers
from .models import Emailv3

class Emailv3Serializer(serializers.ModelSerializer):
    class Meta:
        model = Emailv3
        fields = '__all__'