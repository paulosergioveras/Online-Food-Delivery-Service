from django.contrib import admin
from menu.models import Menu


@admin.register(Menu)
class ModelAdmin(admin.ModelAdmin):
	list_display = ('dish_name', 'dish_description', 'restaurant', 'price', 'is_active')
