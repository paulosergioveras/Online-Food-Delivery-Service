from django.contrib import admin
from restaurants.views import Restaurant


@admin.register(Restaurant)
class ModelAdmin(admin.ModelAdmin):
	list_display = ('name', 'owner', 'address', 'phone', 'is_active', 'description', 'created_at')
	