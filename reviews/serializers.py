from rest_framework import serializers
from django.contrib.auth.models import User
from restaurants.serializers import UserSerializer, RestaurantSerializer
from .models import Reviews


class ReviewsSerializer(serializers.ModelSerializer):
    client = UserSerializer(read_only=True)
    restaurant = RestaurantSerializer(read_only=True)
    
    class Meta:
        model = Reviews
        fields = '__all__'