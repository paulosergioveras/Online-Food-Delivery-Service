from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)
    description = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class Menu(models.Model):
    dish_name = models.CharField(max_length=200)
    dish_description = models.TextField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.dish_name} - {self.price} - {self.restaurant.name}'
    
    
class Order(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('CONFIRMED', 'Confirmed'),
        ('PREPARING', 'Preparing'),
        ('OUT_FOR_DELIVERY', 'Out for delivery'),
        ('DELIVERED', 'Delivered'),
        ('CANCELED', 'Canceled'),
    ]
    
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Menu, through='OrderItem')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    client_address = models.TextField()
    client_contact = models.CharField(max_length=20)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    instructions = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Order #{self.id} - {self.client.username}'
    
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(Menu, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)


class Reviews(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    rating = models.FloatField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comments = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Promotion(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    code = models.CharField(max_length=50, unique=True)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    valid_from = models.DateTimeField()
    valid_until = models.DateTimeField()
    is_active = models.BooleanField(default=True)

class Payment(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('SUCCESS', 'Success'),
        ('FAILED', 'Failed'),
    ]

    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='payment')
    payment_method = models.CharField(max_length=50)
    transaction_id = models.CharField(max_length=100, unique=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Payment for Order #{self.order.id}'


class SupportTicket(models.Model):
    STATUS_CHOICES = [
        ('OPEN', 'Open'),
        ('IN_PROGRESS', 'In Progress'),
        ('RESOLVED', 'Resolved'),
    ]

    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='support_tickets')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='support_tickets', null=True, blank=True)
    subject = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='OPEN')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Support Ticket #{self.id} - {self.subject}'