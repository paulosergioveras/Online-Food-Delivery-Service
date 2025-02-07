from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from restaurants.models import Restaurant


class Reviews(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    rating = models.FloatField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comments = models.TextField() #NAO OBRIGATORIO
    created_at = models.DateTimeField(auto_now_add=True)
