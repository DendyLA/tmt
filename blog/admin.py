from django.contrib import admin
from django.utils.html import format_html

from .models import Blog

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('preview', 'title', 'created_at')
    list_display_links = ('preview', 'title')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)
    
    fieldsets = (
        (None, {
            'fields': ( 'title' ,'image', 'text')
        }),
        ('Дополнительно', {
            'fields': ('created_at',),  # Запятая важна для кортежа!
            'classes': ('collapse',)
        }),
    )

    @admin.display(description="Превью")
    def preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-height: 100px; border: 1px solid #ddd; border-radius: 4px;"/>',
                obj.image.url
            )
        return "-"
