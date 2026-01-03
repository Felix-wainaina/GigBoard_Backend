# orders/views.py
from rest_framework import viewsets, permissions
from .models import Order, Review
from .serializers import OrderSerializer, ReviewSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Users should only see orders relevant to them (Buying or Selling)
        user = self.request.user
        return Order.objects.filter(buyer=user) | Order.objects.filter(service__seller=user)

    def perform_create(self, serializer):
        serializer.save(buyer=self.request.user)
        
    @action(detail=True, methods=['post'])
    def mark_completed(self, request, pk=None):
        order = self.get_object()
        
        # Only the Seller can complete the order
        if order.service.seller != request.user:
            return Response({'error': 'Only the seller can complete this order.'}, status=403)
            
        order.status = 'COMPLETED'
        order.save()
        return Response({'status': 'Order marked as completed'})
        
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Additional logic can go here if needed
        serializer.save()