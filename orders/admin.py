from django.contrib import admin
from orders.models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'restaurant', 'status', 'total_price', 'created_at')
    list_filter = ('status', 'restaurant', 'created_at')
    search_fields = ('client__username', 'restaurant__name', 'client_address')


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'menu_item', 'quantity', 'price')
    list_filter = ('order__status', 'menu_item')
    search_fields = ('order__id', 'menu_item__name')
