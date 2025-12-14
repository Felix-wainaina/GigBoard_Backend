# orders/views.py
from rest_framework import viewsets, permissions
from .models import Order
from .serializers import OrderSerializer

class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Users should only see orders relevant to them (Buying or Selling)
        user = self.request.user
        return Order.objects.filter(buyer=user) | Order.objects.filter(service__seller=user)

    def perform_create(self, serializer):
        serializer.save(buyer=self.request.user)