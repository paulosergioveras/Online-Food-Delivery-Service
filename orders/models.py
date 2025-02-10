from django.db import models
from django.contrib.auth.models import User
from restaurants.models import Restaurant
from menu.models import Menu


STATUS_CHOICES = [
    ('PENDING', 'Pending'),
    ('CONFIRMED', 'Confirmed'),
    ('PREPARING', 'Preparing'),
    ('OUT_FOR_DELIVERY', 'Out for delivery'),
    ('DELIVERED', 'Delivered'),
    ('CANCELED', 'Canceled'),
]


class Order(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Menu, through='OrderItem')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    client_address = models.TextField()
    client_contact = models.CharField(max_length=20)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    instructions = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Order #{self.id} - {self.client.username}'
   
   
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(Menu, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
