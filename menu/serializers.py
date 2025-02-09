from rest_framework import serializers
from menu.models import Menu
from restaurants.serializers import RestaurantSerializer
from restaurants.models import Restaurant



class MenuSerializer(serializers.ModelSerializer):
    restaurant = RestaurantSerializer(read_only=True)
    restaurant_id = serializers.PrimaryKeyRelatedField(
        queryset=Restaurant.objects.all(), source='restaurant', write_only=True
    )

  
    class Meta:
        model = Menu
        fields = '__all__'