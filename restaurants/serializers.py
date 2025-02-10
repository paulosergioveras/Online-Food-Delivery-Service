from rest_framework import serializers
from django.contrib.auth.models import User
from restaurants.models import Restaurant


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'email']

    
class RestaurantSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Restaurant
        fields = '__all__'