# orders/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrderViewSet, ReviewViewSet

router = DefaultRouter()
# Change r'' to r'orders' so the URL becomes .../orders/
router.register(r'orders', OrderViewSet, basename='order')
# Add the reviews route
router.register(r'reviews', ReviewViewSet, basename='review')

urlpatterns = [
    path('', include(router.urls)),
]