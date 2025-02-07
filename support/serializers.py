from rest_framework import serializers
from .models import SupportTicket
from restaurants.serializers import UserSerializer
from orders.serializers import OrderSerializer
from django.contrib.auth.models import User
from orders.models import Order


class SupportTicketSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(read_only=True)
    
    order= serializers.PrimaryKeyRelatedField(
        queryset=Order.objects.all(), required=False, allow_null=True
    )


    class Meta:
        model = SupportTicket
        fields = '__all__'


    def validate_order(self, value):
        if value and value.client != self.context['request'].user:
            raise serializers.ValidationError("Este pedido não pertence ao cliente autenticado.")
        return value

