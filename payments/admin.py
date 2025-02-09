from django.contrib import admin
from payments.models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'payment_method', 'transaction_id', 'total_price', 'status', 'created_at')
    search_fields = ('transaction_id', 'order__id', 'payment_method')
    readonly_fields = ('created_at',)

    
    def order(self, obj):
        return f'Order #{obj.order.id}'
    order.short_description = 'Order'  # Nome da coluna na lista
