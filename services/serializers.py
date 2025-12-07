from rest_framework import serializers
from .models import Service

class ServiceSerializer(serializers.ModelSerializer):
    seller = serializers.StringRelatedField(read_only=True) # Show username, not ID

    class Meta:
        model = Service
        fields = '__all__'