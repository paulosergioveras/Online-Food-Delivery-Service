from rest_framework import serializers
from .models import Restaurant, Menu
from django.contrib.auth.models import User
from restaurants.serializers import MenuSerializer, UserSerializer, RestaurantSerializer
from .models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    menu_items = MenuSerializer(read_only=True)
    
    class Meta:
        model = OrderItem
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    client = UserSerializer(read_only=True)
    restaurant = RestaurantSerializer(read_only=True)
    items = MenuSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = '__all__'