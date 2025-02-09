from django.contrib import admin
from reviews.models import Reviews


@admin.register(Reviews)
class ModelAdmin(admin.ModelAdmin):
    list_display = ('client', 'restaurant', 'rating', 'comments', 'created_at')
