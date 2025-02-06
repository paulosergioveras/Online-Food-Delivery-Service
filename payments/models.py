from django.db import models
from orders.models import Order


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
