from django.contrib import admin
from django.utils.html import format_html

from .models import Project, ProjectImage, AboutServices



class ProjectImageInline(admin.TabularInline):  # или StackedInline
    model = ProjectImage
    extra = 1  # сколько пустых полей для загрузки фото



class ProjectAdmin(admin.ModelAdmin):
    list_display = ('preview', 'title', 'created_at')
    list_display_links = ('preview', 'title')
    inlines = [ProjectImageInline]
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)

    fieldsets = (
        (None, {
            'fields': ( 'title' ,'image', 'descr', 'pdf')
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
    
admin.site.register(Project, ProjectAdmin)



@admin.register(AboutServices)
class ServicesAboutAdmin(admin.ModelAdmin):
    list_display = ('preview', 'title', 'created_at')
    list_display_links = ('preview', 'title')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)
    
    fieldsets = (
        (None, {
            'fields': ( 'image',  'title', 'text')
        }),
        ('Дополнительно', {
            'fields': ('created_at',), 
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