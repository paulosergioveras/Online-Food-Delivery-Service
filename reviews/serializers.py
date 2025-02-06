from rest_framework import serializers
from django.contrib.auth.models import User
from restaurants.serializers import UserSerializer, RestaurantSerializer
from .models import Reviews
from restaurants.models import Restaurant


class ReviewsSerializer(serializers.ModelSerializer):
    client = UserSerializer(read_only=True)
    restaurant = RestaurantSerializer(read_only=True)

    client_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='client', write_only=True
        )
    
    restaurant_id = serializers.PrimaryKeyRelatedField(
        queryset=Restaurant.objects.all(), source='restaurant', write_only=True
    )

    class Meta:
        model = Reviews
        fields = '__all__'