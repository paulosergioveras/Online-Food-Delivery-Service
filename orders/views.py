from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Order, OrderItem
from .serializers import OrderSerializer, OrderItemSerializer


class OrderListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

