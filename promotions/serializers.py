from rest_framework import serializers
from restaurants.serializers import RestaurantSerializer
from .models import Promotion


class PromotionSerializer(serializers.ModelSerializer):
    restaurant = RestaurantSerializer(read_only=True)   

    class Meta:
        model = Promotion
        fields = '__all__'