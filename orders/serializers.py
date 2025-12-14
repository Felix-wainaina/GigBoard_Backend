# orders/serializers.py
from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    buyer = serializers.StringRelatedField(read_only=True)
    service_title = serializers.CharField(source='service.title', read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'service', 'service_title', 'buyer', 'status', 'created_at']
        read_only_fields = ['status', 'buyer'] # Only Seller changes status

    def validate_service(self, value):
        request = self.context.get('request')
        if value.seller == request.user:
            raise serializers.ValidationError("You cannot purchase your own service!")
        return value