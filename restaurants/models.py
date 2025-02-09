from django.db import models
from django.contrib.auth.models import User


class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name