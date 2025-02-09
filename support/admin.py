from django.contrib import admin
from support.models import SupportTicket


@admin.register(SupportTicket)
class ModelAdmin(admin.ModelAdmin):
	list_display = ('client', 'order', 'subject', 'description', 'status', 'created_at')
