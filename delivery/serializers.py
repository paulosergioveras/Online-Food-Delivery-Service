from rest_framework import serializers
from .models import Restaurant, Menu, Order, OrderItem, Reviews, Promotion, Payment, SupportTicket
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
    
class RestaurantSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    class Meta:
        model = Restaurant
        fields = '__all__'

class MenuSerializer(serializers.ModelSerializer):
    restaurant = RestaurantSerializer(read_only=True)
    class Meta:
        model = Menu
        fields = '__all__'

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

class ReviewsSerializer(serializers.ModelSerializer):
    client = UserSerializer(read_only=True)
    restaurant = RestaurantSerializer(read_only=True)
    class Meta:
        model = Reviews
        fields = '__all__'

class PromotionSerializer(serializers.ModelSerializer):
    restaurant = RestaurantSerializer(read_only=True)   
    class Meta:
        model = Promotion
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

class SupportTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupportTicket
        fields = '__all__'