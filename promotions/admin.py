from django.contrib import admin
from promotions.models import Promotion


@admin.register(Promotion)
class ModelAdmin(admin.ModelAdmin):
    list_display = ('restaurant', 'code', 'discount_percentage', 'valid_from', 'valid_until', 'is_active')


