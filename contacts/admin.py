from django.contrib import admin

from .models import ContactMessage


@admin.register(ContactMessage)
class FeedbacksAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone', 'email', 'message')
    list_display_links = ('first_name', 'last_name', 'phone', 'email')
    readonly_fields = ('first_name', 'last_name', 'phone', 'email', 'message', 'created_at')
    ordering = ('-created_at', )
    
