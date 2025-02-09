from django.db import models
from restaurants.models import Restaurant


class Menu(models.Model):
    dish_name = models.CharField(max_length=200)
    dish_description = models.TextField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.dish_name} - {self.price} - {self.restaurant.name}'
