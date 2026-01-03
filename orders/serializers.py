# orders/serializers.py
from rest_framework import serializers
from .models import Order, Review

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

class ReviewSerializer(serializers.ModelSerializer):
    reviewer = serializers.CharField(source='order.buyer.username', read_only=True)

    class Meta:
        model = Review
        fields = ['id', 'order', 'rating', 'comment', 'reviewer', 'created_at']

    def validate_order(self, value):
        # Ensure the person reviewing is the actual buyer
        user = self.context['request'].user
        if value.buyer != user:
            raise serializers.ValidationError("Only the buyer can review this order.")
        return value